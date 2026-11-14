// Đăng nhập của web bán hàng: phiên lưu trong bảng shop_sessions, mã phiên nằm trong cookie httpOnly.
// Khách hàng và nhân viên dùng hai cookie khác nhau.
import { randomBytes } from 'node:crypto';
import { D } from './db.js';

const DAY = 24 * 60 * 60 * 1000;
const COOKIE = { customer: 'shop_sid', admin: 'shop_asid' };

export function parseCookies(req, _res, next) {
  const out = {};
  for (const part of String(req.headers.cookie || '').split(';')) {
    const i = part.indexOf('=');
    if (i > 0) {
      const k = part.slice(0, i).trim();
      try { out[k] = decodeURIComponent(part.slice(i + 1).trim()); } catch { /* bỏ qua cookie hỏng */ }
    }
  }
  req.cookies = out;
  next();
}

const secure = (req) => req.headers['x-forwarded-proto'] === 'https';

export async function createSession(req, res, kind, userId) {
  const token = randomBytes(32).toString('hex');
  const ttl = 30 * DAY;
  await D.q('DELETE FROM shop_sessions WHERE expires_at < ?', [Date.now()]);
  await D.q('INSERT INTO shop_sessions(token, kind, user_id, expires_at) VALUES(?,?,?,?)', [token, kind, userId, Date.now() + ttl]);
  res.cookie(COOKIE[kind], token, { httpOnly: true, sameSite: 'lax', secure: secure(req), maxAge: ttl, path: '/' });
}

export async function destroySession(req, res, kind) {
  const token = req.cookies[COOKIE[kind]];
  if (token) await D.q('DELETE FROM shop_sessions WHERE token = ?', [token]);
  res.clearCookie(COOKIE[kind], { path: '/' });
}

async function readSession(req, kind) {
  const token = req.cookies[COOKIE[kind]];
  if (!token) return null;
  return D.one('SELECT user_id FROM shop_sessions WHERE token = ? AND kind = ? AND expires_at > ?', [token, kind, Date.now()]);
}

// Gắn khách hàng đang đăng nhập (nếu có) vào req.customer
export async function loadCustomer(req, _res, next) {
  const s = await readSession(req, 'customer');
  if (s) {
    const c = await D.one('SELECT id, name, email, phone, address, locked, created_at FROM shop_customers WHERE id = ?', [s.user_id]);
    if (c && !c.locked) req.customer = c;
  }
  next();
}

export function requireCustomer(req, res, next) {
  if (!req.customer) return res.status(401).json({ error: 'Bạn cần đăng nhập' });
  next();
}

export async function requireAdmin(req, res, next) {
  const s = await readSession(req, 'admin');
  if (!s) return res.status(401).json({ error: 'Phiên đăng nhập đã hết hạn' });
  const u = await D.one('SELECT id, name, email, role, active FROM shop_staff WHERE id = ?', [s.user_id]);
  if (!u || !u.active) return res.status(401).json({ error: 'Tài khoản đã bị khoá' });
  req.staff = u;
  next();
}

// Chỉ quản trị viên (role = admin) mới được vào
export function onlyAdmin(req, res, next) {
  if (req.staff.role !== 'admin') return res.status(403).json({ error: 'Chỉ quản trị viên mới có quyền này' });
  next();
}
