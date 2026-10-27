// Lối vào Vercel cho /api/go/sync, logic ở backend/go/sync.go
package handler

import (
	"net/http"

	gobackend "dadiqua/backend/go"
)

func Sync(w http.ResponseWriter, r *http.Request) { gobackend.Sync(w, r) }
