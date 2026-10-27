import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// App nằm ở /ban-do/ trên site.
export default defineConfig({ plugins: [react()], base: '/ban-do/' });
