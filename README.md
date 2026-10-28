# Trang cá nhân: bản đồ du lịch + học tiếng Trung

Monorepo React (Vite + npm workspaces), chia thành các app độc lập dùng chung một thư viện component.

```
packages/ui/            @trang/ui — component dùng chung (Button, Card, Tabs, AppShell, Icon, …) và tokens.css
apps/home/              trang chủ: hai thẻ chọn Travel plan / App học tiếng Trung   → /
apps/hoc-tieng-trung/   app Hán Lộ học tiếng Trung (HashRouter)                     → /hoc-tieng-trung/
apps/ban-do/            bản đồ 34 tỉnh: đánh dấu đã đi / muốn đi và ghi chú          → /ban-do/
packages/sync/          @trang/sync — đồng bộ localStorage lên API, nút "Đồng bộ" chọn Node.js / Go
travel/                 sổ tay chuyến Tam Đảo – Đà Lạt, HTML tĩnh (sẽ chuyển React sau) → /travel/
lop-hoc/                lớp học trực tiếp: video, bảng vẽ trên slide, chat (trang tĩnh + Ably)   → /lop-hoc/
backend/go/, backend/node/   cùng một API viết bằng Go và Node.js (xem backend/README.md)
api/go/, api/node/      lối vào Vercel Functions                                     → /api/go/…, /api/node/…
scripts/build.mjs       build cả site vào dist/
```

Mỗi app build riêng (`npm -w apps/<tên> run build`); `npm run build` gộp tất cả vào `dist/` theo đúng
đường dẫn trên. Các app liên kết với nhau bằng đường dẫn thường, không nạp nhau lúc chạy.

## Lệnh

```bash
npm install
npm run dev:home        # trang chủ ở http://localhost:5173
npm run dev:zh          # app học ở http://localhost:5174/hoc-tieng-trung/
npm run dev:map         # bản đồ ở http://localhost:5175/ban-do/
npm run dev:api         # API Node + Go ở http://localhost:3001 (vite dev tự chuyển /api sang đây)
npm run build           # build cả site vào dist/
npm run preview         # xem bản build ở http://localhost:4173
```

Deploy Vercel: `vercel.json` đã đặt build `npm run build`, thư mục xuất `dist`. Thư mục `api/` tự thành
Vercel Functions (Go và Node). Cần các biến môi trường: `DATABASE_URL` (tự có khi gắn Neon ở mục Storage),
`APP_SECRET` (mã đồng bộ chung), `GEMINI_API_KEY` (thêm `GROQ_API_KEY`, `OPENROUTER_API_KEY`, `MISTRAL_API_KEY` nếu muốn AI dự phòng), và cho lớp học trực tiếp `ABLY_API_KEY`
(xem [lop-hoc/README.md](lop-hoc/README.md)). Mẫu ở `.env.example`.

## Backend: một API, hai ngôn ngữ

Xem [backend/README.md](backend/README.md). Tóm tắt: `/api/<node|go>/sync` lưu dữ liệu localStorage của
các app vào Postgres (bảng `docs`), `/api/<node|go>/ai` gọi Gemini bằng khóa giấu trên server. Hai bản
giống hệt nhau về đường dẫn, dữ liệu vào/ra và bảng, nên trên giao diện (nút "Đồng bộ") đổi qua lại
Node.js ↔ Go bất cứ lúc nào mà không mất gì. Chưa nhập mã đồng bộ thì app chạy như cũ, chỉ lưu trong máy.

## Thư viện component `@trang/ui`

`import '@trang/ui/tokens.css'` một lần ở điểm vào của app (màu, font, giao diện sáng/tối), rồi
`import { Button, Card, AppShell, … } from '@trang/ui'`. Component nhận `as` để dùng với `Link` của router.
Màu chỉ lấy từ token trong `tokens.css`; thêm biểu tượng thì thêm vào `Icon.jsx`.

## Bản đồ "Đã đi qua" (`apps/ban-do/`)

Bản đồ SVG 34 tỉnh thành (sau sáp nhập 1/7/2025) vẽ bằng `d3-geo`; chọn một tỉnh để đánh dấu đã đi /
muốn đi và viết ghi chú, lưu localStorage khóa `da-di-qua-v1`, có xuất/nhập JSON.
Ranh giới nằm sẵn trong `src/data/provinces.json` — xem [apps/ban-do/README.md](apps/ban-do/README.md)
để biết nguồn dữ liệu và lưu ý về chiều cuộn polygon của d3-geo.

## Bản đồ du lịch (`apps/ban-do/`)

Xem `apps/ban-do/README.md`. Các chuyến đi khai báo trong `apps/ban-do/src/trips.js` (điểm dừng, tọa độ,
đường đi); danh sách địa điểm của chuyến 3–11/10 nằm ở `src/data/trip-2026-10.json`, trích từ
`travel/index.html`. Dấu tích "đã ghé" dùng chung khóa localStorage `dadiqua-trip` với sổ tay, nên tích
ở bản đồ hay ở sổ tay đều thấy ở cả hai (cùng trình duyệt).

## App học tiếng Trung (`apps/hoc-tieng-trung/`)

- `src/core/` — dữ liệu (`data.js`), tiến độ trong localStorage khóa `hanlo-v2` (`store.js`), giọng đọc
  (`speech.js`), dựng bài giảng (`lecture.js`), tiện ích pinyin (`pinyin.js`).
- `src/views/` — mỗi màn hình một file + css riêng; `src/components/` — LecturePlayer, Hanzi.
- `src/data/lessons.json` — 30 bài (512 từ) bám chủ đề, từ vựng, ngữ pháp của 新HSK教程 1–2; câu ví dụ,
  hội thoại và lời giảng là nội dung tự soạn. `src/data/pinyin.json` — 400 âm tiết cho bảng pinyin.
- `public/audio/` — giọng đọc tạo sẵn (tiếng Việt: giọng Linh của macOS; tiếng Trung: giọng neural Xiaoxiao) (`<khóa>.mp3`, khóa băm của `ngôn ngữ|câu`, danh sách ở
  `index.json`); câu thiếu file thì đọc bằng giọng trình duyệt.
- `public/video/` — MP4 bài giảng 1280×720, danh sách ở `index.json`.
- Route riêng cho công cụ: `#/render/:id/:bước`, `#/steps/:id`, `#/alltexts`.

### Tạo lại giọng đọc và video

Cần macOS (lệnh `say`), Google Chrome, ffmpeg (`brew install ffmpeg`), Python có `edge-tts`, và bản build đang chạy (`npm run preview`):

```bash
python3 apps/hoc-tieng-trung/tools/gen_audio.py
npm run build   # để public/audio mới vào dist
python3 apps/hoc-tieng-trung/tools/make_video.py /tmp/hanlo apps/hoc-tieng-trung/public/video all
```

`gen_audio.py --lang vi|zh --force` tạo lại một ngôn ngữ (dùng khi đổi giọng).

Pinyin và âm Hán Việt nên được người biết tiếng Trung soát lại trước khi dùng để dạy.
