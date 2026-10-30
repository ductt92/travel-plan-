// Danh mục khóa học cho trang quản lý (apps/quan-ly). Bản Node: backend/node/catalog.js, cùng hợp đồng.
// Đường dẫn, dữ liệu vào/ra và mã lỗi giống hệt nhau, xem phần chú ở đầu file bên Node.
package gobackend

import (
	"context"
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"math"
	"net/http"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgconn"
	"github.com/jackc/pgx/v5/pgxpool"
)

// pgx dùng giao thức mở rộng nên mỗi lần Exec chỉ một câu lệnh, phải tách ra
var catalogTables = []string{
	`CREATE TABLE IF NOT EXISTS catalog_courses (
		id         serial PRIMARY KEY,
		slug       text UNIQUE NOT NULL,
		title      text NOT NULL,
		sort       integer NOT NULL DEFAULT 0,
		created_at timestamptz NOT NULL DEFAULT now()
	)`,
	`CREATE TABLE IF NOT EXISTS catalog_lessons (
		id        serial PRIMARY KEY,
		course_id integer NOT NULL REFERENCES catalog_courses ON DELETE CASCADE,
		num       integer NOT NULL,
		title     text NOT NULL,
		zh        text NOT NULL DEFAULT '',
		visible   boolean NOT NULL DEFAULT true,
		sort      integer NOT NULL DEFAULT 0,
		UNIQUE (course_id, num)
	)`,
	`CREATE TABLE IF NOT EXISTS catalog_assets (
		id         serial PRIMARY KEY,
		lesson_id  integer NOT NULL REFERENCES catalog_lessons ON DELETE CASCADE,
		kind       text NOT NULL CHECK (kind IN ('video', 'slides', 'audio', 'pdf', 'other')),
		name       text NOT NULL,
		size       bigint NOT NULL DEFAULT 0,
		url        text NOT NULL DEFAULT '',
		storage    text NOT NULL CONSTRAINT catalog_assets_storage_check CHECK (storage IN ('repo', 'r2', 'youtube')),
		key        text NOT NULL DEFAULT '',
		created_at timestamptz NOT NULL DEFAULT now()
	)`,
	`CREATE INDEX IF NOT EXISTS catalog_assets_lesson_idx ON catalog_assets (lesson_id)`,
	// bảng tạo trước khi có 'youtube' thì nới ràng buộc, chỉ một lần
	`DO $$ BEGIN
		IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conrelid = 'catalog_assets'::regclass
		               AND conname = 'catalog_assets_storage_check' AND pg_get_constraintdef(oid) LIKE '%youtube%') THEN
			ALTER TABLE catalog_assets DROP CONSTRAINT IF EXISTS catalog_assets_storage_check;
			ALTER TABLE catalog_assets ADD CONSTRAINT catalog_assets_storage_check CHECK (storage IN ('repo', 'r2', 'youtube'));
		END IF;
	END $$`,
}

var (
	catalogOnce sync.Once
	catalogErr  error
)

func catalogPool(ctx context.Context) (*pgxpool.Pool, error) {
	p, err := db(ctx)
	if err != nil {
		return nil, err
	}
	catalogOnce.Do(func() {
		for _, q := range catalogTables {
			if _, catalogErr = p.Exec(ctx, q); catalogErr != nil {
				return
			}
		}
	})
	return p, catalogErr
}

const (
	catMaxTitle  = 200
	catMaxName   = 200
	catMaxURL    = 2000
	catMaxKey    = 1024
	catMaxSort   = 1_000_000
	catMaxNum    = 9999
	catMaxSize   = 1 << 50
	catMaxUpload = 200 * 1024 * 1024
	catMaxID     = math.MaxInt32
	catDBLimit   = 536870912
	catR2Limit   = 10737418240
	catR2Missing = "Chưa cấu hình Cloudflare R2 (cần R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET, R2_PUBLIC_URL)"
)

var (
	catKinds    = []string{"video", "slides", "audio", "pdf", "other"}
	catStorages = []string{"repo", "r2", "youtube"}
	catSlugRe   = regexp.MustCompile(`^[a-z0-9][a-z0-9-]{0,39}$`)
	catTypeRe   = regexp.MustCompile(`^[\w.+-]+/[\w.+-]+$`)
	catYTRe     = regexp.MustCompile(`^(?:https?://)?(?:(?:www\.|m\.)?youtube\.com/(?:watch\?(?:[^#]*&)?v=|embed/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{11})(?:[?&#/].*)?$`)
	catURLRe    = regexp.MustCompile(`^https?://\S+$`)
	catKeyRe    = regexp.MustCompile(`^[A-Za-z0-9._/-]+$`)
	catIDRe     = regexp.MustCompile(`^[1-9]\d{0,9}$`)
)

func catIn(list []string, v any) bool {
	s, ok := v.(string)
	if !ok {
		return false
	}
	for _, x := range list {
		if x == s {
			return true
		}
	}
	return false
}

