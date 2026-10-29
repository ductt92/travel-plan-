import type { Entries } from './types';

/**
 * Dữ liệu mẫu, lấy từ sổ tay chuyến 3–11/10/2026 trong travel/ — hai chặng,
 * nơi ghé theo lịch từng ngày. Tam Đảo thuộc Vĩnh Phúc cũ, từ 1/7/2025 là Phú Thọ.
 *
 * Giai đoạn sau đổi chỗ này thành một lần đọc database là xong, phần còn lại
 * của app chỉ biết tới kiểu Entries chứ không biết dữ liệu từ đâu ra.
 */
export const seed: Entries = {
  'phu-tho': {
    status: 'visited',
    trips: [
      {
        id: 1,
        from: '2026-10-03',
        to: '2026-10-04',
        with: 'Ngọc',
        rate: 0,
        places: [
          'Chợ Tam Đảo', 'Nhà hàng Phố Mây', 'Cafe Lưng Chừng', 'Thác Bạc',
          'Nhà thờ đá Tam Đảo', 'Cổng Trời', 'Quán Gió', 'Đền Bà Chúa Thượng Ngàn',
        ],
        note: 'Ngọc đáp Nội Bài 17:45, đi thẳng Tam Đảo 60 km, tới nơi thì đã tối. Hôm sau gói gọn cả Tam Đảo trong một buổi sáng rồi ra lại Nội Bài, bay chiều vào Đà Lạt.',
      },
    ],
  },
  'lam-dong': {
    status: 'visited',
    trips: [
      {
        id: 2,
        from: '2026-10-04',
        to: '2026-10-11',
        with: 'Ngọc',
        rate: 0,
        places: [
          'Bánh mì Liên Hoa', 'Dốc Thị', 'Bún bò Ấp Ánh Sáng', 'Hồ Xuân Hương', 'Đồ nướng chợ đêm',
          'Thiền viện Trúc Lâm', 'Hồ Tuyền Lâm', 'Nem nướng Bà Hùng', 'Cà phê Tùng', 'Lẩu gà lá é Tao Ngộ',
          'Đỉnh Langbiang', 'Hồ Đankia – Suối Vàng', 'Làng Cù Lần', 'Mê Linh Coffee Garden', 'Lẩu bò Ba Toa',
          'An Cafe', 'Chùa Linh Phước', 'Đồi chè Cầu Đất', 'Cầu Đất Farm', "Thị trấn D'ran",
          'Fujiya Sushi', 'Chợ Đà Lạt', 'Là Việt Coffee', 'Nhà thờ Con Gà', 'Lẩu bò Nhà Gỗ',
          'Bánh mì xíu mại Cô Hồng',
        ],
        note: "Bảy ngày ở Đà Lạt. Ngày đầu ngủ bù, chiều ra Dốc Thị. Hôm 9/10 dậy 4:30 đi Cầu Đất – D'ran, tối mới về lại phố. Ngày cuối ngủ nướng rồi đi mua quà, chiều bay DLI → HAN.",
      },
    ],
  },
};
