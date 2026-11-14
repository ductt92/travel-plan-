// API cho trang quản trị: /api/node/ban-hang/admin/...
import express from 'express';
import { D, getSettings, setSettings, vnDay, ymd, TZ } from './db.js';
import { int, paginate, productOut, uniqueSlug, hashPassword, verifyPassword, isEmail, HttpError, parseJSON } from './util.js';
import { createSession, destroySession, requireAdmin, onlyAdmin } from './auth.js';
import { changeStatus, orderDetail, STATUSES } from './orders.js';

const r = express.Router();
const NOT_CANCELLED = "status != 'cancelled'";
const offOn = (v) => (v === false || v === 0 || v === '0' ? 0 : 1);

// Dựng câu UPDATE từ các cột cho phép (tên cột lấy từ code, không lấy từ người dùng)
async function updateRow(table, id, data, extra = '') {
  const cols = Object.keys(data);
  if (!cols.length) return;
  await D.q(`UPDATE ${table} SET ${cols.map((k) => `${k} = ?`).join(', ')}${extra} WHERE id = ?`, [...cols.map((k) => data[k]), id]);
}
async function insertRow(table, data) {
  const cols = Object.keys(data);
  return (await D.one(`INSERT INTO ${table}(${cols.join(',')}) VALUES(${cols.map(() => '?').join(',')}) RETURNING id`, cols.map((k) => data[k]))).id;
}

// ---------- Đăng nhập quản trị ----------
// Chặn dò mật khẩu: sai 5 lần thì khoá 5 phút (theo IP, trong bộ nhớ của function đang chạy)
const attempts = new Map();
const ipOf = (req) => String(req.headers['x-forwarded-for'] || req.socket?.remoteAddress || '').split(',')[0].trim();

r.post('/login', async (req, res) => {
  const key = ipOf(req);
  const a = attempts.get(key) || { n: 0, until: 0 };
  if (a.until > Date.now()) throw new HttpError(429, 'Đăng nhập sai quá nhiều lần, thử lại sau 5 phút');
  const email = String(req.body.email || '').trim().toLowerCase();
  const u = await D.one('SELECT * FROM shop_staff WHERE email = ?', [email]);
  if (!u || !verifyPassword(req.body.password, u.password_hash)) {
    a.n += 1;
    if (a.n >= 5) { a.until = Date.now() + 5 * 60 * 1000; a.n = 0; }
    attempts.set(key, a);
    throw new HttpError(400, 'Email hoặc mật khẩu không đúng');
  }
  if (!u.active) throw new HttpError(403, 'Tài khoản đã bị khoá');
  attempts.delete(key);
  await D.q('UPDATE shop_staff SET last_login = now() WHERE id = ?', [u.id]);
  await createSession(req, res, 'admin', u.id);
  res.json({ ok: true });
});

r.post('/logout', async (req, res) => { await destroySession(req, res, 'admin'); res.json({ ok: true }); });

r.use(requireAdmin);

r.get('/me', (req, res) => res.json(req.staff));

r.put('/me/password', async (req, res) => {
  const u = await D.one('SELECT password_hash FROM shop_staff WHERE id = ?', [req.staff.id]);
  if (!verifyPassword(req.body.current, u.password_hash)) throw new HttpError(400, 'Mật khẩu hiện tại không đúng', { current: 'Mật khẩu hiện tại không đúng' });
  if (String(req.body.password || '').length < 6) throw new HttpError(400, 'Mật khẩu mới tối thiểu 6 ký tự', { password: 'Tối thiểu 6 ký tự' });
  await D.q('UPDATE shop_staff SET password_hash = ? WHERE id = ?', [hashPassword(req.body.password), req.staff.id]);
  res.json({ ok: true });
});

