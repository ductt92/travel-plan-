import type { Entries, Trip, TripDraft } from './types';

/**
 * Gọi /api/<node|go>/ban-do. Chọn bản Node hay Go dùng chung khóa localStorage với
 * các app khác trong site (nút "Đồng bộ" đặt khóa này), nên đổi ở đâu cũng theo.
 */
const BACKEND_KEY = 'trang-api-backend';
const PASS_KEY = 'ban-do-pass';

const read = (k: string) => {
  try { return localStorage.getItem(k) || ''; } catch { return ''; }
};
const write = (k: string, v: string) => {
  try { v ? localStorage.setItem(k, v) : localStorage.removeItem(k); } catch { /* chặn lưu thì thôi */ }
};

export const savedPass = () => read(PASS_KEY);
export const rememberPass = (v: string) => write(PASS_KEY, v);
const base = () => `/api/${read(BACKEND_KEY) === 'go' ? 'go' : 'node'}/ban-do`;

/** Giữ lại mã HTTP để phân biệt "sai mật khẩu" với "server hỏng". */
export class ApiError extends Error {
  constructor(message: string, readonly status: number) {
    super(message);
  }
}

async function call<T>(query: string, init?: RequestInit & { pass?: string }): Promise<T> {
  const { pass, ...rest } = init ?? {};
  let res: Response;
  try {
    res = await fetch(base() + query, {
      ...rest,
      cache: 'no-store',
      headers: {
        ...(pass ? { 'X-App-Secret': pass } : {}),
        ...(rest.body ? { 'Content-Type': 'application/json' } : {}),
      },
    });
  } catch {
    throw new ApiError('Không gọi được server, kiểm tra mạng rồi thử lại.', 0);
  }

  const body = await res.json().catch(() => null);
  if (!res.ok) throw new ApiError(body?.error || 'Server trả lời không hiểu được.', res.status);
  return body as T;
}

export const loadEntries = () => call<{ entries: Entries }>('').then(r => r.entries);

/** Trả về null nếu mật khẩu đúng, còn lại là câu để hiện ra. */
export async function checkPass(pass: string) {
  try {
    await call('?check', { pass });
    return null;
  } catch (err) {
    return err instanceof ApiError && err.status === 401 ? 'Sai mật khẩu.' : (err as Error).message;
  }
}

const q = (code: string) => `?province=${encodeURIComponent(code)}`;

export const putStatus = (pass: string, code: string, status: string) =>
  call<{ ok: true }>(q(code), { pass, method: 'PUT', body: JSON.stringify({ status }) });

export const postTrip = (pass: string, code: string, trip: TripDraft) =>
  call<{ trip: Trip }>(q(code), { pass, method: 'POST', body: JSON.stringify(trip) }).then(r => r.trip);

export const patchTrip = (pass: string, code: string, id: number, trip: TripDraft) =>
  call<{ trip: Trip }>(`${q(code)}&id=${id}`, { pass, method: 'PATCH', body: JSON.stringify(trip) }).then(r => r.trip);

export const deleteTrip = (pass: string, code: string, id: number) =>
  call<{ ok: true }>(`${q(code)}&id=${id}`, { pass, method: 'DELETE' });
