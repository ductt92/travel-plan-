/** Mấy hình vẽ nhỏ dùng chung, giữ nguyên nét như bản thiết kế. */

const line = {
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 2,
} as const;

export const SearchIcon = () => (
  <svg viewBox="0 0 24 24" width="15" height="15" {...line}>
    <circle cx="11" cy="11" r="7" />
    <path d="m20 20-3.5-3.5" />
  </svg>
);

export const BookIcon = ({ size = 15, width = 2 }: { size?: number; width?: number }) => (
  <svg viewBox="0 0 24 24" width={size} height={size} {...line} strokeWidth={width}>
    <path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H19v16H5.5A1.5 1.5 0 0 1 4 18.5z" />
    <path d="M8 4v16" />
  </svg>
);

export const PinIcon = () => (
  <svg width="40" height="40" viewBox="0 0 24 24" {...line} strokeWidth={1.5}>
    <path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z" />
    <circle cx="12" cy="10" r="2.6" />
  </svg>
);

export const CalendarIcon = () => (
  <svg viewBox="0 0 24 24" width="15" height="15" {...line}>
    <rect x="3" y="5" width="18" height="16" rx="3" />
    <path d="M8 3v4M16 3v4M3 10h18" />
  </svg>
);

export const ChevronIcon = () => (
  <svg viewBox="0 0 24 24" width="12" height="12" {...line} strokeWidth={2.6}>
    <path d="m6 9 6 6 6-6" />
  </svg>
);
