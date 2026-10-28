package gobackend

// GET/PUT/PATCH /api/go/terms
//
// Thuật ngữ du lịch của trang "Ngọc học tiếng Trung" (hsk6/). Mỗi lần ghi là một phiên bản (dòng term_upload kèm bản sao
// cả danh sách); danh sách đang dùng (bảng term) luôn là bản mới nhất ĐANG BẬT, tắt/bật lại từng bản không mất dữ liệu.
// GET ai cũng đọc được (nội dung học, không bí mật); ?versions là lịch sử phiên bản, ?version=N là bản sao của bản N.
// ?check kiểm tra mật khẩu. PUT, PATCH cần mật khẩu (APP_SECRET hoặc HSK6_PASS).
// PUT ghi cả danh sách gửi lên thành bản mới (trang tự gộp khi chọn "thêm vào"), trong một transaction.
// PATCH ?version=N {active} tắt hoặc bật lại bản N, rồi dựng lại danh sách đang dùng từ bản mới nhất còn bật.
// Trang đọc file Excel và chuẩn hóa (TERM_BE trong BaiGiang/web/template.html), server kiểm tra lại từng trường.

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"
	"unicode/utf8"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

const termTables = `
CREATE TABLE IF NOT EXISTS term (
	key      text PRIMARY KEY,
	zh       text NOT NULL,
	pinyin   text NOT NULL,
	vi       text NOT NULL,
	grp      text NOT NULL,
	majors   jsonb NOT NULL,
	sessions text[] NOT NULL,
	n        integer NOT NULL
);
CREATE TABLE IF NOT EXISTS term_upload (
	id           bigserial PRIMARY KEY,
	file_name    text NOT NULL,
	summary_name text NOT NULL,
	sheets       jsonb NOT NULL,
	count        integer NOT NULL,
	created_at   timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE term_upload ADD COLUMN IF NOT EXISTS mode text NOT NULL DEFAULT 'replace';
ALTER TABLE term_upload ADD COLUMN IF NOT EXISTS terms jsonb;
ALTER TABLE term_upload ADD COLUMN IF NOT EXISTS active boolean NOT NULL DEFAULT true`

// sao lưu bản đang dùng: bản mới nhất đang bật mà ghi từ trước khi có lịch sử (chưa có bản sao) thì chép bảng term vào
const termBackup = `UPDATE term_upload SET terms = (SELECT COALESCE(jsonb_agg(jsonb_build_object('key', key, 'zh', zh, 'pinyin', pinyin,
		'vi', vi, 'group', grp, 'majors', majors, 'sessions', sessions, 'n', n) ORDER BY n, key), '[]') FROM term)
	WHERE id = (SELECT max(id) FROM term_upload WHERE active) AND terms IS NULL`

const termCols = `x(key text, zh text, pinyin text, vi text, "group" text, majors jsonb, sessions text[], n integer)`

const (
	maxTerms     = 5000
	maxTermsBody = 4 << 20 // ~1.500 thuật ngữ chỉ khoảng 500 KB
	maxVersions  = 100
)

// replace: ghi đè bằng file; add: trang đã gộp file vào danh sách cũ; restore: khôi phục một bản cũ
var termModes = map[string]bool{"replace": true, "add": true, "restore": true}

var (
	termTablesMu sync.Mutex
	termTablesOK bool
	isoDate      = regexp.MustCompile(`^\d{4}-\d{2}-\d{2}$`)
)

type major struct {
	Name  string `json:"name"`
	Group string `json:"group"`
	N     int64  `json:"n"`
}

type term struct {
	Key      string   `json:"key"`
	Zh       string   `json:"zh"`
	Pinyin   string   `json:"pinyin"`
	Vi       string   `json:"vi"`
	Group    string   `json:"group"`
	Majors   []major  `json:"majors"`
	Sessions []string `json:"sessions"`
	N        int64    `json:"n"`
}

type termUpload struct {
	FileName    string   `json:"fileName"`
	Mode        string   `json:"mode"`
	SummaryName string   `json:"summaryName"`
	Sheets      []string `json:"sheets"`
	Terms       []term   `json:"terms"`
}

type termVersion struct {
	Version   int64      `json:"version"`
	FileName  string     `json:"fileName"`
	Mode      string     `json:"mode"`
	Count     int        `json:"count"`
	CreatedAt *time.Time `json:"createdAt"`
	Saved     bool       `json:"saved"`
	Active    bool       `json:"active"`
}

