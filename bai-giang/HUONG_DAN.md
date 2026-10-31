# Bài giảng video HSK 6 (Hạ)

## Thành phẩm (thư mục `out/`)
- `bai21.mp4` – video bài giảng Bài 21 «未来商店», có phụ đề gắn sẵn trên hình, phụ đề mềm và mục lục chương
- `bai21_slides.pdf` – bộ slide đi kèm (đầy đủ đáp án) để in hoặc trình chiếu
- `bai21.srt` – file phụ đề riêng (dùng khi đăng YouTube…)

## Cấu trúc bài giảng
Mở đầu → Khởi động → Từ mới (54 từ, có âm Hán Việt) → Bài khóa (13 đoạn: nghe đọc, dịch, giảng) →
Bố cục bài → Ngữ pháp 以免, 嫌 → Phân biệt 不免/未免 → Kỹ năng viết: tỉnh lược → Luyện tập → Tổng kết

## Sửa nội dung / làm bài mới
1. Sửa lời giảng trong `bai21_src.py` (hoặc chép thành `bai22_src.py` cho bài mới)
2. Chạy:
   ```bash
   python3 bai21_src.py && python3 make_video.py bai21.json
   ```
   Giọng đọc đã tạo được lưu trong `build/tts_cache`, nên chạy lại chỉ tạo phần thay đổi.

## Trang web học tập (thư mục `site/`)
Trang "Ngọc học tiếng Trung" gồm:
- Video theo từng phần, có slide chạy song song và lời giảng bấm vào để tua
- Slide, từ vựng (danh sách và thẻ ghi nhớ, có đọc mẫu)
- Bài khóa (nghe từng đoạn, xem dịch) và luyện tập (trắc nghiệm, bài tập có đáp án)

Sau khi làm xong video của bài mới, dựng lại trang:
```bash
python3 build_site.py bai21 bai22
```
Giao diện nằm ở `web/template.html`, danh sách bài của các giáo trình ở `web/catalog.json`.

Trang được đưa lên repo `da-di-qua` (monorepo trang cá nhân) ở thư mục `hsk6/`, trang chủ có thẻ "Ngọc học tiếng Trung" mở vào đó. Cập nhật lên repo:
```bash
rsync -a --delete site/ ~/Desktop/Project/da-di-qua/hsk6/
```
rồi commit và push trong repo đó. Video được cắt theo chương và nén 720p, mỗi file dưới 15 MB.

Giọng đọc dùng giọng có sẵn trên macOS: Linh (tiếng Việt) và Tingting (tiếng Trung).
Nếu giọng máy đọc sai chữ đa âm, thêm cặp thay thế vào `tts_replace` (ví dụ `"着重": "酌重"`).
