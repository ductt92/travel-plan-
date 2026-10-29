// Lối vào Vercel cho /api/go/ban-do, logic ở backend/go/bando.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func BanDo(w http.ResponseWriter, r *http.Request) { gobackend.BanDo(w, r) }
