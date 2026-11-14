import { D, tx, getSettings, ymd } from './db.js';
import { int, parseJSON, HttpError, isPhone, isEmail } from './util.js';

export const STATUSES = {
  pending: 'Chờ xác nhận',
  confirmed: 'Đã xác nhận',
  shipping: 'Đang giao',
  completed: 'Hoàn thành',
  cancelled: 'Đã huỷ',
};

const vnd = (n) => `${Number(n).toLocaleString('vi-VN')} ₫`;

// Kiểm tra mã giảm giá, trả về số tiền được giảm
export async function evaluateCoupon(code, subtotal, t = D) {
  if (!code) return { coupon: null, discount: 0 };
  const c = await t.one('SELECT * FROM shop_coupons WHERE lower(code) = lower(?)', [String(code).trim()]);
  if (!c || !c.active) throw new HttpError(400, 'Mã giảm giá không tồn tại', { coupon: 'Mã không hợp lệ' });
  const today = ymd();
  if (c.starts_at && today < c.starts_at) throw new HttpError(400, 'Mã giảm giá chưa đến ngày dùng', { coupon: 'Mã chưa bắt đầu' });
  if (c.expires_at && today > c.expires_at) throw new HttpError(400, 'Mã giảm giá đã hết hạn', { coupon: 'Mã đã hết hạn' });
  if (c.max_uses > 0 && c.used >= c.max_uses) throw new HttpError(400, 'Mã giảm giá đã hết lượt dùng', { coupon: 'Mã đã hết lượt' });
  if (subtotal < c.min_order) throw new HttpError(400, `Đơn tối thiểu ${vnd(c.min_order)} để dùng mã này`, { coupon: `Đơn tối thiểu ${vnd(c.min_order)}` });
  let discount = c.type === 'percent' ? Math.round((subtotal * c.value) / 100) : c.value;
  if (c.type === 'percent' && c.max_discount > 0) discount = Math.min(discount, c.max_discount);
  return { coupon: c, discount: Math.min(discount, subtotal) };
}

function shippingFee(amount, settings) {
  const fee = int(settings.shipping_fee, 0);
  const free = int(settings.free_ship_threshold, 0);
  return free > 0 && amount >= free ? 0 : fee;
}

// Tính giỏ hàng từ dữ liệu thật trong DB (không tin giá từ trình duyệt)
async function priceCart(items, t, lock) {
  if (!Array.isArray(items) || !items.length) throw new HttpError(400, 'Giỏ hàng đang trống');
  if (items.length > 50) throw new HttpError(400, 'Giỏ hàng quá nhiều dòng');
  const lines = [];
  const needed = {};
  for (const it of items) {
    const p = await t.one(`SELECT * FROM shop_products WHERE id = ? AND active = 1${lock ? ' FOR UPDATE' : ''}`, [int(it.product_id)]);
    const qty = Math.max(1, Math.min(99, int(it.qty, 1)));
    if (!p) throw new HttpError(400, 'Có sản phẩm trong giỏ không còn bán');
    needed[p.id] = (needed[p.id] || 0) + qty;
    if (needed[p.id] > p.stock) throw new HttpError(400, `"${p.name}" chỉ còn ${p.stock} sản phẩm`);
    const sizes = parseJSON(p.sizes, []);
    const colors = parseJSON(p.colors, []);
    const size = sizes.length ? String(it.size || '') : '';
    const color = colors.length ? String(it.color || '') : '';
    if (sizes.length && !sizes.includes(size)) throw new HttpError(400, `Chọn size cho "${p.name}"`);
    if (colors.length && !colors.includes(color)) throw new HttpError(400, `Chọn màu cho "${p.name}"`);
    const price = p.sale_price && p.sale_price > 0 && p.sale_price < p.price ? p.sale_price : p.price;
    lines.push({ product_id: p.id, name: p.name, image: parseJSON(p.images, [])[0] || '', price, qty, size, color });
  }
  return { lines, subtotal: lines.reduce((s, l) => s + l.price * l.qty, 0) };
}

export async function quote({ items, coupon }, t = D, lock = false) {
  const settings = await getSettings();
  const { lines, subtotal } = await priceCart(items, t, lock);
  const { coupon: c, discount } = await evaluateCoupon(coupon, subtotal, t);
  const shipping = shippingFee(subtotal - discount, settings);
  return { lines, subtotal, discount, shipping, total: subtotal - discount + shipping, coupon: c };
}

