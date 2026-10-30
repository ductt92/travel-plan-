import type { Asset, AssetKind, Catalog, Course, CourseDraft, Lesson, LessonDraft } from './types';

/** Gọi /api/node/quan-ly. Mật khẩu nhớ trong localStorage như trang bản đồ. */
const BASE = '/api/node/quan-ly';
const PASS_KEY = 'quan-ly-pass';

export const savedPass = () => {
  try { return localStorage.getItem(PASS_KEY) || ''; } catch { return ''; }
};
export const rememberPass = (v: string) => {
  try { v ? localStorage.setItem(PASS_KEY, v) : localStorage.removeItem(PASS_KEY); } catch { /* chặn lưu thì thôi */ }
};

/** Giữ lại mã HTTP để phân biệt "sai mật khẩu" (401), "chưa cấu hình R2" (503) với lỗi khác. */
export class ApiError extends Error {
  constructor(message: string, readonly status: number) {
    super(message);
  }
}

// mật khẩu đang dùng; App đặt sau khi đăng nhập, mọi lệnh gọi tự kèm theo
let pass = savedPass();
export const setPass = (v: string) => { pass = v; };

/** Server báo 401 giữa chừng (đổi mật khẩu bên server): App nghe để mở lại hộp đăng nhập. */
let onUnauthorized: () => void = () => {};
export const handleUnauthorized = (fn: () => void) => { onUnauthorized = fn; };

async function call<T>(query: string, init?: RequestInit & { pass?: string }): Promise<T> {
  const { pass: own, ...rest } = init ?? {};
  const secret = own ?? pass;
  let res: Response;
  try {
    res = await fetch(BASE + query, {
      ...rest,
      cache: 'no-store',
      headers: {
        ...(secret ? { 'X-App-Secret': secret } : {}),
        ...(rest.body ? { 'Content-Type': 'application/json' } : {}),
      },
    });
  } catch {
    throw new ApiError('Không gọi được server, kiểm tra mạng rồi thử lại.', 0);
  }
  const body = await res.json().catch(() => null);
  if (!res.ok) {
    if (res.status === 401 && own === undefined) onUnauthorized();
    throw new ApiError(body?.error || `Server lỗi (${res.status}).`, res.status);
  }
  return body as T;
}

const json = (method: string, data: unknown): RequestInit => ({ method, body: JSON.stringify(data) });

/** null nếu mật khẩu đúng, còn lại là câu để hiện ra. Cắt khoảng trắng: dán hay dính dấu cách. */
export async function checkPass(typed: string) {
  try {
    await call('?check', { pass: typed.trim() });
    return null;
  } catch (err) {
    return err instanceof ApiError && err.status === 401 ? 'Sai mật khẩu.' : (err as Error).message;
  }
}

export const loadCatalog = () => call<Catalog>('');

export const createCourse = (d: CourseDraft) =>
  call<{ course: Course }>('?course', json('POST', d)).then(r => r.course);
export const updateCourse = (id: number, d: Partial<Omit<CourseDraft, 'slug'>>) =>
  call<{ course: Course }>(`?course=${id}`, json('PATCH', d)).then(r => r.course);
export const deleteCourse = (id: number) => call<{ ok: true }>(`?course=${id}`, { method: 'DELETE' });

export const createLesson = (courseId: number, d: LessonDraft) =>
  call<{ lesson: Lesson }>('?lesson', json('POST', { courseId, ...d })).then(r => r.lesson);
export const updateLesson = (id: number, d: Partial<LessonDraft>) =>
  call<{ lesson: Lesson }>(`?lesson=${id}`, json('PATCH', d)).then(r => r.lesson);
export const deleteLesson = (id: number) => call<{ ok: true }>(`?lesson=${id}`, { method: 'DELETE' });

/** Gắn link YouTube cho bài; server kiểm và chuẩn hóa link, sai thì trả 400 {error}. */
export const addYoutube = (lessonId: number, name: string, url: string) =>
  call<{ asset: Asset }>('?asset', json('POST', { lessonId, kind: 'video', name, size: 0, url, storage: 'youtube' }))
    .then(r => r.asset);

export const deleteAsset = (id: number) => call<{ ok: true }>(`?asset=${id}`, { method: 'DELETE' });

export const MAX_UPLOAD = 200 * 1024 * 1024;

interface Ticket { putUrl: string; key: string; publicUrl: string; headers?: Record<string, string> }

/** PUT thẳng lên R2 bằng XHR để có phần trăm (fetch chưa báo tiến độ tải lên). */
function put(file: File, t: Ticket, onProgress: (p: number) => void, signal?: AbortSignal) {
  return new Promise<void>((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('PUT', t.putUrl);
    Object.entries(t.headers ?? {}).forEach(([k, v]) => xhr.setRequestHeader(k, v));
    xhr.upload.onprogress = e => e.lengthComputable && onProgress(Math.round((e.loaded / e.total) * 100));
    xhr.onload = () => (xhr.status >= 200 && xhr.status < 300
      ? resolve()
      : reject(new ApiError(`Cloudflare R2 từ chối file (${xhr.status}).`, xhr.status)));
    xhr.onerror = () => reject(new ApiError('Mất kết nối khi đang tải file lên R2.', 0));
    xhr.onabort = () => reject(new ApiError('Đã hủy tải lên.', 0));
    signal?.addEventListener('abort', () => xhr.abort());
    xhr.send(file);
  });
}

/** Xin chỗ trên R2 → PUT file → ghi vào danh mục. 503 nghĩa là server chưa cấu hình R2. */
export async function uploadAsset(
  lessonId: number, file: File, kind: AssetKind, onProgress: (p: number) => void, signal?: AbortSignal,
) {
  const type = file.type || 'application/octet-stream';
  const ticket = await call<Ticket>('?upload', json('POST', { lessonId, name: file.name, kind, size: file.size, type }));
  await put(file, ticket, onProgress, signal);
  const r = await call<{ asset: Asset }>('?asset', json('POST', {
    lessonId, kind, name: file.name, size: file.size, url: ticket.publicUrl, storage: 'r2', key: ticket.key,
  }));
  return r.asset;
}
