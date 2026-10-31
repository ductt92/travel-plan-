package gobackend

// GET/PUT /api/go/grammar (bản Node: backend/node/grammar.js, cùng bảng và cùng dữ liệu vào/ra)
//
// Trang "Ngữ pháp qua tình huống" (hsk6/ngu-phap/) đọc nhóm bài và các tình huống từ đây.
// Mỗi tình huống là một dòng grammar_case, nội dung giữ nguyên JSON trang dùng (data).
// GET ai cũng đọc được. PUT {groups, cases} cần mật khẩu (APP_SECRET hoặc HSK6_PASS): ghi đè cả bộ trong một
// transaction và lưu bản sao vào grammar_version.

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"regexp"
	"strings"
	"sync"
	"time"

	"github.com/jackc/pgx/v5/pgxpool"
)

const grammarTables = `
CREATE TABLE IF NOT EXISTS grammar_group (
  id   text PRIMARY KEY,
  name text NOT NULL,
  ord  integer NOT NULL
);
CREATE TABLE IF NOT EXISTS grammar_case (
  id         text PRIMARY KEY,
  grp        text NOT NULL REFERENCES grammar_group ON DELETE CASCADE,
  ord        integer NOT NULL,
  data       jsonb NOT NULL,
  updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS grammar_version (
  id         bigserial PRIMARY KEY,
  groups     jsonb NOT NULL,
  cases      jsonb NOT NULL,
  count      integer NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
)`

const (
	maxGrammarCases = 300
	maxGrammarBody  = 3 << 20
)

var (
	grammarTablesMu sync.Mutex
	grammarTablesOK bool
	grammarGroupID  = regexp.MustCompile(`^[A-Z][A-Z0-9]{0,3}$`)
	grammarCaseID   = regexp.MustCompile(`^[a-z0-9-]{1,40}$`)
)

type grammarGroup struct {
	ID   string `json:"id"`
	Name string `json:"name"`
}

type grammarBody struct {
	Groups []grammarGroup    `json:"groups"`
	Cases  []json.RawMessage `json:"cases"`
}

// Chỉ đọc các trường cần kiểm tra; phần còn lại của tình huống lưu nguyên vẹn
type grammarCaseHead struct {
	ID    string `json:"id"`
	G     string `json:"g"`
	Title string `json:"title"`
	Quiz  []struct {
		Opts []json.RawMessage `json:"opts"`
		A    *int              `json:"a"`
	} `json:"quiz"`
}

func grammarPool(ctx context.Context) (*pgxpool.Pool, error) {
	p, err := db(ctx)
	if err != nil {
		return nil, err
	}
	grammarTablesMu.Lock()
	defer grammarTablesMu.Unlock()
	if !grammarTablesOK {
		if _, err := p.Exec(ctx, grammarTables); err != nil {
			return nil, err
		}
		grammarTablesOK = true
	}
	return p, nil
}

func nonEmpty(s string, max int) bool { return strings.TrimSpace(s) != "" && len([]rune(s)) <= max }

// Trả thông báo lỗi đầu tiên, hoặc "" nếu đúng định dạng (giống check trong backend/node/grammar.js)
func checkGrammar(b grammarBody, heads []grammarCaseHead) string {
	if len(b.Groups) == 0 || len(b.Groups) > 20 {
		return "cần 1–20 nhóm"
	}
	gids := map[string]bool{}
	for _, g := range b.Groups {
		if !grammarGroupID.MatchString(g.ID) || gids[g.ID] {
			return "mã nhóm không hợp lệ hoặc trùng: " + g.ID
		}
		if !nonEmpty(g.Name, 80) {
			return "nhóm " + g.ID + " thiếu tên"
		}
		gids[g.ID] = true
	}
	if len(heads) == 0 || len(heads) > maxGrammarCases {
		return fmt.Sprintf("cần 1–%d tình huống", maxGrammarCases)
	}
	ids := map[string]bool{}
	for _, c := range heads {
		if !grammarCaseID.MatchString(c.ID) || ids[c.ID] {
			return "mã tình huống không hợp lệ hoặc trùng: " + c.ID
		}
		if !gids[c.G] {
			return "tình huống " + c.ID + " thuộc nhóm không có: " + c.G
		}
		if !nonEmpty(c.Title, 300) {
			return "tình huống " + c.ID + " thiếu tiêu đề"
		}
		if len(c.Quiz) == 0 {
			return "tình huống " + c.ID + " chưa có câu hỏi"
		}
		for _, q := range c.Quiz {
			if len(q.Opts) < 2 || q.A == nil || *q.A < 0 || *q.A >= len(q.Opts) {
				return "tình huống " + c.ID + " có câu hỏi sai đáp án"
			}
		}
		ids[c.ID] = true
	}
	return ""
}

