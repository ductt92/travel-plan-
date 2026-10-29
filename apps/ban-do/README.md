# Bản đồ "đã đi qua"

Trang bản đồ 34 tỉnh thành: bấm vào một tỉnh để xem và ghi chuyến đi — ngày, người đi cùng,
nơi đã ghé, cảm nhận. Giao diện dựng theo bản thiết kế ở `prototype/index.html`.

React + Vite + TypeScript, build ra `dist/ban-do/` cùng với cả site. Dữ liệu nằm trong Postgres,
đi qua `/api/<node|go>/ban-do` — cùng một API viết bằng hai thứ tiếng như các endpoint khác
(`backend/node/bando.js`, `backend/go/bando.go`).

## Chạy

```bash
npm install          # ở gốc repo
npm run dev:api      # API Node ở :3001, Go ở :3002
npm run dev:map      # http://localhost:5175/ban-do/
```

Vite chuyển `/api` sang `:3001`. Chọn bản Node hay Go bằng khóa localStorage
`trang-api-backend` — dùng chung với nút "Đồng bộ" của các app khác, đổi ở đâu cũng theo.

## Dữ liệu

Hai bảng, tạo tự động ở lần gọi API đầu tiên (giống bảng `docs` và `term`):

- **provinces** — `code` (mã tỉnh), `status` (`none` · `visited` · `wish`). Chỉ có dòng cho tỉnh
  đã đụng tới; hình 34 tỉnh vẫn nằm trong `src/data/provinces.json`.
- **trips** — mỗi chuyến một dòng, khoá ngoại về `provinces.code`, xoá tỉnh thì xoá theo.
  Ngày để kiểu `date` và đọc ra bằng `from_date::text`, nếu không ngày sẽ trôi một hôm theo
  múi giờ máy chủ.

## Đăng nhập

Đọc thì ai vào cũng xem được — trang này nối từ thẻ "Bản đồ du lịch" ở trang chủ. Ghi, sửa và
xoá thì cần mật khẩu `APP_SECRET` hoặc `HSK6_PASS`, gửi qua header `X-App-Secret`, đúng như
`/api/*/terms` của trang hsk6. Trình duyệt nhớ mật khẩu trong localStorage khóa `ban-do-pass`;
mỗi lần mở trang hỏi lại server `?check`, đổi mật khẩu bên server là lần sau tự về chế độ xem.

Chốt thật nằm ở server: `GET` cho qua, mọi method khác đòi mật khẩu rồi mới chạm database.
Ẩn nút trên màn hình chỉ để đỡ rối mắt.

## Nhập dữ liệu đang có

```bash
npm -w apps/ban-do run db:import                          # cả hai nguồn
npm -w apps/ban-do run db:import -- --dry                 # chỉ xem sẽ làm gì
npm -w apps/ban-do run db:import -- --file sao-luu.json   # từ file JSON thay vì bảng docs
```

Chạy lại bao nhiêu lần cũng được: chỉ thêm cái còn thiếu. Hai nguồn:

1. `src/lib/seed.ts` — hai chuyến 3–11/10/2026 rút từ sổ tay `travel/`.
2. Bản ghi `da-di-qua-v1` mà app cũ đồng bộ lên (bảng `docs` trong cùng database), dạng
   `{ "ma-tinh": { status, note } }`. Bảng mới không có chỗ cho ghi chú theo tỉnh, nên mỗi ghi
   chú thành **một chuyến chưa rõ ngày** — chữ giữ nguyên, sửa và xoá được như mọi chuyến khác.
   Mã tỉnh không nhận ra (tên tỉnh đổi từ 1/7/2025) thì bỏ qua và kể tên ra ở cuối.

Dấu tích địa điểm `dadiqua-trip` không nhập: nó là tích từng điểm trong lịch trình `travel/`,
bảng mới không có khái niệm tương ứng.

## Mã nguồn

```
src/App.tsx        nạp nhật ký, giữ mật khẩu, rồi mới dựng bản đồ
src/components/    TravelMap (giữ toàn bộ trạng thái) + bản đồ, bảng tỉnh, bốn popup
src/lib/api.ts     gọi /api/<node|go>/ban-do
src/lib/           kiểu dữ liệu, định dạng ngày, bộ lọc thời gian, soát dữ liệu, hook
src/data/          provinces.json — hình 34 tỉnh, chỗ đặt nhãn, khung bao tính sẵn
scripts/import.mjs nhập dữ liệu đang có
prototype/         bản thiết kế HTML tĩnh mà app này dựng theo
```

Sửa gì hiện ra ngay rồi mới gửi lên API (`src/lib/use-entries.ts`); server báo hỏng thì màn
hình trả về đúng như trước và hiện một dòng lỗi ở đáy trang.

## Bước sau

Ảnh theo từng chuyến, trang chia sẻ công khai, thống kê.
