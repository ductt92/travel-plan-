// Đồng bộ các khóa localStorage lên /api/sync (Go + Neon) giữa các máy của Ngọc và Đức.
//
// Cách dùng trong app:
//   track('dadiqua-trip')            đăng ký khóa (gọi một lần lúc khởi động)
//   changed('dadiqua-trip')          gọi sau mỗi lần app ghi localStorage
// Khi máy khác đổi dữ liệu, thư viện ghi lại localStorage rồi phát sự kiện 'storage'
// cho khóa đó, nên hook nào đang nghe 'storage' sẽ tự vẽ lại.
// Chưa nhập mã đồng bộ thì không làm gì: app chạy y như trước, chỉ lưu trong máy.
import { useSyncExternalStore } from 'react';

const SECRET = 'trang-sync-secret';
const BACKEND = 'trang-api-backend';
const META = 'trang-sync:'; // + khóa → { v: phiên bản trên server, base: bản đã đồng bộ gần nhất }
const POLL_MS = 10000;

const keys = new Map(); // khóa → { strip, keep, queue }
let secret = ls(() => localStorage.getItem(SECRET)) || '';
// Hai bản API cùng hợp đồng, cùng bảng dữ liệu: /api/node/... (Node.js) hoặc /api/go/... (Go)
export const BACKENDS = [{ id: 'node', label: 'Node.js' }, { id: 'go', label: 'Go' }];
let backend = ls(() => localStorage.getItem(BACKEND)) === 'go' ? 'go' : 'node';
let status = { state: secret ? 'idle' : 'off', at: null, error: '', backend };
const subs = new Set();

function ls(fn) { try { return fn(); } catch { return null; } }
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const isObj = x => x && typeof x === 'object' && !Array.isArray(x);

function setStatus(patch) { status = { ...status, ...patch }; subs.forEach(f => f()); }
function readLocal(key) { return ls(() => JSON.parse(localStorage.getItem(key) || 'null')); }
function readMeta(key) { return ls(() => JSON.parse(localStorage.getItem(META + key))) || { v: 0, base: null }; }
function writeMeta(key, m) { ls(() => localStorage.setItem(META + key, JSON.stringify(m))); }

/**
 * Gộp ba chiều: lấy bản server, rồi áp lại những gì máy này đã sửa so với base.
 * Đi sâu 2 cấp nên hai người tích hai địa điểm khác nhau cùng lúc vẫn giữ cả hai.
 */
export function merge3(base, local, remote, depth = 2) {
  if (depth === 0 || !isObj(local) || !isObj(remote)) return eq(local, base) ? remote : local;
  const b = isObj(base) ? base : {};
  const out = { ...remote };
  for (const k of new Set([...Object.keys(b), ...Object.keys(local)])) {
    if (eq(local[k], b[k])) continue; // máy này không sửa mục này
    if (!(k in local)) delete out[k];
    else out[k] = k in remote ? merge3(b[k], local[k], remote[k], depth - 1) : local[k];
  }
  return out;
}

/** Gọi /api/<node|go>/<path> kèm mã đồng bộ; dùng cho cả đồng bộ lẫn Hỏi AI */
export function apiFetch(path, { method = 'GET', body } = {}) {
  return fetch(`/api/${backend}/${path}`, {
    method,
    headers: { 'X-App-Secret': secret, ...(body !== undefined && { 'Content-Type': 'application/json' }) },
    body: body !== undefined ? JSON.stringify(body) : undefined
  });
}

async function call(method, key, body) {
  const res = await apiFetch(`sync?key=${encodeURIComponent(key)}`, { method, body });
  setStatus({ served: res.headers.get('X-Backend') || '' }); // bản API thực sự trả lời
  const data = await res.json().catch(() => ({}));
  if (res.status === 401) { const e = new Error('Sai mã đồng bộ'); e.auth = true; throw e; }
  if (!res.ok && res.status !== 409) throw new Error(data.error || `Máy chủ trả lỗi ${res.status}`);
  return { status: res.status, ...data };
}

// Ghi bản mới vào localStorage (giữ các trường chỉ thuộc về máy này) và báo cho app
function apply(key, next) {
  const opt = keys.get(key);
  const value = opt.keep ? opt.keep(next, readLocal(key)) : next;
  ls(() => localStorage.setItem(key, JSON.stringify(value)));
  window.dispatchEvent(new StorageEvent('storage', { key }));
}

