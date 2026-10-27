import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// App nằm ở /hoc-tieng-trung/ trên site; dùng HashRouter nên không cần cấu hình rewrite.
// /api chuyển sang `npm run dev:api` (Node + Go) khi chạy dev.
export default defineConfig({ plugins: [react()], base: '/hoc-tieng-trung/', server: { proxy: { '/api': 'http://127.0.0.1:3001' } } });
