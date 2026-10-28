# Backend: cùng một API viết bằng Go và Node.js

Mục đích: học hai ngôn ngữ bằng cách đặt chúng cạnh nhau. Hai bản có **cùng hợp đồng** (đường dẫn,
JSON vào/ra, mã lỗi) và **cùng bảng dữ liệu**, nên client chỉ đổi tiền tố `/api/go` ↔ `/api/node`.
Mỗi phản hồi có header `X-Backend: go|node` để biết bản nào đã trả lời.

| Việc | Go | Node.js |
|---|---|---|
| Kết nối DB, tạo bảng, kiểm tra mã | `go/common.go` (pgx, `sync.Once`) | `node/common.js` (pg, Pool) |
| Đồng bộ dữ liệu | `go/sync.go` | `node/sync.js` |
| Hỏi AI (Gemini) | `go/ai.go` | `node/ai.js` |
| Thuật ngữ du lịch (trang hsk6) | `go/terms.go` | `node/terms.js` |
| Token Ably cho lớp học trực tiếp | `go/lophoc.go` | `node/lophoc.js` |
| Lối vào Vercel | `../api/go/*.go` | `../api/node/*.js` |
| Chạy ở máy | `../cmd/dev-api` (gọi từ `npm run dev:api`) | chạy ngay trong `../scripts/dev-api.mjs` |

## Hợp đồng

Mọi request cần header `X-App-Secret: <APP_SECRET>`, sai thì `401 {"error": "sai mã đồng bộ"}`
(riêng `GET /terms` và `POST /lop-hoc` thì không cần). Với `/terms` và `/ai`, header này nhận cả mật khẩu riêng của
trang hsk6 (`HSK6_PASS`, cho Ngọc); `GET /terms?check` trả `200 {ok: true}` nếu đúng, `401` nếu sai (trang dùng lúc đăng nhập).

**`GET /api/<go|node>/sync?key=<khóa>`** → `200 {key, data, version, updatedAt}`
(chưa có thì `version: 0, data: null`). Khóa hợp lệ: `dadiqua-trip`, `da-di-qua-v1`, `hanlo-v2`.

**`PUT /api/<go|node>/sync?key=<khóa>`** với `{data, base}`, trong đó `base` là `version` client đang có.
- Server vẫn ở `base` → ghi, trả `200` với `version` mới.
- Máy khác đã ghi trước → `409` kèm bản mới nhất; client gộp ba chiều (`merge3` trong
  `packages/sync`) rồi gửi lại. Đây là khóa lạc quan: không cần khóa dòng, không mất thay đổi.

**`POST /api/<go|node>/ai`** với `{model?, provider?, system?, contents: [{role, parts: [{text}]}]}` → `200 {text, provider, model}`.
Server chỉ nhận đúng dạng hội thoại, tối đa 16 lượt, mỗi đoạn 8000 ký tự. Gọi lần lượt các AI có khóa
(`GEMINI_API_KEY`, `GROQ_API_KEY`, `OPENROUTER_API_KEY`, `MISTRAL_API_KEY`, thứ tự theo `AI_ORDER`, mặc định
gemini → groq → openrouter → mistral); với Gemini thử lần lượt các model trong `GEMINI_MODELS`
(mặc định `gemini-3.8-flash,gemini-3.5-flash-lite`, mỗi model một hạn mức miễn phí riêng; Google ngừng model cũ thì đổi ở đây hoặc đặt `GEMINI_MODELS`). AI nào hết lượt (429),
lỗi hay quá 20 s thì chuyển sang cái kế tiếp; model vừa hết lượt được bỏ qua một phút. `model` (`gemini-*`) đặt model
Gemini thử đầu tiên, `provider` chỉ dùng một nhà cung cấp (để thử khóa). Tất cả đều hết lượt thì `429`, lỗi khác `502`,
chưa có khóa nào thì `503`; thông báo lỗi liệt kê từng AI đã thử.

**`GET /api/<go|node>/terms`** (không cần mã) → `200 {version, fileName, summaryName, sheets, updatedAt, terms}`,
mỗi thuật ngữ `{key, zh, pinyin, vi, group, majors: [{name, group, n}], sessions: ["2026-09-01"], n}`
(`n` là số dòng trong sheet để giữ thứ tự như file Excel). Chưa có thì `version: 0, terms: []`.

**`GET /api/<go|node>/terms?versions[&limit=20&offset=0]`** → `200 {total, active, limit, offset, versions: [{version, fileName, mode, count, createdAt, saved, active}]}`
(bản đang hiện đứng đầu, còn lại mới nhất trước; mỗi trang mặc định 20, tối đa 100). **`GET ...?version=N`** → bản sao cả danh sách của bản N (`{version, fileName, summaryName,
sheets, mode, updatedAt, terms}`), chưa có bản sao thì `404`.

