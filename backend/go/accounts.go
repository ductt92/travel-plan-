// Tài khoản đăng nhập của trang quản lý và bản đồ. Bản Node: backend/node/accounts.js, cùng hợp đồng
// (cùng bảng app_users, cùng kiểu băm scrypt, cùng token ký HMAC nên đăng nhập ở bản này dùng được ở bản kia).
//
// POST /api/go/tai-khoan?login  {username, password} → { token, user }
// GET  …?me                     (Bearer)             → { user }
// PUT  …?user                   (X-App-Secret) {username, name, role, password} → tạo/sửa tài khoản
package gobackend

import (
	"context"
	"crypto/hmac"
	"crypto/rand"
	"crypto/sha256"
	"crypto/subtle"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
	"golang.org/x/crypto/scrypt"
)

const accountsTables = `
CREATE TABLE IF NOT EXISTS app_users (
  id            serial PRIMARY KEY,
  username      text NOT NULL UNIQUE,
  name          text NOT NULL,
  role          text NOT NULL CHECK (role IN ('superadmin', 'admin', 'editor', 'viewer')),
  pass_hash     text NOT NULL,
  token_version integer NOT NULL DEFAULT 1,
  created_at    timestamptz NOT NULL DEFAULT now()
)`

var (
	accountsOnce sync.Once
	accountsErr  error
)

func accountsDB(ctx context.Context) (*pgxpool.Pool, error) {
	p, err := db(ctx)
	if err != nil {
		return nil, err
	}
	accountsOnce.Do(func() { _, accountsErr = p.Exec(ctx, accountsTables) })
	if accountsErr != nil {
		accountsOnce = sync.Once{}
		return nil, accountsErr
	}
	return p, nil
}

// AppUser: người đang gọi API
type AppUser struct {
	ID       int    `json:"id"`
	Username string `json:"username"`
	Name     string `json:"name"`
	Role     string `json:"role"`
}

var (
	accountRoles = []string{"superadmin", "admin", "editor", "viewer"}
	// Quyền theo vai trò. Hiện mới có superadmin; vai trò khác để dành khi thêm tài khoản mới.
	accountRights = map[string][]string{
		"superadmin": {"read", "write", "delete", "users"},
		"admin":      {"read", "write", "delete"},
		"editor":     {"read", "write"},
		"viewer":     {"read"},
	}
	systemUser       = &AppUser{ID: 0, Username: "system", Name: "Hệ thống", Role: "superadmin"}
	accountNameRe    = regexp.MustCompile(`^[a-z0-9][a-z0-9._-]{1,31}$`)
	accountTokenDays = 180
	// vẫn băm một lần khi không có tài khoản, để thời gian trả lời không lộ tên nào có thật
	dummyHash = "scrypt$16384$8$1$AAAAAAAAAAAAAAAAAAAAAA==$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
)

func can(u *AppUser, right string) bool {
	if u == nil {
		return false
	}
	for _, r := range accountRights[u.Role] {
		if r == right {
			return true
		}
	}
	return false
}

func authKey() []byte {
	if k := os.Getenv("AUTH_SECRET"); k != "" {
		return []byte(k)
	}
	return []byte(os.Getenv("APP_SECRET"))
}

// "scrypt$N$r$p$muối$băm", cùng tham số với bản Node
func hashPassword(password string) (string, error) {
	salt := make([]byte, 16)
	if _, err := rand.Read(salt); err != nil {
		return "", err
	}
	h, err := scrypt.Key([]byte(password), salt, 16384, 8, 1, 32)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("scrypt$16384$8$1$%s$%s", base64.StdEncoding.EncodeToString(salt), base64.StdEncoding.EncodeToString(h)), nil
}

func checkPassword(password, stored string) bool {
	f := strings.Split(stored, "$")
	if len(f) != 6 || f[0] != "scrypt" {
		return false
	}
	n, e1 := strconv.Atoi(f[1])
	r, e2 := strconv.Atoi(f[2])
	p, e3 := strconv.Atoi(f[3])
	salt, e4 := base64.StdEncoding.DecodeString(f[4])
	want, e5 := base64.StdEncoding.DecodeString(f[5])
	if e1 != nil || e2 != nil || e3 != nil || e4 != nil || e5 != nil {
		return false
	}
	got, err := scrypt.Key([]byte(password), salt, n, r, p, len(want))
	return err == nil && subtle.ConstantTimeCompare(got, want) == 1
}

