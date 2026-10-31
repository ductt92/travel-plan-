// Lối vào Vercel cho /api/go/terms và /api/go/grammar (vercel.json chuyển /grammar sang đây kèm ?_api=grammar).
// Gói Hobby chỉ cho 12 function nên hai API của trang hsk6 dùng chung một function; logic ở backend/go/terms.go, grammar.go.
package handler

import (
	"net/http"
	"strings"

	gobackend "dadiqua/backend/go"
)

func Terms(w http.ResponseWriter, r *http.Request) {
	if r.URL.Query().Get("_api") == "grammar" || strings.HasSuffix(r.URL.Path, "/grammar") {
		gobackend.Grammar(w, r)
		return
	}
	gobackend.Terms(w, r)
}
