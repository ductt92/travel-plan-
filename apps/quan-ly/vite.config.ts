import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Trang quản lý học liệu ở /quan-ly/; /api chuyển sang server API chạy bằng `npm run dev:api`.
export default defineConfig({
  plugins: [react()],
  base: '/quan-ly/',
  resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } },
  server: { port: 5176, proxy: { '/api': 'http://127.0.0.1:3001' } },
});
