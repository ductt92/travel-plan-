// Lối vào Vercel cho /api/go/grammar, logic ở backend/go/grammar.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func Grammar(w http.ResponseWriter, r *http.Request) { gobackend.Grammar(w, r) }