type termSnapshot struct {
	Version     int64           `json:"version"`
	FileName    string          `json:"fileName"`
	SummaryName string          `json:"summaryName"`
	Sheets      json.RawMessage `json:"sheets"`
	Mode        string          `json:"mode"`
	UpdatedAt   *time.Time      `json:"updatedAt"`
	Terms       json.RawMessage `json:"terms"`
}

type termList struct {
	Version     int64           `json:"version"`
	FileName    *string         `json:"fileName"`
	SummaryName *string         `json:"summaryName"`
	Sheets      json.RawMessage `json:"sheets"`
	UpdatedAt   *time.Time      `json:"updatedAt"`
	Terms       []term          `json:"terms"`
}

// Bảng thuật ngữ tạo ở lần gọi đầu; lỗi thì lần sau thử lại
func termPool(ctx context.Context) (*pgxpool.Pool, error) {
	p, err := db(ctx)
	if err != nil {
		return nil, err
	}
	termTablesMu.Lock()
	defer termTablesMu.Unlock()
	if !termTablesOK {
		if _, err := p.Exec(ctx, termTables); err != nil {
			return nil, err
		}
		termTablesOK = true
	}
	return p, nil
}

func Terms(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet && r.Method != http.MethodPut && r.Method != http.MethodPatch {
		w.Header().Set("Allow", "GET, PUT, PATCH")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ GET, PUT và PATCH")
		return
	}
	// ?check: trang hsk6 kiểm tra mật khẩu lúc đăng nhập, không cần đến cơ sở dữ liệu
	if r.Method == http.MethodGet && r.URL.Query().Has("check") {
		if authorizedHsk6(r) {
			writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
		} else {
			fail(w, http.StatusUnauthorized, "sai mật khẩu")
		}
		return
	}
	if r.Method != http.MethodGet && !authorizedHsk6(r) {
		fail(w, http.StatusUnauthorized, "sai mật khẩu")
		return
	}
	ctx, cancel := context.WithTimeout(r.Context(), 15*time.Second)
	defer cancel()
	p, err := termPool(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
	}

	if r.Method == http.MethodGet && r.URL.Query().Has("versions") {
		list, err := termVersions(ctx, p)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, map[string]any{"versions": list})
		return
	}
	if r.Method == http.MethodGet && r.URL.Query().Has("version") {
		id, err := strconv.ParseInt(r.URL.Query().Get("version"), 10, 64)
		var snap *termSnapshot
		if err == nil && id > 0 {
			if snap, err = termSnapshotOf(ctx, p, id); err != nil {
				fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
				return
			}
		}
		if snap == nil {
			fail(w, http.StatusNotFound, "không có bản sao của phiên bản này")
			return
		}
		writeJSON(w, http.StatusOK, snap)
		return
	}
	if r.Method == http.MethodGet {
		list, err := loadTerms(ctx, p)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, list)
		return
	}

	if r.Method == http.MethodPatch {
		var body struct {
			Active *bool `json:"active"`
		}
		id, err := strconv.ParseInt(r.URL.Query().Get("version"), 10, 64)
		if err != nil || id <= 0 || json.NewDecoder(http.MaxBytesReader(w, r.Body, 1<<10)).Decode(&body) != nil || body.Active == nil {
			fail(w, http.StatusBadRequest, "cần ?version=N và {active: true|false}")
			return
		}
		out, msg, err := toggleTerms(ctx, p, id, *body.Active)
		switch {
		case err != nil:
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		case out == nil && msg == "":
			fail(w, http.StatusNotFound, "không có phiên bản này")
		case msg != "":
			fail(w, http.StatusBadRequest, msg)
		default:
			writeJSON(w, http.StatusOK, out)
		}
		return
	}

	var body termUpload
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, maxTermsBody)).Decode(&body); err != nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ hoặc quá lớn")
		return
	}
	if msg := checkTerms(body); msg != "" {
		fail(w, http.StatusBadRequest, msg)
		return
	}
	out, err := replaceTerms(ctx, p, body)
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	writeJSON(w, http.StatusOK, out)
}

func strOK(s string, max int, required bool) bool {
	return utf8.RuneCountInString(s) <= max && (!required || strings.TrimSpace(s) != "")
}

func intOK(n int64) bool { return n >= 0 && n < 1<<31 }