export async function createOrder(body, customer) {
  const fields = {};
  const name = String(body.name || '').trim();
  const phone = String(body.phone || '').trim();
  const email = String(body.email || '').trim();
  const address = String(body.address || '').trim();
  if (!name) fields.name = 'Nhập họ tên người nhận';
  if (!isPhone(phone)) fields.phone = 'Số điện thoại chưa đúng';
  if (email && !isEmail(email)) fields.email = 'Email chưa đúng';
  if (address.length < 8) fields.address = 'Nhập địa chỉ giao hàng đầy đủ';
  const settings = await getSettings();
  const method = body.payment_method === 'bank' ? 'bank' : 'cod';
  if (method === 'cod' && settings.cod_enabled === '0') fields.payment_method = 'Cửa hàng tạm ngưng nhận COD';
  if (method === 'bank' && settings.bank_enabled === '0') fields.payment_method = 'Cửa hàng tạm ngưng nhận chuyển khoản';
  if (Object.keys(fields).length) throw new HttpError(400, 'Thông tin đặt hàng chưa đủ', fields);

  return tx(async (t) => {
    // FOR UPDATE: khoá dòng sản phẩm để hai người mua cùng lúc không bán quá tồn kho
    const q = await quote({ items: body.items, coupon: body.coupon }, t, true);
    const { n } = await t.one("SELECT nextval('shop_order_code_seq')::int AS n");
    const code = `DH${n}`;
    const o = await t.one(`INSERT INTO shop_orders(code, customer_id, name, phone, email, address, note, payment_method, subtotal, discount, shipping, total, coupon_code)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) RETURNING id`, [code, customer ? customer.id : null, name, phone, email, address,
      String(body.note || '').slice(0, 500), method, q.subtotal, q.discount, q.shipping, q.total, q.coupon ? q.coupon.code : '']);
    for (const l of q.lines) {
      await t.q('INSERT INTO shop_order_items(order_id, product_id, name, image, price, qty, size, color) VALUES(?,?,?,?,?,?,?,?)',
        [o.id, l.product_id, l.name, l.image, l.price, l.qty, l.size, l.color]);
      await t.q('UPDATE shop_products SET stock = stock - ?, sold = sold + ? WHERE id = ?', [l.qty, l.qty, l.product_id]);
    }
    if (q.coupon) await t.q('UPDATE shop_coupons SET used = used + 1 WHERE id = ?', [q.coupon.id]);
    await t.q('INSERT INTO shop_order_history(order_id, status, note, by_name) VALUES(?,?,?,?)', [o.id, 'pending', 'Khách đặt hàng', name]);
    return { id: o.id, code, total: q.total };
  });
}

// Đổi trạng thái đơn; huỷ đơn thì trả hàng về kho, mở lại thì trừ kho lại
export async function changeStatus(orderId, status, byName, note) {
  if (!STATUSES[status]) throw new HttpError(400, 'Trạng thái không hợp lệ');
  return tx(async (t) => {
    const o = await t.one('SELECT * FROM shop_orders WHERE id = ? FOR UPDATE', [orderId]);
    if (!o) throw new HttpError(404, 'Không tìm thấy đơn hàng');
    if (o.status === status) return o;
    const items = await t.all('SELECT * FROM shop_order_items WHERE order_id = ?', [orderId]);
    if (status === 'cancelled') {
      for (const it of items) if (it.product_id) await t.q('UPDATE shop_products SET stock = stock + ?, sold = GREATEST(sold - ?, 0) WHERE id = ?', [it.qty, it.qty, it.product_id]);
    } else if (o.status === 'cancelled') {
      for (const it of items) if (it.product_id) await t.q('UPDATE shop_products SET stock = stock - ?, sold = sold + ? WHERE id = ?', [it.qty, it.qty, it.product_id]);
    }
    const payment = status === 'completed' && o.payment_method === 'cod' ? 'paid' : o.payment_status;
    await t.q('UPDATE shop_orders SET status = ?, payment_status = ?, updated_at = now() WHERE id = ?', [status, payment, orderId]);
    await t.q('INSERT INTO shop_order_history(order_id, status, note, by_name) VALUES(?,?,?,?)', [orderId, status, note || '', byName || '']);
    return t.one('SELECT * FROM shop_orders WHERE id = ?', [orderId]);
  });
}

export async function orderDetail(where, args) {
  const o = await D.one(`SELECT * FROM shop_orders WHERE ${where}`, args);
  if (!o) return null;
  o.items = await D.all('SELECT * FROM shop_order_items WHERE order_id = ? ORDER BY id', [o.id]);
  o.history = await D.all('SELECT * FROM shop_order_history WHERE order_id = ? ORDER BY id', [o.id]);
  o.status_label = STATUSES[o.status];
  return o;
}