// ---------- Tải ảnh: trình duyệt thu nhỏ ảnh rồi gửi base64, lưu vào bảng shop_images ----------
const MIMES = new Set(['image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/avif']);
r.post('/upload', async (req, res) => {
  const files = Array.isArray(req.body.files) ? req.body.files : [];
  if (!files.length) throw new HttpError(400, 'Chưa có ảnh');
  const urls = [];
  for (const f of files.slice(0, 5)) {
    const type = String(f.type || '');
    if (!MIMES.has(type)) throw new HttpError(400, 'Chỉ nhận file ảnh jpg, png, webp, gif');
    const data = Buffer.from(String(f.data || ''), 'base64');
    if (!data.length) throw new HttpError(400, 'Ảnh hỏng hoặc trống');
    if (data.length > 3 * 1024 * 1024) throw new HttpError(400, 'Ảnh tối đa 3MB');
    const { id } = await D.one('INSERT INTO shop_images(mime, data) VALUES(?, ?) RETURNING id', [type, data]);
    urls.push(`/api/node/ban-hang/img/${id}`);
  }
  res.json({ urls });
});

// ---------- Tổng quan ----------
r.get('/dashboard', async (_req, res) => {
  const s = await getSettings();
  const low = int(s.low_stock_threshold, 5);
  const today = ymd();
  const ms = `${today.slice(0, 8)}01`;
  const [y, m] = [int(today.slice(0, 4)), int(today.slice(5, 7))];
  const ps = m === 1 ? `${y - 1}-12-01` : `${y}-${String(m - 1).padStart(2, '0')}-01`;
  const days = [];
  for (let i = 13; i >= 0; i--) days.push(ymd(new Date(Date.now() - i * 86400000)));
  const day = vnDay('created_at');
  const v = async (sql, args = []) => (await D.one(sql, args)).v;

  const byDay = Object.fromEntries((await D.all(`SELECT to_char(${day}, 'YYYY-MM-DD') AS d, SUM(total)::float8 AS revenue, COUNT(*)::int AS orders
      FROM shop_orders WHERE ${NOT_CANCELLED} AND ${day} >= ?::date GROUP BY 1`, [days[0]])).map((x) => [x.d, x]));

  res.json({
    revenue_month: await v(`SELECT COALESCE(SUM(total),0)::float8 v FROM shop_orders WHERE ${NOT_CANCELLED} AND ${day} >= ?::date`, [ms]),
    revenue_prev_month: await v(`SELECT COALESCE(SUM(total),0)::float8 v FROM shop_orders WHERE ${NOT_CANCELLED} AND ${day} >= ?::date AND ${day} < ?::date`, [ps, ms]),
    orders_month: await v(`SELECT COUNT(*)::int v FROM shop_orders WHERE ${day} >= ?::date`, [ms]),
    orders_today: await v(`SELECT COUNT(*)::int v FROM shop_orders WHERE ${day} = ?::date`, [today]),
    pending: await v("SELECT COUNT(*)::int v FROM shop_orders WHERE status = 'pending'"),
    customers: await v('SELECT COUNT(*)::int v FROM shop_customers'),
    customers_month: await v(`SELECT COUNT(*)::int v FROM shop_customers WHERE ${day} >= ?::date`, [ms]),
    products: await v('SELECT COUNT(*)::int v FROM shop_products WHERE active = 1'),
    reviews_pending: await v('SELECT COUNT(*)::int v FROM shop_reviews WHERE approved = 0'),
    status_counts: await D.all('SELECT status, COUNT(*)::int n FROM shop_orders GROUP BY status'),
    chart: days.map((d) => ({ date: d, revenue: byDay[d] ? byDay[d].revenue : 0, orders: byDay[d] ? byDay[d].orders : 0 })),
    top_products: await D.all(`SELECT oi.name, SUM(oi.qty)::int qty, SUM(oi.qty * oi.price)::float8 revenue FROM shop_order_items oi
        JOIN shop_orders o ON o.id = oi.order_id WHERE o.status != 'cancelled' AND ${vnDay('o.created_at')} >= ?::date
        GROUP BY oi.name ORDER BY qty DESC LIMIT 5`, [days[0]]),
    low_stock: (await D.all('SELECT id, name, stock, images FROM shop_products WHERE active = 1 AND stock <= ? ORDER BY stock ASC LIMIT 8', [low]))
      .map((p) => ({ id: p.id, name: p.name, stock: p.stock, image: parseJSON(p.images, [])[0] || '' })),
    recent_orders: await D.all('SELECT id, code, name, total, status, created_at FROM shop_orders ORDER BY id DESC LIMIT 8'),
    low_stock_threshold: low,
  });
});

