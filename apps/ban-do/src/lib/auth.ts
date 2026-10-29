import 'server-only';
import { createHmac, timingSafeEqual } from 'node:crypto';
import { cookies } from 'next/headers';
import { appSecret, hsk6Pass } from './env';

/**
 * Đăng nhập bằng mật khẩu chung, giống các trang khác trong repo: `HSK6_PASS`
 * (mật khẩu của Ngọc) hoặc `APP_SECRET` (mã chung). Không có bảng người dùng —
 * hai đứa dùng chung một mã, nên phiên chỉ là một cookie đã ký.
 */
const COOKIE = 'ban-do-phien';
const DAYS = 30;

/** So sánh thời gian hằng, để không đoán được mật khẩu qua thời gian phản hồi. */
function same(a: string | undefined, b: string | undefined) {
  const x = Buffer.from(a ?? '');
  const y = Buffer.from(b ?? '');
  return x.length > 0 && x.length === y.length && timingSafeEqual(x, y);
}

export const passwordOk = (pass: string) =>
  same(pass, hsk6Pass()) || same(pass, appSecret());

/** Cookie ký bằng APP_SECRET nên không cần lưu phiên ở đâu cả. */
const sign = (payload: string) =>
  createHmac('sha256', appSecret() ?? '').update(payload).digest('base64url');

/** Thiếu APP_SECRET thì không ký được, coi như trang chỉ để xem. */
export const canSignIn = () => Boolean(appSecret());

export async function startSession() {
  const until = String(Date.now() + DAYS * 86_400_000);
  (await cookies()).set(COOKIE, `${until}.${sign(until)}`, {
    httpOnly: true,
    sameSite: 'lax',
    secure: process.env.NODE_ENV === 'production',
    // app sống ở /ban-do nên cookie cũng chỉ gửi kèm trong phạm vi đó
    path: '/ban-do',
    maxAge: DAYS * 86_400,
  });
}

export async function endSession() {
  (await cookies()).delete({ name: COOKIE, path: '/ban-do' });
}

export async function signedIn() {
  if (!canSignIn()) return false;
  const raw = (await cookies()).get(COOKIE)?.value;
  if (!raw) return false;
  const [until, mac] = raw.split('.');
  if (!until || !mac || !same(mac, sign(until))) return false;
  return Number(until) > Date.now();
}
