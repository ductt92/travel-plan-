'use server';

import { and, eq } from 'drizzle-orm';
import { db } from '@/db/client';
import { toTrip } from '@/db/queries';
import { provinces, trips } from '@/db/schema';
import { signedIn } from '@/lib/auth';
import { checkCode, checkDraft, checkStatus } from '@/lib/validate';
// mọi export của file 'use server' phải là hàm async, nên kiểu trả về để ở lib/types
import type { ActionResult, Trip } from '@/lib/types';

/**
 * Lỗi thật ghi ra log của server, người dùng chỉ thấy một câu gọn. Chuỗi kết nối
 * hay câu SQL hỏng không nên chạy ngược về trình duyệt.
 */
/**
 * Server action là đầu vào công khai: ai cũng gọi thẳng được, không qua giao diện.
 * Nên mọi thao tác ghi đều hỏi lại cookie phiên ở đây, giấu nút trên màn hình thôi
 * thì chưa chặn được gì.
 */
async function denied(): Promise<ActionResult<never> | null> {
  return (await signedIn())
    ? null
    : { ok: false, error: 'Chưa đăng nhập, hoặc phiên đã hết hạn. Đăng nhập lại nhé.' };
}

function failed(where: string, err: unknown): ActionResult<never> {
  console.error(`[ban-do] ${where}`, err);
  return { ok: false, error: 'Chưa lưu được xuống database. Thử lại nhé.' };
}

export async function setStatusAction(rawCode: string, rawStatus: string): Promise<ActionResult> {
  const no = await denied();
  if (no) return no;

  const code = checkCode(rawCode);
  if (!code.ok) return code;
  const status = checkStatus(rawStatus);
  if (!status.ok) return status;

  try {
    await db()
      .insert(provinces)
      .values({ code: code.value, status: status.value })
      .onConflictDoUpdate({
        target: provinces.code,
        set: { status: status.value, updatedAt: new Date() },
      });
    return { ok: true, value: null };
  } catch (err) {
    return failed('setStatus', err);
  }
}

export async function addTripAction(rawCode: string, rawDraft: unknown): Promise<ActionResult<Trip>> {
  const no = await denied();
  if (no) return no;

  const code = checkCode(rawCode);
  if (!code.ok) return code;
  const draft = checkDraft(rawDraft);
  if (!draft.ok) return draft;

  try {
    return await db().transaction(async tx => {
      // ghi chuyến đầu tiên là tỉnh thành "đã đi" luôn, và trips cần dòng tỉnh có sẵn
      await tx
        .insert(provinces)
        .values({ code: code.value, status: 'visited' })
        .onConflictDoUpdate({ target: provinces.code, set: { status: 'visited', updatedAt: new Date() } });

      const [row] = await tx
        .insert(trips)
        .values({
          provinceCode: code.value,
          fromDate: draft.value.from || null,
          toDate: draft.value.to || null,
          companions: draft.value.with,
          rate: draft.value.rate,
          places: draft.value.places,
          note: draft.value.note,
        })
        .returning();
      return { ok: true as const, value: toTrip(row) };
    });
  } catch (err) {
    return failed('addTrip', err);
  }
}

export async function updateTripAction(
  rawCode: string,
  id: number,
  rawDraft: unknown,
): Promise<ActionResult<Trip>> {
  const no = await denied();
  if (no) return no;

  const code = checkCode(rawCode);
  if (!code.ok) return code;
  const draft = checkDraft(rawDraft);
  if (!draft.ok) return draft;
  if (!Number.isInteger(id)) return { ok: false, error: 'Không tìm thấy chuyến này.' };

  try {
    const [row] = await db()
      .update(trips)
      .set({
        fromDate: draft.value.from || null,
        toDate: draft.value.to || null,
        companions: draft.value.with,
        rate: draft.value.rate,
        places: draft.value.places,
        note: draft.value.note,
        updatedAt: new Date(),
      })
      // kèm mã tỉnh để không sửa nhầm chuyến của tỉnh khác khi id bị gửi bừa
      .where(and(eq(trips.id, id), eq(trips.provinceCode, code.value)))
      .returning();

    if (!row) return { ok: false, error: 'Chuyến này không còn nữa — có thể đã xoá ở máy khác.' };
    return { ok: true, value: toTrip(row) };
  } catch (err) {
    return failed('updateTrip', err);
  }
}

export async function removeTripAction(rawCode: string, id: number): Promise<ActionResult> {
  const no = await denied();
  if (no) return no;

  const code = checkCode(rawCode);
  if (!code.ok) return code;
  if (!Number.isInteger(id)) return { ok: false, error: 'Không tìm thấy chuyến này.' };

  try {
    await db().delete(trips).where(and(eq(trips.id, id), eq(trips.provinceCode, code.value)));
    return { ok: true, value: null };
  } catch (err) {
    return failed('removeTrip', err);
  }
}
