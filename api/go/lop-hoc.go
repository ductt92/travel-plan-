// Lối vào Vercel cho /api/go/lop-hoc, logic ở backend/go/lophoc.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func LopHoc(w http.ResponseWriter, r *http.Request) { gobackend.LopHoc(w, r) }
