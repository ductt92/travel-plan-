// API cho trang cửa hàng (khách): /api/node/ban-hang/...
import express from 'express';
import { D, getSettings } from './db.js';
import { int, paginate, productOut, hashPassword, verifyPassword, isEmail, isPhone, HttpError } from './util.js';
import { createSession, destroySession, requireCustomer } from './auth.js';
import { quote, createOrder, orderDetail, changeStatus, STATUSES } from './orders.js';

const r = express.Router();
const PRICE = 'CASE WHEN p.sale_price > 0 AND p.sale_price < p.price THEN p.sale_price ELSE p.price END';

// Toàn bộ nội dung chung của trang: cài đặt, menu, danh mục, banner, trang tĩnh
r.get('/site', async (_req, res) => {
  const s = await getSettings();
  let menu = [];
  try { menu = JSON.parse(s.menu || '[]'); } catch { menu = []; }
  delete s.menu;
  res.json({
    settings: s,
    menu,
    categories: await D.all(`SELECT c.id, c.name, c.slug, c.image, c.description,
        (SELECT COUNT(*)::int FROM shop_products p WHERE p.category_id = c.id AND p.active = 1) AS count
        FROM shop_categories c WHERE c.active = 1 ORDER BY c.sort, c.id`),
    banners: await D.all('SELECT * FROM shop_banners WHERE active = 1 ORDER BY sort, id'),
    pages: await D.all('SELECT title, slug, show_in_footer FROM shop_pages WHERE active = 1 ORDER BY id'),
    statuses: STATUSES,
  });
});

r.get('/products', async (req, res) => {
  const { limit, page, offset } = paginate(req, 12);
  const where = ['p.active = 1'];
  const args = [];
  const q = req.query;
  if (q.q) { where.push('(p.name ILIKE ? OR p.short_desc ILIKE ? OR p.sku ILIKE ?)'); const s = `%${q.q}%`; args.push(s, s, s); }
  if (q.category) { where.push('c.slug = ?'); args.push(String(q.category)); }
  if (q.featured) where.push('p.featured = 1');
  if (q.sale) where.push('p.sale_price > 0 AND p.sale_price < p.price');
  if (q.ids) {
    const ids = String(q.ids).split(',').map((x) => int(x)).filter(Boolean).slice(0, 100);
    if (!ids.length) return res.json({ items: [], total: 0, page, pages: 0 });
    where.push('p.id = ANY(?::int[])'); args.push(ids);
  }
  if (q.min) { where.push(`${PRICE} >= ?`); args.push(int(q.min)); }
  if (q.max) { where.push(`${PRICE} <= ?`); args.push(int(q.max)); }
  if (q.size) { where.push('p.sizes LIKE ?'); args.push(`%"${String(q.size).replace(/[%_"]/g, '')}"%`); }
  const sorts = { newest: 'p.id DESC', price_asc: `${PRICE} ASC`, price_desc: `${PRICE} DESC`, best: 'p.sold DESC, p.id DESC', name: 'p.name ASC' };
  const order = sorts[q.sort] || 'p.featured DESC, p.id DESC';
  const base = `FROM shop_products p LEFT JOIN shop_categories c ON c.id = p.category_id WHERE ${where.join(' AND ')}`;
  const { n: total } = await D.one(`SELECT COUNT(*)::int AS n ${base}`, args);
  const items = (await D.all(`SELECT p.*, c.name AS category_name, c.slug AS category_slug,
      (SELECT ROUND(AVG(rating)::numeric, 1)::float8 FROM shop_reviews rv WHERE rv.product_id = p.id AND rv.approved = 1) AS rating,
      (SELECT COUNT(*)::int FROM shop_reviews rv WHERE rv.product_id = p.id AND rv.approved = 1) AS review_count
      ${base} ORDER BY ${order} LIMIT ? OFFSET ?`, [...args, limit, offset])).map(productOut);
  res.json({ items, total, page, pages: Math.ceil(total / limit) });
});