type accountToken struct {
	U   int   `json:"u"`
	V   int   `json:"v"`
	Exp int64 `json:"exp"`
}

func signToken(id, version int) string {
	raw, _ := json.Marshal(accountToken{U: id, V: version, Exp: time.Now().Unix() + int64(accountTokenDays)*86400})
	body := base64.RawURLEncoding.EncodeToString(raw)
	m := hmac.New(sha256.New, authKey())
	m.Write([]byte(body))
	return body + "." + base64.RawURLEncoding.EncodeToString(m.Sum(nil))
}

func verifyToken(token string) *accountToken {
	body, mac, ok := strings.Cut(token, ".")
	if !ok || body == "" || len(authKey()) == 0 {
		return nil
	}
	m := hmac.New(sha256.New, authKey())
	m.Write([]byte(body))
	got, err := base64.RawURLEncoding.DecodeString(mac)
	if err != nil || !hmac.Equal(got, m.Sum(nil)) {
		return nil
	}
	raw, err := base64.RawURLEncoding.DecodeString(body)
	var t accountToken
	if err != nil || json.Unmarshal(raw, &t) != nil || t.Exp <= time.Now().Unix() {
		return nil
	}
	return &t
}

// currentUser: token của tài khoản, hoặc "Hệ thống" nếu gửi mã chung APP_SECRET; nil nếu không có.
// Mỗi lần tra lại tài khoản để tài khoản bị xoá/đổi mật khẩu thì token cũ thôi dùng được.
func currentUser(ctx context.Context, r *http.Request) (*AppUser, error) {
	if authorized(r) {
		return systemUser, nil
	}
	tok, ok := strings.CutPrefix(r.Header.Get("Authorization"), "Bearer ")
	t := verifyToken(strings.TrimSpace(tok))
	if !ok || t == nil {
		return nil, nil
	}
	p, err := accountsDB(ctx)
	if err != nil {
		return nil, err
	}
	var u AppUser
	var version int
	err = p.QueryRow(ctx, `SELECT id, username, name, role, token_version FROM app_users WHERE id = $1`, t.U).
		Scan(&u.ID, &u.Username, &u.Name, &u.Role, &version)
	if err == pgx.ErrNoRows || (err == nil && version != t.V) {
		return nil, nil
	}
	if err != nil {
		return nil, err
	}
	return &u, nil
}

var vnFold = strings.NewReplacer(
	"à", "a", "á", "a", "ả", "a", "ã", "a", "ạ", "a", "ă", "a", "ằ", "a", "ắ", "a", "ẳ", "a", "ẵ", "a", "ặ", "a",
	"â", "a", "ầ", "a", "ấ", "a", "ẩ", "a", "ẫ", "a", "ậ", "a", "è", "e", "é", "e", "ẻ", "e", "ẽ", "e", "ẹ", "e",
	"ê", "e", "ề", "e", "ế", "e", "ể", "e", "ễ", "e", "ệ", "e", "ì", "i", "í", "i", "ỉ", "i", "ĩ", "i", "ị", "i",
	"ò", "o", "ó", "o", "ỏ", "o", "õ", "o", "ọ", "o", "ô", "o", "ồ", "o", "ố", "o", "ổ", "o", "ỗ", "o", "ộ", "o",
	"ơ", "o", "ờ", "o", "ớ", "o", "ở", "o", "ỡ", "o", "ợ", "o", "ù", "u", "ú", "u", "ủ", "u", "ũ", "u", "ụ", "u",
	"ư", "u", "ừ", "u", "ứ", "u", "ử", "u", "ữ", "u", "ự", "u", "ỳ", "y", "ý", "y", "ỷ", "y", "ỹ", "y", "ỵ", "y", "đ", "d",
)

// loginName: bỏ dấu, chữ thường — gõ "Đức", "duc" hay "DUC" đều ra cùng một tài khoản
func loginName(s string) string { return strings.TrimSpace(vnFold.Replace(strings.ToLower(s))) }

