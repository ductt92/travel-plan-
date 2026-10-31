# Bài giảng video HSK 6 và 顶石中文

Bộ dựng bài giảng cho trang "Ngọc học tiếng Trung" (`/hsk6/` của site). Trước đây nằm ở `~/Desktop/HSK/BaiGiang`;
ngày 31/10/2026 thư mục đó bị xoá, phần này được khôi phục vào repo (xem mục **Khôi phục** cuối trang).

## Thư mục
- `baiNN_src.py` – kịch bản 40 bài HSK 6 (Thượng: 1–20, Hạ: 21–40); `dsXY_src.py` – 24 bài 顶石中文 (chủ đề X, bài Y)
- `make_video.py` – dựng video bài giảng từ `<bài>.json`
- `build_site.py` – dựng trang web, ghi thẳng vào `../hsk6/` (đổi chỗ bằng biến `HSK6_SITE`)
- `web/` – giao diện `template.html`, danh sách bài `catalog.json`, trang ngữ pháp `ngu-phap.html`, ảnh, file mẫu
- `thuat_ngu.py` – đọc file Excel thuật ngữ (dữ liệu nay nằm trong Postgres, xem trang bản đồ)
- `tools/overnight_site.sh` – chạy qua đêm: bài nào render xong thì dựng trang, cuối cùng commit và push `hsk6/`
- `out/`, `build/`, `<bài>.json` là file sinh ra, không đưa lên git (`.gitignore`)

## Thành phẩm của một bài (thư mục `out/`)
- `bai21.mp4` – video bài giảng, có phụ đề gắn sẵn trên hình, phụ đề mềm và mục lục chương
- `bai21_slides.pdf` – bộ slide đi kèm (đầy đủ đáp án) để in hoặc trình chiếu
- `bai21.srt` – file phụ đề riêng (dùng khi đăng YouTube…)

## Sửa nội dung / làm bài mới
1. Sửa lời giảng trong `bai21_src.py` (hoặc chép thành `bai22_src.py` cho bài mới)
2. Chạy (trong thư mục `bai-giang/`):
   ```bash
   python3 bai21_src.py && python3 make_video.py bai21.json
   ```
   Giọng đọc đã tạo được lưu trong `build/tts_cache`, nên chạy lại chỉ tạo phần thay đổi.

## Trang web học tập (`hsk6/` của repo)
Trang gồm video theo từng phần (slide chạy song song, lời giảng bấm vào để tua), slide, từ vựng (danh sách và
thẻ ghi nhớ, có đọc mẫu), bài khóa và luyện tập.

Sau khi làm xong video của bài mới, dựng lại trang rồi commit, push `hsk6/`:
```bash
python3 build_site.py ds41 ds42
```
Bài không ghi tên giữ nguyên dữ liệu đang có trong `hsk6/index.html`, nên chỉ cần `out/` của các bài vừa làm.
Video được cắt theo chương và nén 720p, mỗi file dưới 15 MB.

Giọng đọc dùng giọng có sẵn trên macOS: Linh (tiếng Việt) và Tingting (tiếng Trung).
Nếu giọng máy đọc sai chữ đa âm, thêm cặp thay thế vào `tts_replace` (ví dụ `"着重": "酌重"`).

## Khôi phục (31/10/2026)
Các file được dựng lại từ lịch sử các phiên Claude (mọi lần Write/Edit, theo thứ tự thời gian):
- `web/template.html`, `web/catalog.json`, `web/ngu-phap.html`, ảnh và `web/samples/` lấy ngược từ trang đã
  dựng trong `hsk6/`, nên giống hệt bản đang chạy (dựng lại không đổi gì `hsk6/index.html`).
- 64 kịch bản `*_src.py` đều chạy được. 53 bài khớp số slide với trang đang chạy; 11 bài thiếu 1–3 slide so với bản
  đã render (sửa sau bằng lệnh ngoài, không còn lịch sử): bai07, bai19, bai20, bai25, bai26, bai37, bai38, ds12,
  ds13, ds22, ds23. Các bài này vẫn đủ trên web; chỉ cần bổ sung nếu render lại.
- 16 bài 顶石中文 chưa render (ds33, ds41–ds83) còn nguyên kịch bản, render được ngay.
- `make_video.py`, `build_site.py` có thể thiếu vài sửa nhỏ làm ngoài Edit: kiểm tra kỹ bài đầu tiên khi render lại.
- Không khôi phục được: PDF giáo trình gốc, file Excel thuật ngữ gốc, `out/` (video trọn bài), `dispatch.sh`.
  Video trọn bài HSK 6 có thể ghép lại từ `hsk6/baiNN/vid/c*.mp4`.
