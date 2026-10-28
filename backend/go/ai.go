package gobackend

// POST /api/go/ai  { model?, provider?, system?, contents: [{role, parts:[{text}]}] } → { text, provider, model }
// Gọi AI bằng khóa giấu trên server, người dùng chỉ cần mã đồng bộ chung (hoặc mật khẩu trang hsk6).
// Nhiều nhà cung cấp có gói miễn phí, thử lần lượt: hết lượt (429), quá tải, lỗi hay quá giờ thì chuyển sang cái kế tiếp.
// Chỉ dùng cái nào có khóa trong biến môi trường; đổi thứ tự bằng AI_ORDER (vd "groq,gemini"), đổi model bằng <TÊN>_MODELS,
// đổi địa chỉ (proxy, máy chủ thử) bằng <TÊN>_BASE_URL. Giống hệt bản Node.

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
	"sync"
	"time"
	"unicode/utf8"
)

var (
	modelRe = regexp.MustCompile(`^gemini-[\w.-]{1,40}$`)
	thinkRe = regexp.MustCompile(`(?s)<think>.*?</think>`)
)

const (
	maxTurns   = 16
	maxChars   = 8000
	aiTimeout  = 20 * time.Second // mỗi lần gọi một model
	aiBudget   = 50 * time.Second // cả chuỗi, dưới maxDuration 60 s trong vercel.json
	aiCooldown = time.Minute      // model hết lượt thì bỏ qua một phút (chỉ trong function đang "ấm")
	aiOrder    = "gemini,groq,openrouter,mistral"
)

type part struct {
	Text string `json:"text"`
}
type content struct {
	Role  string `json:"role"`
	Parts []part `json:"parts"`
}

type aiProvider struct {
	Name, Key, Base, Models string
}

// Gemini: mỗi model có hạn mức miễn phí riêng nên thử lần lượt từng model. Còn lại theo chuẩn chat/completions của OpenAI.
var aiProviders = map[string]aiProvider{
	"gemini":     {"Gemini", "GEMINI_API_KEY", "https://generativelanguage.googleapis.com/v1beta", "gemini-3.8-flash,gemini-3.5-flash-lite"},
	"groq":       {"Groq", "GROQ_API_KEY", "https://api.groq.com/openai/v1", "llama-3.3-70b-versatile"},
	"openrouter": {"OpenRouter", "OPENROUTER_API_KEY", "https://openrouter.ai/api/v1", "meta-llama/llama-3.3-70b-instruct:free"},
	"mistral":    {"Mistral", "MISTRAL_API_KEY", "https://api.mistral.ai/v1", "mistral-small-latest"},
}

var (
	cooldownMu sync.Mutex
	cooldown   = map[string]time.Time{}
)

func splitList(v, def string) []string {
	if strings.TrimSpace(v) == "" {
		v = def
	}
	out := []string{}
	for _, s := range strings.Split(v, ",") {
		if s = strings.TrimSpace(s); s != "" {
			out = append(out, s)
		}
	}
	return out
}

func env(id, suffix, def string) string {
	if v := os.Getenv(strings.ToUpper(id) + suffix); v != "" {
		return v
	}
	return def
}

func cut(s string) string {
	if r := []rune(s); len(r) > maxChars {
		return string(r[:maxChars])
	}
	return s
}

type aiError struct {
	status int
	msg    string
}

func (e *aiError) Error() string { return e.msg }

// model "suy nghĩ" (Qwen, DeepSeek…) có thể trả kèm <think>…</think>, bỏ đi để chỉ còn câu trả lời
func aiAnswer(s string) string { return strings.TrimSpace(thinkRe.ReplaceAllString(s, "")) }

// Gửi JSON, đọc JSON; lỗi HTTP thành *aiError kèm thông báo của nhà cung cấp
func aiPost(ctx context.Context, endpoint string, headers map[string]string, payload any, out any) error {
	b, _ := json.Marshal(payload)
	req, _ := http.NewRequestWithContext(ctx, http.MethodPost, endpoint, bytes.NewReader(b))
	req.Header.Set("Content-Type", "application/json")
	for k, v := range headers {
		req.Header.Set(k, v)
	}
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}
	defer res.Body.Close()
	var raw json.RawMessage
	json.NewDecoder(res.Body).Decode(&raw)
	if res.StatusCode != http.StatusOK {
		var e struct {
			Error   json.RawMessage `json:"error"`
			Message string          `json:"message"`
		}
		json.Unmarshal(raw, &e)
		var em struct {
			Message string `json:"message"`
		}
		msg := e.Message
		if json.Unmarshal(e.Error, &em) == nil && em.Message != "" {
			msg = em.Message
		} else if s := ""; json.Unmarshal(e.Error, &s) == nil && s != "" {
			msg = s
		}
		if msg == "" {
			msg = fmt.Sprintf("lỗi %d", res.StatusCode)
		}
		return &aiError{res.StatusCode, msg}
	}
	return json.Unmarshal(raw, out)
}

