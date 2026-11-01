// Lối vào Vercel cho /api/go/quan-ly và /api/go/tai-khoan (vercel.json chuyển /tai-khoan sang đây kèm ?_api=tai-khoan).
// Gói Hobby chỉ cho 12 function nên tài khoản dùng chung function với trang quản lý; logic ở backend/go/catalog.go, accounts.go.
package handler

import (
	"net/http"
	"strings"

	gobackend "dadiqua/backend/go"
)

func QuanLy(w http.ResponseWriter, r *http.Request) {
	if r.URL.Query().Get("_api") == "tai-khoan" || strings.HasSuffix(r.URL.Path, "/tai-khoan") {
		gobackend.Accounts(w, r)
		return
	}
	gobackend.Catalog(w, r)
}
