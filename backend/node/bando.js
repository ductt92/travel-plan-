// Nhật ký chuyến đi của trang bản đồ (apps/ban-do). Bản Go: backend/go/bando.go, cùng hợp đồng.
//
// GET    /api/<node|go>/ban-do               → { entries: { "<mã tỉnh>": { status, trips: [...] } } }
// GET    /api/<node|go>/ban-do?check         → kiểm mật khẩu, không đụng cơ sở dữ liệu
// PUT    …?province=<mã>        {status}     → đặt trạng thái tỉnh
// POST   …?province=<mã>        {chuyến}     → thêm chuyến, trả về chuyến vừa tạo (có id thật)
// PATCH  …?province=<mã>&id=<n> {chuyến}     → sửa chuyến, trả về chuyến sau khi sửa
// DELETE …?province=<mã>&id=<n>              → xoá chuyến
//
// GET ai đọc cũng được (trang này nối công khai từ trang chủ); mọi thao tác ghi cần mật khẩu
// APP_SECRET hoặc HSK6_PASS gửi qua header X-App-Secret, giống /terms.
import { authorizedHsk6, db, fail, readJson, send } from './common.js';

const TABLES = `
DO $$ BEGIN
  CREATE TYPE province_status AS ENUM ('none', 'visited', 'wish');
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;
CREATE TABLE IF NOT EXISTS provinces (
  code       text PRIMARY KEY,
  status     province_status NOT NULL DEFAULT 'none',
  updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS trips (
  id            serial PRIMARY KEY,
  province_code text NOT NULL REFERENCES provinces(code) ON DELETE CASCADE,
  from_date     date,
  to_date       date,
  companions    text NOT NULL DEFAULT '',
  rate          integer NOT NULL DEFAULT 0,
  places        jsonb NOT NULL DEFAULT '[]'::jsonb,
  note          text NOT NULL DEFAULT '',
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS trips_province_idx ON trips (province_code);
CREATE INDEX IF NOT EXISTS trips_from_idx     ON trips (from_date);
`;

let ready = null;
async function pool() {
  const p = await db();
  ready ??= p.query(TABLES).catch(e => { ready = null; throw e; });
  await ready;
  return p;
}

const STATUSES = ['none', 'visited', 'wish'];
const CODE_RE = /^[a-z][a-z0-9-]{1,39}$/;
const MAX_PLACES = 120;
const MAX_PLACE = 120;
const MAX_WITH = 200;
const MAX_NOTE = 8000;

const text = (v, limit) => (typeof v === 'string' ? v.trim().slice(0, limit) : '');

/** '' (chưa rõ ngày) → null, còn lại phải là một ngày có thật dạng YYYY-MM-DD. */
function day(v) {
  if (v === undefined || v === null || v === '') return null;
  if (typeof v !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(v)) return undefined;
  const d = new Date(`${v}T00:00:00Z`);
  return Number.isNaN(+d) || d.toISOString().slice(0, 10) !== v ? undefined : v;
}

/** Trả về { trip } hoặc { error }. Soát lại ở đây chứ không tin phía trình duyệt. */
function checkTrip(body) {
  if (!body || typeof body !== 'object') return { error: 'dữ liệu chuyến không đọc được' };
  const from = day(body.from);
  const to = day(body.to);
  if (from === undefined || to === undefined) return { error: 'ngày không hợp lệ' };
  if (from && to && to < from) return { error: 'ngày về trước ngày đi' };

  const rate = Number(body.rate ?? 0);
  if (!Number.isInteger(rate) || rate < 0 || rate > 5) return { error: 'số sao không hợp lệ' };

  if (!Array.isArray(body.places)) return { error: 'danh sách địa điểm không đọc được' };
  const places = body.places.map(p => text(p, MAX_PLACE)).filter(Boolean).slice(0, MAX_PLACES);

  return {
    trip: { from, to, with: text(body.with, MAX_WITH), rate, places, note: text(body.note, MAX_NOTE) },
  };
}

// from_date/to_date ép sang text ngay trong câu lệnh: để pg tự dịch kiểu date thành
// Date của JavaScript là ngày trôi mất một hôm theo múi giờ máy chủ
const TRIP_COLS = `id, province_code, from_date::text AS from_date, to_date::text AS to_date,
                   companions, rate, places, note`;

const toTrip = r => ({
  id: r.id,
  from: r.from_date ?? '',
  to: r.to_date ?? '',
  with: r.companions,
  rate: r.rate,
  places: r.places,
  note: r.note,
});