func catAbsent(b map[string]any, k string) bool { v, ok := b[k]; return !ok || v == nil }

func catText(v any, limit int) string { s, _ := v.(string); return clip(s, limit) }

// Số nguyên trong [min, max]: vắng → present=false; có mà sai → ok=false
func catInt(v any, min, max int64) (n int64, present, ok bool) {
	if v == nil {
		return 0, false, true
	}
	num, isNum := v.(json.Number)
	if !isNum {
		return 0, true, false
	}
	f, err := num.Float64()
	if err != nil || f != math.Trunc(f) || f < float64(min) || f > float64(max) {
		return 0, true, false
	}
	return int64(f), true, true
}

func catIDParam(r *http.Request, name string) int64 {
	v := r.URL.Query().Get(name)
	if !catIDRe.MatchString(v) {
		return 0
	}
	n, err := strconv.ParseInt(v, 10, 64)
	if err != nil || n > catMaxID {
		return 0
	}
	return n
}

func catValidURL(u string) bool { return strings.HasPrefix(u, "/") || catURLRe.MatchString(u) }

func catYouTube(u string) string {
	if m := catYTRe.FindStringSubmatch(u); m != nil {
		return "https://www.youtube.com/watch?v=" + m[1]
	}
	return ""
}

// Bỏ dấu tiếng Việt bằng bảng tay (giống bản Node), ký tự khác ngoài [A-Za-z0-9._-] thành '-'
var catVI = func() map[rune]rune {
	m := map[rune]rune{}
	for base, chars := range map[rune]string{
		'a': "àáạảãâầấậẩẫăằắặẳẵ", 'e': "èéẹẻẽêềếệểễ", 'i': "ìíịỉĩ", 'o': "òóọỏõôồốộổỗơờớợởỡ",
		'u': "ùúụủũưừứựửữ", 'y': "ỳýỵỷỹ", 'd': "đ",
	} {
		for _, c := range chars {
			m[c] = base
			m[[]rune(strings.ToUpper(string(c)))[0]] = []rune(strings.ToUpper(string(base)))[0]
		}
	}
	return m
}()

var (
	catDashes   = regexp.MustCompile(`-+`)
	catDot      = regexp.MustCompile(`-*\.-*`)
	catEdges    = regexp.MustCompile(`^[-.]+|[-.]+$`)
	catTrailing = regexp.MustCompile(`[-.]+$`)
)

func catSafeName(name string) string {
	var b strings.Builder
	for _, c := range name {
		switch {
		case catVI[c] != 0:
			b.WriteRune(catVI[c])
		case c < 128 && (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c >= '0' && c <= '9' || c == '.' || c == '_' || c == '-'):
			b.WriteRune(c)
		default:
			b.WriteByte('-')
		}
	}
	s := catEdges.ReplaceAllString(catDot.ReplaceAllString(catDashes.ReplaceAllString(b.String(), "-"), "."), "")
	if len(s) > 80 {
		s = catTrailing.ReplaceAllString(s[:80], "")
	}
	if s == "" {
		return "file"
	}
	return s
}

// ---- Cloudflare R2: chữ ký AWS SigV4 viết tay (URL ký sẵn), không cần SDK ----

type r2Env struct{ account, accessKey, secret, bucket, publicURL string }

func r2FromEnv() r2Env {
	return r2Env{os.Getenv("R2_ACCOUNT_ID"), os.Getenv("R2_ACCESS_KEY_ID"), os.Getenv("R2_SECRET_ACCESS_KEY"),
		os.Getenv("R2_BUCKET"), strings.TrimRight(os.Getenv("R2_PUBLIC_URL"), "/")}
}

func (e r2Env) ready() bool {
	return e.account != "" && e.accessKey != "" && e.secret != "" && e.bucket != "" && e.publicURL != ""
}

// mã hoá kiểu RFC 3986 như AWS yêu cầu (url.PathEscape còn chừa vài ký tự)
func awsEscape(s string) string {
	var b strings.Builder
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z' || c >= '0' && c <= '9' || c == '-' || c == '_' || c == '.' || c == '~' {
			b.WriteByte(c)
		} else {
			fmt.Fprintf(&b, "%%%02X", c)
		}
	}
	return b.String()
}

func hmacSHA256(key []byte, data string) []byte {
	h := hmac.New(sha256.New, key)
	h.Write([]byte(data))
	return h.Sum(nil)
}

