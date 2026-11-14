// API của web bán hàng (trang /ban-hang/), chạy bằng Express bên trong function có sẵn api/node/quan-ly.js
// (gói Hobby chỉ cho 12 function nên không tạo function mới). vercel.json chuyển
//   /api/node/ban-hang/<đường dẫn>  →  /api/node/quan-ly?_api=ban-hang&_path=<đường dẫn>
//
// Biến môi trường: DATABASE_URL (chung cả repo), SHOP_ADMIN_PASSWORD (mật khẩu admin lúc tạo lần đầu, thiếu thì dùng APP_SECRET).
// Chưa có bản Go cho phần này: /api/go/ban-hang không tồn tại.
import express from 'express';
import { readJson } from '../common.js';
import { parseCookies, loadCustomer } from './auth.js';
import { seedIfEmpty } from './seed.js';
import publicRoutes from './public.js';
import adminRoutes from './admin.js';

const app = express();
app.disable('x-powered-by');
app.set('etag', false);

// Chặn POST/PUT/DELETE gửi từ trang web khác (chống CSRF đơn giản, cookie đã là SameSite=Lax)
app.use((req, res, next) => {
  if (['GET', 'HEAD', 'OPTIONS'].includes(req.method)) return next();
  const origin = req.headers.origin;
  try {
    if (origin && new URL(origin).host !== (req.headers['x-forwarded-host'] || req.headers.host)) return res.status(403).json({ error: 'Yêu cầu không hợp lệ' });
  } catch {
    return res.status(403).json({ error: 'Yêu cầu không hợp lệ' });
  }
  next();
});
app.use((_req, res, next) => { res.setHeader('Cache-Control', 'no-store'); res.setHeader('X-Backend', 'node'); next(); });
app.use(parseCookies);

let seeded = null;
app.use(async (_req, _res, next) => {
  seeded ??= seedIfEmpty().catch((e) => { seeded = null; throw e; });
  await seeded;
  next();
});

app.use(loadCustomer);
app.use('/admin', adminRoutes);
app.use('/', publicRoutes);
app.use((_req, res) => res.status(404).json({ error: 'Không tìm thấy' }));

// Lỗi chung: thông báo tiếng Việt kèm lỗi theo từng ô nhập
// eslint-disable-next-line no-unused-vars
app.use((err, _req, res, _next) => {
  const status = err.status || 500;
  if (status >= 500) console.error('[ban-hang]', err);
  res.status(status).json({ error: status >= 500 ? 'Có lỗi xảy ra, vui lòng thử lại' : err.message, fields: err.fields });
});

export default async function banHang(req, res) {
  const u = new URL(req.url, 'http://x');
  const marker = '/ban-hang/';
  const fromPath = u.pathname.includes(marker) ? u.pathname.slice(u.pathname.indexOf(marker) + marker.length) : null;
  const path = fromPath ?? String(u.searchParams.get('_path') || req.query?._path || '');
  u.searchParams.delete('_api');
  u.searchParams.delete('_path');
  req.url = `/${path.replace(/^\/+/, '')}${u.search}`;
  // Vercel gắn sẵn req.body (getter), chạy ở máy thì tự đọc luồng; ghi đè bằng defineProperty cho chắc
  let body = {};
  if (!['GET', 'HEAD'].includes(req.method)) {
    try {
      body = (await readJson(req, 8 << 20)) || {};
    } catch {
      res.statusCode = 400;
      res.setHeader('Content-Type', 'application/json; charset=utf-8');
      return res.end(JSON.stringify({ error: 'Dữ liệu gửi lên không hợp lệ hoặc quá lớn' }));
    }
  }
  Object.defineProperty(req, 'body', { value: body, writable: true, configurable: true, enumerable: true });
  return app(req, res);
}
