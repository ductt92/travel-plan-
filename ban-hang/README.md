# ban-hang: web bán đồ tập FITGEAR

Trang tĩnh (HTML/CSS/JS thuần, không qua Vite) chạy ở `/ban-hang/`, trang quản trị ở `/ban-hang/quan-tri/`.
`scripts/build.mjs` chép nguyên thư mục này vào `dist/ban-hang/` (trừ file README này).

- API: `/api/node/ban-hang/*`, logic ở `backend/node/banhang/` (Express). Không tạo function mới vì gói Hobby giới hạn
  12 function: `vercel.json` chuyển `/api/node/ban-hang/<đường dẫn>` sang `api/node/quan-ly.js` kèm `?_api=ban-hang&_path=…`.
  Chưa có bản Go.
- Dữ liệu: các bảng `shop_*` trong cùng Postgres (Neon) của repo, tự tạo bảng và dữ liệu ban đầu lần đầu có người mở trang.
- Ảnh có sẵn ở `anh/` là ảnh minh hoạ từ Unsplash. Ảnh tải lên trong trang quản trị được trình duyệt thu nhỏ (tối đa 1600px)
  rồi lưu vào bảng `shop_images`, đọc qua `/api/node/ban-hang/img/<id>`.
- `vercel.json` có rewrite `/ban-hang/:path*` về `index.html` để đường dẫn như `/ban-hang/san-pham/...` mở thẳng được.

## Đăng nhập quản trị

Email `admin@fitgear.local`, mật khẩu là `SHOP_ADMIN_PASSWORD` nếu có đặt trên Vercel, không thì là `APP_SECRET`
(chỉ dùng lúc tạo tài khoản lần đầu). Đổi mật khẩu ngay sau khi vào, bằng nút tên tài khoản ở góc phải trên.

## Chạy ở máy

```bash
npm run dev:api          # API ở http://localhost:3001/api/node/ban-hang/...
```

Trang tĩnh gọi API bằng đường dẫn tuyệt đối `/api/node/ban-hang`, nên cần một server phục vụ cả `ban-hang/` lẫn API
cùng một địa chỉ (ví dụ `vercel dev`).

Dữ liệu demo (khách, đơn hàng, nhân viên `nhanvien@fitgear.local`) chỉ nên tạo trên database thử:

```bash
DATABASE_URL=postgres://... node scripts/seed-ban-hang.mjs --demo
DATABASE_URL=postgres://... node scripts/seed-ban-hang.mjs --reset --yes --demo   # xoá hết rồi tạo lại
```

`.env.local` có thể đang trỏ vào Neon thật, nên luôn ghi rõ `DATABASE_URL` khi chạy lệnh trên.