// ---------- Sản phẩm ----------
function productInput(b) {
  const fields = {};
  const name = String(b.name || '').trim();
  const price = int(b.price, -1);
  const sale = b.sale_price === '' || b.sale_price == null ? null : int(b.sale_price, 0);
  if (!name) fields.name = 'Nhập tên sản phẩm';
  if (price < 0) fields.price = 'Nhập giá bán';
  if (sale != null && sale > 0 && sale >= price) fields.sale_price = 'Giá khuyến mãi phải thấp hơn giá bán';
  if (int(b.stock, 0) < 0) fields.stock = 'Tồn kho không được âm';
  if (Object.keys(fields).length) throw new HttpError(400, 'Thông tin sản phẩm chưa đúng', fields);
  const arr = (v) => (Array.isArray(v) ? v : String(v || '').split(',')).map((x) => String(x).trim()).filter(Boolean);
  return {
    name, price, sale_price: sale && sale > 0 ? sale : null,
    sku: String(b.sku || '').trim(),
    category_id: int(b.category_id) || null,
    short_desc: String(b.short_desc || ''),
    description: String(b.description || ''),
    images: JSON.stringify(arr(b.images)),
    sizes: JSON.stringify(arr(b.sizes)),
    colors: JSON.stringify(arr(b.colors)),
    stock: int(b.stock, 0),
    featured: b.featured ? 1 : 0,
    active: offOn(b.active),
  };
}

r.get('/products', async (req, res) => {
  const { limit, page, offset } = paginate(req, 20);
  const where = ['1=1'];
  const args = [];
  if (req.query.q) { where.push('(p.name ILIKE ? OR p.sku ILIKE ?)'); args.push(`%${req.query.q}%`, `%${req.query.q}%`); }
  if (req.query.category) { where.push('p.category_id = ?'); args.push(int(req.query.category)); }
  if (req.query.status === 'active') where.push('p.active = 1');
  if (req.query.status === 'hidden') where.push('p.active = 0');
  if (req.query.status === 'low') { where.push('p.stock <= ?'); args.push(int((await getSettings()).low_stock_threshold, 5)); }
  if (req.query.status === 'sale') where.push('p.sale_price > 0');
  const base = `FROM shop_products p LEFT JOIN shop_categories c ON c.id = p.category_id WHERE ${where.join(' AND ')}`;
  const { n: total } = await D.one(`SELECT COUNT(*)::int n ${base}`, args);
  const items = (await D.all(`SELECT p.*, c.name category_name ${base} ORDER BY p.id DESC LIMIT ? OFFSET ?`, [...args, limit, offset])).map(productOut);
  res.json({ items, total, page, pages: Math.ceil(total / limit) });
});

r.get('/products/:id', async (req, res) => {
  const p = await D.one('SELECT * FROM shop_products WHERE id = ?', [int(req.params.id)]);
  if (!p) throw new HttpError(404, 'Không tìm thấy sản phẩm');
  res.json(productOut(p));
});

r.post('/products', async (req, res) => {
  const d = productInput(req.body);
  d.slug = await uniqueSlug(D, 'shop_products', req.body.slug || d.name);
  res.json({ id: await insertRow('shop_products', d) });
});

r.put('/products/:id', async (req, res) => {
  const id = int(req.params.id);
  if (!(await D.one('SELECT id FROM shop_products WHERE id = ?', [id]))) throw new HttpError(404, 'Không tìm thấy sản phẩm');
  const d = productInput(req.body);
  d.slug = await uniqueSlug(D, 'shop_products', req.body.slug || d.name, id);
  await updateRow('shop_products', id, d, ', updated_at = now()');
  res.json({ ok: true });
});