// Accounts là handler cho /api/go/tai-khoan
func Accounts(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	q := r.URL.Query()
	p, err := accountsDB(ctx)
	if err != nil {
		fail(w, http.StatusServiceUnavailable, "không kết nối được cơ sở dữ liệu")
		return
	}

	switch {
	case r.Method == http.MethodGet && q.Has("me"):
		u, err := currentUser(ctx, r)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
		} else if u == nil {
			fail(w, http.StatusUnauthorized, "chưa đăng nhập hoặc phiên đã hết hạn")
		} else {
			writeJSON(w, http.StatusOK, map[string]any{"user": u})
		}

	case r.Method == http.MethodPost && q.Has("login"):
		var body struct{ Username, Password string }
		if json.NewDecoder(http.MaxBytesReader(w, r.Body, 4096)).Decode(&body) != nil {
			fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
			return
		}
		name := loginName(body.Username)
		if name == "" || body.Password == "" {
			fail(w, http.StatusBadRequest, "cần tên đăng nhập và mật khẩu")
			return
		}
		rows, err := p.Query(ctx, `SELECT id, username, name, role, pass_hash, token_version FROM app_users`)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi đọc dữ liệu")
			return
		}
		var found *AppUser
		hash, version := dummyHash, 0
		for rows.Next() {
			var u AppUser
			var h string
			var v int
			if rows.Scan(&u.ID, &u.Username, &u.Name, &u.Role, &h, &v) == nil && found == nil &&
				(u.Username == name || loginName(u.Name) == name) {
				found, hash, version = &u, h, v
			}
		}
		rows.Close()
		ok := checkPassword(body.Password, hash)
		if found == nil || !ok {
			fail(w, http.StatusUnauthorized, "sai tên đăng nhập hoặc mật khẩu")
			return
		}
		writeJSON(w, http.StatusOK, map[string]any{"token": signToken(found.ID, version), "user": found})

	// tạo/sửa tài khoản: chỉ bằng mã chung (script trên máy), chưa có trang quản lý tài khoản
	case r.Method == http.MethodPut && q.Has("user"):
		if !authorized(r) {
			fail(w, http.StatusUnauthorized, "sai mật khẩu")
			return
		}
		var body struct{ Username, Name, Role, Password string }
		if json.NewDecoder(http.MaxBytesReader(w, r.Body, 4096)).Decode(&body) != nil {
			fail(w, http.StatusBadRequest, "dữ liệu không hợp lệ")
			return
		}
		username, name := loginName(body.Username), strings.TrimSpace(body.Name)
		if len([]rune(name)) > 60 {
			name = string([]rune(name)[:60])
		}
		validRole := false
		for _, x := range accountRoles {
			validRole = validRole || x == body.Role
		}
		switch {
		case !accountNameRe.MatchString(username):
			fail(w, http.StatusBadRequest, "tên đăng nhập chỉ gồm chữ thường, số, . _ -")
			return
		case name == "":
			fail(w, http.StatusBadRequest, "cần tên hiển thị")
			return
		case !validRole:
			fail(w, http.StatusBadRequest, "vai trò không hợp lệ")
			return
		case len(body.Password) < 6:
			fail(w, http.StatusBadRequest, "mật khẩu tối thiểu 6 ký tự")
			return
		}
		h, err := hashPassword(body.Password)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		var u AppUser
		err = p.QueryRow(ctx, `INSERT INTO app_users (username, name, role, pass_hash) VALUES ($1, $2, $3, $4)
			ON CONFLICT (username) DO UPDATE SET name = EXCLUDED.name, role = EXCLUDED.role, pass_hash = EXCLUDED.pass_hash,
			                                     token_version = app_users.token_version + 1
			RETURNING id, username, name, role`, username, name, body.Role, h).Scan(&u.ID, &u.Username, &u.Name, &u.Role)
		if err != nil {
			fail(w, http.StatusInternalServerError, "lỗi ghi dữ liệu")
			return
		}
		writeJSON(w, http.StatusOK, map[string]any{"user": u})

	default:
		fail(w, http.StatusBadRequest, "cần ?login, ?me hoặc ?user")
	}
}
