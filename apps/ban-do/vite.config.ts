import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// App nằm ở /ban-do/ trên site; /api chuyển sang server API chạy bằng `npm run dev:api`.
export default defineConfig({
  plugins: [react()],
  base: '/ban-do/',
  // '@/…' trong mã nguồn: tsconfig khai cho TypeScript, chỗ này khai cho Vite
  resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } },
  server: { proxy: { '/api': 'http://127.0.0.1:3001' } },
});
