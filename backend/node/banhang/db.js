// Cơ sở dữ liệu của web bán hàng: dùng chung Postgres (Neon) với cả repo qua common.js,
// mọi bảng có tiền tố shop_ để không đụng bảng của trang khác.
// Viết SQL với dấu ? như SQLite, hàm toPg đổi sang $1, $2… của Postgres.
import { db } from '../common.js';

const SCHEMA = `
CREATE TABLE IF NOT EXISTS shop_settings (key text PRIMARY KEY, value text);
CREATE TABLE IF NOT EXISTS shop_categories (
  id serial PRIMARY KEY, name text NOT NULL, slug text NOT NULL UNIQUE, description text NOT NULL DEFAULT '',
  image text NOT NULL DEFAULT '', sort integer NOT NULL DEFAULT 0, active integer NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS shop_products (
  id serial PRIMARY KEY, name text NOT NULL, slug text NOT NULL UNIQUE, sku text NOT NULL DEFAULT '',
  category_id integer REFERENCES shop_categories(id) ON DELETE SET NULL,
  short_desc text NOT NULL DEFAULT '', description text NOT NULL DEFAULT '',
  price integer NOT NULL DEFAULT 0, sale_price integer,
  images text NOT NULL DEFAULT '[]', sizes text NOT NULL DEFAULT '[]', colors text NOT NULL DEFAULT '[]',
  stock integer NOT NULL DEFAULT 0, sold integer NOT NULL DEFAULT 0,
  featured integer NOT NULL DEFAULT 0, active integer NOT NULL DEFAULT 1,
  created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_customers (
  id serial PRIMARY KEY, name text NOT NULL, email text NOT NULL UNIQUE, phone text NOT NULL DEFAULT '',
  address text NOT NULL DEFAULT '', password_hash text NOT NULL, locked integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_staff (
  id serial PRIMARY KEY, name text NOT NULL, email text NOT NULL UNIQUE, password_hash text NOT NULL,
  role text NOT NULL DEFAULT 'staff', active integer NOT NULL DEFAULT 1, last_login timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_sessions (token text PRIMARY KEY, kind text NOT NULL, user_id integer NOT NULL, expires_at bigint NOT NULL);
CREATE SEQUENCE IF NOT EXISTS shop_order_code_seq START 100001;
CREATE TABLE IF NOT EXISTS shop_orders (
  id serial PRIMARY KEY, code text NOT NULL UNIQUE,
  customer_id integer REFERENCES shop_customers(id) ON DELETE SET NULL,
  name text NOT NULL, phone text NOT NULL, email text NOT NULL DEFAULT '', address text NOT NULL, note text NOT NULL DEFAULT '',
  payment_method text NOT NULL DEFAULT 'cod', payment_status text NOT NULL DEFAULT 'unpaid', status text NOT NULL DEFAULT 'pending',
  subtotal integer NOT NULL DEFAULT 0, discount integer NOT NULL DEFAULT 0, shipping integer NOT NULL DEFAULT 0, total integer NOT NULL DEFAULT 0,
  coupon_code text NOT NULL DEFAULT '', admin_note text NOT NULL DEFAULT '',
  created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_order_items (
  id serial PRIMARY KEY, order_id integer NOT NULL REFERENCES shop_orders(id) ON DELETE CASCADE,
  product_id integer REFERENCES shop_products(id) ON DELETE SET NULL,
  name text NOT NULL, image text NOT NULL DEFAULT '', price integer NOT NULL, qty integer NOT NULL,
  size text NOT NULL DEFAULT '', color text NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS shop_order_history (
  id serial PRIMARY KEY, order_id integer NOT NULL REFERENCES shop_orders(id) ON DELETE CASCADE,
  status text NOT NULL, note text NOT NULL DEFAULT '', by_name text NOT NULL DEFAULT '', created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_coupons (
  id serial PRIMARY KEY, code text NOT NULL UNIQUE, description text NOT NULL DEFAULT '', type text NOT NULL DEFAULT 'percent',
  value integer NOT NULL, max_discount integer NOT NULL DEFAULT 0, min_order integer NOT NULL DEFAULT 0,
  max_uses integer NOT NULL DEFAULT 0, used integer NOT NULL DEFAULT 0,
  starts_at text NOT NULL DEFAULT '', expires_at text NOT NULL DEFAULT '', active integer NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS shop_banners (
  id serial PRIMARY KEY, title text NOT NULL DEFAULT '', subtitle text NOT NULL DEFAULT '', image text NOT NULL DEFAULT '',
  button_text text NOT NULL DEFAULT '', link text NOT NULL DEFAULT '', sort integer NOT NULL DEFAULT 0, active integer NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS shop_pages (
  id serial PRIMARY KEY, title text NOT NULL, slug text NOT NULL UNIQUE, content text NOT NULL DEFAULT '',
  show_in_footer integer NOT NULL DEFAULT 1, active integer NOT NULL DEFAULT 1, updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_reviews (
  id serial PRIMARY KEY, product_id integer NOT NULL REFERENCES shop_products(id) ON DELETE CASCADE,
  customer_id integer REFERENCES shop_customers(id) ON DELETE SET NULL,
  name text NOT NULL, rating integer NOT NULL, content text NOT NULL DEFAULT '', approved integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shop_images (id serial PRIMARY KEY, mime text NOT NULL, data bytea NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS shop_products_cat ON shop_products(category_id);
CREATE INDEX IF NOT EXISTS shop_orders_status ON shop_orders(status);
CREATE INDEX IF NOT EXISTS shop_orders_created ON shop_orders(created_at);
CREATE INDEX IF NOT EXISTS shop_items_order ON shop_order_items(order_id);
`;

let ready = null;
export async function pool() {
  const p = await db();
  ready ??= p.query(SCHEMA).catch((e) => { ready = null; throw e; });
  await ready;
  return p;
}

const toPg = (sql) => { let i = 0; return sql.replace(/\?/g, () => `$${++i}`); };

// Bộ hàm truy vấn, gắn với pool hoặc với một kết nối đang trong giao dịch
function bind(client) {
  const run = async (sql, params = []) => (client || (await pool())).query(toPg(sql), params);
  return {
    q: run,
    one: async (sql, params) => (await run(sql, params)).rows[0],
    all: async (sql, params) => (await run(sql, params)).rows,
  };
}
export const D = bind(null);

// Chạy fn trong một giao dịch; lỗi thì huỷ toàn bộ
export async function tx(fn) {
  const c = await (await pool()).connect();
  try {
    await c.query('BEGIN');
    const out = await fn(bind(c));
    await c.query('COMMIT');
    return out;
  } catch (e) {
    await c.query('ROLLBACK').catch(() => {});
    throw e;
  } finally {
    c.release();
  }
}

export async function getSettings() {
  const out = {};
  for (const r of await D.all('SELECT key, value FROM shop_settings')) out[r.key] = r.value;
  return out;
}

export async function setSettings(obj, t = D) {
  for (const [k, v] of Object.entries(obj)) {
    await t.q('INSERT INTO shop_settings(key, value) VALUES(?, ?) ON CONFLICT (key) DO UPDATE SET value = excluded.value', [k, v == null ? '' : String(v)]);
  }
}

// Ngày theo giờ Việt Nam (máy chủ Vercel chạy giờ UTC)
export const TZ = 'Asia/Ho_Chi_Minh';
export const vnDay = (col) => `((${col}) AT TIME ZONE '${TZ}')::date`;
const fmt = new Intl.DateTimeFormat('en-CA', { timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit' });
export const ymd = (d = new Date()) => fmt.format(d);
