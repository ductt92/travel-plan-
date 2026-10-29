import type { Metadata, Viewport } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Đức & Ngọc — Câu chuyện của chúng mình',
  description: 'Bản đồ những nơi chúng mình đã đi qua, mỗi tỉnh một trang nhật ký.',
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  viewportFit: 'cover',
};

/**
 * Chữ lấy thẳng từ Google Fonts như bản thiết kế. (next/font tải font lúc build,
 * máy này ra ngoài mạng không ổn định nên chưa dùng được — đổi sau cũng chỉ là
 * sửa hai biến --f-ui, --f-serif trong globals.css.)
 */
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Lora:ital,wght@0,500;0,600;1,400;1,500&display=swap"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