**`PUT /api/<go|node>/terms`** với `{fileName, summaryName, sheets, terms, mode?}` → **ghi đè toàn bộ**: xóa hết
thuật ngữ cũ rồi ghi danh sách mới trong một transaction, trả `200 {version, count, updatedAt}`.
`mode` chỉ để ghi vào lịch sử: `replace` (mặc định, ghi đè bằng file), `add` (trang đã gộp file vào danh sách cũ),
`edit` (sửa tay trên danh sách), `restore` (khôi phục bản cũ). Mỗi lần ghi lưu kèm bản sao cả danh sách vào `term_upload.terms`, nên bản nào cũng
khôi phục được; bản ghi từ trước khi có lịch sử thì được sao lưu ngay trước lần ghi kế tiếp.

**`PATCH /api/<go|node>/terms?version=N`** với `{active: true|false}` → tắt hoặc bật lại bản N, trả `200 {version, count}`
(bản đang hiện sau khi đổi). Danh sách `GET /terms` luôn là bản mới nhất **đang bật**; tắt hết thì danh sách trống.
Tắt/bật không xóa gì, bản sao vẫn ở `term_upload` (cột `active`).
Trang hsk6 đọc file Excel và chuẩn hóa (`TERM_BE` trong `BaiGiang/web/template.html` bên repo HSK);
server kiểm tra lại từng trường (tối đa 5.000 thuật ngữ, khóa không trùng, buổi học dạng `YYYY-MM-DD`),
sai thì `400` kèm lý do và dữ liệu cũ giữ nguyên.

**`POST /api/<go|node>/lop-hoc`** với `{room, clientId, pass?}` → `200` TokenRequest của Ably
`{keyName, ttl, capability, clientId, timestamp, nonce, mac}`, ký bằng `ABLY_API_KEY` y như `Auth.createTokenRequest`
của thư viện Ably, chỉ cho `presence`, `publish`, `subscribe` trên kênh `lop:<room>`, hạn 1 giờ (thư viện tự xin lại).
`room` dạng `[a-z0-9-]{1,32}`, `clientId` dạng `gv-…` (giáo viên, `pass` phải đúng `HSK6_PASS` hoặc `APP_SECRET`, sai thì `401`)
hoặc `hs-…` (học sinh) với 8–32 chữ thường/số; sai dạng thì `400`, thiếu biến môi trường thì `503`.

Bảng:

```sql
CREATE TABLE IF NOT EXISTS docs (
  key        text PRIMARY KEY,
  data       jsonb NOT NULL,
  version    bigint NOT NULL,
  updated_at timestamptz NOT NULL DEFAULT now()
);
-- thuật ngữ: mỗi lần ghi đè thêm một dòng term_upload, version = id mới nhất
CREATE TABLE IF NOT EXISTS term (
  key text PRIMARY KEY, zh text NOT NULL, pinyin text NOT NULL, vi text NOT NULL, grp text NOT NULL,
  majors jsonb NOT NULL, sessions text[] NOT NULL, n integer NOT NULL
);
CREATE TABLE IF NOT EXISTS term_upload (
  id bigserial PRIMARY KEY, file_name text NOT NULL, summary_name text NOT NULL, sheets jsonb NOT NULL,
  count integer NOT NULL, created_at timestamptz NOT NULL DEFAULT now(),
  mode text NOT NULL DEFAULT 'replace', terms jsonb,  -- bản sao cả danh sách sau lần ghi này
  active boolean NOT NULL DEFAULT true                 -- tắt thì danh sách bỏ qua bản này
);
```

## Chạy ở máy

```bash
docker run -d --name dadiqua-pg -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=dadiqua -p 127.0.0.1:5433:5432 postgres:16-alpine
cp .env.example .env.local      # điền APP_SECRET (và GEMINI_API_KEY nếu muốn thử Hỏi AI)
npm run dev:api                 # Node ở :3001, Go ở :3002 (Node chuyển tiếp /api/go/* sang Go)
npm run dev:map                 # hoặc dev:zh; /api được chuyển sang :3001
```

Thử nhanh bằng curl, đổi `node` thành `go` để so sánh:

```bash
curl -H "X-App-Secret: $APP_SECRET" "http://localhost:3001/api/node/sync?key=dadiqua-trip"
```

## Trên Vercel (miễn phí)

1. Project → Storage → Create → Neon (vùng Singapore) → Connect: tự thêm `DATABASE_URL`.
2. Settings → Environment Variables: thêm `APP_SECRET` và `GEMINI_API_KEY`.
3. Deploy lại. Bảng `docs` tự tạo ở lần gọi đầu.

Trên web, bấm nút **Đồng bộ** (trang chủ app học, trang Hỏi AI, hoặc đầu bản đồ), nhập mã chung và
chọn **Node.js** hoặc **Go**.