r.get('/products/:slug', async (req, res) => {
  const p = await D.one(`SELECT p.*, c.name AS category_name, c.slug AS category_slug FROM shop_products p
      LEFT JOIN shop_categories c ON c.id = p.category_id WHERE p.slug = ? AND p.active = 1`, [req.params.slug]);
  if (!p) return res.status(404).json({ error: 'Không tìm thấy sản phẩm' });
  const reviews = await D.all('SELECT id, name, rating, content, created_at FROM shop_reviews WHERE product_id = ? AND approved = 1 ORDER BY id DESC', [p.id]);
  const related = (await D.all('SELECT * FROM shop_products WHERE category_id = ? AND id != ? AND active = 1 ORDER BY sold DESC LIMIT 4', [p.category_id, p.id])).map(productOut);
  const out = productOut(p);
  out.reviews = reviews;
  out.rating = reviews.length ? Math.round((reviews.reduce((s, x) => s + x.rating, 0) / reviews.length) * 10) / 10 : null;
  res.json({ product: out, related });
});

r.post('/products/:id/reviews', async (req, res) => {
  const p = await D.one('SELECT id FROM shop_products WHERE id = ? AND active = 1', [int(req.params.id)]);
  if (!p) throw new HttpError(404, 'Không tìm thấy sản phẩm');
  const name = String(req.body.name || (req.customer && req.customer.name) || '').trim().slice(0, 80);
  const rating = int(req.body.rating);
  const content = String(req.body.content || '').trim().slice(0, 1000);
  const fields = {};
  if (!name) fields.name = 'Nhập tên của bạn';
  if (rating < 1 || rating > 5) fields.rating = 'Chọn số sao';
  if (content.length < 5) fields.content = 'Viết vài dòng nhận xét';
  if (Object.keys(fields).length) throw new HttpError(400, 'Đánh giá chưa đủ thông tin', fields);
  await D.q('INSERT INTO shop_reviews(product_id, customer_id, name, rating, content) VALUES(?,?,?,?,?)',
    [p.id, req.customer ? req.customer.id : null, name, rating, content]);
  res.json({ ok: true, message: 'Cảm ơn bạn! Đánh giá sẽ hiện sau khi cửa hàng duyệt.' });
});

r.get('/pages/:slug', async (req, res) => {
  const pg = await D.one('SELECT title, slug, content, updated_at FROM shop_pages WHERE slug = ? AND active = 1', [req.params.slug]);
  if (!pg) return res.status(404).json({ error: 'Không tìm thấy trang' });
  res.json(pg);
});

// Ảnh tải lên từ trang quản trị (lưu trong Postgres)
r.get('/img/:id', async (req, res) => {
  const img = await D.one('SELECT mime, data FROM shop_images WHERE id = ?', [int(req.params.id)]);
  if (!img) return res.status(404).json({ error: 'Không có ảnh' });
  res.setHeader('Content-Type', img.mime);
  res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  res.end(img.data);
});

// Tính tiền giỏ hàng (giá, giảm giá, phí ship) trước khi đặt
r.post('/cart/quote', async (req, res) => {
  const q = await quote({ items: req.body.items, coupon: req.body.coupon });
  res.json({ ...q, coupon: q.coupon ? { code: q.coupon.code, description: q.coupon.description } : null });
});

r.post('/orders', async (req, res) => {
  res.json(await createOrder(req.body, req.customer));
});

r.get('/orders/track', async (req, res) => {
  const code = String(req.query.code || '').trim().toUpperCase();
  const phone = String(req.query.phone || '').replace(/\s/g, '');
  const o = await orderDetail("code = ? AND REPLACE(phone, ' ', '') = ?", [code, phone]);
  if (!o) return res.status(404).json({ error: 'Không tìm thấy đơn với mã và số điện thoại này' });
  delete o.admin_note;
  res.json(o);
});

