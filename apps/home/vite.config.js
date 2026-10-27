import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Trang chủ nằm ở gốc site: dist/index.html
export default defineConfig({ plugins: [react()], base: '/' });