func callGemini(ctx context.Context, key, model, system string, contents []content) (string, error) {
	req := map[string]any{"contents": contents}
	if system != "" {
		req["systemInstruction"] = content{Parts: []part{{Text: system}}}
	}
	var out struct {
		Candidates []struct {
			Content content `json:"content"`
		} `json:"candidates"`
	}
	endpoint := env("gemini", "_BASE_URL", aiProviders["gemini"].Base) + "/models/" + url.PathEscape(model) + ":generateContent"
	if err := aiPost(ctx, endpoint, map[string]string{"x-goog-api-key": key}, req, &out); err != nil {
		return "", err
	}
	var sb strings.Builder
	if len(out.Candidates) > 0 {
		for _, p := range out.Candidates[0].Content.Parts {
			sb.WriteString(p.Text)
		}
	}
	return aiAnswer(sb.String()), nil
}

func callOpenAI(ctx context.Context, id, key, model, system string, contents []content) (string, error) {
	type msg struct {
		Role    string `json:"role"`
		Content string `json:"content"`
	}
	messages := []msg{}
	if system != "" {
		messages = append(messages, msg{"system", system})
	}
	for _, c := range contents {
		role := "user"
		if c.Role == "model" {
			role = "assistant"
		}
		messages = append(messages, msg{role, c.Parts[0].Text})
	}
	var out struct {
		Choices []struct {
			Message msg `json:"message"`
		} `json:"choices"`
	}
	endpoint := env(id, "_BASE_URL", aiProviders[id].Base) + "/chat/completions"
	req := map[string]any{"model": model, "messages": messages, "temperature": 0.2}
	if err := aiPost(ctx, endpoint, map[string]string{"Authorization": "Bearer " + key}, req, &out); err != nil {
		return "", err
	}
	if len(out.Choices) == 0 {
		return "", nil
	}
	return aiAnswer(out.Choices[0].Message.Content), nil
}

func short(s string, n int) string {
	if utf8.RuneCountInString(s) <= n {
		return s
	}
	return string([]rune(s)[:n])
}

func AI(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		w.Header().Set("Allow", "POST")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ POST")
		return
	}
	if !authorizedHsk6(r) {
		fail(w, http.StatusUnauthorized, "sai mã đồng bộ hoặc mật khẩu")
		return
	}

	var body struct {
		Model    string    `json:"model"`
		Provider string    `json:"provider"`
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
	system := strings.TrimSpace(cut(body.System))

	// provider: chỉ dùng một nhà cung cấp (để thử từng khóa); không có thì theo AI_ORDER
	order := []string{}
	if _, ok := aiProviders[body.Provider]; ok {
		order = []string{body.Provider}
	} else {
		for _, id := range splitList(os.Getenv("AI_ORDER"), aiOrder) {
			if _, ok := aiProviders[id]; ok {
				order = append(order, id)
			}
		}
	}

	start := time.Now()
	errs := []string{}
	tried, limited := 0, 0
	for _, id := range order {
		p := aiProviders[id]
		key := os.Getenv(p.Key)
		if key == "" {
			continue
		}
		models := splitList(os.Getenv(strings.ToUpper(id)+"_MODELS"), p.Models)
		if id == "gemini" && modelRe.MatchString(body.Model) {
			rest := []string{body.Model}
			for _, m := range models {
				if m != body.Model {
					rest = append(rest, m)
				}
			}
			models = rest
		}
		for _, model := range models {
			left := aiBudget - time.Since(start)
			if left < 3*time.Second {
				break
			}
			tried++
			ck := id + ":" + model
			cooldownMu.Lock()
			until := cooldown[ck]
			cooldownMu.Unlock()
			if time.Now().Before(until) {
				limited++
				errs = append(errs, p.Name+" "+model+": vừa hết lượt, đang chờ")
				continue
			}
			ctx, cancel := context.WithTimeout(r.Context(), min(aiTimeout, left))
			var text string
			var err error
			if id == "gemini" {
				text, err = callGemini(ctx, key, model, system, contents)
			} else {
				text, err = callOpenAI(ctx, id, key, model, system, contents)
			}
			cancel()
			if err == nil && text == "" {
				err = &aiError{http.StatusBadGateway, "trả về rỗng"}
			}
			if err == nil {
				writeJSON(w, http.StatusOK, map[string]string{"text": text, "provider": id, "model": model})
				return
			}
			msg := err.Error()
			if e, ok := err.(*aiError); ok && e.status == http.StatusTooManyRequests {
				limited++
				msg = "hết lượt"
				cooldownMu.Lock()
				cooldown[ck] = time.Now().Add(aiCooldown)
				cooldownMu.Unlock()
			}
			errs = append(errs, p.Name+" "+model+": "+short(msg, 160))
		}
	}
	if tried == 0 {
		keys := []string{}
		for _, id := range splitList("", aiOrder) {
			keys = append(keys, aiProviders[id].Key)
		}
		fail(w, http.StatusServiceUnavailable, "server chưa cấu hình khóa AI nào ("+strings.Join(keys, ", ")+")")
		return
	}
	status := http.StatusBadGateway
	if limited == tried {
		status = http.StatusTooManyRequests
	}
	fail(w, status, "các AI đều chưa trả lời được: "+strings.Join(errs, "; "))
}
