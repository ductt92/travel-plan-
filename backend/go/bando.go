// Nhật ký chuyến đi của trang bản đồ (apps/ban-do). Bản Node: backend/node/bando.js, cùng hợp đồng.
// Đường dẫn, dữ liệu vào/ra và mã lỗi giống hệt nhau, xem phần chú ở đầu file bên Node.
package gobackend

import (
	"context"
	"encoding/json"
	"net/http"
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
const banDoCols = `id, province_code, from_date::text, to_date::text, companions, rate, places, note`

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
	err := rows.Scan(&t.ID, &code, &from, &to, &t.With, &t.Rate, &t.Places, &t.Note)
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

	// trang bấm Đăng nhập thì hỏi đúng câu này, chưa cần tới cơ sở dữ liệu
	if r.Method == http.MethodGet && q.Has("check") {
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

	p, err := banDoPool(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
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
			`INSERT INTO provinces (code, status) VALUES ($1, $2)
			 ON CONFLICT (code) DO UPDATE SET status = EXCLUDED.status, updated_at = now()`, code, body.Status)
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
			`INSERT INTO trips (province_code, from_date, to_date, companions, rate, places, note)
			 VALUES ($1, $2, $3, $4, $5, $6, $7) RETURNING `+banDoCols,
			code, from, to, with, body.Rate, places, note)
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
		                  places = $7, note = $8, updated_at = now()
		 WHERE id = $1 AND province_code = $2 RETURNING `+banDoCols,
		id, code, from, to, with, body.Rate, places, note)
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
