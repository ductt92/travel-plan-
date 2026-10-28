import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';

/**
 * Lấy DATABASE_URL. Trên Vercel biến có sẵn; chạy ở máy thì app này nằm trong repo
 * nên mượn luôn .env.local ở gốc repo, khỏi phải chép chuỗi kết nối ra hai chỗ.
 * Đặt .env.local ngay trong apps/ban-do-next thì Next nạp trước, và bản đó thắng.
 */
export function databaseUrl(): string | undefined {
  if (process.env.DATABASE_URL) return process.env.DATABASE_URL;

  const file = path.join(process.cwd(), '..', '..', '.env.local');
  if (!existsSync(file)) return undefined;

  for (const line of readFileSync(file, 'utf8').split('\n')) {
    const m = line.match(/^\s*DATABASE_URL\s*=\s*(.*?)\s*$/);
    if (!m) continue;
    const value = m[1].replace(/^(['"])(.*)\1$/, '$2');
    if (value) {
      process.env.DATABASE_URL = value;
      return value;
    }
  }
  return undefined;
}
