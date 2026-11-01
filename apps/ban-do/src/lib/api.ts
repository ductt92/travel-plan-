import type { Entries, Trip, TripDraft } from './types';

/**
 * Gọi /api/<node|go>/ban-do. Chọn bản Node hay Go dùng chung khóa localStorage với
 * các app khác trong site (nút "Đồng bộ" đặt khóa này), nên đổi ở đâu cũng theo.
 * Lệnh ghi kèm token của tài khoản đang đăng nhập (@trang/ui/auth, dùng chung với trang quản lý).
 */
const BACKEND_KEY = 'trang-api-backend';

const read = (k: string) => {
  try { return localStorage.getItem(k) || ''; } catch { return ''; }
};
const base = () => `/api/${read(BACKEND_KEY) === 'go' ? 'go' : 'node'}/ban-do`;

/** Giữ lại mã HTTP để phân biệt "sai mật khẩu" với "server hỏng". */
export class ApiError extends Error {
  constructor(message: string, readonly status: number) {
    super(message);
  }
}

async function call<T>(query: string, init?: RequestInit & { token?: string }): Promise<T> {
  const { token, ...rest } = init ?? {};
  let res: Response;
  try {
    res = await fetch(base() + query, {
      ...rest,
      cache: 'no-store',
      headers: {
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
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

const q = (code: string) => `?province=${encodeURIComponent(code)}`;

export const putStatus = (token: string, code: string, status: string) =>
  call<{ ok: true }>(q(code), { token, method: 'PUT', body: JSON.stringify({ status }) });

export const postTrip = (token: string, code: string, trip: TripDraft) =>
  call<{ trip: Trip }>(q(code), { token, method: 'POST', body: JSON.stringify(trip) }).then(r => r.trip);

export const patchTrip = (token: string, code: string, id: number, trip: TripDraft) =>
  call<{ trip: Trip }>(`${q(code)}&id=${id}`, { token, method: 'PATCH', body: JSON.stringify(trip) }).then(r => r.trip);

export const deleteTrip = (token: string, code: string, id: number) =>
  call<{ ok: true }>(`${q(code)}&id=${id}`, { token, method: 'DELETE' });
