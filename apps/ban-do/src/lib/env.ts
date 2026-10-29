import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';

/**
 * Trên Vercel các biến đã nằm sẵn trong môi trường. Chạy ở máy thì app này nằm
 * trong repo nên mượn luôn .env.local ở gốc repo — giống scripts/dev-api.mjs —
 * khỏi phải chép chuỗi kết nối và mật khẩu ra thêm một chỗ nữa.
 *
 * Biến đã có sẵn thì giữ nguyên, nên đặt .env.local ngay trong thư mục này
 * (Next nạp trước) là đè được.
 */
let loaded = false;

function loadRootEnv() {
  if (loaded) return;
  loaded = true;

  const file = path.join(process.cwd(), '..', '..', '.env.local');
  if (!existsSync(file)) return;

  for (const line of readFileSync(file, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (!m || m[1] in process.env) continue;
    process.env[m[1]] = m[2].replace(/^(['"])(.*)\1$/, '$2');
  }
}

function envOf(name: string) {
  loadRootEnv();
  return process.env[name] || undefined;
}

export const databaseUrl = () => envOf('DATABASE_URL');
/** Mã chung của hai đứa; cũng là khóa ký cookie phiên. */
export const appSecret = () => envOf('APP_SECRET');
/** Mật khẩu riêng của Ngọc, dùng chung với trang hsk6 và lớp học trực tiếp. */
export const hsk6Pass = () => envOf('HSK6_PASS');