// presign tạo URL ký sẵn SigV4 (chỉ ký header host, payload UNSIGNED-PAYLOAD). path đã gồm bucket nếu dùng path-style.
func presign(method, host, path, region, accessKey, secret string, date time.Time, expires int) string {
	stamp := date.UTC().Format("20060102T150405Z")
	day := stamp[:8]
	scope := day + "/" + region + "/s3/aws4_request"
	params := [][2]string{
		{"X-Amz-Algorithm", "AWS4-HMAC-SHA256"}, {"X-Amz-Credential", accessKey + "/" + scope},
		{"X-Amz-Date", stamp}, {"X-Amz-Expires", strconv.Itoa(expires)}, {"X-Amz-SignedHeaders", "host"},
	}
	parts := make([]string, len(params))
	for i, kv := range params {
		parts[i] = awsEscape(kv[0]) + "=" + awsEscape(kv[1])
	}
	sort.Strings(parts)
	query := strings.Join(parts, "&")
	segs := strings.Split(path, "/")
	for i, s := range segs {
		segs[i] = awsEscape(s)
	}
	canonPath := strings.Join(segs, "/")
	canonical := strings.Join([]string{method, canonPath, query, "host:" + host + "\n", "host", "UNSIGNED-PAYLOAD"}, "\n")
	sum := sha256.Sum256([]byte(canonical))
	toSign := strings.Join([]string{"AWS4-HMAC-SHA256", stamp, scope, hex.EncodeToString(sum[:])}, "\n")
	key := hmacSHA256(hmacSHA256(hmacSHA256(hmacSHA256([]byte("AWS4"+secret), day), region), "s3"), "aws4_request")
	return "https://" + host + canonPath + "?" + query + "&X-Amz-Signature=" + hex.EncodeToString(hmacSHA256(key, toSign))
}

func (e r2Env) url(method, key string, expires int) string {
	return presign(method, e.account+".r2.cloudflarestorage.com", "/"+e.bucket+"/"+key, "auto", e.accessKey, e.secret, time.Now(), expires)
}

// Xoá các object trên R2; true nếu xoá được hết (404 coi như đã xoá).
func (e r2Env) remove(ctx context.Context, keys []string) bool {
	client := &http.Client{Timeout: 10 * time.Second}
	for _, key := range keys {
		req, err := http.NewRequestWithContext(ctx, http.MethodDelete, e.url(http.MethodDelete, key, 60), nil)
		if err != nil {
			return false
		}
		res, err := client.Do(req)
		if err != nil {
			return false
		}
		res.Body.Close()
		if res.StatusCode >= 300 && res.StatusCode != http.StatusNotFound {
			return false
		}
	}
	return true
}

// ---- đọc / ghi ----

type catAsset struct {
	ID        int    `json:"id"`
	Kind      string `json:"kind"`
	Name      string `json:"name"`
	Size      int64  `json:"size"`
	URL       string `json:"url"`
	Storage   string `json:"storage"`
	Key       string `json:"key"`
	CreatedAt string `json:"createdAt"`
	LessonID  int    `json:"lessonId,omitempty"`
}

type catLesson struct {
	ID       int         `json:"id"`
	Num      int         `json:"num"`
	Title    string      `json:"title"`
	Zh       string      `json:"zh"`
	Visible  bool        `json:"visible"`
	Sort     int         `json:"sort"`
	Assets   *[]catAsset `json:"assets,omitempty"`
	CourseID int         `json:"courseId,omitempty"`
}

type catCourse struct {
	ID      int           `json:"id"`
	Slug    string        `json:"slug"`
	Title   string        `json:"title"`
	Sort    int           `json:"sort"`
	Lessons *[]*catLesson `json:"lessons,omitempty"`
}

const (
	catCourseCols = `id, slug, title, sort`
	catLessonCols = `id, course_id, num, title, zh, visible, sort`
	catAssetCols  = `id, lesson_id, kind, name, size, url, storage, key,
		to_char(created_at AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS.MS"Z"')`
)

func scanCourse(row pgx.Row) (catCourse, error) {
	var c catCourse
	err := row.Scan(&c.ID, &c.Slug, &c.Title, &c.Sort)
	return c, err
}

func scanLesson(row pgx.Row) (catLesson, error) {
	var l catLesson
	err := row.Scan(&l.ID, &l.CourseID, &l.Num, &l.Title, &l.Zh, &l.Visible, &l.Sort)
	return l, err
}

func scanAsset(row pgx.Row) (catAsset, error) {
	var a catAsset
	err := row.Scan(&a.ID, &a.LessonID, &a.Kind, &a.Name, &a.Size, &a.URL, &a.Storage, &a.Key, &a.CreatedAt)
	return a, err
}

// struct thay cho map để khóa JSON ra đúng thứ tự như bản Node
type catAll struct {
	Courses []*catCourse `json:"courses"`
	Usage   struct {
		DBBytes      int64 `json:"dbBytes"`
		DBLimitBytes int64 `json:"dbLimitBytes"`
		R2Bytes      int64 `json:"r2Bytes"`
		R2LimitBytes int64 `json:"r2LimitBytes"`
		RepoBytes    int64 `json:"repoBytes"`
		YoutubeCount int64 `json:"youtubeCount"`
	} `json:"usage"`
	R2 struct {
		Configured bool   `json:"configured"`
		PublicURL  string `json:"publicUrl"`
	} `json:"r2"`
}