// Sửa nhanh 1 trường (ẩn/hiện, nổi bật, tồn kho) ngay trên bảng
r.patch('/products/:id', async (req, res) => {
  const allowed = { active: (v) => (v ? 1 : 0), featured: (v) => (v ? 1 : 0), stock: (v) => Math.max(0, int(v)) };
  const d = {};
  for (const [k, fn] of Object.entries(allowed)) if (k in req.body) d[k] = fn(req.body[k]);
  if (!Object.keys(d).length) throw new HttpError(400, 'Không có gì để cập nhật');
  await updateRow('shop_products', int(req.params.id), d, ', updated_at = now()');
  res.json({ ok: true });
});

r.delete('/products/:id', async (req, res) => {
  await D.q('DELETE FROM shop_products WHERE id = ?', [int(req.params.id)]);
  res.json({ ok: true });
});

// ---------- Danh mục ----------
r.get('/categories', async (_req, res) => {
  res.json(await D.all('SELECT c.*, (SELECT COUNT(*)::int FROM shop_products p WHERE p.category_id = c.id) AS count FROM shop_categories c ORDER BY sort, id'));
});
function categoryInput(b) {
  const name = String(b.name || '').trim();
  if (!name) throw new HttpError(400, 'Nhập tên danh mục', { name: 'Nhập tên danh mục' });
  return { name, description: String(b.description || ''), image: String(b.image || ''), sort: int(b.sort, 0), active: offOn(b.active) };
}
r.post('/categories', async (req, res) => {
  const d = categoryInput(req.body);
  d.slug = await uniqueSlug(D, 'shop_categories', req.body.slug || d.name);
  res.json({ id: await insertRow('shop_categories', d) });
});
r.put('/categories/:id', async (req, res) => {
  const id = int(req.params.id);
  const d = categoryInput(req.body);
  d.slug = await uniqueSlug(D, 'shop_categories', req.body.slug || d.name, id);
  await updateRow('shop_categories', id, d);
  res.json({ ok: true });
});
r.delete('/categories/:id', async (req, res) => {
  await D.q('DELETE FROM shop_categories WHERE id = ?', [int(req.params.id)]);
  res.json({ ok: true });
});

// ---------- Đơn hàng ----------
function orderFilter(req) {
  const where = ['1=1'];
  const args = [];
  const day = vnDay('created_at');
  if (req.query.status) { where.push('status = ?'); args.push(String(req.query.status)); }
  if (req.query.payment) { where.push('payment_status = ?'); args.push(String(req.query.payment)); }
  if (req.query.q) { where.push('(code ILIKE ? OR name ILIKE ? OR phone ILIKE ? OR email ILIKE ?)'); const q = `%${req.query.q}%`; args.push(q, q, q, q); }
  if (/^\d{4}-\d{2}-\d{2}$/.test(req.query.from || '')) { where.push(`${day} >= ?::date`); args.push(req.query.from); }
  if (/^\d{4}-\d{2}-\d{2}$/.test(req.query.to || '')) { where.push(`${day} <= ?::date`); args.push(req.query.to); }
  return { where: where.join(' AND '), args };
}

r.get('/orders', async (req, res) => {
  const { limit, page, offset } = paginate(req, 20);
  const { where, args } = orderFilter(req);
  const { n: total } = await D.one(`SELECT COUNT(*)::int n FROM shop_orders WHERE ${where}`, args);
  const items = await D.all(`SELECT o.*, (SELECT SUM(qty)::int FROM shop_order_items WHERE order_id = o.id) AS item_count
      FROM shop_orders o WHERE ${where} ORDER BY id DESC LIMIT ? OFFSET ?`, [...args, limit, offset]);
  const counts = Object.fromEntries((await D.all('SELECT status, COUNT(*)::int n FROM shop_orders GROUP BY status')).map((x) => [x.status, x.n]));
  res.json({ items, total, page, pages: Math.ceil(total / limit), counts });
});

