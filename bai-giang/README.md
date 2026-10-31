# bai-giang/ — bản sao lưu bộ dựng bài giảng HSK 6 và 顶石中文

Bản làm việc nằm ở `~/Desktop/HSK/BaiGiang` (cách dùng: `HUONG_DAN.md`). Thư mục này chỉ để lưu trên git,
phòng khi bản trên máy mất như ngày 31/10/2026; không đưa lên web (`scripts/build.mjs` không chép nó).

- Đồng bộ từ bản làm việc (chỉ mã nguồn, không chép `out/`, `build/`, `site/`):
  ```bash
  B=~/Desktop/HSK/BaiGiang
  rsync -a $B/*_src.py $B/make_video.py $B/build_site.py $B/thuat_ngu.py $B/HUONG_DAN.md $B/ngu-phap-tinh-huong.html bai-giang/
  rsync -a $B/tools/*.sh bai-giang/tools/
  rsync -a $B/web/{template.html,catalog.json,ngu-phap.html,published.json,ngoc.webp} bai-giang/web/
  rsync -a --delete $B/web/samples/ bai-giang/web/samples/
  ```
- Khôi phục lại bản làm việc: chép ngược thư mục này về `~/Desktop/HSK/BaiGiang`. `web/published.json` giữ dữ liệu
  mọi bài đã lên trang, nên dựng lại không làm rơi bài cũ dù không còn video gốc trong `out/`.
- Đừng chạy `tools/overnight_site.sh` ngay trong repo: nó dựng vào `site/` cạnh nó rồi `rsync --delete` sang `hsk6/`,
  mà `site/` ở đây trống, sẽ xoá các bài đang có.
