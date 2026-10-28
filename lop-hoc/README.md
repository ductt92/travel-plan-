# Lớp học trực tiếp (bản thử)

1 giáo viên + tối đa 5 học sinh: video/mic như Google Meet, giáo viên vẽ lên slide bài giảng, chat, giơ tay.
Video đi thẳng giữa các máy (WebRTC), server Socket.IO chỉ làm mối và chuyển nét vẽ, chat, trạng thái.
Slide lấy từ `../hsk6/<bài>/slides` (trong repo), hoặc `../BaiGiang/site` (thư mục làm bài), hoặc thư mục đặt ở `SLIDES_DIR`.
Không nằm trong npm workspaces và không được build lên Vercel: cần một server Node chạy liên tục (máy mình, Render, Railway…).

```bash
npm install
npm start            # http://localhost:8780, mật khẩu giáo viên mặc định "giaovien"
```

Đổi mật khẩu: `TEACHER_PASS=... npm start`.

## Thử trên một máy

Mở nhiều tab với `?fake=1` (camera giả, không cần webcam), ví dụ `http://localhost:8780/?fake=1&room=thu`.
Một tab vào bằng Giáo viên, các tab còn lại là Học sinh.

## Đã có

- Video + mic giữa mọi người, bật/tắt mic và camera, đổi camera trước/sau trên điện thoại
- Giáo viên chọn bài, chuyển slide (nút hoặc phím ←/→); học sinh tự theo slide của giáo viên
- Vẽ lên slide: 5 màu, 3 độ dày, tẩy, hoàn tác, xóa trang; nét vẽ giữ riêng cho từng slide
- Giáo viên giao bút cho học sinh, tắt mic học sinh, hạ tay giúp
- Chat, giơ tay, người vào muộn thấy lại nét vẽ và 100 tin nhắn gần nhất
- Nút "Phóng to giáo viên" (hoặc bấm đúp vào ô giáo viên): camera giáo viên chiếm chỗ chính, bảng thu nhỏ
  ở góc nhưng vẫn cập nhật và vẽ được; bấm "Phóng to bảng" hoặc Esc để trở lại. Mỗi người tự chọn, máy nhớ lựa chọn

## Chưa có / lưu ý

- Mọi thứ chỉ nằm trong bộ nhớ server: tắt server là mất nét vẽ và chat
- Điện thoại thật cần **HTTPS** mới mở được camera (localhost thì không cần). Muốn thử bằng điện thoại
  trong cùng wifi, dùng đường hầm HTTPS như `cloudflared tunnel --url http://localhost:8780`
- Chỉ có STUN, chưa có TURN: hai máy ở mạng chặn kết nối trực tiếp (một số mạng 4G, wifi công ty) có thể không thấy hình nhau
- Chưa chia sẻ màn hình, chưa ghi lại buổi học