r.get('/orders/export.csv', async (req, res) => {
  const { where, args } = orderFilter(req);
  const rows = await D.all(`SELECT * FROM shop_orders WHERE ${where} ORDER BY id DESC`, args);
  const esc = (v) => `"${String(v == null ? '' : v).replace(/"/g, '""')}"`;
  const when = (d) => new Date(d).toLocaleString('vi-VN', { timeZone: TZ });
  const head = ['Mã đơn', 'Ngày đặt', 'Khách hàng', 'Điện thoại', 'Email', 'Địa chỉ', 'Thanh toán', 'Trạng thái TT', 'Trạng thái', 'Tạm tính', 'Giảm giá', 'Phí ship', 'Tổng cộng', 'Mã giảm giá', 'Ghi chú'];
  const lines = rows.map((o) => [o.code, when(o.created_at), o.name, o.phone, o.email, o.address, o.payment_method === 'bank' ? 'Chuyển khoản' : 'COD',
    o.payment_status === 'paid' ? 'Đã thanh toán' : 'Chưa thanh toán', STATUSES[o.status], o.subtotal, o.discount, o.shipping, o.total, o.coupon_code, o.note].map(esc).join(','));
  res.setHeader('Content-Type', 'text/csv; charset=utf-8');
  res.setHeader('Content-Disposition', `attachment; filename="don-hang-${ymd()}.csv"`);
  res.send('﻿' + [head.map(esc).join(','), ...lines].join('\r\n'));
});

r.get('/orders/:id', async (req, res) => {
  const o = await orderDetail('id = ?', [int(req.params.id)]);
  if (!o) throw new HttpError(404, 'Không tìm thấy đơn hàng');
  if (o.customer_id) o.customer = await D.one('SELECT id, name, email, phone FROM shop_customers WHERE id = ?', [o.customer_id]);
  res.json(o);
});

r.put('/orders/:id', async (req, res) => {
  const id = int(req.params.id);
  const o = await D.one('SELECT * FROM shop_orders WHERE id = ?', [id]);
  if (!o) throw new HttpError(404, 'Không tìm thấy đơn hàng');
  if (req.body.status && req.body.status !== o.status) await changeStatus(id, req.body.status, req.staff.name, req.body.status_note);
  const d = {};
  for (const k of ['name', 'phone', 'email', 'address', 'admin_note']) if (k in req.body) d[k] = String(req.body[k] || '');
  if ('payment_status' in req.body) d.payment_status = req.body.payment_status === 'paid' ? 'paid' : 'unpaid';
  await updateRow('shop_orders', id, d, ', updated_at = now()');
  res.json({ ok: true });
});

r.delete('/orders/:id', onlyAdmin, async (req, res) => {
  const id = int(req.params.id);
  const o = await D.one('SELECT status FROM shop_orders WHERE id = ?', [id]);
  if (o && o.status !== 'cancelled' && o.status !== 'completed') await changeStatus(id, 'cancelled', req.staff.name, 'Xoá đơn');
  await D.q('DELETE FROM shop_orders WHERE id = ?', [id]);
  res.json({ ok: true });
});

