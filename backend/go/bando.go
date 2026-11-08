// Nhật ký chuyến đi của trang bản đồ (apps/ban-do). Bản Node: backend/node/bando.js, cùng hợp đồng.
// Đường dẫn, dữ liệu vào/ra và mã lỗi giống hệt nhau, xem phần chú ở đầu file bên Node.
package gobackend

import (
	"bytes"
	"context"
	"crypto/subtle"
	"encoding/json"
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

// pgx dùng giao thức mở rộng nên mỗi lần Exec chỉ một câu lệnh, phải tách ra
var banDoTables = []string{
	`DO $$ BEGIN
		CREATE TYPE province_status AS ENUM ('none', 'visited', 'wish');
	EXCEPTION WHEN duplicate_object THEN NULL;
	END $$`,
	`CREATE TABLE IF NOT EXISTS provinces (
		code       text PRIMARY KEY,
		status     province_status NOT NULL DEFAULT 'none',
		updated_at timestamptz NOT NULL DEFAULT now()
	)`,
	`CREATE TABLE IF NOT EXISTS trips (
		id            serial PRIMARY KEY,
		province_code text NOT NULL REFERENCES provinces(code) ON DELETE CASCADE,
		from_date     date,
		to_date       date,
		companions    text NOT NULL DEFAULT '',
		rate          integer NOT NULL DEFAULT 0,
		places        jsonb NOT NULL DEFAULT '[]'::jsonb,
		note          text NOT NULL DEFAULT '',
		created_at    timestamptz NOT NULL DEFAULT now(),
		updated_at    timestamptz NOT NULL DEFAULT now()
	)`,
	`CREATE INDEX IF NOT EXISTS trips_province_idx ON trips (province_code)`,
	`CREATE INDEX IF NOT EXISTS trips_from_idx     ON trips (from_date)`,
	// tên người thêm/sửa (bảng tạo trước khi có tài khoản thì thêm cột, dòng cũ để trống)
	`ALTER TABLE provinces ADD COLUMN IF NOT EXISTS updated_by text NOT NULL DEFAULT ''`,
	`ALTER TABLE trips ADD COLUMN IF NOT EXISTS created_by text NOT NULL DEFAULT ''`,
	`ALTER TABLE trips ADD COLUMN IF NOT EXISTS updated_by text NOT NULL DEFAULT ''`,
	`CREATE TABLE IF NOT EXISTS love_notes (
		id         serial PRIMARY KEY,
		body       text NOT NULL,
		created_by text NOT NULL DEFAULT '',
		created_at timestamptz NOT NULL DEFAULT now()
	)`,
}

var (
	banDoOnce sync.Once
	banDoErr  error
)

func banDoPool(ctx context.Context) (*pgxpool.Pool, error) {
	p, err := db(ctx)
	if err != nil {
		return nil, err
	}
	banDoOnce.Do(func() {
		for _, q := range banDoTables {
			if _, banDoErr = p.Exec(ctx, q); banDoErr != nil {
				return
			}
		}
	})
	return p, banDoErr
}

type banDoTrip struct {
	ID     int      `json:"id"`
	From   string   `json:"from"`
	To     string   `json:"to"`
	With   string   `json:"with"`
	Rate   int      `json:"rate"`
	Places []string `json:"places"`
	Note   string   `json:"note"`
	By     string   `json:"by"`
	Edited string   `json:"editedBy"`
}

type banDoEntry struct {
	Status string      `json:"status"`
	Trips  []banDoTrip `json:"trips"`
}

const (
	maxPlaces = 120
	maxPlace  = 120
	maxWith   = 200
	maxNote   = 8000
)

var banDoCode = regexp.MustCompile(`^[a-z][a-z0-9-]{1,39}$`)

// from_date/to_date ép sang text ngay trong câu lệnh, để ngày không trôi theo múi giờ
const banDoCols = `id, province_code, from_date::text, to_date::text, companions, rate, places, note, created_by, updated_by`

// cắt theo ký tự chứ không theo byte, để không xén đôi chữ tiếng Việt
func clip(s string, limit int) string {
	s = strings.TrimSpace(s)
	r := []rune(s)
	if len(r) > limit {
		return string(r[:limit])
	}
	return s
}

// "" là chưa rõ ngày; còn lại phải là một ngày có thật dạng YYYY-MM-DD
func banDoDay(v string) (*string, bool) {
	if v == "" {
		return nil, true
	}
	d, err := time.Parse("2006-01-02", v)
	if err != nil || d.Format("2006-01-02") != v {
		return nil, false
	}
	return &v, true
}

type banDoBody struct {
	Status string   `json:"status"`
	From   string   `json:"from"`
	To     string   `json:"to"`
	With   string   `json:"with"`
	Rate   int      `json:"rate"`
	Places []string `json:"places"`
	Note   string   `json:"note"`
}

// Soát lại dữ liệu từ trình duyệt; trả về câu lỗi rỗng nếu hợp lệ.
func checkBanDoTrip(b banDoBody) (from, to *string, places []string, msg string) {
	from, ok := banDoDay(b.From)
	if !ok {
		return nil, nil, nil, "ngày không hợp lệ"
	}
	to, ok = banDoDay(b.To)
	if !ok {
		return nil, nil, nil, "ngày không hợp lệ"
	}
	if from != nil && to != nil && *to < *from {
		return nil, nil, nil, "ngày về trước ngày đi"
	}
	if b.Rate < 0 || b.Rate > 5 {
		return nil, nil, nil, "số sao không hợp lệ"
	}
	places = []string{}
	for _, p := range b.Places {
		if s := clip(p, maxPlace); s != "" && len(places) < maxPlaces {
			places = append(places, s)
		}
	}
	return from, to, places, ""
}

func scanBanDoTrip(rows pgx.Rows) (string, banDoTrip, error) {
	var t banDoTrip
	var code string
	var from, to *string
	err := rows.Scan(&t.ID, &code, &from, &to, &t.With, &t.Rate, &t.Places, &t.Note, &t.By, &t.Edited)
	if from != nil {
		t.From = *from
	}
	if to != nil {
		t.To = *to
	}
	if t.Places == nil {
		t.Places = []string{}
	}
	return code, t, err
}

const maxLove = 2000

// Báo qua Telegram khi có lời nhắn mới của người trong TELEGRAM_NOTIFY_FROM (mặc định "Ngọc").
// Cần TELEGRAM_BOT_TOKEN và TELEGRAM_CHAT_ID; thiếu thì thôi. Lỗi gửi không làm hỏng việc lưu lời nhắn.
func notifyLove(ctx context.Context, n loveNote) {
	token, chat := os.Getenv("TELEGRAM_BOT_TOKEN"), os.Getenv("TELEGRAM_CHAT_ID")
	from := os.Getenv("TELEGRAM_NOTIFY_FROM")
	if from == "" {
		from = "Ngọc"
	}
	match := false
	for _, f := range strings.Split(from, ",") {
		if strings.TrimSpace(f) == n.By {
			match = true
		}
	}
	if token == "" || chat == "" || !match {
		return
	}
	body, _ := json.Marshal(map[string]string{"chat_id": chat, "text": "💌 " + n.By + " vừa để lại lời nhắn:\n\n" + n.Text})
	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
	defer cancel()
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, "https://api.telegram.org/bot"+token+"/sendMessage", bytes.NewReader(body))
	if err != nil {
		return
	}
	req.Header.Set("Content-Type", "application/json")
	if res, err := http.DefaultClient.Do(req); err == nil {
		res.Body.Close()
	}
}

