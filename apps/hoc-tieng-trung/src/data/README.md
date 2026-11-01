# Dữ liệu bài học

- `lessons.json`: bài Cấp 1–3, có sẵn trong gói app. `lv` là cấp, `no` là số bài.
- `lessons-4.json`, `lessons-5.json`, `lessons-6.json`, `lessons-7.json`: bài Cấp 4, 5, 6 và Cấp 7–9 (`lv` 7), mỗi bài một dòng.
  App chỉ tải file của một cấp khi cần (`loadLevel` trong `src/core/data.js`); tóm tắt các bài lấy qua module ảo `virtual:lesson-index` (`vite.config.js`). Mỗi từ là mảng
  `[chữ Hán, pinyin theo âm tiết, Hán Việt, nghĩa, ví dụ (tách từ bằng |), pinyin ví dụ, nghĩa ví dụ]`.
- `pinyin.json`: bảng âm tiết pinyin.

## Nguồn

| Cấp | Nguồn |
| --- | --- |
| 1 | Giáo trình 新HSK教程 1 (SÁCH HSK1 PHIÊN BẢN 3.0) |
| 2 | Giáo trình 新HSK教程 2 (Giáo trình chuẩn HSK 2 phiên bản 3.0) |
| 3 | Chuẩn chính thức 《国际中文教育中文水平等级标准》 GF0025-2021, danh sách từ vựng và ngữ pháp cấp 3 |
| 4, 5, 6, 7–9 | Cùng chuẩn GF0025-2021, danh sách từ vựng và ngữ pháp của từng cấp (Cấp 7–9 gộp một như trong chuẩn) |

Cấp 3 chưa có giáo trình nên bám thẳng vào chuẩn HSK 3.0 do Bộ Giáo dục Trung Quốc và Ủy ban Ngôn ngữ Văn tự Quốc gia ban hành
(GF0025-2021, áp dụng từ 01/07/2021). Bản gốc là PDF quét, không có lớp chữ, nên danh sách lấy từ bản đã số hóa và đối chiếu:

- Repo [ivankra/hsk30](https://github.com/ivankra/hsk30), commit `4ff9e3915ce87baaecd7ebe263085573a4ea3192` (08/11/2023), giấy phép MIT.
  Dữ liệu ở đó được đối chiếu với bản OCR của elkmovie/hsk30 và cơ sở dữ liệu trên trang chinesetest.cn.
  - Từ vựng: <https://raw.githubusercontent.com/ivankra/hsk30/master/hsk30.csv>
  - Ngữ pháp: <https://raw.githubusercontent.com/ivankra/hsk30/master/hsk30-grammar.csv>

Thư mục `hsk30/` giữ phần trích cấp 3:

- `cap3-tu-vung.csv`: 973 mục từ cấp 3 (cột của repo gốc, bớt các cột không dùng).
- `cap3-ngu-phap.csv`: 81 điểm ngữ pháp cấp 3 (No 131–211).
- `cap3-ke-hoach.txt`: kế hoạch 40 bài theo chủ đề đời sống. Mỗi dòng: số bài, chủ đề, các điểm ngữ pháp, các từ.
  Kế hoạch phủ 944 mục từ cấp 3 chưa có ở Cấp 1–2 của app (29 từ cấp 3 đã học trong giáo trình Cấp 1–2 nên không lặp lại)
  và đủ 81 điểm ngữ pháp.

Một chữ có hai mục trong chuẩn (把 giới từ và lượng từ, 背 bēi và bèi, 调 tiáo và diào, 为, 任, 精神) được gộp thành một từ trong bài,
nghĩa ghi cả hai. Các mục hậu tố, tiền tố dùng từ ví dụ của chuẩn làm mục từ: `…极了` → 极了, `初（初一）` → 初一,
`化（现代化）` → 现代化, `性（积极性）` → 积极性, `员（服务员）` → 服务员, `者（志愿者）` → 志愿者.

Ví dụ, hội thoại, giải thích ngữ pháp và lời giảng của Cấp 3 do Claude soạn theo kế hoạch trên, không chép từ sách.

## Soạn thêm bài Cấp 3

1. Viết bài theo đúng dạng các bài `lv: 3` hiện có, đủ từ và ngữ pháp của dòng tương ứng trong `cap3-ke-hoach.txt`.
2. `python3 tools/check_cap3.py` kiểm tra từ, pinyin, Hán Việt, lời giảng không lẫn chữ Hán và báo tiến độ phủ chuẩn.
3. `npm run build && npm run preview`, rồi `tools/gen_audio.py` tạo giọng đọc, `tools/make_video.py <tạm> public/video 3-11 ...` dựng video.

## Cấp 4 trở lên

`hsk30/` có thêm `cap4-…`, `cap5-…`, `cap6-…`, `cap7-9-…` (từ vựng, ngữ pháp, kế hoạch), cùng cách làm như Cấp 3:
Cấp 4, 5, 6 mỗi cấp 40 bài, Cấp 7–9 150 bài, phủ đủ từ và điểm ngữ pháp của chuẩn.
Mục từ có ngoặc dùng từ ví dụ của chuẩn (`…分之…` → 百分之, `力（影响力）` → 影响力…); vài từ đã dạy ở Cấp 1–2 với cùng âm và nghĩa
(女士, 妻子, 丈夫, 售货员, 蛋糕, 没意思) không lặp lại; chữ trùng mặt chữ nhưng là âm hay nghĩa mới (得 děi, 好 hào, 着 zháo…) vẫn học.
Bảng chuẩn hóa nằm trong `tools/check_level.py`.

- `python3 tools/check_level.py 4` kiểm tra kế hoạch và các bài trong `lessons-4.json` (Cấp 7–9 dùng số 7): đủ từ, pinyin đúng chuẩn,
  số âm Hán Việt, lời giảng không lẫn chữ Hán.
- `python3 tools/check_level.py 4 --show 12` in từ và điểm ngữ pháp của bài 12 để soạn.
- Giọng đọc: route `#/alltexts/4` liệt kê câu của Cấp 4 (mặc định `#/alltexts` chỉ là Cấp 1–3). Chưa có video cho Cấp 4 trở lên.
