import { randomBytes, scryptSync, timingSafeEqual } from 'node:crypto';

export function slugify(str) {
  return String(str || '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/đ/g, 'd')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80) || 'item';
}

const SLUG_TABLES = new Set(['shop_products', 'shop_categories', 'shop_pages']);
export async function uniqueSlug(D, table, base, excludeId) {
  if (!SLUG_TABLES.has(table)) throw new Error('bảng không hợp lệ');
  const root = slugify(base);
  let slug = root;
  let i = 1;
  while (await D.one(`SELECT id FROM ${table} WHERE slug = ? AND id != ?`, [slug, excludeId || 0])) slug = `${root}-${++i}`;
  return slug;
}

export function hashPassword(password) {
  const salt = randomBytes(16).toString('hex');
  return `${salt}:${scryptSync(String(password), salt, 64).toString('hex')}`;
}

export function verifyPassword(password, stored) {
  if (!stored || !stored.includes(':')) return false;
  const [salt, hash] = stored.split(':');
  const test = scryptSync(String(password || ''), salt, 64);
  const buf = Buffer.from(hash, 'hex');
  return buf.length === test.length && timingSafeEqual(buf, test);
}

export function parseJSON(v, fallback) {
  try { const x = JSON.parse(v); return x == null ? fallback : x; } catch { return fallback; }
}

export function int(v, def = 0) {
  const n = parseInt(v, 10);
  return Number.isFinite(n) ? n : def;
}

export function paginate(req, defLimit = 20) {
  const limit = Math.min(Math.max(int(req.query.limit, defLimit), 1), 200);
  const page = Math.max(int(req.query.page, 1), 1);
  return { limit, page, offset: (page - 1) * limit };
}

export function productOut(p) {
  if (!p) return p;
  return {
    ...p,
    images: parseJSON(p.images, []),
    sizes: parseJSON(p.sizes, []),
    colors: parseJSON(p.colors, []),
    featured: !!p.featured,
    active: !!p.active,
    final_price: p.sale_price && p.sale_price > 0 && p.sale_price < p.price ? p.sale_price : p.price,
  };
}

export const isEmail = (s) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(s || ''));
export const isPhone = (s) => /^(\+?84|0)\d{9,10}$/.test(String(s || '').replace(/[\s.-]/g, ''));

export class HttpError extends Error {
  constructor(status, message, fields) { super(message); this.status = status; this.fields = fields; }
}
