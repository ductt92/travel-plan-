package gobackend

// POST /api/go/lop-hoc  { room, clientId, pass?, ice? } → TokenRequest của Ably (+ iceServers nếu ice: true)
// (bản Node: backend/node/lophoc.js)
//
// Ký "phiếu xin token" bằng khóa Ably giấu trên server, cho vào đúng một kênh lop:<phòng>.
// clientId "gv-…" là giáo viên (mật khẩu là HSK6_PASS của Ngọc, hoặc mã chung APP_SECRET), "hs-…" là học sinh.
// ice: true thì trả thêm iceServers (TURN Cloudflare qua CF_TURN_KEY_ID + CF_TURN_API_TOKEN,
// hoặc TURN_URLS + TURN_USERNAME + TURN_CREDENTIAL), không cấu hình thì chỉ có STUN.

import (
	"bytes"
	"context"
	"crypto/hmac"
	"crypto/rand"
	"crypto/sha256"
	"crypto/subtle"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
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

type iceServer struct {
	URLs       any    `json:"urls"`
	Username   string `json:"username,omitempty"`
	Credential string `json:"credential,omitempty"`
}

var stunServer = iceServer{URLs: "stun:stun.l.google.com:19302"}

// Danh sách ICE cho RTCPeerConnection. Cloudflare cấp tên/mật khẩu TURN ngắn hạn, lỗi thì lùi về STUN.
func iceServers(ctx context.Context) []iceServer {
	if id, token := os.Getenv("CF_TURN_KEY_ID"), os.Getenv("CF_TURN_API_TOKEN"); id != "" && token != "" {
		if list, err := cloudflareTurn(ctx, id, token); err == nil && len(list) > 0 {
			return list
		} else if err != nil {
			log.Printf("lop-hoc: không lấy được TURN Cloudflare: %v", err)
		}
	}
	if raw := os.Getenv("TURN_URLS"); raw != "" {
		var urls []string
		for _, u := range strings.Split(raw, ",") {
			if u = strings.TrimSpace(u); u != "" {
				urls = append(urls, u)
			}
		}
		return []iceServer{stunServer, {URLs: urls, Username: os.Getenv("TURN_USERNAME"), Credential: os.Getenv("TURN_CREDENTIAL")}}
	}
	return []iceServer{stunServer}
}

func cloudflareTurn(ctx context.Context, id, token string) ([]iceServer, error) {
	ctx, cancel := context.WithTimeout(ctx, 4*time.Second)
	defer cancel()
	url := "https://rtc.live.cloudflare.com/v1/turn/keys/" + id + "/credentials/generate-ice-servers"
	req, _ := http.NewRequestWithContext(ctx, http.MethodPost, url, bytes.NewBufferString(`{"ttl":21600}`))
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Content-Type", "application/json")
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer res.Body.Close()
	if res.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("Cloudflare TURN %d", res.StatusCode)
	}
	var out struct {
		IceServers json.RawMessage `json:"iceServers"`
	}
	if err := json.NewDecoder(res.Body).Decode(&out); err != nil {
		return nil, err
	}
	// bản API mới trả mảng, bản cũ trả một đối tượng
	var list []iceServer
	if err := json.Unmarshal(out.IceServers, &list); err != nil {
		var one iceServer
		if err := json.Unmarshal(out.IceServers, &one); err != nil {
			return nil, err
		}
		list = []iceServer{one}
	}
	return list, nil
}

func samePass(got, want string) bool {
	return want != "" && subtle.ConstantTimeCompare([]byte(got), []byte(want)) == 1
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
		Ice      bool   `json:"ice"`
	}
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, 4096)).Decode(&body); err != nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
		return
	}
	if !roomRe.MatchString(body.Room) || !clientRe.MatchString(body.ClientID) {
		fail(w, http.StatusBadRequest, "mã phòng hoặc mã người dùng không hợp lệ")
		return
	}
	// giáo viên dùng chung mật khẩu với trang hsk6 (giống authorizedHsk6, nhưng mật khẩu gửi trong body)
	if strings.HasPrefix(body.ClientID, "gv-") && !samePass(body.Pass, os.Getenv("HSK6_PASS")) && !samePass(body.Pass, os.Getenv("APP_SECRET")) {
		fail(w, http.StatusUnauthorized, "Sai mật khẩu giáo viên")
		return
	}
	nonce := make([]byte, 16)
	rand.Read(nonce)
	token := tokenRequest(key, body.ClientID, body.Room, time.Now().UnixMilli(), hex.EncodeToString(nonce))
	if !body.Ice {
		writeJSON(w, http.StatusOK, token)
		return
	}
	writeJSON(w, http.StatusOK, struct {
		ablyTokenRequest
		IceServers []iceServer `json:"iceServers"`
	}{token, iceServers(r.Context())})
}
