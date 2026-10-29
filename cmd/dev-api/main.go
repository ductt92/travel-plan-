// Chạy bản Go của API ở máy (trên Vercel thì mỗi file trong api/go là một function riêng).
// Dùng qua `npm run dev:api` (scripts/dev-api.mjs), không cần gọi trực tiếp.
package main

import (
	"log"
	"net/http"
	"os"

	gobackend "dadiqua/backend/go"
)

func main() {
	port := os.Getenv("GO_API_PORT")
	if port == "" {
		port = "3002"
	}
	http.HandleFunc("/api/go/sync", gobackend.Sync)
	http.HandleFunc("/api/go/ai", gobackend.AI)
	http.HandleFunc("/api/go/terms", gobackend.Terms)
	http.HandleFunc("/api/go/lop-hoc", gobackend.LopHoc)
	http.HandleFunc("/api/go/ban-do", gobackend.BanDo)
	log.Printf("API Go: http://localhost:%s/api/go/{sync,ai,terms,lop-hoc,ban-do}", port)
	log.Fatal(http.ListenAndServe("127.0.0.1:"+port, nil))
}