async function readAll(p) {
  const [provinces, trips] = await Promise.all([
    p.query('SELECT code, status FROM provinces'),
    p.query(`SELECT ${TRIP_COLS} FROM trips ORDER BY from_date ASC NULLS LAST, id ASC`),
  ]);
  const entries = {};
  for (const r of provinces.rows) entries[r.code] = { status: r.status, trips: [] };
  for (const r of trips.rows) (entries[r.province_code] ??= { status: 'none', trips: [] }).trips.push(toTrip(r));
  return entries;
}

export default async function banDo(req, res) {
  const url = new URL(req.url, 'http://localhost');
  const method = req.method;

  if (!['GET', 'PUT', 'POST', 'PATCH', 'DELETE'].includes(method)) {
    res.setHeader('Allow', 'GET, PUT, POST, PATCH, DELETE');
    return fail(res, 405, 'chỉ hỗ trợ GET, PUT, POST, PATCH và DELETE');
  }

  // trang bấm Đăng nhập thì hỏi đúng câu này, chưa cần tới cơ sở dữ liệu
  if (method === 'GET' && url.searchParams.has('check'))
    return authorizedHsk6(req) ? send(res, 200, { ok: true }) : fail(res, 401, 'sai mật khẩu');

  if (method !== 'GET' && !authorizedHsk6(req)) return fail(res, 401, 'sai mật khẩu');

  let p;
  try { p = await pool(); } catch { return fail(res, 503, 'không kết nối được cơ sở dữ liệu'); }

  if (method === 'GET') {
    try { return send(res, 200, { entries: await readAll(p) }); }
    catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
  }

  const code = url.searchParams.get('province') || '';
  if (!CODE_RE.test(code)) return fail(res, 400, 'cần ?province=<mã tỉnh>');

  if (method === 'DELETE') {
    const id = Number(url.searchParams.get('id'));
    if (!Number.isInteger(id) || id <= 0) return fail(res, 400, 'cần ?id=<số>');
    try {
      // kèm mã tỉnh để id gửi bừa không xoá nhầm chuyến của tỉnh khác
      const r = await p.query('DELETE FROM trips WHERE id = $1 AND province_code = $2', [id, code]);
      return r.rowCount ? send(res, 200, { ok: true }) : fail(res, 404, 'không còn chuyến này nữa');
    } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
  }

  let body;
  try { body = await readJson(req, 1 << 20); } catch { return fail(res, 400, 'dữ liệu không hợp lệ hoặc quá lớn'); }

  if (method === 'PUT') {
    const status = body?.status;
    if (!STATUSES.includes(status)) return fail(res, 400, 'trạng thái không hợp lệ');
    try {
      await p.query(
        `INSERT INTO provinces (code, status) VALUES ($1, $2)
         ON CONFLICT (code) DO UPDATE SET status = EXCLUDED.status, updated_at = now()`,
        [code, status],
      );
      return send(res, 200, { ok: true });
    } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
  }

  const { trip, error } = checkTrip(body);
  if (error) return fail(res, 400, error);

  if (method === 'POST') {
    const client = await p.connect();
    try {
      await client.query('BEGIN');
      // ghi chuyến đầu tiên là tỉnh thành "đã đi" luôn, và trips cần dòng tỉnh có sẵn
      await client.query(
        `INSERT INTO provinces (code, status) VALUES ($1, 'visited')
         ON CONFLICT (code) DO UPDATE SET status = 'visited', updated_at = now()`,
        [code],
      );
      const r = await client.query(
        `INSERT INTO trips (province_code, from_date, to_date, companions, rate, places, note)
         VALUES ($1, $2, $3, $4, $5, $6::jsonb, $7) RETURNING ${TRIP_COLS}`,
        [code, trip.from, trip.to, trip.with, trip.rate, JSON.stringify(trip.places), trip.note],
      );
      await client.query('COMMIT');
      return send(res, 200, { trip: toTrip(r.rows[0]) });
    } catch {
      await client.query('ROLLBACK').catch(() => {});
      return fail(res, 500, 'lỗi ghi dữ liệu');
    } finally {
      client.release();
    }
  }

  const id = Number(url.searchParams.get('id'));
  if (!Number.isInteger(id) || id <= 0) return fail(res, 400, 'cần ?id=<số>');
  try {
    const r = await p.query(
      `UPDATE trips SET from_date = $3, to_date = $4, companions = $5, rate = $6,
                        places = $7::jsonb, note = $8, updated_at = now()
       WHERE id = $1 AND province_code = $2 RETURNING ${TRIP_COLS}`,
      [id, code, trip.from, trip.to, trip.with, trip.rate, JSON.stringify(trip.places), trip.note],
    );
    return r.rowCount ? send(res, 200, { trip: toTrip(r.rows[0]) }) : fail(res, 404, 'không còn chuyến này nữa');
  } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
}
