# Backend: cùng một API viết bằng Go và Node.js

Mục đích: học hai ngôn ngữ bằng cách đặt chúng cạnh nhau. Hai bản có **cùng hợp đồng** (đường dẫn,
JSON vào/ra, mã lỗi) và **cùng bảng dữ liệu**, nên client chỉ đổi tiền tố `/api/go` ↔ `/api/node`.
Mỗi phản hồi có header `X-Backend: go|node` để biết bản nào đã trả lời.

| Việc | Go | Node.js |
|---|---|---|
| Kết nối DB, tạo bảng, kiểm tra mã | `go/common.go` (pgx, `sync.Once`) | `node/common.js` (pg, Pool) |
| Đồng bộ dữ liệu | `go/sync.go` | `node/sync.js` |
| Hỏi AI (Gemini) | `go/ai.go` | `node/ai.js` |
| Nhật ký bản đồ | `go/bando.go` | `node/bando.js` |
| Thuật ngữ du lịch (trang hsk6) | `go/terms.go` | `node/terms.js` |
| Token Ably cho lớp học trực tiếp | `go/lophoc.go` | `node/lophoc.js` |
| Danh mục khóa học (trang quản lý) | `go/catalog.go` | `node/catalog.js` |
| Lối vào Vercel | `../api/go/*.go` | `../api/node/*.js` (tổng cộng 12 function, 6 Node + 6 Go, đúng giới hạn gói Hobby: thêm API mới phải gộp bớt) |
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

**`/api/<go|node>/ban-do`** — nhật ký chuyến đi của trang bản đồ. `GET` ai cũng đọc được, trả
`{entries: {"<mã tỉnh>": {status, trips}}}`; `GET ?check` kiểm mật khẩu. Ghi thì cần mật khẩu
(`APP_SECRET` hoặc `HSK6_PASS`): `PUT ?province=` đặt trạng thái, `POST ?province=` thêm chuyến,
`PATCH ?province=&id=` sửa, `DELETE ?province=&id=` xoá. Bảng `provinces` và `trips` tự tạo ở lần
gọi đầu. Ngày đọc ra bằng `from_date::text` cho khỏi trôi theo múi giờ.

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
Gửi thêm `ice: true` (trang chỉ gửi ở lần xin đầu) thì kèm `iceServers` cho `RTCPeerConnection`: TURN Cloudflare cấp
ngắn hạn (`CF_TURN_KEY_ID`, `CF_TURN_API_TOKEN`), hoặc TURN tĩnh (`TURN_URLS`, `TURN_USERNAME`, `TURN_CREDENTIAL`),
không cấu hình hay Cloudflare lỗi thì chỉ có STUN.

**`/api/<go|node>/quan-ly`** — danh mục khóa học cho trang quản lý: khóa → bài → file. Cơ sở dữ liệu chỉ giữ
danh mục, không giữ file (Neon miễn phí chỉ 0,5 GB). File nằm ở một trong ba nơi (`storage`): `repo` (có sẵn trong repo,
`url` tương đối như `/hsk6/bai01/`), `r2` (Cloudflare R2, trình duyệt tải thẳng lên bằng URL ký sẵn) hoặc `youtube` (chỉ là link).
**Mọi** request cần `X-App-Secret` đúng `APP_SECRET` (không nhận `HSK6_PASS`), sai thì `401 {error}`. Dữ liệu sai thì `400`
kèm lý do, id không có thì `404`, chuỗi bị cắt bớt (tên 200 ký tự, url 2000). Ba bảng `catalog_*` tự tạo ở lần gọi đầu.

- `GET ?check` → `200 {ok: true}` (không đụng cơ sở dữ liệu).
- `GET` → `200 {courses, usage, r2}`:
  `courses: [{id, slug, title, sort, lessons: [{id, num, title, zh, visible, sort, assets: [{id, kind, name, size, url, storage, key, createdAt}]}]}]`
  (khóa theo `sort, id`; bài theo `sort, num`; file theo `kind, name`; `size` là số byte, `createdAt` dạng `2026-10-30T12:00:00.000Z`),
  `usage: {dbBytes, dbLimitBytes: 536870912, r2Bytes, r2LimitBytes: 10737418240, repoBytes, youtubeCount}`
  (`dbBytes` = `pg_database_size` cả cơ sở dữ liệu; `r2Bytes`/`repoBytes` cộng `size` theo nơi lưu, link YouTube chỉ đếm số lượng),
  `r2: {configured, publicUrl}` (`configured` khi đủ năm biến `R2_*`).
- `POST ?course` `{slug, title, sort?}` → `201 {course: {id, slug, title, sort}}`; `slug` dạng `[a-z0-9][a-z0-9-]{0,39}`, trùng thì `409`.
  `PATCH ?course=<id>` `{title?, sort?}` → `200 {course}`. `DELETE ?course=<id>` → `200 {ok: true}` (xoá luôn bài và file bên trong).
- `POST ?lesson` `{courseId, num, title, zh?, visible?, sort?}` → `201 {lesson: {id, num, title, zh, visible, sort, courseId}}`;
  `PATCH ?lesson=<id>` `{num?, title?, zh?, visible?, sort?}` → `200 {lesson}`; `DELETE ?lesson=<id>` → `200 {ok: true}`.
  Trùng số bài trong một khóa thì `409`, `courseId` không có thì `404`. `num` 0–9999, `sort` mặc định 0.