type loveNote struct {
	ID   int    `json:"id"`
	Text string `json:"text"`
	By   string `json:"by"`
	At   string `json:"at"`
}

// Note tình yêu: lời nhắn riêng của hai người, ?notes trên cùng endpoint (xem chú thích bên Node).
func banDoNotes(w http.ResponseWriter, r *http.Request, p *pgxpool.Pool, user *AppUser) {
	ctx := r.Context()
	if user == nil {
		fail(w, http.StatusUnauthorized, "cần đăng nhập")
		return
	}
	right := "write"
	if r.Method == http.MethodGet {
		right = "read"
	}
	if !can(user, right) {
		fail(w, http.StatusForbidden, "tài khoản này không có quyền")
		return
	}
	scan := func(row pgx.Row) (loveNote, error) {
		var n loveNote
		var at time.Time
		err := row.Scan(&n.ID, &n.Text, &n.By, &at)
		n.At = at.UTC().Format("2006-01-02T15:04:05.000Z")
		return n, err
	}
	switch r.Method {
	case http.MethodGet:
		rows, err := p.Query(ctx, `SELECT id, body, created_by, created_at FROM love_notes ORDER BY created_at DESC, id DESC LIMIT 300`)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc ghi dữ liệu")
			return
		}
		defer rows.Close()
		list := []loveNote{}
		for rows.Next() {
			n, err := scan(rows)
			if err != nil {
				fail(w, http.StatusInternalServerError, "lỗi đọc ghi dữ liệu")
				return
			}
			list = append(list, n)
		}
		writeJSON(w, http.StatusOK, map[string]any{"notes": list})
	case http.MethodPost:
		var body struct {
			Text string `json:"text"`
		}
		if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, 1<<16)).Decode(&body); err != nil {
			fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ hoặc quá lớn")
			return
		}
		t := clip(body.Text, maxLove)
		if t == "" {
			fail(w, http.StatusBadRequest, "lời nhắn đang trống")
			return
		}
		n, err := scan(p.QueryRow(ctx,
			`INSERT INTO love_notes (body, created_by) VALUES ($1, $2) RETURNING id, body, created_by, created_at`, t, user.Name))
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc ghi dữ liệu")
			return
		}
		notifyLove(ctx, n) // chờ gửi xong: trên Vercel trả lời rồi là function có thể bị dừng
		writeJSON(w, http.StatusOK, map[string]any{"note": n})
	case http.MethodDelete:
		id, err := strconv.Atoi(r.URL.Query().Get("id"))
		if err != nil || id <= 0 {
			fail(w, http.StatusBadRequest, "cần ?id=<số>")
			return
		}
		var q string
		args := []any{id}
		if can(user, "delete") {
			q = `DELETE FROM love_notes WHERE id = $1`
		} else {
			q = `DELETE FROM love_notes WHERE id = $1 AND created_by = $2`
			args = append(args, user.Name)
		}
		tag, err := p.Exec(ctx, q, args...)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc ghi dữ liệu")
			return
		}
		if tag.RowsAffected() == 0 {
			fail(w, http.StatusNotFound, "không còn lời nhắn này nữa")
			return
		}
		writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
	default:
		fail(w, http.StatusMethodNotAllowed, "lời nhắn chỉ hỗ trợ GET, POST và DELETE")
	}
}