// Trả thông báo lỗi đầu tiên, rỗng nếu dữ liệu đúng định dạng (giống check() của bản Node)
func checkTerms(b termUpload) string {
	if !strOK(b.FileName, 200, true) {
		return "thiếu tên file"
	}
	if !strOK(b.SummaryName, 200, true) {
		return "thiếu tên sheet tổng hợp"
	}
	if b.Mode != "" && !termModes[b.Mode] {
		return "cách ghi không hợp lệ"
	}
	if b.Sheets == nil || len(b.Sheets) > 50 {
		return "danh sách sheet không hợp lệ"
	}
	for _, s := range b.Sheets {
		if !strOK(s, 200, true) {
			return "danh sách sheet không hợp lệ"
		}
	}
	if len(b.Terms) == 0 {
		return "file không có thuật ngữ nào"
	}
	if len(b.Terms) > maxTerms {
		return fmt.Sprintf("tối đa %d thuật ngữ", maxTerms)
	}
	seen := make(map[string]bool, len(b.Terms))
	for i, t := range b.Terms {
		at := fmt.Sprintf("thuật ngữ thứ %d", i+1)
		if !strOK(t.Key, 200, true) || !strOK(t.Zh, 200, true) {
			return at + ": thiếu chữ Hán"
		}
		if seen[t.Key] {
			return fmt.Sprintf("%s: trùng \"%s\"", at, t.Key)
		}
		seen[t.Key] = true
		if !strOK(t.Pinyin, 300, false) || !strOK(t.Vi, 1000, false) || !strOK(t.Group, 200, false) {
			return fmt.Sprintf("%s (%s): pinyin, nghĩa hoặc nhóm không hợp lệ", at, t.Zh)
		}
		if !intOK(t.N) {
			return fmt.Sprintf("%s (%s): thứ tự không hợp lệ", at, t.Zh)
		}
		if t.Majors == nil || len(t.Majors) > 20 {
			return fmt.Sprintf("%s (%s): chuyên ngành không hợp lệ", at, t.Zh)
		}
		for _, m := range t.Majors {
			if !strOK(m.Name, 200, true) || !strOK(m.Group, 200, false) || !intOK(m.N) {
				return fmt.Sprintf("%s (%s): chuyên ngành không hợp lệ", at, t.Zh)
			}
		}
		if t.Sessions == nil || len(t.Sessions) > 100 {
			return fmt.Sprintf("%s (%s): buổi học không hợp lệ", at, t.Zh)
		}
		for _, d := range t.Sessions {
			if !isoDate.MatchString(d) {
				return fmt.Sprintf("%s (%s): buổi học không hợp lệ", at, t.Zh)
			}
		}
	}
	return ""
}

func loadTerms(ctx context.Context, p *pgxpool.Pool) (termList, error) {
	l := termList{Sheets: json.RawMessage("[]"), Terms: []term{}}
	err := p.QueryRow(ctx, `SELECT id, file_name, summary_name, sheets, created_at FROM term_upload WHERE active ORDER BY id DESC LIMIT 1`).
		Scan(&l.Version, &l.FileName, &l.SummaryName, &l.Sheets, &l.UpdatedAt)
	if err != nil && !errors.Is(err, pgx.ErrNoRows) {
		return l, err
	}
	l.UpdatedAt = utc(l.UpdatedAt)
	rows, err := p.Query(ctx, `SELECT key, zh, pinyin, vi, grp, majors, sessions, n FROM term ORDER BY n, key`)
	if err != nil {
		return l, err
	}
	defer rows.Close()
	for rows.Next() {
		var t term
		var majors []byte
		if err := rows.Scan(&t.Key, &t.Zh, &t.Pinyin, &t.Vi, &t.Group, &majors, &t.Sessions, &t.N); err != nil {
			return l, err
		}
		if err := json.Unmarshal(majors, &t.Majors); err != nil {
			return l, err
		}
		l.Terms = append(l.Terms, t)
	}
	return l, rows.Err()
}

func termVersions(ctx context.Context, p *pgxpool.Pool) ([]termVersion, error) {
	rows, err := p.Query(ctx, fmt.Sprintf(`SELECT id, file_name, mode, count, created_at, terms IS NOT NULL, active
		FROM term_upload ORDER BY id DESC LIMIT %d`, maxVersions))
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	list := []termVersion{}
	for rows.Next() {
		var v termVersion
		if err := rows.Scan(&v.Version, &v.FileName, &v.Mode, &v.Count, &v.CreatedAt, &v.Saved, &v.Active); err != nil {
			return nil, err
		}
		v.CreatedAt = utc(v.CreatedAt)
		list = append(list, v)
	}
	return list, rows.Err()
}