// ---------- Khách hàng ----------
r.get('/customers', async (req, res) => {
  const { limit, page, offset } = paginate(req, 20);
  const where = ['1=1'];
  const args = [];
  if (req.query.q) { where.push('(c.name ILIKE ? OR c.email ILIKE ? OR c.phone ILIKE ?)'); const q = `%${req.query.q}%`; args.push(q, q, q); }
  if (req.query.status === 'locked') where.push('c.locked = 1');
  const w = where.join(' AND ');
  const { n: total } = await D.one(`SELECT COUNT(*)::int n FROM shop_customers c WHERE ${w}`, args);
  const items = await D.all(`SELECT c.id, c.name, c.email, c.phone, c.address, c.locked, c.created_at,
      (SELECT COUNT(*)::int FROM shop_orders o WHERE o.customer_id = c.id) AS orders,
      (SELECT COALESCE(SUM(total),0)::float8 FROM shop_orders o WHERE o.customer_id = c.id AND o.status != 'cancelled') AS spent
      FROM shop_customers c WHERE ${w} ORDER BY c.id DESC LIMIT ? OFFSET ?`, [...args, limit, offset]);
  res.json({ items, total, page, pages: Math.ceil(total / limit) });
});
r.get('/customers/:id', async (req, res) => {
  const c = await D.one('SELECT id, name, email, phone, address, locked, created_at FROM shop_customers WHERE id = ?', [int(req.params.id)]);
  if (!c) throw new HttpError(404, 'Không tìm thấy khách hàng');
  c.orders = await D.all('SELECT id, code, total, status, created_at FROM shop_orders WHERE customer_id = ? ORDER BY id DESC', [c.id]);
  res.json(c);
});
r.put('/customers/:id', async (req, res) => {
  const id = int(req.params.id);
  const b = req.body;
  if ('locked' in b) {
    await D.q('UPDATE shop_customers SET locked = ? WHERE id = ?', [b.locked ? 1 : 0, id]);
    if (b.locked) await D.q("DELETE FROM shop_sessions WHERE kind = 'customer' AND user_id = ?", [id]);
  }
  if ('name' in b) {
    if (!String(b.name).trim()) throw new HttpError(400, 'Nhập họ tên', { name: 'Nhập họ tên' });
    await D.q('UPDATE shop_customers SET name = ?, phone = ?, address = ? WHERE id = ?', [String(b.name).trim(), String(b.phone || ''), String(b.address || ''), id]);
  }
  if (b.new_password) {
    if (String(b.new_password).length < 6) throw new HttpError(400, 'Mật khẩu tối thiểu 6 ký tự', { new_password: 'Tối thiểu 6 ký tự' });
    await D.q('UPDATE shop_customers SET password_hash = ? WHERE id = ?', [hashPassword(b.new_password), id]);
  }
  res.json({ ok: true });
});
r.delete('/customers/:id', onlyAdmin, async (req, res) => {
  await D.q('DELETE FROM shop_customers WHERE id = ?', [int(req.params.id)]);
  res.json({ ok: true });
});

// ---------- Mã giảm giá ----------
r.get('/coupons', async (_req, res) => res.json(await D.all('SELECT * FROM shop_coupons ORDER BY id DESC')));
function couponInput(b) {
  const fields = {};
  const code = String(b.code || '').trim().toUpperCase().replace(/\s+/g, '');
  const value = int(b.value, 0);
  const date = (v) => (/^\d{4}-\d{2}-\d{2}$/.test(v || '') ? v : '');
  if (!/^[A-Z0-9_-]{3,30}$/.test(code)) fields.code = 'Mã 3–30 ký tự, chỉ chữ, số, - và _';
  if (value <= 0) fields.value = 'Nhập mức giảm';
  if (b.type === 'percent' && value > 100) fields.value = 'Tối đa 100%';
  if (date(b.starts_at) && date(b.expires_at) && b.starts_at > b.expires_at) fields.expires_at = 'Ngày hết hạn phải sau ngày bắt đầu';
  if (Object.keys(fields).length) throw new HttpError(400, 'Mã giảm giá chưa đúng', fields);
  return {
    code, description: String(b.description || ''), type: b.type === 'fixed' ? 'fixed' : 'percent', value,
    max_discount: int(b.max_discount, 0), min_order: int(b.min_order, 0), max_uses: int(b.max_uses, 0),
    starts_at: date(b.starts_at), expires_at: date(b.expires_at), active: offOn(b.active),
  };
}
r.post('/coupons', async (req, res) => {
  const d = couponInput(req.body);
  if (await D.one('SELECT id FROM shop_coupons WHERE code = ?', [d.code])) throw new HttpError(400, 'Mã này đã tồn tại', { code: 'Mã này đã tồn tại' });
  res.json({ id: await insertRow('shop_coupons', d) });
});
r.put('/coupons/:id', async (req, res) => {
  const id = int(req.params.id);
  const d = couponInput(req.body);
  if (await D.one('SELECT id FROM shop_coupons WHERE code = ? AND id != ?', [d.code, id])) throw new HttpError(400, 'Mã này đã tồn tại', { code: 'Mã này đã tồn tại' });
  await updateRow('shop_coupons', id, d);
  res.json({ ok: true });
});
r.delete('/coupons/:id', async (req, res) => { await D.q('DELETE FROM shop_coupons WHERE id = ?', [int(req.params.id)]); res.json({ ok: true }); });

