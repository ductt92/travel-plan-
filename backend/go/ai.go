package gobackend

// POST /api/go/ai  { model?, system?, contents: [{role, parts:[{text}]}] } → { text }
// Gọi Gemini bằng khóa giấu trên server, người dùng chỉ cần mã đồng bộ chung.

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"regexp"
	"strings"
	"time"
)

var modelRe = regexp.MustCompile(`^gemini-[\w.-]{1,40}$`)

const (
	defaultModel = "gemini-2.5-flash"
	maxTurns     = 16
	maxChars     = 8000
)

type part struct {
	Text string `json:"text"`
}
type content struct {
	Role  string `json:"role"`
	Parts []part `json:"parts"`
}

func cut(s string) string {
	if r := []rune(s); len(r) > maxChars {
		return string(r[:maxChars])
	}
	return s
}

func AI(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		w.Header().Set("Allow", "POST")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ POST")
		return
	}
	if !authorized(r) {
		fail(w, http.StatusUnauthorized, "sai mã đồng bộ")
		return
	}
	key := os.Getenv("GEMINI_API_KEY")
	if key == "" {
		fail(w, http.StatusServiceUnavailable, "server chưa cấu hình GEMINI_API_KEY")
		return
	}

	var body struct {
		Model    string    `json:"model"`
		System   string    `json:"system"`
		Contents []content `json:"contents"`
	}
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, maxBody)).Decode(&body); err != nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
		return
	}
	// Chỉ chuyển tiếp đúng dạng hội thoại, cắt bớt để không ai dùng API làm proxy tùy ý
	if len(body.Contents) > maxTurns {
		body.Contents = body.Contents[len(body.Contents)-maxTurns:]
	}
	contents := make([]content, 0, len(body.Contents))
	for _, c := range body.Contents {
		role := "user"
		if c.Role == "model" {
			role = "model"
		}
		text := ""
		if len(c.Parts) > 0 {
			text = c.Parts[0].Text
		}
		contents = append(contents, content{Role: role, Parts: []part{{Text: cut(text)}}})
	}
	if len(contents) == 0 || contents[0].Role != "user" {
		fail(w, http.StatusBadRequest, "hội thoại phải bắt đầu bằng câu hỏi")
		return
	}
	model := defaultModel
	if modelRe.MatchString(body.Model) {
		model = body.Model
	}

	req := map[string]any{"contents": contents}
	if s := strings.TrimSpace(body.System); s != "" {
		req["systemInstruction"] = content{Parts: []part{{Text: cut(s)}}}
	}
	payload, _ := json.Marshal(req)

	ctx, cancel := context.WithTimeout(r.Context(), 25*time.Second)
	defer cancel()
	endpoint := "https://generativelanguage.googleapis.com/v1beta/models/" + url.PathEscape(model) + ":generateContent"
	greq, _ := http.NewRequestWithContext(ctx, http.MethodPost, endpoint, bytes.NewReader(payload))
	greq.Header.Set("Content-Type", "application/json")
	greq.Header.Set("x-goog-api-key", key)
	res, err := http.DefaultClient.Do(greq)
	if err != nil {
		fail(w, http.StatusGatewayTimeout, "không gọi được Gemini: "+err.Error())
		return
	}
	defer res.Body.Close()

	var out struct {
		Candidates []struct {
			Content content `json:"content"`
		} `json:"candidates"`
		Error *struct {
			Message string `json:"message"`
		} `json:"error"`
	}
	json.NewDecoder(res.Body).Decode(&out)
	if res.StatusCode != http.StatusOK {
		msg := fmt.Sprintf("Gemini trả lỗi %d", res.StatusCode)
		if out.Error != nil && out.Error.Message != "" {
			msg = out.Error.Message
		}
		fail(w, http.StatusBadGateway, msg)
		return
	}
	var sb strings.Builder
	if len(out.Candidates) > 0 {
		for _, p := range out.Candidates[0].Content.Parts {
			sb.WriteString(p.Text)
		}
	}
	writeJSON(w, http.StatusOK, map[string]string{"text": sb.String()})
}