async function push(key, tries = 3) {
  const opt = keys.get(key);
  const meta = readMeta(key);
  const local = opt.strip(readLocal(key));
  if (local == null || (meta.v > 0 && eq(local, meta.base))) return;
  const r = await call('PUT', key, { data: local, base: meta.v });
  if (r.status === 409) { // máy kia ghi trước: gộp rồi gửi lại
    const merged = merge3(meta.base, local, r.data);
    writeMeta(key, { v: r.version, base: r.data });
    apply(key, merged);
    if (tries > 1) return push(key, tries - 1);
    return;
  }
  writeMeta(key, { v: r.version, base: local });
}

async function pull(key) {
  const opt = keys.get(key);
  const r = await call('GET', key);
  const meta = readMeta(key);
  if (r.version === 0) return push(key); // server chưa có: đưa dữ liệu máy này lên
  const local = opt.strip(readLocal(key));
  const dirty = local != null && !eq(local, meta.base);
  if (r.version !== meta.v) {
    const next = dirty ? merge3(meta.base, local, r.data) : r.data;
    writeMeta(key, { v: r.version, base: r.data });
    if (!eq(next, local)) apply(key, next);
  }
  if (dirty) return push(key);
}

// Mỗi khóa chạy tuần tự để hai lần đồng bộ không giẫm lên nhau
function run(key, job) {
  const opt = keys.get(key);
  if (!opt || !secret) return Promise.resolve();
  opt.queue = opt.queue.then(async () => {
    setStatus({ state: 'syncing' });
    try {
      await job(key);
      setStatus({ state: 'ok', at: Date.now(), error: '' });
    } catch (e) {
      setStatus({ state: e.auth ? 'denied' : 'error', error: e.message });
    }
  });
  return opt.queue;
}

const pullAll = () => Promise.all([...keys.keys()].map(k => run(k, pull)));

/**
 * Đăng ký một khóa localStorage để đồng bộ.
 * strip(data): bỏ phần không được đưa lên server (vd. khóa API riêng).
 * keep(next, local): khi nhận bản từ server, giữ lại phần riêng của máy này.
 */
export function track(key, { strip = d => d, keep = null } = {}) {
  if (keys.has(key)) return;
  keys.set(key, { strip, keep, queue: Promise.resolve() });
  start();
  run(key, pull);
}

const timers = new Map();
/** Báo app vừa ghi khóa này; gửi lên sau 800 ms để gom các lần sửa liên tiếp */
export function changed(key) {
  if (!secret || !keys.has(key)) return;
  clearTimeout(timers.get(key));
  timers.set(key, setTimeout(() => run(key, push), 800));
}

let started = false;
function start() {
  if (started || typeof window === 'undefined') return;
  started = true;
  setInterval(() => { if (document.visibilityState === 'visible') pullAll(); }, POLL_MS);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') pullAll(); });
  window.addEventListener('online', pullAll);
}

/** Lưu mã đồng bộ rồi kéo dữ liệu về ngay; trả về lỗi (nếu có) để form hiển thị */
export async function connect(code) {
  secret = code.trim();
  ls(() => localStorage.setItem(SECRET, secret));
  await pullAll();
  if (status.state === 'denied') { const e = status.error; disconnect(); return e; } // sai mã: không lưu lại
  return status.state === 'error' ? status.error : '';
}

/** Tắt đồng bộ trên máy này (dữ liệu trong máy vẫn giữ nguyên) */
export function disconnect() {
  secret = '';
  ls(() => localStorage.removeItem(SECRET));
  for (const k of keys.keys()) ls(() => localStorage.removeItem(META + k));
  setStatus({ state: 'off', at: null, error: '' });
}

/** Đổi bản API (node | go). Dữ liệu dùng chung một bảng nên chỉ cần kéo lại cho chắc */
export function setBackend(id) {
  backend = id === 'go' ? 'go' : 'node';
  ls(() => localStorage.setItem(BACKEND, backend));
  setStatus({ backend });
  pullAll();
}

export const getSecret = () => secret;
export const getBackend = () => backend;
export const useSyncStatus = () => useSyncExternalStore(f => { subs.add(f); return () => subs.delete(f); }, () => status);

export { SyncButton } from './SyncButton.jsx';
