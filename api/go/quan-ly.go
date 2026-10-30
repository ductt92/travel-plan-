// Lối vào Vercel cho /api/go/quan-ly, logic ở backend/go/catalog.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func QuanLy(w http.ResponseWriter, r *http.Request) { gobackend.Catalog(w, r) }
