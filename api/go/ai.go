// Lối vào Vercel cho /api/go/ai, logic ở backend/go/ai.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func AI(w http.ResponseWriter, r *http.Request) { gobackend.AI(w, r) }
