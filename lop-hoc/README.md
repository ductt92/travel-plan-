# Lớp học trực tiếp (`/lop-hoc/`)

1 giáo viên + tối đa 5 học sinh: video/mic như Google Meet, giáo viên vẽ lên slide bài giảng, chat, giơ tay.
Chạy miễn phí hoàn toàn, không có server riêng phải bật:

- **Trang** là file tĩnh `index.html`, build vào `dist/lop-hoc/` cùng `lessons.json` (danh sách slide lấy từ `hsk6/`).
- **Video/mic** đi thẳng giữa các máy (WebRTC, mỗi người nối với từng người), không tốn băng thông server.
- **Nét vẽ, chat, làm mối video, ai đang trong phòng** đi qua [Ably](https://ably.com) (gói Free), mỗi phòng một kênh `lop:<phòng>`.
- **Token Ably** do `/api/<node|go>/lop-hoc` ký bằng khóa giấu trên server (xem `backend/README.md`).

## Cài một lần trên Vercel

1. Tạo tài khoản Ably (gói Free), tạo app, vào **API Keys** chép khóa dạng `appId.keyId:secret`.
2. Vercel → Settings → Environment Variables: thêm `ABLY_API_KEY` (khóa vừa chép). Mật khẩu giáo viên dùng chung
   `HSK6_PASS` (mật khẩu trang hsk6 của Ngọc), hoặc mã đồng bộ `APP_SECRET`.
3. **TURN** (để máy khác mạng vẫn thấy và nghe nhau, nên có): Cloudflare Dashboard → Realtime → TURN Server → tạo khóa,
   chép **Turn Token ID** vào `CF_TURN_KEY_ID` và **API Token** vào `CF_TURN_API_TOKEN` (miễn phí 1 TB/tháng).
   Dùng TURN khác (Metered…) thì đặt `TURN_URLS` (cách nhau bởi dấu phẩy), `TURN_USERNAME`, `TURN_CREDENTIAL`.
4. Deploy lại. Vào `https://<tên-miền>/lop-hoc/`, chọn **Giáo viên**, nhập mật khẩu, rồi bấm **Sao chép link mời** gửi học sinh.

## Chạy ở máy

```bash
node lop-hoc/dev.mjs     # http://localhost:8780/lop-hoc/  (đọc ABLY_API_KEY, HSK6_PASS, APP_SECRET từ .env.local)
```

Chưa có khóa Ably: thêm `?local=1` vào link, các tab cùng trình duyệt nói chuyện với nhau qua BroadcastChannel
(không kiểm tra mật khẩu giáo viên). Thêm `?fake=1` để dùng camera giả, ví dụ
`http://localhost:8780/lop-hoc/?local=1&fake=1&room=thu` mở ở vài tab: một tab Giáo viên, còn lại Học sinh.
`?api=go` để xin token qua bản Go thay vì Node.

## Cách các máy giữ cho bảng giống nhau

Không có server giữ trạng thái, nên mỗi máy giữ đủ slide đang mở, nét vẽ mọi trang, ai được giao bút và chat.
Người mới vào gửi `hello`; giáo viên trả lời (không có giáo viên thì người có mã nhỏ nhất) bằng `state` và các gói
`page` (~30 KB một gói). Giáo viên tải lại trang giữa buổi cũng lấy lại được bảng từ học sinh.

Ably gắn `clientId` đã xác thực vào mọi tin. `gv-…` chỉ có được khi đúng `HSK6_PASS` hoặc `APP_SECRET`, nên lệnh đổi slide, xóa trang,
giao bút, tắt mic, hạ tay chỉ được nhận khi đến từ `gv-…`; nét vẽ chỉ nhận từ giáo viên hoặc học sinh đang được giao bút.

## Đã có

- Video + mic, bật/tắt mic và camera, đổi camera trước/sau trên điện thoại
- Giáo viên bấm **📚 Chọn bài giảng** ở thanh trên: danh sách bài có tên đầy đủ, bấm vào bài thấy từng slide kèm tiêu đề,
  chia theo phần (Mở đầu, Từ mới, Bài khóa…), bấm slide nào mở slide đó. Dưới bảng chỉ còn ‹ › (hoặc phím ←/→)
  và tiêu đề slide đang chiếu; học sinh tự theo slide của giáo viên và cũng thấy tiêu đề đó.
  Tên bài và tiêu đề slide lấy từ `hsk6/<bài>/slides/titles.json` (do `BaiGiang/build_site.py` ghi ra cùng ảnh slide)
- Vẽ lên slide: 5 màu, 3 độ dày, tẩy, hoàn tác, xóa trang; nét vẽ giữ riêng cho từng slide
- Giáo viên giao bút cho học sinh, tắt mic học sinh, hạ tay giúp
- Chat, giơ tay; người vào muộn thấy lại nét vẽ và 40 tin nhắn gần nhất
- Nút "Phóng to giáo viên" (hoặc bấm đúp vào ô giáo viên): camera giáo viên chiếm chỗ chính, bảng thu nhỏ ở góc
  nhưng vẫn cập nhật và vẽ được; bấm "Phóng to bảng" hoặc Esc để trở lại

## Chưa có / lưu ý

- Cả phòng rời đi là bảng mất (chưa lưu vào Neon)
- Chưa cấu hình TURN (bước 3) thì chỉ có STUN: hai máy ở mạng chặn kết nối trực tiếp (nhiều mạng 4G, wifi công ty/trường)
  sẽ kẹt ở "không nối được". Đã có TURN thì video đi vòng qua TURN khi không nối thẳng được
- Kết nối hỏng giữa chừng (đổi wifi ↔ 4G…) thì người gọi tự gửi lại offer `iceRestart` để nối lại
- Trình duyệt chặn tự phát video có tiếng (hay gặp trên iPhone) thì hiện nút "Bấm để xem và nghe mọi người"
- Chưa chia sẻ màn hình, chưa ghi lại buổi học
- Nét vẽ gửi 10 lô/giây để tiết kiệm tin nhắn Ably; gói Free đủ cho vài người, xem hạn mức hiện tại ở trang giá của Ably