type catImportResult struct {
	OK      bool `json:"ok"`
	Courses int  `json:"courses"`
	Lessons int  `json:"lessons"`
	Assets  int  `json:"assets"`
}

func catReadAll(ctx context.Context, p *pgxpool.Pool) (*catAll, error) {
	courses := []*catCourse{}
	byCourse := map[int]*catCourse{}
	rows, err := p.Query(ctx, `SELECT `+catCourseCols+` FROM catalog_courses ORDER BY sort, id`)
	if err != nil {
		return nil, err
	}
	for rows.Next() {
		c, err := scanCourse(rows)
		if err != nil {
			rows.Close()
			return nil, err
		}
		ls := []*catLesson{}
		c.Lessons = &ls
		byCourse[c.ID] = &c
		courses = append(courses, &c)
	}
	rows.Close()

	byLesson := map[int]*catLesson{}
	rows, err = p.Query(ctx, `SELECT `+catLessonCols+` FROM catalog_lessons ORDER BY sort, num, id`)
	if err != nil {
		return nil, err
	}
	for rows.Next() {
		l, err := scanLesson(rows)
		if err != nil {
			rows.Close()
			return nil, err
		}
		as := []catAsset{}
		l.Assets = &as
		course := l.CourseID
		l.CourseID = 0 // danh sách lồng nhau không lặp lại courseId
		byLesson[l.ID] = &l
		if c := byCourse[course]; c != nil {
			*c.Lessons = append(*c.Lessons, &l)
		}
	}
	rows.Close()

	rows, err = p.Query(ctx, `SELECT `+catAssetCols+` FROM catalog_assets ORDER BY kind, name, id`)
	if err != nil {
		return nil, err
	}
	for rows.Next() {
		a, err := scanAsset(rows)
		if err != nil {
			rows.Close()
			return nil, err
		}
		lesson := a.LessonID
		a.LessonID = 0
		if l := byLesson[lesson]; l != nil {
			*l.Assets = append(*l.Assets, a)
		}
	}
	rows.Close()

	var dbBytes, r2Bytes, repoBytes, ytCount int64
	if err := p.QueryRow(ctx, `SELECT pg_database_size(current_database())::bigint`).Scan(&dbBytes); err != nil {
		return nil, err
	}
	if err := p.QueryRow(ctx, `SELECT coalesce(sum(size) FILTER (WHERE storage = 'r2'), 0)::bigint,
	                                  coalesce(sum(size) FILTER (WHERE storage = 'repo'), 0)::bigint,
	                                  count(*) FILTER (WHERE storage = 'youtube')::bigint
	                           FROM catalog_assets`).Scan(&r2Bytes, &repoBytes, &ytCount); err != nil {
		return nil, err
	}
	out := &catAll{Courses: courses}
	out.Usage.DBBytes, out.Usage.DBLimitBytes, out.Usage.R2Bytes, out.Usage.R2LimitBytes = dbBytes, catDBLimit, r2Bytes, catR2Limit
	out.Usage.RepoBytes, out.Usage.YoutubeCount = repoBytes, ytCount
	e := r2FromEnv()
	out.R2.Configured, out.R2.PublicURL = e.ready(), e.publicURL
	return out, nil
}

// Xoá khóa/bài: file R2 bên trong xoá trước, xoá không được thì giữ nguyên dòng
func catRemoveWithFiles(w http.ResponseWriter, ctx context.Context, p *pgxpool.Pool, table, where string, id int64, missing string) {
	rows, err := p.Query(ctx, `SELECT a.key FROM catalog_assets a JOIN catalog_lessons l ON l.id = a.lesson_id
		WHERE a.storage = 'r2' AND a.key <> '' AND `+where+` = $1`, id)
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	keys, err := pgx.CollectRows(rows, pgx.RowTo[string])
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	if len(keys) > 0 {
		e := r2FromEnv()
		if !e.ready() {
			fail(w, http.StatusServiceUnavailable, catR2Missing)
			return
		}
		if !e.remove(ctx, keys) {
			fail(w, http.StatusBadGateway, "không xoá được file trên R2, chưa xoá gì, thử lại sau")
			return
		}
	}
	tag, err := p.Exec(ctx, `DELETE FROM `+table+` WHERE id = $1`, id)
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	if tag.RowsAffected() == 0 {
		fail(w, http.StatusNotFound, missing)
		return
	}
	writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
}

type catImportAsset struct {
	kind, name, url string
	size            int64
}
type catImportLesson struct {
	num       int64
	title, zh string
	assets    []catImportAsset
}
type catImportCourse struct {
	slug, title string
	sort        int64
	lessons     []catImportLesson
}

