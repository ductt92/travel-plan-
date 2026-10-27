# Trang cá nhân: bản đồ du lịch + học tiếng Trung

Monorepo React (Vite + npm workspaces), chia thành các app độc lập dùng chung một thư viện component.

```
packages/ui/            @trang/ui — component dùng chung (Button, Card, Tabs, AppShell, Icon, …) và tokens.css
apps/home/              trang chủ: hai thẻ chọn Travel plan / App học tiếng Trung   → /
apps/hoc-tieng-trung/   app Hán Lộ học tiếng Trung (HashRouter)                     → /hoc-tieng-trung/
apps/ban-do/            bản đồ 34 tỉnh: đánh dấu đã đi / muốn đi và ghi chú          → /ban-do/
travel/                 sổ tay chuyến Tam Đảo – Đà Lạt, HTML tĩnh (sẽ chuyển React sau) → /travel/
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
npm run dev:map         # bản đồ ở http://localhost:5175/ban-do/
npm run build           # build cả site vào dist/
npm run preview         # xem bản build ở http://localhost:4173
```

Deploy Vercel: `vercel.json` đã đặt build `npm run build`, thư mục xuất `dist`.

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
