import { pad } from './format';
import type { Entries, Period, Trip } from './types';

/** '2026-10-04' → '2026-10' */
const ym = (s: string) => (s ? s.slice(0, 7) : '');

/**
 * Chuyến có nằm trong khoảng đang chọn không. So trên cả from…to nên chuyến vắt
 * qua hai tháng (hay hai năm) hiện ở cả hai bên chứ không rơi mất.
 */
export function inPeriod(t: Trip, { year, month }: Period) {
  if (!year) return true;
  const a = ym(t.from);
  if (!a) return false;
  const b = ym(t.to) || a;
  if (!month) return +a.slice(0, 4) <= year && year <= +b.slice(0, 4);
  const k = `${year}-${pad(month)}`;
  return a <= k && k <= b;
}

export const tripsIn = (entries: Entries, code: string, period: Period) =>
  (entries[code]?.trips ?? []).filter(t => inPeriod(t, period));

export const allYears = (entries: Entries) =>
  [...new Set(Object.values(entries).flatMap(e => e.trips.map(t => (t.from ? +t.from.slice(0, 4) : 0))).filter(Boolean))]
    .sort((a, b) => b - a);

/** Mọi tháng 'YYYY-MM' có chuyến, để chấm dấu trong bộ chọn. */
export function tripMonths(entries: Entries) {
  const set = new Set<string>();
  for (const e of Object.values(entries))
    for (const t of e.trips) {
      const a = ym(t.from);
      if (!a) continue;
      const b = ym(t.to) || a;
      for (let y = +a.slice(0, 4); y <= +b.slice(0, 4); y++)
        for (let m = 1; m <= 12; m++) {
          const k = `${y}-${pad(m)}`;
          if (k >= a && k <= b) set.add(k);
        }
    }
  return set;
}

/** Số chuyến rơi vào một năm, dùng cho dòng chú trong bộ chọn. */
export const tripsOfYear = (entries: Entries, y: number) =>
  Object.values(entries).reduce(
    (n, e) => n + e.trips.filter(t => inPeriod(t, { year: y, month: null })).length,
    0,
  );

export const scopeLabel = ({ year, month }: Period) =>
  !year ? null : month ? `tháng ${month}/${year}` : `năm ${year}`;

export const scopeShort = ({ year, month }: Period) =>
  !year ? '' : month ? `${pad(month)}/${year}` : String(year);
