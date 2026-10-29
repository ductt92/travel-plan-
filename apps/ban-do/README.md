# Bản đồ "đã đi qua" — Next.js

Trang bản đồ 34 tỉnh thành: bấm vào một tỉnh để xem và ghi chuyến đi. Giao diện dựng
theo bản thiết kế ở `apps/ban-do/prototype/index.html`, dữ liệu nằm trong Postgres
(Neon trên Vercel, Docker ở máy) qua Drizzle và server action.

## Chạy

```bash
npm install          # chạy trong thư mục này, không phải ở gốc repo
npm run db:migrate   # tạo hai bảng, chỉ cần lần đầu
npm run db:import    # nạp dữ liệu đang có
npm run dev          # http://localhost:5177
```

Từ gốc repo cũng được: `npm run dev:map`.

App này **không nằm trong npm workspaces của repo**. Nó dùng React 19 (Next 15 cần),
ba app kia dùng React 18; để chung thì npm kéo React 18 lên gốc và Next lấy nhầm bản
đó, làm hỏng lúc dựng trang. Tách ra nên nó có `node_modules` và `package-lock.json`
riêng, và `npm run build` ở gốc repo không đụng tới nó.

## Database

`DATABASE_URL` lấy theo thứ tự: biến môi trường sẵn có (trên Vercel) → `.env.local`
trong thư mục này → `.env.local` ở gốc repo. **Nghĩa là chạy `npm run db:migrate`
mà không đặt gì thì nó chạy thẳng vào Neon**, vì đó là chuỗi kết nối trong
`.env.local` ở gốc. Muốn thử ở máy thì đặt riêng:

```bash
cp .env.example .env.local    # trỏ vào Postgres chạy bằng Docker (backend/README)
```

Hai bảng, định nghĩa ở `src/db/schema.ts`:

- **provinces** — `code` (mã tỉnh), `status` (`none` · `visited` · `wish`). Chỉ có dòng
  cho tỉnh đã đụng tới; hình 34 tỉnh vẫn nằm trong `src/data/provinces.json`.
- **trips** — mỗi chuyến một dòng, khoá ngoại về `provinces.code`, xoá tỉnh thì xoá theo.
  Ngày để kiểu `date` nên không lệch múi giờ, `places` là `jsonb` giữ nguyên thứ tự.

Đổi schema thì `npm run db:generate` ra file SQL mới trong `drizzle/`, rồi
`npm run db:migrate`. Xem dữ liệu bằng `npm run db:studio`.

Chưa có đăng nhập: server action là đầu vào công khai, ai mở được trang cũng ghi và
xoá được. Dữ liệu từ form đều soát lại ở `src/lib/validate.ts` chứ không tin trình
duyệt, nhưng đó là chống dữ liệu hỏng, không phải chống người lạ.

## Nhập dữ liệu đang có

```bash
npm run db:import                          # cả hai nguồn
npm run db:import -- --dry                 # chỉ xem sẽ làm gì
npm run db:import -- --file sao-luu.json   # từ một file JSON thay vì bảng docs
```

Chạy lại bao nhiêu lần cũng được: chỉ thêm cái còn thiếu.

Hai nguồn:

1. `src/lib/seed.ts` — hai chuyến 3–11/10/2026 rút từ sổ tay `travel/`.
2. Bản ghi `da-di-qua-v1` mà app Vite cũ đồng bộ lên (bảng `docs` trong cùng database),
   dạng `{ "ma-tinh": { status, note } }`. Bảng mới không có chỗ cho ghi chú theo tỉnh,
   nên mỗi ghi chú thành **một chuyến chưa rõ ngày** — chữ giữ nguyên, sửa và xoá được
   như mọi chuyến khác. Mã tỉnh không nhận ra (tên tỉnh đổi từ 1/7/2025) thì bỏ qua và
   kể tên ra ở cuối.

Dấu tích địa điểm `dadiqua-trip` không nhập: nó là tích từng điểm trong lịch trình
`travel/`, bảng mới không có khái niệm tương ứng.

## Mã nguồn

```
src/app/        layout, page (server component), actions.ts (server action), globals.css
src/components/ TravelMap (giữ toàn bộ trạng thái) + bản đồ, bảng tỉnh, ba popup
src/db/         schema, pool + Drizzle, câu đọc
src/lib/        kiểu dữ liệu, định dạng ngày, bộ lọc thời gian, soát dữ liệu, hook
src/data/       provinces.json — hình 34 tỉnh, chỗ đặt nhãn, khung bao tính sẵn
drizzle/        file SQL sinh ra từ schema
scripts/        import.ts
```

Sửa gì hiện ra ngay rồi mới gửi lên server (`src/lib/use-entries.ts`); server báo hỏng
thì màn hình trả về đúng như trước và hiện một dòng lỗi ở đáy trang.

Trang có ba trạng thái: đọc được database thì ghi thẳng xuống đó; chưa cấu hình
`DATABASE_URL` thì bày dữ liệu mẫu và nói rõ là không lưu; có cấu hình mà đọc hỏng thì
để trống chứ không bày dữ liệu mẫu ra — nhìn vào tưởng mất sạch còn tệ hơn.

## Bước sau

1. Auth.js (Google) để chỉ hai đứa sửa được.
2. Ảnh theo từng chuyến, trang chia sẻ công khai, thống kê.

## Trên Vercel

App này là **một project Vercel riêng**, Root Directory đặt là `apps/ban-do`. Nó không gộp được
vào project chính vì project đó build ra một thư mục `dist/` tĩnh, còn app này cần server để chạy
server action và nối Postgres.

Trang chính giữ nguyên đường dẫn `/ban-do/` bằng `rewrites` trong `vercel.json` ở gốc repo, trỏ sang
tên miền của project này. Vì vậy app đặt `basePath: '/ban-do'` — mở thẳng tên miền của project này
ở gốc sẽ ra 404, phải vào `/ban-do/`. Và `allowedOrigins` trong `next.config.ts` phải có tên miền
trang chính, không thì Next chặn server action đi qua proxy.

Nhớ vào Storage của project nối cùng database Neon để có `DATABASE_URL`.

Mỗi lần deploy, id của server action đổi theo. Trang ai đó đang mở từ trước gửi id cũ lên thì server
không nhận ra — app bắt lỗi đó và hiện "Trang đang mở cũ hơn bản trên server, tải lại trang rồi thử
lại", chứ không đánh sập trang. Muốn hết hẳn thì bật **Skew Protection** trong Settings của project,
Vercel sẽ giữ bản cũ sống thêm một thời gian cho các tab đang mở.
