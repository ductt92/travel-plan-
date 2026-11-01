// Tài khoản đăng nhập của trang quản lý và bản đồ. Bản Go: backend/go/accounts.go, cùng hợp đồng.
//
// Mỗi người một tài khoản (Đức, Ngọc là superadmin); mật khẩu chỉ lưu dạng băm scrypt trong Neon.
// Đăng nhập xong nhận token ký HMAC (khóa AUTH_SECRET, không có thì APP_SECRET), gửi lại bằng
// "Authorization: Bearer <token>"; hai bản Node/Go đọc được token của nhau. Đổi mật khẩu thì
// token_version tăng, token cũ hết hiệu lực. Mã chung APP_SECRET (X-App-Secret) vẫn dùng được cho
// các script (seed-catalog…), khi đó người ghi là "Hệ thống".
//
// POST /api/<node|go>/tai-khoan?login  {username, password} → { token, user }
// GET  …?me                     (Bearer)                    → { user }
// PUT  …?user                   (X-App-Secret) {username, name, role, password} → tạo/sửa tài khoản
import { createHmac, randomBytes, scryptSync, timingSafeEqual } from 'node:crypto';
import { authorized, db, fail, readJson, send } from './common.js';

const TABLES = `
CREATE TABLE IF NOT EXISTS app_users (
  id            serial PRIMARY KEY,
  username      text NOT NULL UNIQUE,
  name          text NOT NULL,
  role          text NOT NULL CHECK (role IN ('superadmin', 'admin', 'editor', 'viewer')),
  pass_hash     text NOT NULL,
  token_version integer NOT NULL DEFAULT 1,
  created_at    timestamptz NOT NULL DEFAULT now()
);
`;

let ready = null;
async function pool() {
  const p = await db();
  ready ??= p.query(TABLES).catch(e => { ready = null; throw e; });
  await ready;
  return p;
}

export const ROLES = ['superadmin', 'admin', 'editor', 'viewer'];
// Quyền theo vai trò. Hiện mới có superadmin; vai trò khác để dành khi thêm tài khoản mới.
const RIGHTS = {
  superadmin: ['read', 'write', 'delete', 'users'],
  admin: ['read', 'write', 'delete'],
  editor: ['read', 'write'],
  viewer: ['read'],
};
export const can = (user, right) => !!user && (RIGHTS[user.role] || []).includes(right);

const SYSTEM = { id: 0, username: 'system', name: 'Hệ thống', role: 'superadmin' };
const TOKEN_DAYS = 180;
const N = 16384, R = 8, P = 1, KEYLEN = 32;

const b64u = buf => Buffer.from(buf).toString('base64url');
const key = () => process.env.AUTH_SECRET || process.env.APP_SECRET || '';

/** "scrypt$N$r$p$muối$băm" — bản Go dùng cùng tham số */
export function hashPassword(password) {
  const salt = randomBytes(16);
  const h = scryptSync(password, salt, KEYLEN, { N, r: R, p: P });
  return `scrypt$${N}$${R}$${P}$${salt.toString('base64')}$${h.toString('base64')}`;
}

function checkPassword(password, stored) {
  const [alg, n, r, p, salt, hash] = String(stored).split('$');
  if (alg !== 'scrypt') return false;
  const want = Buffer.from(hash, 'base64');
  const got = scryptSync(password, Buffer.from(salt, 'base64'), want.length, { N: +n, r: +r, p: +p, maxmem: 64 << 20 });
  return timingSafeEqual(got, want);
}

function sign(user) {
  const body = b64u(JSON.stringify({ u: user.id, v: user.token_version, exp: Math.floor(Date.now() / 1000) + TOKEN_DAYS * 86400 }));
  return `${body}.${b64u(createHmac('sha256', key()).update(body).digest())}`;
}

/** { u, v } nếu chữ ký đúng và còn hạn, ngược lại null */
function verify(token) {
  const [body, mac] = String(token).split('.');
  if (!body || !mac || !key()) return null;
  const want = createHmac('sha256', key()).update(body).digest();
  const got = Buffer.from(mac, 'base64url');
  if (got.length !== want.length || !timingSafeEqual(got, want)) return null;
  try {
    const t = JSON.parse(Buffer.from(body, 'base64url').toString('utf8'));
    return t.exp > Date.now() / 1000 ? t : null;
  } catch { return null; }
}

