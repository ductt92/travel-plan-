// Lối vào Vercel cho /api/go/tai-khoan, logic ở backend/go/accounts.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func TaiKhoan(w http.ResponseWriter, r *http.Request) { gobackend.Accounts(w, r) }
