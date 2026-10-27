# Ngọc về · 3 – 11/10

Sổ tay một chuyến chín ngày, hai chặng:

| Ngày | Ở đâu |
|---|---|
| T7 03/10 | Ngọc đáp Nội Bài **17:45** → đi thẳng Tam Đảo (60 km), tới nơi đã tối |
| CN 04/10 | Cả Tam Đảo trong một buổi sáng → ra thẳng Nội Bài, bay chiều vào Đà Lạt |
| T2 05/10 | Ngủ bù, chiều Dốc Thị |
| T3–T4 06–07/10 | Trung tâm: Tuyền Lâm, Langbiang |
| T5 08/10 | Trại Mát + chùa Ve Chai, chiều để trống |
| T6 09/10 | Dậy 4:30 đi Cầu Đất – D'ran, tối về lại phố |
| T7 10/10 | Ngủ nướng, chiều mua quà |
| CN 11/10 | Bay DLI → HAN |

Đầu trang có **đồng hồ đếm ngược** tới lúc Ngọc đáp Nội Bài (17:45 ngày 3/10);
sau mốc đó nó tự chuyển sang đếm ngày thứ mấy của chuyến, và sau 11/10 thì dừng.
Mốc nằm trong `travel/index.html` dưới dạng `Date.parse('2026-10-03T17:45:00+07:00')` —
đổi giờ bay thì đổi đúng chỗ đó.

Sau 11/10 ô đó đổi thành **"Đã đi cùng nhau"** và hiện tấm ảnh chụp chung. Ảnh
đọc từ `anh/da-di-cung-nhau.jpg`; chưa có file thì nó hiện một khung gạch đứt
nhắc bỏ ảnh vào, chứ không vỡ layout.

Mở ra là lịch trình theo ngày; hai mục **Tam Đảo** và **Đà Lạt** bên dưới là danh
sách chi tiết từng quán và từng điểm, tích vào ô khi đã ghé. Dấu tích dùng chung
một mã `data-place`, nên tích ở lịch trình là ăn sang danh sách chi tiết và ngược lại.

Toàn bộ là **một file `travel/index.html` tĩnh** — không build, không dependency, không
backend. Font lấy từ Google Fonts qua CDN; ngoài ra không gọi mạng.

## Chạy tại chỗ

Mở thẳng `travel/index.html` bằng trình duyệt là xong. Hoặc chạy một server tĩnh:

```bash
python3 -m http.server 8000   # chạy ở gốc repo rồi mở /travel/
```

## Deploy lên Vercel

Zero-config, không cần `vercel.json`:

```bash
npx vercel deploy --prod
```

Lần đầu Vercel sẽ hỏi đăng nhập và tên project. Hoặc push repo này lên GitHub rồi
Import vào Vercel — nó tự nhận đây là static site.

## Dấu tích được lưu ở đâu

Trang lưu vào `localStorage` dưới khóa `dadiqua-trip`. Lần mở đầu tiên, nếu chưa có
khóa đó, nó gộp dấu tích cũ từ `dadiqua-dalat` và `dadiqua-tamdao` của bản hai-điểm-đến
trước đây, nên không mất gì.

Nghĩa là **dấu tích không đồng bộ giữa các máy** — mở trên điện thoại sẽ là một
danh sách trắng. Bản chạy trên Claude Artifact có đồng bộ qua server (doc `trip/2026-10`);
bản tĩnh này thì không. Muốn đồng bộ thì cần thêm một backend (Vercel KV, Upstash,
Supabase) và một API route đọc/ghi.

Code đã viết sẵn nhánh cho cả hai: nếu `window.claude` tồn tại thì dùng server,
không thì tự lùi về `localStorage`. Ô trạng thái ở đầu trang cho biết đang ở chế độ nào.

## Sửa nội dung

Địa điểm nằm rải trong `travel/index.html` dưới dạng:

```html
<input type="checkbox" data-place="docthi" data-cat="an">
```

- `data-place` — mã định danh, **trùng mã thì tích một chỗ là ăn sang mọi chỗ khác**
- `data-cat` — `an` hoặc `choi`, quyết định nhãn màu và bảng đếm

Các con số trên đầu trang đều tự đếm từ DOM, không hardcode:

- ô lớn và thanh tiến độ đếm những nơi **nằm trong lịch trình** (`#lich`)
- nơi đã tích nhưng không có trong lịch hiện ra thành "thêm N nơi ngoài lịch"
- mỗi `<div class="leg">` tự đếm phần của chặng đó
- ô ngày trên dải chín ngày sáng lên khi mọi nơi của ngày đó đã tích — dải này nối
  với ngày qua `href="#d03"` và `id="d03"`, đổi ngày thì đổi cả hai

## Nguồn dữ liệu

Địa chỉ, giờ mở cửa và số điện thoại tra từ các trang du lịch / ẩm thực Đà Lạt và
Vĩnh Phúc, **không gọi kiểm chứng từng nơi**. Nên xác nhận lại trước khi đi xa.
