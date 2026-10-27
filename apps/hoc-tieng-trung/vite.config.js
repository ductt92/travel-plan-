import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// App nằm ở /hoc-tieng-trung/ trên site; dùng HashRouter nên không cần cấu hình rewrite.
export default defineConfig({ plugins: [react()], base: '/hoc-tieng-trung/' });