func catCheckImport(body map[string]any) ([]catImportCourse, string) {
	list, ok := body["courses"].([]any)
	if !ok || len(list) > 50 {
		return nil, "cần courses: [...] (tối đa 50 khóa)"
	}
	out := []catImportCourse{}
	slugs := map[string]bool{}
	for i, item := range list {
		c, ok := item.(map[string]any)
		if !ok {
			return nil, fmt.Sprintf("khóa #%d: không đọc được", i+1)
		}
		slug, _ := c["slug"].(string)
		slug = strings.TrimSpace(slug)
		at := "khóa " + slug
		if slug == "" {
			at = fmt.Sprintf("khóa #%d", i+1)
		}
		if !catSlugRe.MatchString(slug) {
			return nil, at + ": mã khóa học chỉ gồm chữ thường, số và dấu gạch ngang"
		}
		if slugs[slug] {
			return nil, at + ": mã khóa học bị trùng"
		}
		slugs[slug] = true
		title := catText(c["title"], catMaxTitle)
		if title == "" {
			return nil, at + ": cần tên khóa học"
		}
		sortN, _, ok := catInt(c["sort"], -catMaxSort, catMaxSort)
		if !ok {
			return nil, at + ": thứ tự không hợp lệ"
		}
		rawLessons, ok := c["lessons"].([]any)
		if !ok || len(rawLessons) > 500 {
			return nil, at + ": cần lessons: [...] (tối đa 500 bài)"
		}
		course := catImportCourse{slug: slug, title: title, sort: sortN, lessons: []catImportLesson{}}
		nums := map[int64]bool{}
		for _, rl := range rawLessons {
			l, ok := rl.(map[string]any)
			if !ok {
				return nil, at + ": có bài không đọc được"
			}
			num, present, ok := catInt(l["num"], 0, catMaxNum)
			if !ok || !present {
				return nil, at + ": số bài không hợp lệ"
			}
			atL := fmt.Sprintf("%s bài %d", at, num)
			if nums[num] {
				return nil, atL + ": số bài bị trùng"
			}
			nums[num] = true
			ltitle := catText(l["title"], catMaxTitle)
			if ltitle == "" {
				return nil, atL + ": cần tên bài"
			}
			var rawAssets []any
			if !catAbsent(l, "assets") {
				if rawAssets, ok = l["assets"].([]any); !ok || len(rawAssets) > 50 {
					return nil, atL + ": assets phải là mảng (tối đa 50 file)"
				}
			}
			lesson := catImportLesson{num: num, title: ltitle, zh: catText(l["zh"], catMaxTitle)}
			for _, ra := range rawAssets {
				a, ok := ra.(map[string]any)
				if !ok {
					return nil, atL + ": có file không đọc được"
				}
				if !catIn(catKinds, a["kind"]) {
					return nil, atL + ": loại file không hợp lệ"
				}
				name := catText(a["name"], catMaxName)
				if name == "" {
					return nil, atL + ": cần tên file"
				}
				size, _, ok := catInt(a["size"], 0, catMaxSize)
				if !ok {
					return nil, atL + ": dung lượng không hợp lệ"
				}
				u := catText(a["url"], catMaxURL)
				if !catValidURL(u) {
					return nil, atL + ": đường dẫn không hợp lệ"
				}
				lesson.assets = append(lesson.assets, catImportAsset{kind: a["kind"].(string), name: name, url: u, size: size})
			}
			course.lessons = append(course.lessons, lesson)
		}
		out = append(out, course)
	}
	return out, ""
}

func catRunImport(ctx context.Context, p *pgxpool.Pool, courses []catImportCourse) (*catImportResult, error) {
	tx, err := p.Begin(ctx)
	if err != nil {
		return nil, err
	}
	defer tx.Rollback(ctx)
	nc, nl, na := 0, 0, 0
	for _, c := range courses {
		var courseID int
		if err := tx.QueryRow(ctx,
			`INSERT INTO catalog_courses (slug, title, sort) VALUES ($1, $2, $3)
			 ON CONFLICT (slug) DO UPDATE SET title = EXCLUDED.title, sort = EXCLUDED.sort RETURNING id`,
			c.slug, c.title, c.sort).Scan(&courseID); err != nil {
			return nil, err
		}
		nc++
		if len(c.lessons) == 0 {
			continue
		}
		// mỗi khóa ba câu lệnh: ghi gộp bài, xoá file 'repo' cũ của các bài đó, ghi file mới (r2, youtube giữ nguyên)
		nums, titles, zhs := []int64{}, []string{}, []string{}
		for _, l := range c.lessons {
			nums, titles, zhs = append(nums, l.num), append(titles, l.title), append(zhs, l.zh)
		}
		rows, err := tx.Query(ctx,
			`INSERT INTO catalog_lessons (course_id, num, title, zh)
			 SELECT $1, * FROM unnest($2::int[], $3::text[], $4::text[])
			 ON CONFLICT (course_id, num) DO UPDATE SET title = EXCLUDED.title, zh = EXCLUDED.zh RETURNING id, num`,
			courseID, nums, titles, zhs)
		if err != nil {
			return nil, err
		}
		idOf := map[int64]int64{}
		ids := []int64{}
		for rows.Next() {
			var id, num int64
			if err := rows.Scan(&id, &num); err != nil {
				rows.Close()
				return nil, err
			}
			idOf[num] = id
			ids = append(ids, id)
		}
		rows.Close()
		if err := rows.Err(); err != nil {
			return nil, err
		}
		nl += len(ids)
		if _, err := tx.Exec(ctx, `DELETE FROM catalog_assets WHERE storage = 'repo' AND lesson_id = ANY($1::int[])`, ids); err != nil {
			return nil, err
		}
		var lids, sizes []int64
		var kinds, names, urls []string
		for _, l := range c.lessons {
			for _, a := range l.assets {
				lids, kinds, names, sizes, urls = append(lids, idOf[l.num]), append(kinds, a.kind), append(names, a.name), append(sizes, a.size), append(urls, a.url)
			}
		}
		if len(lids) > 0 {
			if _, err := tx.Exec(ctx,
				`INSERT INTO catalog_assets (lesson_id, kind, name, size, url, storage)
				 SELECT l, k, nm, s, u, 'repo' FROM unnest($1::int[], $2::text[], $3::text[], $4::bigint[], $5::text[]) AS t(l, k, nm, s, u)`,
				lids, kinds, names, sizes, urls); err != nil {
				return nil, err
			}
			na += len(lids)
		}
	}
	if err := tx.Commit(ctx); err != nil {
		return nil, err
	}
	return &catImportResult{OK: true, Courses: nc, Lessons: nl, Assets: na}, nil
}

