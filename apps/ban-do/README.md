# Bản đồ du lịch của Ngọc và Đức

App React: bản đồ 34 tỉnh thành Việt Nam của hai người. Các chuyến đi (khai báo trong `src/trips.js`) hiện
thành trái tim ở từng điểm dừng và đường bay nét đứt; tỉnh có điểm dừng tô hồng. Bấm trái tim để xem và tích
các quán ăn, điểm chơi của chặng đó (dùng chung dấu tích với sổ tay `travel/`). Bấm vào một tỉnh để đánh dấu
**đã đi** / **muốn đi** và viết ghi chú. Dữ liệu nằm trong `localStorage` khoá `da-di-qua-v1`,
không có backend; có nút xuất/nhập file JSON để chuyển máy hoặc sao lưu.

Là một workspace của repo (`@trang/ban-do`), chạy từ gốc repo:

```bash
npm install          # một lần, ở gốc repo
npm run dev:map      # http://localhost:5175/ban-do/
npm run build        # build cả site, app này ra dist/ban-do/
```

## Cấu trúc

| File | Việc |
|---|---|
| `src/App.jsx` | Bố cục, đếm số tỉnh, ô tìm kiếm, xuất/nhập file |
| `src/VietnamMap.jsx` | Vẽ SVG từ GeoJSON (d3-geo), hover/chọn tỉnh, phóng to – kéo |
| `src/ProvincePanel.jsx` | Panel bên phải: trạng thái + ô ghi chú |
| `src/TripPanels.jsx` | Thẻ chuyến đi và bảng một điểm dừng (danh sách địa điểm, tích đã ghé) |
| `src/trips.js` | Các chuyến: điểm dừng, tọa độ, đường đi; hook đọc/ghi dấu tích `dadiqua-trip` |
| `src/data/trip-2026-10.json` | 49 địa điểm của chuyến 3–11/10, trích từ `travel/index.html` |
| `src/store.js` | Đọc/ghi `localStorage` |
| `src/data/provinces.json` | Ranh giới 34 tỉnh (GeoJSON, ~71 KB) |
| `src/data/provinces.meta.json` | Tên, miền, thành phố trực thuộc TW, tên các tỉnh cũ |

## Dữ liệu bản đồ

Nguồn: [geoBoundaries](https://www.geoboundaries.org/) ADM1 Việt Nam (bản simplified,
CC BY 4.0) — gồm 63 tỉnh cũ. Quy trình tạo `provinces.json`:

1. Gán mỗi tỉnh cũ vào tỉnh mới theo Nghị quyết sáp nhập có hiệu lực 1/7/2025.
2. `mapshaper -dissolve2 fields=code,name -simplify 35% keep-shapes -clean` để xoá
   ranh giới nội bộ và giảm dung lượng.

Lưu ý khi sửa code: file GeoJSON theo đúng chuẩn RFC 7946 (vòng ngoài ngược chiều kim
đồng hồ), còn `d3-geo` tính trên mặt cầu nên cần chiều ngược lại — `VietnamMap.jsx` đảo
chiều lúc nạp. Bỏ bước đó thì mỗi tỉnh sẽ phủ kín quả địa cầu và bản đồ ra một ô vuông.

Bản đồ chỉ có phần đất liền và đảo ven bờ, không vẽ Hoàng Sa – Trường Sa.