// ---------- Đánh giá ----------
r.get('/reviews', async (req, res) => {
  const where = req.query.status === 'pending' ? 'WHERE rv.approved = 0' : req.query.status === 'approved' ? 'WHERE rv.approved = 1' : '';
  res.json(await D.all(`SELECT rv.*, p.name product_name, p.slug product_slug FROM shop_reviews rv LEFT JOIN shop_products p ON p.id = rv.product_id ${where} ORDER BY rv.id DESC LIMIT 200`));
});
r.put('/reviews/:id', async (req, res) => { await D.q('UPDATE shop_reviews SET approved = ? WHERE id = ?', [req.body.approved ? 1 : 0, int(req.params.id)]); res.json({ ok: true }); });
r.delete('/reviews/:id', async (req, res) => { await D.q('DELETE FROM shop_reviews WHERE id = ?', [int(req.params.id)]); res.json({ ok: true }); });

// ---------- Banner (chỉ quản trị viên) ----------
r.get('/banners', onlyAdmin, async (_req, res) => res.json(await D.all('SELECT * FROM shop_banners ORDER BY sort, id')));
function bannerInput(b) {
  if (!b.image) throw new HttpError(400, 'Chọn ảnh banner', { image: 'Chọn ảnh banner' });
  return { title: String(b.title || ''), subtitle: String(b.subtitle || ''), image: String(b.image), button_text: String(b.button_text || ''), link: String(b.link || ''), sort: int(b.sort, 0), active: offOn(b.active) };
}
r.post('/banners', onlyAdmin, async (req, res) => res.json({ id: await insertRow('shop_banners', bannerInput(req.body)) }));
r.put('/banners/:id', onlyAdmin, async (req, res) => { await updateRow('shop_banners', int(req.params.id), bannerInput(req.body)); res.json({ ok: true }); });
r.delete('/banners/:id', onlyAdmin, async (req, res) => { await D.q('DELETE FROM shop_banners WHERE id = ?', [int(req.params.id)]); res.json({ ok: true }); });

// ---------- Trang nội dung ----------
r.get('/pages', onlyAdmin, async (_req, res) => res.json(await D.all('SELECT * FROM shop_pages ORDER BY id')));
r.get('/pages/:id', onlyAdmin, async (req, res) => {
  const p = await D.one('SELECT * FROM shop_pages WHERE id = ?', [int(req.params.id)]);
  if (!p) throw new HttpError(404, 'Không tìm thấy trang');
  res.json(p);
});
function pageInput(b) {
  const title = String(b.title || '').trim();
  if (!title) throw new HttpError(400, 'Nhập tiêu đề trang', { title: 'Nhập tiêu đề trang' });
  return { title, content: String(b.content || ''), show_in_footer: b.show_in_footer ? 1 : 0, active: offOn(b.active) };
}
r.post('/pages', onlyAdmin, async (req, res) => {
  const d = pageInput(req.body);
  d.slug = await uniqueSlug(D, 'shop_pages', req.body.slug || d.title);
  res.json({ id: await insertRow('shop_pages', d) });
});
r.put('/pages/:id', onlyAdmin, async (req, res) => {
  const id = int(req.params.id);
  const d = pageInput(req.body);
  d.slug = await uniqueSlug(D, 'shop_pages', req.body.slug || d.title, id);
  await updateRow('shop_pages', id, d, ', updated_at = now()');
  res.json({ ok: true });
});
r.delete('/pages/:id', onlyAdmin, async (req, res) => { await D.q('DELETE FROM shop_pages WHERE id = ?', [int(req.params.id)]); res.json({ ok: true }); });