// Webhook Telegram: bạn trả lời bot thì tin đó lên Note tình yêu (xem chú thích bên Node).
func banDoTelegram(w http.ResponseWriter, r *http.Request, p *pgxpool.Pool) {
	ctx := r.Context()
	secret := os.Getenv("TELEGRAM_WEBHOOK_SECRET")
	got := r.Header.Get("X-Telegram-Bot-Api-Secret-Token")
	if secret == "" || subtle.ConstantTimeCompare([]byte(got), []byte(secret)) != 1 {
		fail(w, http.StatusUnauthorized, "sai mã webhook")
		return
	}
	var update struct {
		Message *struct {
			Text string `json:"text"`
			Chat struct {
				ID int64 `json:"id"`
			} `json:"chat"`
		} `json:"message"`
	}
	ok := map[string]bool{"ok": true}
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, 1<<20)).Decode(&update); err != nil || update.Message == nil {
		writeJSON(w, http.StatusOK, ok)
		return
	}
	msg := update.Message
	t := clip(msg.Text, maxLove)
	if strconv.FormatInt(msg.Chat.ID, 10) != os.Getenv("TELEGRAM_CHAT_ID") || t == "" {
		writeJSON(w, http.StatusOK, ok)
		return
	}
	reply := func(text string) {
		writeJSON(w, http.StatusOK, map[string]any{"method": "sendMessage", "chat_id": msg.Chat.ID, "text": text})
	}
	if strings.HasPrefix(t, "/") {
		reply("Nhắn gì cho bot là lời đó lên Note tình yêu 💌")
		return
	}
	as := os.Getenv("TELEGRAM_REPLY_AS")
	if as == "" {
		as = "Đức"
	}
	if _, err := p.Exec(ctx, `INSERT INTO love_notes (body, created_by) VALUES ($1, $2)`, t, as); err != nil {
		reply("⚠️ Chưa lưu được, nhắn lại sau nhé")
		return
	}
	reply("✅ Đã đăng lên Note tình yêu")
}