func loadGrammar(ctx context.Context, p *pgxpool.Pool) (map[string]any, error) {
	groups := []grammarGroup{}
	rows, err := p.Query(ctx, `SELECT id, name FROM grammar_group ORDER BY ord`)
	if err != nil {
		return nil, err
	}
	for rows.Next() {
		var g grammarGroup
		if err := rows.Scan(&g.ID, &g.Name); err != nil {
			return nil, err
		}
		groups = append(groups, g)
	}
	cases := []json.RawMessage{}
	rows, err = p.Query(ctx, `SELECT c.data FROM grammar_case c JOIN grammar_group g ON g.id = c.grp ORDER BY g.ord, c.ord`)
	if err != nil {
		return nil, err
	}
	for rows.Next() {
		var d json.RawMessage
		if err := rows.Scan(&d); err != nil {
			return nil, err
		}
		cases = append(cases, d)
	}
	var version *int64
	var at *time.Time
	if err := p.QueryRow(ctx, `SELECT max(id), max(created_at) FROM grammar_version`).Scan(&version, &at); err != nil {
		return nil, err
	}
	v := int64(0)
	if version != nil {
		v = *version
	}
	return map[string]any{"version": v, "updatedAt": at, "groups": groups, "cases": cases}, nil
}

func replaceGrammar(ctx context.Context, p *pgxpool.Pool, b grammarBody, heads []grammarCaseHead) (map[string]any, error) {
	tx, err := p.Begin(ctx)
	if err != nil {
		return nil, err
	}
	defer tx.Rollback(ctx)
	if _, err := tx.Exec(ctx, `DELETE FROM grammar_case`); err != nil {
		return nil, err
	}
	if _, err := tx.Exec(ctx, `DELETE FROM grammar_group`); err != nil {
		return nil, err
	}
	for i, g := range b.Groups {
		if _, err := tx.Exec(ctx, `INSERT INTO grammar_group (id, name, ord) VALUES ($1, $2, $3)`, g.ID, strings.TrimSpace(g.Name), i); err != nil {
			return nil, err
		}
	}
	// thứ tự trong nhóm giữ đúng thứ tự gửi lên
	order := map[string]int{}
	for i, h := range heads {
		if _, err := tx.Exec(ctx, `INSERT INTO grammar_case (id, grp, ord, data) VALUES ($1, $2, $3, $4)`,
			h.ID, h.G, order[h.G], string(b.Cases[i])); err != nil {
			return nil, err
		}
		order[h.G]++
	}
	groups, _ := json.Marshal(b.Groups)
	cases, _ := json.Marshal(b.Cases)
	var id int64
	var at time.Time
	if err := tx.QueryRow(ctx, `INSERT INTO grammar_version (groups, cases, count) VALUES ($1, $2, $3) RETURNING id, created_at`,
		string(groups), string(cases), len(heads)).Scan(&id, &at); err != nil {
		return nil, err
	}
	if err := tx.Commit(ctx); err != nil {
		return nil, err
	}
	return map[string]any{"version": id, "count": len(heads), "updatedAt": at}, nil
}

func Grammar(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet && r.Method != http.MethodPut {
		w.Header().Set("Allow", "GET, PUT")
		fail(w, http.StatusMethodNotAllowed, "chỉ hỗ trợ GET và PUT")
		return
	}
	if r.Method == http.MethodPut && !authorizedHsk6(r) {
		fail(w, http.StatusUnauthorized, "sai mật khẩu")
		return
	}
	ctx, cancel := context.WithTimeout(r.Context(), 15*time.Second)
	defer cancel()
	p, err := grammarPool(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
	}
	if r.Method == http.MethodGet {
		out, err := loadGrammar(ctx, p)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, out)
		return
	}
	var body grammarBody
	if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, maxGrammarBody)).Decode(&body); err != nil {
		fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
		return
	}
	heads := make([]grammarCaseHead, len(body.Cases))
	for i, raw := range body.Cases {
		if err := json.Unmarshal(raw, &heads[i]); err != nil {
			fail(w, http.StatusBadRequest, "tình huống phải là đối tượng")
			return
		}
	}
	if msg := checkGrammar(body, heads); msg != "" {
		fail(w, http.StatusBadRequest, msg)
		return
	}
	out, err := replaceGrammar(ctx, p, body, heads)
	if err != nil {
		fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
		return
	}
	writeJSON(w, http.StatusOK, out)
}
