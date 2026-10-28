import { byCode } from './map-data';
import type { Status, TripDraft } from './types';

export type Checked<T> = { ok: true; value: T } | { ok: false; error: string };

const MAX_PLACES = 120;
const MAX_PLACE = 120;
const MAX_WITH = 200;
const MAX_NOTE = 8000;
const STATUSES: Status[] = ['none', 'visited', 'wish'];

const text = (v: unknown, limit: number) =>
  typeof v === 'string' ? v.trim().slice(0, limit) : '';

/** '' (chưa rõ ngày) hoặc đúng một ngày có thật dạng YYYY-MM-DD. */
function day(v: unknown): string | null {
  if (typeof v !== 'string' || !v) return '';
  if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) return null;
  const d = new Date(`${v}T00:00:00Z`);
  return Number.isNaN(+d) || d.toISOString().slice(0, 10) !== v ? null : v;
}

export function checkCode(code: unknown): Checked<string> {
  return typeof code === 'string' && byCode[code]
    ? { ok: true, value: code }
    : { ok: false, error: 'Không tìm thấy tỉnh này.' };
}

export function checkStatus(status: unknown): Checked<Status> {
  return STATUSES.includes(status as Status)
    ? { ok: true, value: status as Status }
    : { ok: false, error: 'Trạng thái không hợp lệ.' };
}

/**
 * Server action là một đầu vào công khai, nên dữ liệu từ form phải soát lại ở đây
 * chứ không tin phía trình duyệt đã soát rồi.
 */
export function checkDraft(input: unknown): Checked<TripDraft> {
  if (!input || typeof input !== 'object') return { ok: false, error: 'Không đọc được dữ liệu chuyến.' };
  const raw = input as Record<string, unknown>;

  const from = day(raw.from);
  const to = day(raw.to);
  if (from === null || to === null) return { ok: false, error: 'Ngày không hợp lệ.' };
  if (from && to && to < from) return { ok: false, error: 'Ngày về trước ngày đi.' };

  const rate = Number(raw.rate);
  if (!Number.isInteger(rate) || rate < 0 || rate > 5) return { ok: false, error: 'Số sao không hợp lệ.' };

  if (!Array.isArray(raw.places)) return { ok: false, error: 'Không đọc được danh sách địa điểm.' };
  const places = raw.places
    .map(p => text(p, MAX_PLACE))
    .filter(Boolean)
    .slice(0, MAX_PLACES);

  return {
    ok: true,
    value: { from, to, with: text(raw.with, MAX_WITH), rate, places, note: text(raw.note, MAX_NOTE) },
  };
}
