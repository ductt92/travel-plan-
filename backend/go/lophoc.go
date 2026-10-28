package gobackend

// POST /api/go/lop-hoc  { room, clientId, pass? } → TokenRequest của Ably (bản Node: backend/node/lophoc.js)
//
// Ký "phiếu xin token" bằng khóa Ably giấu trên server, cho vào đúng một kênh lop:<phòng>.
// clientId "gv-…" là giáo viên (phải đúng TEACHER_PASS), "hs-…" là học sinh.

import (
	"crypto/hmac"
	"crypto/rand"
	"crypto/sha256"
	"crypto/subtle"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"
)

var (
	roomRe   = regexp.MustCompile(`^[a-z0-9-]{1,32}$`)
	clientRe = regexp.MustCompile(`^(gv|hs)-[a-z0-9]{8,32}$`)
)

const lopTTL = int64(60 * 60 * 1000) // hết hạn thì thư viện Ably tự xin lại

type ablyTokenRequest struct {
	KeyName    string `json:"keyName"`
	TTL        int64  `json:"ttl"`
	Capability string `json:"capability"`
	ClientID   string `json:"clientId"`
	Timestamp  int64  `json:"timestamp"`
	Nonce      string `json:"nonce"`
	Mac        string `json:"mac"`
}

// Ký giống hệt Auth.createTokenRequest của thư viện Ably
func tokenRequest(key, clientID, room string, timestamp int64, nonce string) ablyTokenRequest {
	keyName, secret, _ := strings.Cut(key, ":")
	// room đã qua roomRe nên ghép chuỗi thẳng không cần thoát ký tự
	capability := `{"lop:` + room + `":["presence","publish","subscribe"]}`
	text := strings.Join([]string{keyName, strconv.FormatInt(lopTTL, 10), capability, clientID,
		strconv.FormatInt(timestamp, 10), nonce, ""}, "\n")
	m := hmac.New(sha256.New, []byte(secret))
	m.Write([]byte(text))
	return ablyTokenRequest{keyName, lopTTL, capability, clientID, timestamp, nonce, base64.StdEncoding.EncodeToString(m.Sum(nil))}
}

func LopHoc(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		w.Header().Set("Allow", "POST")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ POST")
		return
	}
	key := os.Getenv("ABLY_API_KEY")
	if !strings.Contains(key, ":") {
		fail(w, http.StatusServiceUnavailable, "server chưa cấu hình ABLY_API_KEY")
		return
	}
	var body struct {
		Room     string `json:"room"`
		ClientID string `json:"clientId"`
		Pass     string `json:"pass"`
	}
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, 4096)).Decode(&body); err != nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
		return
	}
	if !roomRe.MatchString(body.Room) || !clientRe.MatchString(body.ClientID) {
		fail(w, http.StatusBadRequest, "mã phòng hoặc mã người dùng không hợp lệ")
		return
	}
	if strings.HasPrefix(body.ClientID, "gv-") {
		pass := os.Getenv("TEACHER_PASS")
		if pass == "" {
			fail(w, http.StatusServiceUnavailable, "server chưa cấu hình TEACHER_PASS")
			return
		}
		if subtle.ConstantTimeCompare([]byte(body.Pass), []byte(pass)) != 1 {
			fail(w, http.StatusUnauthorized, "Sai mật khẩu giáo viên")
			return
		}
	}
	nonce := make([]byte, 16)
	rand.Read(nonce)
	writeJSON(w, http.StatusOK, tokenRequest(key, body.ClientID, body.Room, time.Now().UnixMilli(), hex.EncodeToString(nonce)))
}