// BanDo xử lý /api/go/ban-do.
func BanDo(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	q := r.URL.Query()

	switch r.Method {
	case http.MethodGet, http.MethodPut, http.MethodPost, http.MethodPatch, http.MethodDelete:
	default:
		w.Header().Set("Allow", "GET, PUT, POST, PATCH, DELETE")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ GET, PUT, POST, PATCH và DELETE")
		return
	}

	p, err := banDoPool(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
	}

	if r.Method == http.MethodPost && q.Has("telegram") {
		banDoTelegram(w, r, p)
		return
	}

	var user *AppUser
	if r.Method != http.MethodGet || q.Has("check") || q.Has("notes") {
		if user, err = currentUser(ctx, r); err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
	}
	if q.Has("notes") {
		banDoNotes(w, r, p, user)
		return
	}
	// hỏi xem phiên đăng nhập còn dùng được không
	if r.Method == http.MethodGet && q.Has("check") {
		if user != nil {
			writeJSON(w, http.StatusOK, map[string]any{"ok": true, "user": user})
		} else {
			fail(w, http.StatusUnauthorized, "chưa đăng nhập")
		}
		return
	}
	if r.Method != http.MethodGet {
		right := "write"
		if r.Method == http.MethodDelete {
			right = "delete"
		}
		if user == nil {
			fail(w, http.StatusUnauthorized, "cần đăng nhập")
			return
		}
		if !can(user, right) {
			fail(w, http.StatusForbidden, "tài khoản này không có quyền sửa")
			return
		}
	}

	if r.Method == http.MethodGet {
		entries := map[string]*banDoEntry{}
		rows, err := p.Query(ctx, `SELECT code, status FROM provinces`)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		for rows.Next() {
			var code, status string
			if err := rows.Scan(&code, &status); err != nil {
				rows.Close()
				fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
				return
			}
			entries[code] = &banDoEntry{Status: status, Trips: []banDoTrip{}}
		}
		rows.Close()

		tripRows, err := p.Query(ctx, `SELECT `+banDoCols+` FROM trips ORDER BY from_date ASC NULLS LAST, id ASC`)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		defer tripRows.Close()
		for tripRows.Next() {
			code, t, err := scanBanDoTrip(tripRows)
			if err != nil {
				fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
				return
			}
			if entries[code] == nil {
				entries[code] = &banDoEntry{Status: "none", Trips: []banDoTrip{}}
			}
			entries[code].Trips = append(entries[code].Trips, t)
		}
		writeJSON(w, http.StatusOK, map[string]any{"entries": entries})
		return
	}

	code := q.Get("province")
	if !banDoCode.MatchString(code) {
		fail(w, http.StatusBadRequest, "cần ?province=<mã tỉnh>")
		return
	}

	if r.Method == http.MethodDelete {
		id, err := strconv.Atoi(q.Get("id"))
		if err != nil || id <= 0 {
			fail(w, http.StatusBadRequest, "cần ?id=<số>")
			return
		}
		// kèm mã tỉnh để id gửi bừa không xoá nhầm chuyến của tỉnh khác
		tag, err := p.Exec(ctx, `DELETE FROM trips WHERE id = $1 AND province_code = $2`, id, code)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		if tag.RowsAffected() == 0 {
			fail(w, http.StatusNotFound, "không còn chuyến này nữa")
			return
		}
		writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
		return
	}

	var body banDoBody
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, 1<<20)).Decode(&body); err != nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ hoặc quá lớn")
		return
	}

	if r.Method == http.MethodPut {
		if body.Status != "none" && body.Status != "visited" && body.Status != "wish" {
			fail(w, http.StatusBadRequest, "trạng thái không hợp lệ")
			return
		}
		_, err := p.Exec(ctx,
			`INSERT INTO provinces (code, status, updated_by) VALUES ($1, $2, $3)
			 ON CONFLICT (code) DO UPDATE SET status = EXCLUDED.status, updated_by = EXCLUDED.updated_by, updated_at = now()`,
			code, body.Status, user.Name)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
		return
	}

	from, to, places, msg := checkBanDoTrip(body)
	if msg != "" {
		fail(w, http.StatusBadRequest, msg)
		return
	}
	with, note := clip(body.With, maxWith), clip(body.Note, maxNote)

	if r.Method == http.MethodPost {
		tx, err := p.Begin(ctx)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		defer tx.Rollback(ctx)
		// ghi chuyến đầu tiên là tỉnh thành "đã đi" luôn, và trips cần dòng tỉnh có sẵn
		if _, err := tx.Exec(ctx,
			`INSERT INTO provinces (code, status) VALUES ($1, 'visited')
			 ON CONFLICT (code) DO UPDATE SET status = 'visited', updated_at = now()`, code); err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		rows, err := tx.Query(ctx,
			`INSERT INTO trips (province_code, from_date, to_date, companions, rate, places, note, created_by, updated_by)
			 VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $8) RETURNING `+banDoCols,
			code, from, to, with, body.Rate, places, note, user.Name)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		if !rows.Next() {
			rows.Close()
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		_, trip, err := scanBanDoTrip(rows)
		rows.Close()
		if err != nil || tx.Commit(ctx) != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, map[string]any{"trip": trip})
		return
	}

	id, err := strconv.Atoi(q.Get("id"))
	if err != nil || id <= 0 {
		fail(w, http.StatusBadRequest, "cần ?id=<số>")
		return
	}
	rows, err := p.Query(ctx,
		`UPDATE trips SET from_date = $3, to_date = $4, companions = $5, rate = $6,
		                  places = $7, note = $8, updated_by = $9, updated_at = now()
		 WHERE id = $1 AND province_code = $2 RETURNING `+banDoCols,
		id, code, from, to, with, body.Rate, places, note, user.Name)
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	defer rows.Close()
	if !rows.Next() {
		fail(w, http.StatusNotFound, "không còn chuyến này nữa")
		return
	}
	_, trip, err := scanBanDoTrip(rows)
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	writeJSON(w, http.StatusOK, map[string]any{"trip": trip})
}
