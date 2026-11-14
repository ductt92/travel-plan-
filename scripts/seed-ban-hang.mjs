// Tạo lại dữ liệu của web bán hàng (/ban-hang/).
//   node scripts/seed-ban-hang.mjs --demo          thêm đơn hàng, khách và nhân viên demo (DB còn trống)
//   node scripts/seed-ban-hang.mjs --reset --yes   XOÁ HẾT bảng shop_* rồi tạo lại (thêm --demo nếu muốn có đơn demo)
// Đọc DATABASE_URL từ biến môi trường, không có thì từ .env.local. Cẩn thận: .env.local có thể đang trỏ vào Neon thật.
import { readFileSync, existsSync } from 'node:fs';

const envFile = new URL('../.env.local', import.meta.url);
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^(['"])(.*)\1$/, '$2');
  }
}
const args = process.argv.slice(2);
const reset = args.includes('--reset');
const demo = args.includes('--demo');
const host = (() => { try { return new URL(process.env.DATABASE_URL).host; } catch { return '(chưa có DATABASE_URL)'; } })();
if (reset && !args.includes('--yes')) {
  console.error(`--reset sẽ xoá toàn bộ dữ liệu bán hàng trên ${host}. Thêm --yes nếu chắc chắn.`);
  process.exit(1);
}
const { pool } = await import('../backend/node/banhang/db.js');
const { seed } = await import('../backend/node/banhang/seed.js');
const p = await pool();
if (!reset && (await p.query('SELECT COUNT(*)::int n FROM shop_staff')).rows[0].n) {
  console.error(`Dữ liệu bán hàng trên ${host} đã có sẵn. Dùng --reset --yes để tạo lại.`);
  process.exit(1);
}
await seed({ demo, reset });
console.log(`Đã tạo dữ liệu bán hàng trên ${host}${demo ? ' (kèm đơn hàng demo)' : ''}.`);
await p.end();