// Bản sao của một phiên bản; nil nếu không có bản đó hoặc bản đó ghi từ trước khi có lịch sử
func termSnapshotOf(ctx context.Context, p *pgxpool.Pool, id int64) (*termSnapshot, error) {
	var s termSnapshot
	var terms []byte
	err := p.QueryRow(ctx, `SELECT id, file_name, summary_name, sheets, mode, created_at, terms FROM term_upload WHERE id = $1`, id).
		Scan(&s.Version, &s.FileName, &s.SummaryName, &s.Sheets, &s.Mode, &s.UpdatedAt, &terms)
	if errors.Is(err, pgx.ErrNoRows) || (err == nil && terms == nil) {
		return nil, nil
	}
	if err != nil {
		return nil, err
	}
	s.UpdatedAt, s.Terms = utc(s.UpdatedAt), terms
	return &s, nil
}

// Tắt/bật lại bản id rồi dựng lại bảng term từ bản mới nhất còn bật (không còn bản nào thì danh sách trống).
// Không có bản đó: (nil, "", nil); bật lại bản không có bản sao: (nil, thông báo lỗi, nil).
func toggleTerms(ctx context.Context, p *pgxpool.Pool, id int64, active bool) (map[string]any, string, error) {
	tx, err := p.Begin(ctx)
	if err != nil {
		return nil, "", err
	}
	defer tx.Rollback(ctx)
	if _, err := tx.Exec(ctx, termBackup); err != nil {
		return nil, "", err
	}
	var saved bool
	err = tx.QueryRow(ctx, `SELECT terms IS NOT NULL FROM term_upload WHERE id = $1 FOR UPDATE`, id).Scan(&saved)
	if errors.Is(err, pgx.ErrNoRows) {
		return nil, "", nil
	}
	if err != nil {
		return nil, "", err
	}
	if active && !saved {
		return nil, "bản này ghi từ trước khi có lịch sử, không có bản sao để bật lại", nil
	}
	if _, err := tx.Exec(ctx, `UPDATE term_upload SET active = $2 WHERE id = $1`, id, active); err != nil {
		return nil, "", err
	}
	if _, err := tx.Exec(ctx, `DELETE FROM term`); err != nil {
		return nil, "", err
	}
	if _, err := tx.Exec(ctx, `INSERT INTO term (key, zh, pinyin, vi, grp, majors, sessions, n)
		SELECT x.key, x.zh, x.pinyin, x.vi, x."group", x.majors, x.sessions, x.n
		FROM term_upload u, jsonb_to_recordset(u.terms) AS `+termCols+`
		WHERE u.id = (SELECT max(id) FROM term_upload WHERE active) AND u.terms IS NOT NULL`); err != nil {
		return nil, "", err
	}
	var cur *int64
	var n int64
	if err := tx.QueryRow(ctx, `SELECT (SELECT max(id) FROM term_upload WHERE active), (SELECT count(*) FROM term)`).Scan(&cur, &n); err != nil {
		return nil, "", err
	}
	if err := tx.Commit(ctx); err != nil {
		return nil, "", err
	}
	version := int64(0)
	if cur != nil {
		version = *cur
	}
	return map[string]any{"version": version, "count": n}, "", nil
}

// Ghi đè trong một transaction: lỗi giữa chừng thì giữ nguyên danh sách cũ
func replaceTerms(ctx context.Context, p *pgxpool.Pool, b termUpload) (map[string]any, error) {
	terms, err := json.Marshal(b.Terms)
	if err != nil {
		return nil, err
	}
	sheets, err := json.Marshal(b.Sheets)
	if err != nil {
		return nil, err
	}
	tx, err := p.Begin(ctx)
	if err != nil {
		return nil, err
	}
	defer tx.Rollback(ctx)
	if _, err := tx.Exec(ctx, termBackup); err != nil {
		return nil, err
	}
	if _, err := tx.Exec(ctx, `DELETE FROM term`); err != nil {
		return nil, err
	}
	if _, err := tx.Exec(ctx, `INSERT INTO term (key, zh, pinyin, vi, grp, majors, sessions, n)
		SELECT x.key, x.zh, x.pinyin, x.vi, x."group", x.majors, x.sessions, x.n
		FROM jsonb_to_recordset($1::jsonb) AS `+termCols, string(terms)); err != nil {
		return nil, err
	}
	var id int64
	var at *time.Time
	mode := b.Mode
	if mode == "" {
		mode = "replace"
	}
	if err := tx.QueryRow(ctx, `INSERT INTO term_upload (file_name, summary_name, sheets, count, mode, terms)
		VALUES ($1, $2, $3, $4, $5, $6) RETURNING id, created_at`, b.FileName, b.SummaryName, string(sheets), len(b.Terms), mode, string(terms)).Scan(&id, &at); err != nil {
		return nil, err
	}
	if err := tx.Commit(ctx); err != nil {
		return nil, err
	}
	return map[string]any{"version": id, "count": len(b.Terms), "updatedAt": utc(at)}, nil
}
