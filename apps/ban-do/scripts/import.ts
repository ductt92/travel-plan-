/**
 * Nhập dữ liệu đang có vào hai bảng mới. Chạy lại bao nhiêu lần cũng được: chỉ thêm
 * cái còn thiếu, không đụng tới cái đã nằm trong database.
 *
 *   npm run db:import              # cả hai nguồn dưới đây
 *   npm run db:import -- --dry     # chỉ xem sẽ làm gì
 *   npm run db:import -- --seed    # chỉ hai chuyến trong travel/
 *   npm run db:import -- --docs    # chỉ bản ghi cũ của app Vite
 *   npm run db:import -- --file ../../sao-luu.json
 *
 * Hai nguồn:
 *   seed  src/lib/seed.ts — hai chuyến 3–11/10/2026 rút từ sổ tay travel/.
 *   docs  bản ghi 'da-di-qua-v1' mà app Vite cũ đồng bộ lên (bảng docs trong cùng
 *         database), hoặc một file JSON cùng dạng qua --file. Dạng của nó là
 *         { "ma-tinh": { status, note } }: mỗi tỉnh một trạng thái và một ghi chú.
 *         Bảng mới không có chỗ cho ghi chú theo tỉnh, nên ghi chú thành một chuyến
 *         chưa rõ ngày — chữ giữ nguyên, vẫn sửa và xoá được như mọi chuyến khác.
 */
import { readFileSync } from 'node:fs';
import { drizzle } from 'drizzle-orm/node-postgres';
import { and, eq, isNull } from 'drizzle-orm';
import pg from 'pg';
import { databaseUrl } from '../src/lib/env';
import { provinces, trips } from '../src/db/schema';
import { byCode } from '../src/lib/map-data';
import { seed } from '../src/lib/seed';
import type { Status } from '../src/lib/types';

const args = process.argv.slice(2);
const has = (flag: string) => args.includes(flag);
const dry = has('--dry');
const fileAt = args.indexOf('--file');
const file = fileAt >= 0 ? args[fileAt + 1] : null;
// không chọn nguồn nào thì làm cả hai
const only = has('--seed') || has('--docs') || Boolean(file);
const wantSeed = !only || has('--seed');
const wantDocs = !only || has('--docs') || Boolean(file);

const url = databaseUrl();
if (!url) {
  console.error('Chưa có DATABASE_URL. Đặt trong .env.local ở gốc repo hoặc trong thư mục này.');
  process.exit(1);
}

const pool = new pg.Pool({
  connectionString: url,
  max: 2,
  ssl: /sslmode=require|neon\.tech/.test(url) ? { rejectUnauthorized: true } : false,
});
const db = drizzle(pool);

const added = { provinces: 0, trips: 0 };
const skipped = { provinces: 0, trips: 0, unknown: [] as string[] };

/** Thêm dòng tỉnh nếu chưa có. Đã có thì để nguyên, không đè trạng thái người dùng đặt sau này. */
async function keepProvince(code: string, status: Status) {
  const [row] = await db.select().from(provinces).where(eq(provinces.code, code));
  if (row) {
    skipped.provinces++;
    return;
  }
  console.log(`  + tỉnh ${byCode[code].name} → ${status}`);
  added.provinces++;
  if (!dry) await db.insert(provinces).values({ code, status });
}

/** Có chuyến nào của tỉnh này trùng khoảng ngày (hoặc trùng ghi chú, với chuyến chưa rõ ngày) chưa. */
async function tripExists(code: string, from: string, to: string, note: string) {
  const rows = await db.select().from(trips).where(
    from
      ? and(eq(trips.provinceCode, code), eq(trips.fromDate, from), to ? eq(trips.toDate, to) : isNull(trips.toDate))
      : and(eq(trips.provinceCode, code), isNull(trips.fromDate), eq(trips.note, note)),
  );
  return rows.length > 0;
}

async function keepTrip(code: string, t: {
  from: string; to: string; with: string; rate: number; places: string[]; note: string;
}) {
  if (await tripExists(code, t.from, t.to, t.note)) {
    skipped.trips++;
    return;
  }
  console.log(`  + chuyến ${byCode[code].name} ${t.from || '(chưa rõ ngày)'}${t.to ? `–${t.to}` : ''}`);
  added.trips++;
  if (dry) return;
  await db.insert(trips).values({
    provinceCode: code,
    fromDate: t.from || null,
    toDate: t.to || null,
    companions: t.with,
    rate: t.rate,
    places: t.places,
    note: t.note,
  });
}

/** Bản ghi cũ: { "ma-tinh": { status, note } }. */
async function importDocs(data: unknown) {
  if (!data || typeof data !== 'object') return;
  for (const [code, raw] of Object.entries(data as Record<string, unknown>)) {
    if (!byCode[code]) {
      skipped.unknown.push(code);
      continue;
    }
    const entry = (raw ?? {}) as { status?: unknown; note?: unknown };
    const status: Status = entry.status === 'visited' || entry.status === 'wish' ? entry.status : 'none';
    const note = typeof entry.note === 'string' ? entry.note.trim() : '';
    if (status === 'none' && !note) continue;

    await keepProvince(code, status);
    if (note) await keepTrip(code, { from: '', to: '', with: '', rate: 0, places: [], note });
  }
}

async function main() {
  console.log(`Database: ${new URL(url!).host}${dry ? '  (--dry, không ghi gì)' : ''}\n`);

  if (wantSeed) {
    console.log('Từ src/lib/seed.ts:');
    for (const [code, entry] of Object.entries(seed)) {
      await keepProvince(code, entry.status);
      for (const t of entry.trips) await keepTrip(code, t);
    }
  }

  if (wantDocs) {
    console.log('\nTừ bản ghi cũ da-di-qua-v1:');
    if (file) {
      await importDocs(JSON.parse(readFileSync(file, 'utf8')));
    } else {
      const res = await pool
        .query("SELECT data FROM docs WHERE key = 'da-di-qua-v1'")
        .catch(() => null);   // chưa từng bấm Đồng bộ thì bảng docs còn chưa có
      if (!res?.rows.length) console.log('  (không thấy, bỏ qua)');
      else await importDocs(res.rows[0].data);
    }
  }

  console.log(
    `\nThêm ${added.provinces} tỉnh, ${added.trips} chuyến.` +
    ` Bỏ qua vì đã có: ${skipped.provinces} tỉnh, ${skipped.trips} chuyến.`,
  );
  if (skipped.unknown.length) {
    console.log(`Không nhận ra mã tỉnh: ${skipped.unknown.join(', ')} (tên tỉnh đổi từ 1/7/2025?)`);
  }
}

main()
  .catch(err => {
    console.error('\nHỏng:', err instanceof Error ? err.message : err);
    process.exitCode = 1;
  })
  .finally(() => pool.end());
