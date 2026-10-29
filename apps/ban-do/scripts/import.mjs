/**
 * Nhập dữ liệu đang có vào hai bảng provinces/trips. Chạy lại bao nhiêu lần cũng được:
 * chỉ thêm cái còn thiếu, không đụng tới cái đã nằm trong database.
 *
 *   npm -w apps/ban-do run db:import              # cả hai nguồn
 *   npm -w apps/ban-do run db:import -- --dry     # chỉ xem sẽ làm gì
 *   npm -w apps/ban-do run db:import -- --seed    # chỉ hai chuyến trong travel/
 *   npm -w apps/ban-do run db:import -- --file ../../sao-luu.json
 *
 * Hai nguồn:
 *   seed  src/lib/seed.ts — hai chuyến 3–11/10/2026 rút từ sổ tay travel/.
 *   docs  bản ghi 'da-di-qua-v1' mà app cũ đồng bộ lên (bảng docs trong cùng database),
 *         hoặc một file JSON cùng dạng qua --file. Dạng của nó là
 *         { "ma-tinh": { status, note } }: mỗi tỉnh một trạng thái và một ghi chú.
 *         Bảng mới không có chỗ cho ghi chú theo tỉnh, nên ghi chú thành một chuyến
 *         chưa rõ ngày — chữ giữ nguyên, vẫn sửa và xoá được như mọi chuyến khác.
 *
 * DATABASE_URL lấy từ biến môi trường, hoặc .env.local ở gốc repo.
 */
import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import pg from 'pg';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(here, '..', '..', '..');

function databaseUrl() {
  if (process.env.DATABASE_URL) return process.env.DATABASE_URL;
  const file = path.join(root, '.env.local');
  if (!existsSync(file)) return '';
  for (const line of readFileSync(file, 'utf8').split('\n')) {
    const m = line.match(/^\s*DATABASE_URL\s*=\s*(.*?)\s*$/);
    if (m) return m[1].replace(/^(['"])(.*)\1$/, '$2');
  }
  return '';
}

const args = process.argv.slice(2);
const has = f => args.includes(f);
const dry = has('--dry');
const fileAt = args.indexOf('--file');
const file = fileAt >= 0 ? args[fileAt + 1] : null;
const only = has('--seed') || has('--docs') || Boolean(file);
const wantSeed = !only || has('--seed');
const wantDocs = !only || has('--docs') || Boolean(file);

const url = databaseUrl();
if (!url) {
  console.error('Chưa có DATABASE_URL. Đặt biến môi trường hoặc điền vào .env.local ở gốc repo.');
  process.exit(1);
}

// seed.ts là TypeScript nhưng chỉ chứa dữ liệu, bóc phần object ra là dùng được
const seedSrc = readFileSync(path.join(here, '..', 'src', 'lib', 'seed.ts'), 'utf8');
const seed = new Function(`${seedSrc.replace(/^import[^;]+;/m, '').replace('export const seed: Entries =', 'return')}`)();

const names = Object.fromEntries(
  JSON.parse(readFileSync(path.join(here, '..', 'src', 'data', 'provinces.json'), 'utf8'))
    .provinces.map(p => [p.code, p.name]),
);

const client = new pg.Client({
  connectionString: url,
  ssl: /sslmode=require|neon\.tech/.test(url) ? { rejectUnauthorized: true } : false,
});

const added = { provinces: 0, trips: 0 };
const skipped = { provinces: 0, trips: 0, unknown: [] };

async function keepProvince(code, status) {
  const r = await client.query('SELECT 1 FROM provinces WHERE code = $1', [code]);
  if (r.rowCount) { skipped.provinces++; return; }
  console.log(`  + tỉnh ${names[code]} → ${status}`);
  added.provinces++;
  if (!dry) await client.query('INSERT INTO provinces (code, status) VALUES ($1, $2)', [code, status]);
}

/** Trùng khoảng ngày, hoặc (với chuyến chưa rõ ngày) trùng ghi chú, thì coi như đã có. */
async function tripExists(code, from, to, note) {
  const r = from
    ? await client.query(
        `SELECT 1 FROM trips WHERE province_code = $1 AND from_date = $2
           AND to_date IS NOT DISTINCT FROM $3`, [code, from, to || null])
    : await client.query(
        'SELECT 1 FROM trips WHERE province_code = $1 AND from_date IS NULL AND note = $2', [code, note]);
  return r.rowCount > 0;
}

async function keepTrip(code, t) {
  if (await tripExists(code, t.from, t.to, t.note)) { skipped.trips++; return; }
  console.log(`  + chuyến ${names[code]} ${t.from || '(chưa rõ ngày)'}${t.to ? `–${t.to}` : ''}`);
  added.trips++;
  if (dry) return;
  await client.query(
    `INSERT INTO trips (province_code, from_date, to_date, companions, rate, places, note)
     VALUES ($1, $2, $3, $4, $5, $6::jsonb, $7)`,
    [code, t.from || null, t.to || null, t.with, t.rate, JSON.stringify(t.places), t.note],
  );
}

/** Bản ghi cũ: { "ma-tinh": { status, note } }. */
async function importDocs(data) {
  if (!data || typeof data !== 'object') return;
  for (const [code, raw] of Object.entries(data)) {
    if (!names[code]) { skipped.unknown.push(code); continue; }
    const status = raw?.status === 'visited' || raw?.status === 'wish' ? raw.status : 'none';
    const note = typeof raw?.note === 'string' ? raw.note.trim() : '';
    if (status === 'none' && !note) continue;
    await keepProvince(code, status);
    if (note) await keepTrip(code, { from: '', to: '', with: '', rate: 0, places: [], note });
  }
}

await client.connect();
try {
  console.log(`Database: ${new URL(url).host}${dry ? '  (--dry, không ghi gì)' : ''}\n`);

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
      // chưa từng bấm Đồng bộ thì bảng docs còn chưa có
      const r = await client.query("SELECT data FROM docs WHERE key = 'da-di-qua-v1'").catch(() => null);
      if (!r?.rowCount) console.log('  (không thấy, bỏ qua)');
      else await importDocs(r.rows[0].data);
    }
  }

  console.log(
    `\nThêm ${added.provinces} tỉnh, ${added.trips} chuyến.` +
    ` Bỏ qua vì đã có: ${skipped.provinces} tỉnh, ${skipped.trips} chuyến.`,
  );
  if (skipped.unknown.length) {
    console.log(`Không nhận ra mã tỉnh: ${skipped.unknown.join(', ')} (tên tỉnh đổi từ 1/7/2025?)`);
  }
} finally {
  await client.end();
}
