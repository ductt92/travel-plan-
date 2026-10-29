'use server';

import { canSignIn, endSession, passwordOk, startSession } from '@/lib/auth';
import type { ActionResult } from '@/lib/types';

/** Đoán sai thì chờ một nhịp, dò mật khẩu bằng máy sẽ chậm hẳn đi. */
const slowDown = () => new Promise(r => setTimeout(r, 400));

export async function signInAction(pass: unknown): Promise<ActionResult> {
  if (!canSignIn()) return { ok: false, error: 'Server chưa cấu hình APP_SECRET.' };
  if (typeof pass !== 'string' || !passwordOk(pass)) {
    await slowDown();
    return { ok: false, error: 'Sai mật khẩu.' };
  }
  await startSession();
  return { ok: true, value: null };
}

export async function signOutAction(): Promise<ActionResult> {
  await endSession();
  return { ok: true, value: null };
}
