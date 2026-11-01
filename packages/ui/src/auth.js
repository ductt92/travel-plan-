// Phiên đăng nhập dùng chung cho trang quản lý và bản đồ (cùng một site nên cùng localStorage):
// đăng nhập ở trang này là trang kia cũng biết ai đang dùng. Server: /api/<node|go>/tai-khoan
// (backend/node/accounts.js). Token gửi kèm bằng "Authorization: Bearer …".
const KEY = 'trang-auth';
const BACKEND_KEY = 'trang-api-backend';

const read = k => { try { return localStorage.getItem(k) || ''; } catch { return ''; } };
const base = () => `/api/${read(BACKEND_KEY) === 'go' ? 'go' : 'node'}/tai-khoan`;

/** { token, user: { id, username, name, role } } hoặc null */
export function getSession() {
  try {
    const s = JSON.parse(read(KEY) || 'null');
    return s && s.token && s.user ? s : null;
  } catch { return null; }
}

const listeners = new Set();
function save(s) {
  try { s ? localStorage.setItem(KEY, JSON.stringify(s)) : localStorage.removeItem(KEY); } catch { /* chặn lưu thì chỉ giữ trong trang */ }
  listeners.forEach(fn => fn(s));
}

/** Gọi lại khi đăng nhập/đăng xuất (cả ở tab khác). Trả về hàm huỷ. */
export function onSessionChange(fn) {
  listeners.add(fn);
  const onStorage = e => { if (e.key === KEY) fn(getSession()); };
  window.addEventListener('storage', onStorage);
  return () => { listeners.delete(fn); window.removeEventListener('storage', onStorage); };
}

/** Header kèm theo các lệnh ghi; rỗng khi chưa đăng nhập */
export function authHeaders() {
  const s = getSession();
  return s ? { Authorization: `Bearer ${s.token}` } : {};
}

/** Trả về null nếu đăng nhập được, còn lại là câu để hiện ra */
export async function signIn(username, password) {
  let res;
  try {
    res = await fetch(`${base()}?login`, {
      method: 'POST', cache: 'no-store', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.trim(), password }),
    });
  } catch { return 'Không gọi được server, kiểm tra mạng rồi thử lại.'; }
  const body = await res.json().catch(() => null);
  if (res.status === 401) return 'Sai tên đăng nhập hoặc mật khẩu.';
  if (!res.ok || !body?.token) return body?.error || `Server lỗi (${res.status}).`;
  save({ token: body.token, user: body.user });
  return null;
}

export const signOut = () => save(null);

/** Hỏi lại server phiên còn dùng được không (đổi mật khẩu, xoá tài khoản thì tự đăng xuất). Lỗi mạng thì giữ nguyên. */
export async function refreshSession() {
  const s = getSession();
  if (!s) return null;
  try {
    const res = await fetch(`${base()}?me`, { cache: 'no-store', headers: { Authorization: `Bearer ${s.token}` } });
    if (res.status === 401) { save(null); return null; }
    const body = await res.json().catch(() => null);
    if (res.ok && body?.user) { const next = { ...s, user: body.user }; save(next); return next; }
  } catch { /* mạng lỗi: coi như vẫn đăng nhập, lệnh ghi sẽ báo nếu hết hạn */ }
  return s;
}
