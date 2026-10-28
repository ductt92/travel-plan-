// Lối vào Vercel cho /api/go/terms, logic ở backend/go/terms.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func Terms(w http.ResponseWriter, r *http.Request) { gobackend.Terms(w, r) }
