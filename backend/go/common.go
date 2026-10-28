// Package gobackend: bản Go của API (bản Node nằm ở backend/node, cùng hợp đồng).
// Các file trong api/go/ chỉ là lối vào mỏng để Vercel tạo function, logic nằm ở đây.
//
// Biến môi trường:
//   DATABASE_URL    chuỗi kết nối Postgres (Neon trên Vercel, Docker ở máy)
//   APP_SECRET      mã chung, client gửi qua header X-App-Secret
//   GEMINI_API_KEY  khóa Gemini cho /api/go/ai
package gobackend

import (
	"context"
	"crypto/subtle"
	"encoding/json"
	"errors"
	"net/http"
	"os"
	"sync"

	"github.com/jackc/pgx/v5/pgxpool"
)

var (
	poolOnce sync.Once
	pool     *pgxpool.Pool
	poolErr  error
)

// Một pool dùng lại giữa các lần gọi khi function còn "ấm"; tạo bảng ở lần đầu.
// Bảng docs dùng chung với bản Node nên đổi qua lại không mất dữ liệu.
func db(ctx context.Context) (*pgxpool.Pool, error) {
	poolOnce.Do(func() {
		url := os.Getenv("DATABASE_URL")
		if url == "" {
			poolErr = errors.New("chưa cấu hình DATABASE_URL")
			return
		}
		cfg, err := pgxpool.ParseConfig(url)
		if err != nil {
			poolErr = err
			return
		}
		cfg.MaxConns = 4
		if pool, poolErr = pgxpool.NewWithConfig(ctx, cfg); poolErr != nil {
			return
		}
		_, poolErr = pool.Exec(ctx, createTable)
	})
	return pool, poolErr
}

const createTable = `CREATE TABLE IF NOT EXISTS docs (
	key        text PRIMARY KEY,
	data       jsonb NOT NULL,
	version    bigint NOT NULL,
	updated_at timestamptz NOT NULL DEFAULT now()
)`

func writeJSON(w http.ResponseWriter, status int, v any) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.Header().Set("Cache-Control", "no-store")
	w.Header().Set("X-Backend", "go")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(v)
}

func fail(w http.ResponseWriter, status int, msg string) {
	writeJSON(w, status, map[string]string{"error": msg})
}

// So sánh thời gian hằng để không lộ mã qua thời gian phản hồi
func matches(r *http.Request, secret string) bool {
	got := r.Header.Get("X-App-Secret")
	return secret != "" && subtle.ConstantTimeCompare([]byte(got), []byte(secret)) == 1
}

func authorized(r *http.Request) bool { return matches(r, os.Getenv("APP_SECRET")) }

// API của trang hsk6 (thuật ngữ, AI): mã chung APP_SECRET hoặc mật khẩu riêng của trang HSK6_PASS (cho Ngọc)
func authorizedHsk6(r *http.Request) bool { return authorized(r) || matches(r, os.Getenv("HSK6_PASS")) }
