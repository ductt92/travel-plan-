import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// App nằm ở /ban-do/ trên site.
// /api chuyển sang `npm run dev:api` (Node + Go) khi chạy dev.
export default defineConfig({ plugins: [react()], base: '/ban-do/', server: { proxy: { '/api': 'http://127.0.0.1:3001' } } });