// ---- Tài khoản khách hàng ----
r.post('/auth/register', async (req, res) => {
  const name = String(req.body.name || '').trim();
  const email = String(req.body.email || '').trim().toLowerCase();
  const phone = String(req.body.phone || '').trim();
  const password = String(req.body.password || '');
  const fields = {};
  if (!name) fields.name = 'Nhập họ tên';
  if (!isEmail(email)) fields.email = 'Email chưa đúng';
  if (phone && !isPhone(phone)) fields.phone = 'Số điện thoại chưa đúng';
  if (password.length < 6) fields.password = 'Mật khẩu tối thiểu 6 ký tự';
  if (!fields.email && (await D.one('SELECT id FROM shop_customers WHERE email = ?', [email]))) fields.email = 'Email này đã có tài khoản';
  if (Object.keys(fields).length) throw new HttpError(400, 'Thông tin đăng ký chưa đúng', fields);
  const c = await D.one('INSERT INTO shop_customers(name, email, phone, password_hash) VALUES(?,?,?,?) RETURNING id', [name, email, phone, hashPassword(password)]);
  await createSession(req, res, 'customer', c.id);
  res.json({ ok: true });
});

r.post('/auth/login', async (req, res) => {
  const email = String(req.body.email || '').trim().toLowerCase();
  const c = await D.one('SELECT * FROM shop_customers WHERE email = ?', [email]);
  if (!c || !verifyPassword(req.body.password, c.password_hash)) throw new HttpError(400, 'Email hoặc mật khẩu không đúng', { password: 'Email hoặc mật khẩu không đúng' });
  if (c.locked) throw new HttpError(403, 'Tài khoản đã bị khoá, vui lòng liên hệ cửa hàng');
  await createSession(req, res, 'customer', c.id);
  res.json({ ok: true });
});

r.post('/auth/logout', async (req, res) => { await destroySession(req, res, 'customer'); res.json({ ok: true }); });

r.get('/auth/me', (req, res) => res.json({ customer: req.customer || null }));

r.put('/account', requireCustomer, async (req, res) => {
  const name = String(req.body.name || '').trim();
  const phone = String(req.body.phone || '').trim();
  const address = String(req.body.address || '').trim();
  const fields = {};
  if (!name) fields.name = 'Nhập họ tên';
  if (phone && !isPhone(phone)) fields.phone = 'Số điện thoại chưa đúng';
  if (Object.keys(fields).length) throw new HttpError(400, 'Thông tin chưa đúng', fields);
  await D.q('UPDATE shop_customers SET name = ?, phone = ?, address = ? WHERE id = ?', [name, phone, address, req.customer.id]);
  res.json({ ok: true });
});

r.put('/account/password', requireCustomer, async (req, res) => {
  const c = await D.one('SELECT password_hash FROM shop_customers WHERE id = ?', [req.customer.id]);
  if (!verifyPassword(req.body.current, c.password_hash)) throw new HttpError(400, 'Mật khẩu hiện tại không đúng', { current: 'Mật khẩu hiện tại không đúng' });
  if (String(req.body.password || '').length < 6) throw new HttpError(400, 'Mật khẩu mới tối thiểu 6 ký tự', { password: 'Tối thiểu 6 ký tự' });
  await D.q('UPDATE shop_customers SET password_hash = ? WHERE id = ?', [hashPassword(req.body.password), req.customer.id]);
  res.json({ ok: true });
});

r.get('/account/orders', requireCustomer, async (req, res) => {
  const orders = await D.all('SELECT id, code, status, total, payment_method, payment_status, created_at FROM shop_orders WHERE customer_id = ? ORDER BY id DESC', [req.customer.id]);
  for (const o of orders) {
    o.items = await D.all('SELECT name, image, qty, size, color, price FROM shop_order_items WHERE order_id = ? ORDER BY id', [o.id]);
    o.status_label = STATUSES[o.status];
  }
  res.json(orders);
});

r.post('/account/orders/:code/cancel', requireCustomer, async (req, res) => {
  const o = await D.one('SELECT * FROM shop_orders WHERE code = ? AND customer_id = ?', [req.params.code, req.customer.id]);
  if (!o) throw new HttpError(404, 'Không tìm thấy đơn hàng');
  if (o.status !== 'pending') throw new HttpError(400, 'Đơn đã được xác nhận, vui lòng liên hệ cửa hàng để huỷ');
  await changeStatus(o.id, 'cancelled', req.customer.name, 'Khách tự huỷ');
  res.json({ ok: true });
});

export default r;
