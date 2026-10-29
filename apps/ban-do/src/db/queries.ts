import 'server-only';
import { asc } from 'drizzle-orm';
import { db } from './client';
import { provinces, trips, type TripRow } from './schema';
import type { Entries, Trip } from '@/lib/types';

/** Dòng trong bảng → kiểu Trip mà giao diện dùng. */
export const toTrip = (r: TripRow): Trip => ({
  id: r.id,
  from: r.fromDate ?? '',
  to: r.toDate ?? '',
  with: r.companions,
  rate: r.rate,
  places: r.places,
  note: r.note,
});

/** Cả nhật ký, gom theo tỉnh. Hai câu truy vấn rồi ghép ở đây cho khỏi join. */
export async function loadEntries(): Promise<Entries> {
  const d = db();
  const [provinceRows, tripRows] = await Promise.all([
    d.select().from(provinces),
    d.select().from(trips).orderBy(asc(trips.fromDate), asc(trips.id)),
  ]);

  const out: Entries = {};
  for (const p of provinceRows) out[p.code] = { status: p.status, trips: [] };
  for (const t of tripRows) {
    (out[t.provinceCode] ??= { status: 'none', trips: [] }).trips.push(toTrip(t));
  }
  return out;
}