const publicUser = u => ({ id: u.id, username: u.username, name: u.name, role: u.role });

/**
 * Người đang gọi API: token của tài khoản, hoặc "Hệ thống" nếu gửi mã chung APP_SECRET; null nếu không có.
 * Mỗi lần tra lại tài khoản để tài khoản bị xoá/đổi mật khẩu thì token cũ thôi dùng được.
 */
export async function currentUser(req) {
  if (authorized(req)) return SYSTEM;
  const m = /^Bearer\s+(\S+)$/.exec(String(req.headers.authorization || ''));
  const t = m && verify(m[1]);
  if (!t) return null;
  const p = await pool();
  const { rows: [u] } = await p.query('SELECT id, username, name, role, token_version FROM app_users WHERE id = $1', [t.u]);
  return u && u.token_version === t.v ? publicUser(u) : null;
}

/** Bỏ dấu, chữ thường: gõ "Đức", "duc" hay "DUC" đều ra cùng một tài khoản */
export const loginName = s => String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/gi, 'd').toLowerCase().trim();

export default async function accounts(req, res) {
  const url = new URL(req.url, 'http://localhost');
  let p;
  try { p = await pool(); } catch { return fail(res, 503, 'không kết nối được cơ sở dữ liệu'); }

  if (req.method === 'GET' && url.searchParams.has('me')) {
    let u;
    try { u = await currentUser(req); } catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
    return u ? send(res, 200, { user: u }) : fail(res, 401, 'chưa đăng nhập hoặc phiên đã hết hạn');
  }

  if (req.method === 'POST' && url.searchParams.has('login')) {
    let body;
    try { body = await readJson(req, 4096); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
    const name = loginName(body?.username);
    const password = typeof body?.password === 'string' ? body.password : '';
    if (!name || !password) return fail(res, 400, 'cần tên đăng nhập và mật khẩu');
    try {
      const { rows } = await p.query('SELECT id, username, name, role, pass_hash, token_version FROM app_users');
      const u = rows.find(r => r.username === name || loginName(r.name) === name);
      // vẫn băm một lần khi không có tài khoản, để thời gian trả lời không lộ tên nào có thật
      const ok = checkPassword(password, u?.pass_hash || 'scrypt$16384$8$1$AAAAAAAAAAAAAAAAAAAAAA==$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=');
      if (!u || !ok) return fail(res, 401, 'sai tên đăng nhập hoặc mật khẩu');
      return send(res, 200, { token: sign(u), user: publicUser(u) });
    } catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
  }

  // tạo/sửa tài khoản: chỉ bằng mã chung (script trên máy), chưa có trang quản lý tài khoản
  if (req.method === 'PUT' && url.searchParams.has('user')) {
    if (!authorized(req)) return fail(res, 401, 'sai mật khẩu');
    let body;
    try { body = await readJson(req, 4096); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
    const username = loginName(body?.username);
    const name = typeof body?.name === 'string' ? body.name.trim().slice(0, 60) : '';
    const role = body?.role;
    const password = typeof body?.password === 'string' ? body.password : '';
    if (!/^[a-z0-9][a-z0-9._-]{1,31}$/.test(username)) return fail(res, 400, 'tên đăng nhập chỉ gồm chữ thường, số, . _ -');
    if (!name) return fail(res, 400, 'cần tên hiển thị');
    if (!ROLES.includes(role)) return fail(res, 400, 'vai trò không hợp lệ');
    if (password.length < 6) return fail(res, 400, 'mật khẩu tối thiểu 6 ký tự');
    try {
      const { rows: [u] } = await p.query(
        `INSERT INTO app_users (username, name, role, pass_hash) VALUES ($1, $2, $3, $4)
         ON CONFLICT (username) DO UPDATE SET name = EXCLUDED.name, role = EXCLUDED.role, pass_hash = EXCLUDED.pass_hash,
                                              token_version = app_users.token_version + 1
         RETURNING id, username, name, role`,
        [username, name, role, hashPassword(password)]);
      return send(res, 200, { user: publicUser(u) });
    } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
  }

  return fail(res, 400, 'cần ?login, ?me hoặc ?user');
}