// ---------- Cài đặt và giao diện ----------
r.get('/settings', onlyAdmin, async (_req, res) => res.json(await getSettings()));
r.put('/settings', onlyAdmin, async (req, res) => {
  const b = { ...req.body };
  if ('menu' in b && typeof b.menu !== 'string') b.menu = JSON.stringify(b.menu || []);
  if ('primary_color' in b && !/^#[0-9a-fA-F]{6}$/.test(b.primary_color)) throw new HttpError(400, 'Màu chưa đúng định dạng #RRGGBB', { primary_color: 'Dạng #RRGGBB' });
  await setSettings(b);
  res.json({ ok: true });
});

// ---------- Nhân viên (chỉ quản trị viên) ----------
r.get('/staff', onlyAdmin, async (_req, res) => res.json(await D.all('SELECT id, name, email, role, active, last_login, created_at FROM shop_staff ORDER BY id')));
r.post('/staff', onlyAdmin, async (req, res) => {
  const b = req.body;
  const fields = {};
  const email = String(b.email || '').trim().toLowerCase();
  if (!String(b.name || '').trim()) fields.name = 'Nhập họ tên';
  if (!isEmail(email)) fields.email = 'Email chưa đúng';
  else if (await D.one('SELECT id FROM shop_staff WHERE email = ?', [email])) fields.email = 'Email đã được dùng';
  if (String(b.password || '').length < 6) fields.password = 'Mật khẩu tối thiểu 6 ký tự';
  if (Object.keys(fields).length) throw new HttpError(400, 'Thông tin nhân viên chưa đúng', fields);
  const id = await insertRow('shop_staff', { name: String(b.name).trim(), email, password_hash: hashPassword(b.password), role: b.role === 'admin' ? 'admin' : 'staff', active: b.active === false ? 0 : 1 });
  res.json({ id });
});
r.put('/staff/:id', onlyAdmin, async (req, res) => {
  const id = int(req.params.id);
  const b = req.body;
  if (id === req.staff.id && (b.role !== 'admin' || b.active === false)) throw new HttpError(400, 'Bạn không thể tự hạ quyền hoặc khoá chính mình');
  const email = String(b.email || '').trim().toLowerCase();
  if (!isEmail(email)) throw new HttpError(400, 'Email chưa đúng', { email: 'Email chưa đúng' });
  if (await D.one('SELECT id FROM shop_staff WHERE email = ? AND id != ?', [email, id])) throw new HttpError(400, 'Email đã được dùng', { email: 'Email đã được dùng' });
  if (b.password && String(b.password).length < 6) throw new HttpError(400, 'Mật khẩu tối thiểu 6 ký tự', { password: 'Tối thiểu 6 ký tự' });
  await updateRow('shop_staff', id, { name: String(b.name || '').trim(), email, role: b.role === 'admin' ? 'admin' : 'staff', active: b.active === false ? 0 : 1 });
  if (b.password) await D.q('UPDATE shop_staff SET password_hash = ? WHERE id = ?', [hashPassword(b.password), id]);
  if (b.active === false) await D.q("DELETE FROM shop_sessions WHERE kind = 'admin' AND user_id = ?", [id]);
  res.json({ ok: true });
});
r.delete('/staff/:id', onlyAdmin, async (req, res) => {
  const id = int(req.params.id);
  if (id === req.staff.id) throw new HttpError(400, 'Bạn không thể xoá chính mình');
  await D.q('DELETE FROM shop_staff WHERE id = ?', [id]);
  await D.q("DELETE FROM shop_sessions WHERE kind = 'admin' AND user_id = ?", [id]);
  res.json({ ok: true });
});

export default r;
