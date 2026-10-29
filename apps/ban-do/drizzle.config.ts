import { defineConfig } from 'drizzle-kit';
import { databaseUrl } from './src/lib/env';

// Không có DATABASE_URL thì drizzle-kit tự báo lỗi, để trống cho nó nói
export default defineConfig({
  schema: './src/db/schema.ts',
  out: './drizzle',
  dialect: 'postgresql',
  dbCredentials: { url: databaseUrl() ?? '' },
});