- `POST ?upload` `{lessonId, name, kind, size, type}` → `200 {putUrl, key, publicUrl, headers: {"Content-Type": type}}`: URL `PUT` ký sẵn
  (SigV4, hạn 15 phút) để trình duyệt gửi thẳng file lên R2 với đúng các header đó; `key` = `<slug khóa>/<số bài 2 chữ số>/<unix ms>-<tên file ASCII>`
  (bỏ dấu tiếng Việt, ký tự lạ thành `-`). `size` bắt buộc, quá 200 MB thì `400`; `type` sai dạng thì thành `application/octet-stream`.
  Chưa cấu hình R2 thì `503 {error: "Chưa cấu hình Cloudflare R2 (…)"}`. Tải xong thì gọi `POST ?asset` để ghi vào danh mục.
- `POST ?asset` `{lessonId, kind, name, size?, url, storage, key?}` → `201 {asset: {…, lessonId}}`. `kind` ∈ `video, slides, audio, pdf, other`.
  `storage: "repo"`: `url` bắt đầu bằng `/` hoặc `http(s)://`. `storage: "r2"`: cần `key` (phải nằm dưới `<slug>/<NN>/` của đúng bài này),
  `url` do server dựng = `R2_PUBLIC_URL + "/" + key` (bỏ qua `url` client gửi), `size` tối đa 200 MB. `storage: "youtube"`: `url` phải là link
  `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/embed/` hoặc `youtube.com/shorts/`, server chuẩn hoá thành `https://www.youtube.com/watch?v=<id>`;
  `size` mặc định 0, `key` luôn rỗng, `kind` thường là `video`.
- `DELETE ?asset=<id>` → `200 {ok: true}`. File `r2` thì gửi lệnh xoá (ký SigV4) lên R2 trước, R2 lỗi thì `502` và giữ nguyên dòng;
  `repo` và `youtube` chỉ xoá dòng. Xoá khóa/bài có file `r2` bên trong cũng xoá trên R2 trước như vậy (R2 lỗi → `502`, chưa xoá gì).
- `POST ?import` `{courses: [{slug, title, sort, lessons: [{num, title, zh, assets: [{kind, name, size, url}]}]}]}` → `200 {ok: true, courses, lessons, assets}`
  (số dòng đã ghi). Một transaction: khóa ghi gộp theo `slug` (cập nhật `title`, `sort`), bài theo `(khóa, num)` (cập nhật `title`, `zh`; giữ `visible`, `sort`),
  file của mỗi bài được nhập thì **chỉ thay các file `storage = 'repo'`**, file `r2` và `youtube` giữ nguyên. Tối đa 50 khóa × 500 bài × 50 file, thân 5 MB
  (trên Vercel thân request bị chặn ở 4,5 MB; danh mục hiện tại chỉ ~27 KB). `scripts/seed-catalog.mjs` dựng dữ liệu này từ repo:
  `node scripts/seed-catalog.mjs --dry` để xem tóm tắt, bỏ `--dry` (và `--url …` nếu không chạy ở máy) để ghi.

Cloudflare R2 (10 GB miễn phí, tải xuống không mất phí) cho file mới:
1. Cloudflare → R2 → Create bucket (ví dụ `hsk-media`).
2. Bucket → Settings → Public access: bật `r2.dev` hoặc gắn tên miền riêng; địa chỉ đó là `R2_PUBLIC_URL` (không có `/` cuối).
3. R2 → Manage API tokens → Create token quyền **Object Read & Write**, chỉ cho bucket đó; lấy Access Key ID, Secret Access Key và Account ID.
4. Bucket → Settings → CORS policy, cho phép trình duyệt tải thẳng lên:
   ```json
   [{"AllowedOrigins": ["https://<tên-miền-trang>", "http://localhost:*"], "AllowedMethods": ["PUT", "GET", "HEAD"], "AllowedHeaders": ["Content-Type"], "MaxAgeSeconds": 3600}]
   ```
5. Vercel → Settings → Environment Variables: `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`, `R2_PUBLIC_URL`
   (ở máy thì điền vào `.env.local`). Chữ ký SigV4 viết tay (`presign` trong hai file catalog), không cần SDK.

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
-- trang quản lý: chỉ danh mục, file thật ở repo / R2 / YouTube
CREATE TABLE IF NOT EXISTS catalog_courses (
  id serial PRIMARY KEY, slug text UNIQUE NOT NULL, title text NOT NULL,
  sort integer NOT NULL DEFAULT 0, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS catalog_lessons (
  id serial PRIMARY KEY, course_id integer NOT NULL REFERENCES catalog_courses ON DELETE CASCADE,
  num integer NOT NULL, title text NOT NULL, zh text NOT NULL DEFAULT '',
  visible boolean NOT NULL DEFAULT true, sort integer NOT NULL DEFAULT 0, UNIQUE (course_id, num)
);
CREATE TABLE IF NOT EXISTS catalog_assets (
  id serial PRIMARY KEY, lesson_id integer NOT NULL REFERENCES catalog_lessons ON DELETE CASCADE,
  kind text NOT NULL CHECK (kind IN ('video', 'slides', 'audio', 'pdf', 'other')),
  name text NOT NULL, size bigint NOT NULL DEFAULT 0, url text NOT NULL DEFAULT '',
  storage text NOT NULL CHECK (storage IN ('repo', 'r2', 'youtube')),  -- bảng cũ chưa có 'youtube' thì tự nới ràng buộc
  key text NOT NULL DEFAULT '',                                        -- key object trên R2
  created_at timestamptz NOT NULL DEFAULT now()
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
