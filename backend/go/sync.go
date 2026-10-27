package gobackend

// GET/PUT /api/go/sync?key=<khóa>
//
// Mỗi khóa localStorage của các app (bản đồ, tiến độ học) là một dòng trong bảng docs.
// Ghi theo kiểu khóa lạc quan: client gửi kèm base (phiên bản nó đang có); nếu máy khác
// đã ghi trước thì trả 409 kèm bản mới nhất để client gộp rồi gửi lại.

import (
	"context"
	"encoding/json"
	"errors"
	"net/http"
	"time"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

// Chỉ nhận các khóa đã biết để không ai ghi rác vào DB
var allowedKeys = map[string]bool{
	"dadiqua-trip": true, // dấu tích địa điểm đã ghé trong chuyến đi
	"da-di-qua-v1": true, // trạng thái + ghi chú từng tỉnh
	"hanlo-v2":     true, // tiến độ học tiếng Trung
}

const maxBody = 1 << 20 // 1 MB mỗi tài liệu là quá đủ

type doc struct {
	Key       string          `json:"key"`
	Data      json.RawMessage `json:"data"`
	Version   int64           `json:"version"`
	UpdatedAt *time.Time      `json:"updatedAt"`
}

func Sync(w http.ResponseWriter, r *http.Request) {
	if !authorized(r) {
		fail(w, http.StatusUnauthorized, "sai mã đồng bộ")
		return
	}
	key := r.URL.Query().Get("key")
	if !allowedKeys[key] {
		fail(w, http.StatusBadRequest, "khóa không hợp lệ")
		return
	}
	ctx, cancel := context.WithTimeout(r.Context(), 8*time.Second)
	defer cancel()
	p, err := db(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
	}

	switch r.Method {
	case http.MethodGet:
		d, err := load(ctx, p, key)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, d)

	case http.MethodPut:
		var body struct {
			Data json.RawMessage `json:"data"`
			Base int64           `json:"base"`
		}
		if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, maxBody)).Decode(&body); err != nil || len(body.Data) == 0 || !json.Valid(body.Data) || string(body.Data) == "null" {
			fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
			return
		}
		d, ok, err := save(ctx, p, key, body.Data, body.Base)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		if !ok {
			writeJSON(w, http.StatusConflict, d) // máy khác đã ghi trước: trả bản mới nhất
			return
		}
		writeJSON(w, http.StatusOK, d)

	default:
		w.Header().Set("Allow", "GET, PUT")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ GET và PUT")
	}
}

// Chưa có dòng nào thì trả version 0, data null
func load(ctx context.Context, p *pgxpool.Pool, key string) (doc, error) {
	d := doc{Key: key, Data: json.RawMessage("null")}
	err := p.QueryRow(ctx, `SELECT data, version, updated_at FROM docs WHERE key = $1`, key).Scan(&d.Data, &d.Version, &d.UpdatedAt)
	if errors.Is(err, pgx.ErrNoRows) {
		return d, nil
	}
	return d, err
}

// Ghi khi phiên bản trên DB vẫn bằng base; ok=false nghĩa là xung đột và d là bản hiện tại
func save(ctx context.Context, p *pgxpool.Pool, key string, data json.RawMessage, base int64) (doc, bool, error) {
	d := doc{Key: key, Data: data}
	var err error
	if base == 0 {
		err = p.QueryRow(ctx, `INSERT INTO docs (key, data, version) VALUES ($1, $2, 1)
			ON CONFLICT (key) DO NOTHING RETURNING version, updated_at`, key, data).Scan(&d.Version, &d.UpdatedAt)
	} else {
		err = p.QueryRow(ctx, `UPDATE docs SET data = $2, version = version + 1, updated_at = now()
			WHERE key = $1 AND version = $3 RETURNING version, updated_at`, key, data, base).Scan(&d.Version, &d.UpdatedAt)
	}
	if errors.Is(err, pgx.ErrNoRows) {
		cur, err := load(ctx, p, key)
		return cur, false, err
	}
	return d, err == nil, err
}
