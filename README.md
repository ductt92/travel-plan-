# Đà Lạt & Tam Đảo

Sổ tay hai chuyến nghỉ dưỡng. Mở ra là màn chọn điểm đến, vào rồi thì chọn độ dài
chuyến, xem danh sách Ăn / Chơi và tích vào từng nơi đã ghé.

Toàn bộ là **một file `index.html` tĩnh** — không build, không dependency, không
backend. Font lấy từ Google Fonts qua CDN; ngoài ra không gọi mạng.

## Chạy tại chỗ

Mở thẳng `index.html` bằng trình duyệt là xong. Hoặc chạy một server tĩnh:

```bash
python3 -m http.server 8000
```

## Deploy lên Vercel

Zero-config, không cần `vercel.json`:

```bash
npx vercel deploy --prod
```

Lần đầu Vercel sẽ hỏi đăng nhập và tên project. Hoặc push repo này lên GitHub rồi
Import vào Vercel — nó tự nhận đây là static site.

## Dấu tích được lưu ở đâu

Trang lưu vào `localStorage` của trình duyệt: những nơi đã tích và độ dài chuyến
đang chọn, tách riêng cho từng điểm đến.

Nghĩa là **dấu tích không đồng bộ giữa các máy** — mở trên điện thoại sẽ là một
danh sách trắng. Bản chạy trên Claude Artifact có đồng bộ qua server; bản tĩnh này
thì không. Muốn đồng bộ thì cần thêm một backend (Vercel KV, Upstash, Supabase) và
một API route đọc/ghi.

Code đã viết sẵn nhánh cho cả hai: nếu `window.claude` tồn tại thì dùng server,
không thì tự lùi về `localStorage`. Ô trạng thái ở đầu trang cho biết đang ở chế độ nào.

## Sửa nội dung

Địa điểm nằm rải trong `index.html` dưới dạng:

```html
<input type="checkbox" data-place="docthi" data-cat="an">
```

- `data-place` — mã định danh, **trùng mã thì tích một chỗ là ăn sang mọi chỗ khác**
- `data-cat` — `an` hoặc `choi`, quyết định nhãn màu và bảng đếm

Mỗi lịch trình là một `<div class="plan" data-plan data-plan-len="3">`; số ở
`data-plan-len` phải khớp với `data-len` của nút chọn tương ứng.

## Nguồn dữ liệu

Địa chỉ, giờ mở cửa và số điện thoại tra từ các trang du lịch / ẩm thực Đà Lạt và
Vĩnh Phúc, **không gọi kiểm chứng từng nơi**. Nên xác nhận lại trước khi đi xa.