var catActions = []string{"course", "lesson", "asset", "upload", "import"}

// Catalog xử lý /api/go/quan-ly.
func Catalog(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	q := r.URL.Query()

	var allowed []string
	switch r.Method {
	case http.MethodGet:
	case http.MethodPost:
		allowed = catActions
	case http.MethodPatch:
		allowed = []string{"course", "lesson"}
	case http.MethodDelete:
		allowed = []string{"course", "lesson", "asset"}
	default:
		w.Header().Set("Allow", "GET, POST, PATCH, DELETE")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ GET, POST, PATCH và DELETE")
		return
	}
	if !authorized(r) {
		fail(w, http.StatusUnauthorized, "sai mật khẩu")
		return
	}
	if r.Method == http.MethodGet && q.Has("check") {
		writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
		return
	}

	action := ""
	for _, a := range catActions {
		if q.Has(a) {
			action = a
			break
		}
	}
	if r.Method != http.MethodGet && !catIn(allowed, action) {
		names := make([]string, len(allowed))
		for i, a := range allowed {
			names[i] = "?" + a
		}
		fail(w, http.StatusBadRequest, r.Method+" cần một trong: "+strings.Join(names, ", "))
		return
	}

	p, err := catalogPool(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
	}

	if r.Method == http.MethodGet {
		out, err := catReadAll(ctx, p)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, out)
		return
	}

	if r.Method == http.MethodDelete {
		id := catIDParam(r, action)
		if id == 0 {
			fail(w, http.StatusBadRequest, "cần ?"+action+"=<số>")
			return
		}
		switch action {
		case "course":
			catRemoveWithFiles(w, ctx, p, "catalog_courses", "l.course_id", id, "không có khóa học này")
		case "lesson":
			catRemoveWithFiles(w, ctx, p, "catalog_lessons", "l.id", id, "không có bài này")
		default:
			var storage, key string
			err := p.QueryRow(ctx, `SELECT storage, key FROM catalog_assets WHERE id = $1`, id).Scan(&storage, &key)
			if errors.Is(err, pgx.ErrNoRows) {
				fail(w, http.StatusNotFound, "không có file này")
				return
			}
			if err != nil {
				fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
				return
			}
			if storage == "r2" && key != "" {
				e := r2FromEnv()
				if !e.ready() {
					fail(w, http.StatusServiceUnavailable, catR2Missing)
					return
				}
				if !e.remove(ctx, []string{key}) {
					fail(w, http.StatusBadGateway, "không xoá được file trên R2, thử lại sau")
					return
				}
			}
			if _, err := p.Exec(ctx, `DELETE FROM catalog_assets WHERE id = $1`, id); err != nil {
				fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
				return
			}
			writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
		}
		return
	}

	limit := int64(1 << 20)
	if action == "import" {
		limit = 5 << 20
	}
	var body map[string]any
	dec := json.NewDecoder(http.MaxBytesReader(w, r.Body, limit))
	dec.UseNumber()
	if err := dec.Decode(&body); err != nil || body == nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ hoặc quá lớn")
		return
	}

	var id int64
	if r.Method == http.MethodPatch {
		if id = catIDParam(r, action); id == 0 {
			fail(w, http.StatusBadRequest, "cần ?"+action+"=<số>")
			return
		}
	}

	// lỗi từ Postgres: trùng khóa → 409, khóa ngoại không có → 404
	dbFail := func(err error) {
		var pgErr *pgconn.PgError
		switch {
		case errors.As(err, &pgErr) && pgErr.Code == "23505":
			if action == "course" {
				fail(w, http.StatusConflict, "mã khóa học đã có")
			} else {
				fail(w, http.StatusConflict, "số bài này đã có trong khóa học")
			}
		case errors.As(err, &pgErr) && pgErr.Code == "23503":
			if action == "lesson" {
				fail(w, http.StatusNotFound, "không có khóa học này")
			} else {
				fail(w, http.StatusNotFound, "không có bài này")
			}
		default:
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		}
	}

	switch action {
	case "course":
		title := catText(body["title"], catMaxTitle)
		sortN, hasSort, ok := catInt(body["sort"], -catMaxSort, catMaxSort)
		if !ok {
			fail(w, http.StatusBadRequest, "thứ tự không hợp lệ")
			return
		}
		if r.Method == http.MethodPost {
			slug, _ := body["slug"].(string)
			slug = strings.TrimSpace(slug)
			if !catSlugRe.MatchString(slug) {
				fail(w, http.StatusBadRequest, "mã khóa học chỉ gồm chữ thường, số và dấu gạch ngang (tối đa 40 ký tự)")
				return
			}
			if title == "" {
				fail(w, http.StatusBadRequest, "cần tên khóa học")
				return
			}
			c, err := scanCourse(p.QueryRow(ctx,
				`INSERT INTO catalog_courses (slug, title, sort) VALUES ($1, $2, $3) RETURNING `+catCourseCols, slug, title, sortN))
			if err != nil {
				dbFail(err)
				return
			}
			writeJSON(w, http.StatusCreated, map[string]any{"course": c})
			return
		}
		if !catAbsent(body, "title") && title == "" {
			fail(w, http.StatusBadRequest, "cần tên khóa học")
			return
		}
		c, err := scanCourse(p.QueryRow(ctx,
			`UPDATE catalog_courses SET title = coalesce($2, title), sort = coalesce($3, sort) WHERE id = $1 RETURNING `+catCourseCols,
			id, catOptStr(title), catOptInt(sortN, hasSort)))
		if errors.Is(err, pgx.ErrNoRows) {
			fail(w, http.StatusNotFound, "không có khóa học này")
			return
		}
		if err != nil {
			dbFail(err)
			return
		}
		writeJSON(w, http.StatusOK, map[string]any{"course": c})

	case "lesson":
		num, hasNum, ok := catInt(body["num"], 0, catMaxNum)
		if !ok {
			fail(w, http.StatusBadRequest, "số bài không hợp lệ")
			return
		}
		title := catText(body["title"], catMaxTitle)
		if !catAbsent(body, "title") && title == "" {
			fail(w, http.StatusBadRequest, "cần tên bài")
			return
		}
		var zh *string
		if !catAbsent(body, "zh") {
			s, isStr := body["zh"].(string)
			if !isStr {
				fail(w, http.StatusBadRequest, "tên tiếng Trung không hợp lệ")
				return
			}
			s = clip(s, catMaxTitle)
			zh = &s
		}
		var visible *bool
		if !catAbsent(body, "visible") {
			v, isBool := body["visible"].(bool)
			if !isBool {
				fail(w, http.StatusBadRequest, "trạng thái hiện/ẩn không hợp lệ")
				return
			}
			visible = &v
		}
		sortN, hasSort, ok := catInt(body["sort"], -catMaxSort, catMaxSort)
		if !ok {
			fail(w, http.StatusBadRequest, "thứ tự không hợp lệ")
			return
		}
		var l catLesson
		var err error
		if r.Method == http.MethodPost {
			courseID, present, ok := catInt(body["courseId"], 1, catMaxID)
			if !ok || !present {
				fail(w, http.StatusBadRequest, "mã khóa học (courseId) không hợp lệ")
				return
			}
			if !hasNum {
				fail(w, http.StatusBadRequest, "số bài không hợp lệ")
				return
			}
			if title == "" {
				fail(w, http.StatusBadRequest, "cần tên bài")
				return
			}
			zhV, visV := "", true
			if zh != nil {
				zhV = *zh
			}
			if visible != nil {
				visV = *visible
			}
			l, err = scanLesson(p.QueryRow(ctx,
				`INSERT INTO catalog_lessons (course_id, num, title, zh, visible, sort) VALUES ($1, $2, $3, $4, $5, $6) RETURNING `+catLessonCols,
				courseID, num, title, zhV, visV, sortN))
			if err != nil {
				dbFail(err)
				return
			}
			writeJSON(w, http.StatusCreated, map[string]any{"lesson": l})
			return
		}
		l, err = scanLesson(p.QueryRow(ctx,
			`UPDATE catalog_lessons SET num = coalesce($2, num), title = coalesce($3, title), zh = coalesce($4, zh),
			        visible = coalesce($5, visible), sort = coalesce($6, sort) WHERE id = $1 RETURNING `+catLessonCols,
			id, catOptInt(num, hasNum), catOptStr(title), zh, visible, catOptInt(sortN, hasSort)))
		if errors.Is(err, pgx.ErrNoRows) {
			fail(w, http.StatusNotFound, "không có bài này")
			return
		}
		if err != nil {
			dbFail(err)
			return
		}
		writeJSON(w, http.StatusOK, map[string]any{"lesson": l})

	case "upload", "asset":
		lessonID, present, ok := catInt(body["lessonId"], 1, catMaxID)
		if !ok || !present {
			fail(w, http.StatusBadRequest, "mã bài (lessonId) không hợp lệ")
			return
		}
		if !catIn(catKinds, body["kind"]) {
			fail(w, http.StatusBadRequest, "loại file không hợp lệ")
			return
		}
		kind := body["kind"].(string)
		name := catText(body["name"], catMaxName)
		if name == "" {
			fail(w, http.StatusBadRequest, "cần tên file")
			return
		}
		size, hasSize, ok := catInt(body["size"], 0, catMaxSize)
		if !ok || (action == "upload" && !hasSize) {
			fail(w, http.StatusBadRequest, "dung lượng không hợp lệ")
			return
		}
		storage := "r2"
		if action == "asset" {
			storage, _ = body["storage"].(string)
		}
		if !catIn(catStorages, storage) {
			fail(w, http.StatusBadRequest, "nơi lưu không hợp lệ")
			return
		}
		if storage == "r2" && size > catMaxUpload {
			fail(w, http.StatusBadRequest, "file quá 200 MB")
			return
		}

		link := ""
		if action == "asset" && storage == "repo" {
			if link = catText(body["url"], catMaxURL); !catValidURL(link) {
				fail(w, http.StatusBadRequest, "đường dẫn không hợp lệ")
				return
			}
		}
		if action == "asset" && storage == "youtube" {
			if link = catYouTube(catText(body["url"], catMaxURL)); link == "" {
				fail(w, http.StatusBadRequest, "link YouTube không hợp lệ")
				return
			}
		}

		var slug string
		var lessonNum int
		err := p.QueryRow(ctx, `SELECT c.slug, l.num FROM catalog_lessons l JOIN catalog_courses c ON c.id = l.course_id WHERE l.id = $1`,
			lessonID).Scan(&slug, &lessonNum)
		if errors.Is(err, pgx.ErrNoRows) {
			fail(w, http.StatusNotFound, "không có bài này")
			return
		}
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		prefix := fmt.Sprintf("%s/%02d/", slug, lessonNum)

		key := ""
		if storage == "r2" {
			e := r2FromEnv()
			if action == "upload" {
				if !e.ready() {
					fail(w, http.StatusServiceUnavailable, catR2Missing)
					return
				}
				typ := catText(body["type"], 100)
				if !catTypeRe.MatchString(typ) {
					typ = "application/octet-stream"
				}
				key = fmt.Sprintf("%s%d-%s", prefix, time.Now().UnixMilli(), catSafeName(name))
				writeJSON(w, http.StatusOK, struct {
					PutURL    string            `json:"putUrl"`
					Key       string            `json:"key"`
					PublicURL string            `json:"publicUrl"`
					Headers   map[string]string `json:"headers"`
				}{e.url(http.MethodPut, key, 900), key, e.publicURL + "/" + key, map[string]string{"Content-Type": typ}})
				return
			}
			key = catText(body["key"], catMaxKey)
			if !strings.HasPrefix(key, prefix) || !catKeyRe.MatchString(key) || strings.Contains(key, "..") {
				fail(w, http.StatusBadRequest, "key R2 không thuộc bài này")
				return
			}
			if e.publicURL == "" {
				fail(w, http.StatusServiceUnavailable, catR2Missing)
				return
			}
			link = e.publicURL + "/" + key
		}

		a, err := scanAsset(p.QueryRow(ctx,
			`INSERT INTO catalog_assets (lesson_id, kind, name, size, url, storage, key) VALUES ($1, $2, $3, $4, $5, $6, $7) RETURNING `+catAssetCols,
			lessonID, kind, name, size, link, storage, key))
		if err != nil {
			dbFail(err)
			return
		}
		writeJSON(w, http.StatusCreated, map[string]any{"asset": a})

	default: // import
		courses, msg := catCheckImport(body)
		if msg != "" {
			fail(w, http.StatusBadRequest, msg)
			return
		}
		out, err := catRunImport(ctx, p, courses)
		if err != nil {
			dbFail(err)
			return
		}
		writeJSON(w, http.StatusOK, out)
	}
}

// tham số tuỳ chọn cho coalesce(): vắng thì NULL
func catOptStr(s string) *string {
	if s == "" {
		return nil
	}
	return &s
}

func catOptInt(n int64, present bool) *int64 {
	if !present {
		return nil
	}
	return &n
}
