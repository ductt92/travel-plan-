// Danh mục khóa học cho trang quản lý (apps/quan-ly). Bản Go: backend/go/catalog.go, cùng hợp đồng.
//
// Cơ sở dữ liệu chỉ giữ danh mục (khóa → bài → file); file thật nằm trong repo (storage 'repo'),
// trên Cloudflare R2 ('r2', trình duyệt tải thẳng lên bằng URL ký sẵn) hoặc là link YouTube ('youtube').
//
// GET    /api/<node|go>/quan-ly            → { courses, usage, r2 }
// GET    …?check                           → kiểm mật khẩu, không đụng cơ sở dữ liệu
// POST   …?course  | PATCH/DELETE …?course=<id>
// POST   …?lesson  | PATCH/DELETE …?lesson=<id>
// POST   …?upload  {lessonId,name,kind,size,type} → URL PUT ký sẵn lên R2 (15 phút)
// POST   …?asset   | DELETE …?asset=<id>   (file R2 thì xoá trên R2 trước)
// POST   …?import  {courses:[…]}           → ghi gộp cả danh mục (scripts/seed-catalog.mjs)
//
// Mọi request cần APP_SECRET qua header X-App-Secret (không nhận HSK6_PASS).
// Biến môi trường R2: R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET, R2_PUBLIC_URL.
import { createHash, createHmac } from 'node:crypto';
import { authorized, db, fail, readJson, send } from './common.js';

const TABLES = `
CREATE TABLE IF NOT EXISTS catalog_courses (
  id         serial PRIMARY KEY,
  slug       text UNIQUE NOT NULL,
  title      text NOT NULL,
  sort       integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS catalog_lessons (
  id        serial PRIMARY KEY,
  course_id integer NOT NULL REFERENCES catalog_courses ON DELETE CASCADE,
  num       integer NOT NULL,
  title     text NOT NULL,
  zh        text NOT NULL DEFAULT '',
  visible   boolean NOT NULL DEFAULT true,
  sort      integer NOT NULL DEFAULT 0,
  UNIQUE (course_id, num)
);
CREATE TABLE IF NOT EXISTS catalog_assets (
  id         serial PRIMARY KEY,
  lesson_id  integer NOT NULL REFERENCES catalog_lessons ON DELETE CASCADE,
  kind       text NOT NULL CHECK (kind IN ('video', 'slides', 'audio', 'pdf', 'other')),
  name       text NOT NULL,
  size       bigint NOT NULL DEFAULT 0,
  url        text NOT NULL DEFAULT '',
  storage    text NOT NULL CONSTRAINT catalog_assets_storage_check CHECK (storage IN ('repo', 'r2', 'youtube')),
  key        text NOT NULL DEFAULT '',
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS catalog_assets_lesson_idx ON catalog_assets (lesson_id);
DO $$ BEGIN
  -- bảng tạo trước khi có 'youtube' thì nới ràng buộc, chỉ một lần
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conrelid = 'catalog_assets'::regclass
                 AND conname = 'catalog_assets_storage_check' AND pg_get_constraintdef(oid) LIKE '%youtube%') THEN
    ALTER TABLE catalog_assets DROP CONSTRAINT IF EXISTS catalog_assets_storage_check;
    ALTER TABLE catalog_assets ADD CONSTRAINT catalog_assets_storage_check CHECK (storage IN ('repo', 'r2', 'youtube'));
  END IF;
END $$;
`;

let ready = null;
async function pool() {
  const p = await db();
  ready ??= p.query(TABLES).catch(e => { ready = null; throw e; });
  await ready;
  return p;
}

const KINDS = ['video', 'slides', 'audio', 'pdf', 'other'];
const STORAGES = ['repo', 'r2', 'youtube'];
const SLUG_RE = /^[a-z0-9][a-z0-9-]{0,39}$/;
const TYPE_RE = /^[\w.+-]+\/[\w.+-]+$/;
const YT_RE = /^(?:https?:\/\/)?(?:(?:www\.|m\.)?youtube\.com\/(?:watch\?(?:[^#]*&)?v=|embed\/|shorts\/)|youtu\.be\/)([A-Za-z0-9_-]{11})(?:[?&#/].*)?$/;
const MAX_TITLE = 200;
const MAX_NAME = 200;
const MAX_URL = 2000;
const MAX_KEY = 1024;
const MAX_SORT = 1_000_000;
const MAX_NUM = 9999;
const MAX_SIZE = 2 ** 50;
const MAX_UPLOAD = 200 * 1024 * 1024;
const DB_LIMIT = 536870912;
const R2_LIMIT = 10737418240;
const R2_MISSING = 'Chưa cấu hình Cloudflare R2 (cần R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET, R2_PUBLIC_URL)';

const text = (v, limit) => (typeof v === 'string' ? v.trim().slice(0, limit) : '');
const absent = v => v === undefined || v === null;
/** Số nguyên trong [min, max]; vắng thì def, sai thì undefined. */
const int = (v, min, max, def) => (absent(v) ? def : Number.isInteger(v) && v >= min && v <= max ? v : undefined);
const pad2 = n => String(n).padStart(2, '0');
const idParam = (url, name) => {
  const v = url.searchParams.get(name) || '';
  return /^[1-9]\d{0,9}$/.test(v) && Number(v) <= 2147483647 ? Number(v) : 0;
};
const validUrl = u => u.startsWith('/') || /^https?:\/\/\S+$/.test(u);
const youtube = u => { const m = YT_RE.exec(u); return m ? `https://www.youtube.com/watch?v=${m[1]}` : ''; };

// Bỏ dấu tiếng Việt bằng bảng tay (Go không có sẵn NFD), ký tự khác ngoài [A-Za-z0-9._-] thành '-'
const VI = { a: 'àáạảãâầấậẩẫăằắặẳẵ', e: 'èéẹẻẽêềếệểễ', i: 'ìíịỉĩ', o: 'òóọỏõôồốộổỗơờớợởỡ', u: 'ùúụủũưừứựửữ', y: 'ỳýỵỷỹ', d: 'đ' };
const VI_MAP = new Map();
for (const [base, chars] of Object.entries(VI)) for (const c of chars) { VI_MAP.set(c, base); VI_MAP.set(c.toUpperCase(), base.toUpperCase()); }
export function safeName(name) {
  let s = '';
  for (const c of name) s += VI_MAP.get(c) ?? (/[A-Za-z0-9._-]/.test(c) ? c : '-');
  s = s.replace(/-+/g, '-').replace(/-*\.-*/g, '.').replace(/^[-.]+|[-.]+$/g, '').slice(0, 80).replace(/[-.]+$/, '');
  return s || 'file';
}

// ---- Cloudflare R2: chữ ký AWS SigV4 viết tay (URL ký sẵn), không cần SDK ----

const r2env = () => ({
  account: process.env.R2_ACCOUNT_ID || '', accessKey: process.env.R2_ACCESS_KEY_ID || '',
  secret: process.env.R2_SECRET_ACCESS_KEY || '', bucket: process.env.R2_BUCKET || '',
  publicUrl: (process.env.R2_PUBLIC_URL || '').replace(/\/+$/, ''),
});
const r2ready = e => !!(e.account && e.accessKey && e.secret && e.bucket && e.publicUrl);

// mã hoá kiểu RFC 3986 như AWS yêu cầu (encodeURIComponent còn chừa !'()*)
const awsEscape = s => encodeURIComponent(s).replace(/[!'()*]/g, c => '%' + c.charCodeAt(0).toString(16).toUpperCase());
const hmac = (key, data) => createHmac('sha256', key).update(data).digest();
const sha256hex = data => createHash('sha256').update(data).digest('hex');

/** URL ký sẵn SigV4 (chỉ ký header host, payload UNSIGNED-PAYLOAD). path đã gồm bucket nếu dùng path-style. */
export function presign({ method, host, path, region, accessKey, secret, date, expires }) {
  const stamp = date.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, ''); // 20130524T000000Z
  const day = stamp.slice(0, 8);
  const scope = `${day}/${region}/s3/aws4_request`;
  const query = [
    ['X-Amz-Algorithm', 'AWS4-HMAC-SHA256'], ['X-Amz-Credential', `${accessKey}/${scope}`],
    ['X-Amz-Date', stamp], ['X-Amz-Expires', String(expires)], ['X-Amz-SignedHeaders', 'host'],
  ].map(([k, v]) => `${awsEscape(k)}=${awsEscape(v)}`).sort().join('&');
  const canonPath = path.split('/').map(awsEscape).join('/');
  const canonical = [method, canonPath, query, `host:${host}\n`, 'host', 'UNSIGNED-PAYLOAD'].join('\n');
  const toSign = ['AWS4-HMAC-SHA256', stamp, scope, sha256hex(canonical)].join('\n');
  const kSigning = hmac(hmac(hmac(hmac(`AWS4${secret}`, day), region), 's3'), 'aws4_request');
  const signature = createHmac('sha256', kSigning).update(toSign).digest('hex');
  return `https://${host}${canonPath}?${query}&X-Amz-Signature=${signature}`;
}

const r2url = (e, method, key, expires) => presign({
  method, host: `${e.account}.r2.cloudflarestorage.com`, path: `/${e.bucket}/${key}`, region: 'auto',
  accessKey: e.accessKey, secret: e.secret, date: new Date(), expires,
});

/** Xoá các object trên R2; true nếu xoá được hết (404 coi như đã xoá). */
async function r2delete(e, keys) {
  for (const key of keys) {
    try {
      const r = await fetch(r2url(e, 'DELETE', key, 60), { method: 'DELETE', signal: AbortSignal.timeout(10_000) });
      if (!r.ok && r.status !== 404) return false;
    } catch { return false; }
  }
  return true;
}

// ---- đọc / ghi ----

const COURSE_COLS = 'id, slug, title, sort';
const LESSON_COLS = 'id, course_id, num, title, zh, visible, sort';
const ASSET_COLS = `id, lesson_id, kind, name, size, url, storage, key,
  to_char(created_at AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS.MS"Z"') AS created_at`;

const toCourse = r => ({ id: r.id, slug: r.slug, title: r.title, sort: r.sort });
const toLesson = r => ({ id: r.id, num: r.num, title: r.title, zh: r.zh, visible: r.visible, sort: r.sort });
// pg trả bigint dạng chuỗi; dung lượng luôn dưới 2^53 nên đổi sang số được
const toAsset = r => ({
  id: r.id, kind: r.kind, name: r.name, size: Number(r.size), url: r.url, storage: r.storage, key: r.key, createdAt: r.created_at,
});

async function readAll(p) {
  const [courses, lessons, assets, size, sums] = await Promise.all([
    p.query(`SELECT ${COURSE_COLS} FROM catalog_courses ORDER BY sort, id`),
    p.query(`SELECT ${LESSON_COLS} FROM catalog_lessons ORDER BY sort, num, id`),
    p.query(`SELECT ${ASSET_COLS} FROM catalog_assets ORDER BY kind, name, id`),
    p.query('SELECT pg_database_size(current_database())::bigint AS n'),
    p.query(`SELECT coalesce(sum(size) FILTER (WHERE storage = 'r2'), 0)::bigint   AS r2,
                    coalesce(sum(size) FILTER (WHERE storage = 'repo'), 0)::bigint AS repo,
                    count(*) FILTER (WHERE storage = 'youtube')::bigint            AS yt
             FROM catalog_assets`),
  ]);
  const byCourse = new Map(courses.rows.map(r => [r.id, { ...toCourse(r), lessons: [] }]));
  const byLesson = new Map();
  for (const r of lessons.rows) {
    const l = { ...toLesson(r), assets: [] };
    byLesson.set(r.id, l);
    byCourse.get(r.course_id)?.lessons.push(l);
  }
  for (const r of assets.rows) byLesson.get(r.lesson_id)?.assets.push(toAsset(r));
  const e = r2env();
  return {
    courses: [...byCourse.values()],
    usage: {
      dbBytes: Number(size.rows[0].n), dbLimitBytes: DB_LIMIT,
      r2Bytes: Number(sums.rows[0].r2), r2LimitBytes: R2_LIMIT,
      repoBytes: Number(sums.rows[0].repo), youtubeCount: Number(sums.rows[0].yt),
    },
    r2: { configured: r2ready(e), publicUrl: e.publicUrl },
  };
}

/** Các key R2 sẽ mất theo khi xoá khóa/bài, để xoá trên R2 trước. */
async function r2keys(p, where, id) {
  const r = await p.query(
    `SELECT a.key FROM catalog_assets a JOIN catalog_lessons l ON l.id = a.lesson_id
     WHERE a.storage = 'r2' AND a.key <> '' AND ${where} = $1`, [id]);
  return r.rows.map(x => x.key);
}

// Xoá khóa/bài: file R2 bên trong xoá trước, xoá không được thì giữ nguyên dòng
async function removeWithFiles(res, p, table, where, id, missing) {
  const keys = await r2keys(p, where, id);
  if (keys.length) {
    const e = r2env();
    if (!r2ready(e)) return fail(res, 503, R2_MISSING);
    if (!(await r2delete(e, keys))) return fail(res, 502, 'không xoá được file trên R2, chưa xoá gì, thử lại sau');
  }
  const r = await p.query(`DELETE FROM ${table} WHERE id = $1`, [id]);
  return r.rowCount ? send(res, 200, { ok: true }) : fail(res, 404, missing);
}

function checkImport(body) {
  if (!Array.isArray(body?.courses) || body.courses.length > 50) return { error: 'cần courses: [...] (tối đa 50 khóa)' };
  const out = [];
  const slugs = new Set();
  for (const [i, c] of body.courses.entries()) {
    if (!c || typeof c !== 'object') return { error: `khóa #${i + 1}: không đọc được` };
    const slug = typeof c.slug === 'string' ? c.slug.trim() : '';
    const at = `khóa ${slug || '#' + (i + 1)}`;
    if (!SLUG_RE.test(slug)) return { error: `${at}: mã khóa học chỉ gồm chữ thường, số và dấu gạch ngang` };
    if (slugs.has(slug)) return { error: `${at}: mã khóa học bị trùng` };
    slugs.add(slug);
    const title = text(c.title, MAX_TITLE);
    if (!title) return { error: `${at}: cần tên khóa học` };
    const sort = int(c.sort, -MAX_SORT, MAX_SORT, 0);
    if (sort === undefined) return { error: `${at}: thứ tự không hợp lệ` };
    if (!Array.isArray(c.lessons) || c.lessons.length > 500) return { error: `${at}: cần lessons: [...] (tối đa 500 bài)` };
    const lessons = [];
    const nums = new Set();
    for (const l of c.lessons) {
      if (!l || typeof l !== 'object') return { error: `${at}: có bài không đọc được` };
      const num = int(l.num, 0, MAX_NUM, undefined);
      if (num === undefined) return { error: `${at}: số bài không hợp lệ` };
      const atL = `${at} bài ${num}`;
      if (nums.has(num)) return { error: `${atL}: số bài bị trùng` };
      nums.add(num);
      const ltitle = text(l.title, MAX_TITLE);
      if (!ltitle) return { error: `${atL}: cần tên bài` };
      const assets = l.assets ?? [];
      if (!Array.isArray(assets) || assets.length > 50) return { error: `${atL}: assets phải là mảng (tối đa 50 file)` };
      const files = [];
      for (const a of assets) {
        if (!a || typeof a !== 'object') return { error: `${atL}: có file không đọc được` };
        if (!KINDS.includes(a.kind)) return { error: `${atL}: loại file không hợp lệ` };
        const name = text(a.name, MAX_NAME);
        if (!name) return { error: `${atL}: cần tên file` };
        const size = int(a.size, 0, MAX_SIZE, 0);
        if (size === undefined) return { error: `${atL}: dung lượng không hợp lệ` };
        const url = text(a.url, MAX_URL);
        if (!validUrl(url)) return { error: `${atL}: đường dẫn không hợp lệ` };
        files.push({ kind: a.kind, name, size, url });
      }
      lessons.push({ num, title: ltitle, zh: text(l.zh, MAX_TITLE), assets: files });
    }
    out.push({ slug, title, sort, lessons });
  }
  return { courses: out };
}

async function runImport(p, courses) {
  const c = await p.connect();
  const n = { courses: 0, lessons: 0, assets: 0 };
  try {
    await c.query('BEGIN');
    for (const course of courses) {
      const { rows: [row] } = await c.query(
        `INSERT INTO catalog_courses (slug, title, sort) VALUES ($1, $2, $3)
         ON CONFLICT (slug) DO UPDATE SET title = EXCLUDED.title, sort = EXCLUDED.sort RETURNING id`,
        [course.slug, course.title, course.sort]);
      n.courses++;
      if (!course.lessons.length) continue;
      // mỗi khóa ba câu lệnh: ghi gộp bài, xoá file 'repo' cũ của các bài đó, ghi file mới (r2, youtube giữ nguyên)
      const ls = course.lessons;
      const { rows: ids } = await c.query(
        `INSERT INTO catalog_lessons (course_id, num, title, zh)
         SELECT $1, * FROM unnest($2::int[], $3::text[], $4::text[])
         ON CONFLICT (course_id, num) DO UPDATE SET title = EXCLUDED.title, zh = EXCLUDED.zh RETURNING id, num`,
        [row.id, ls.map(l => l.num), ls.map(l => l.title), ls.map(l => l.zh)]);
      n.lessons += ids.length;
      const idOf = new Map(ids.map(r => [r.num, r.id]));
      await c.query(`DELETE FROM catalog_assets WHERE storage = 'repo' AND lesson_id = ANY($1::int[])`, [ids.map(r => r.id)]);
      const files = ls.flatMap(l => l.assets.map(a => ({ ...a, lesson: idOf.get(l.num) })));
      if (files.length) {
        await c.query(
          `INSERT INTO catalog_assets (lesson_id, kind, name, size, url, storage)
           SELECT l, k, nm, s, u, 'repo' FROM unnest($1::int[], $2::text[], $3::text[], $4::bigint[], $5::text[]) AS t(l, k, nm, s, u)`,
          [files.map(f => f.lesson), files.map(f => f.kind), files.map(f => f.name), files.map(f => String(f.size)), files.map(f => f.url)]);
        n.assets += files.length;
      }
    }
    await c.query('COMMIT');
    return n;
  } catch (e) {
    await c.query('ROLLBACK').catch(() => {});
    throw e;
  } finally {
    c.release();
  }
}

const ACTIONS = ['course', 'lesson', 'asset', 'upload', 'import'];
// TẠM BỎ mật khẩu (người dùng yêu cầu 31/10): ai có link cũng xem và sửa được.
// Bật lại: đổi OPEN thành false ở đây, catOpen trong backend/go/catalog.go và OPEN trong apps/quan-ly/src/App.tsx.
const OPEN = true;

export default async function catalog(req, res) {
  const url = new URL(req.url, 'http://localhost');
  const method = req.method;

  if (!['GET', 'POST', 'PATCH', 'DELETE'].includes(method)) {
    res.setHeader('Allow', 'GET, POST, PATCH, DELETE');
    return fail(res, 405, 'chỉ hỗ trợ GET, POST, PATCH và DELETE');
  }
  if (!OPEN && !authorized(req)) return fail(res, 401, 'sai mật khẩu');
  if (method === 'GET' && url.searchParams.has('check')) return send(res, 200, { ok: true });

  const action = ACTIONS.find(a => url.searchParams.has(a));
  const allowed = { GET: [undefined], POST: ACTIONS, PATCH: ['course', 'lesson'], DELETE: ['course', 'lesson', 'asset'] }[method];
  if (method !== 'GET' && !allowed.includes(action)) {
    return fail(res, 400, `${method} cần một trong: ${allowed.map(a => '?' + a).join(', ')}`);
  }

  let p;
  try { p = await pool(); } catch { return fail(res, 503, 'không kết nối được cơ sở dữ liệu'); }

  if (method === 'GET') {
    try { return send(res, 200, await readAll(p)); } catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
  }

  if (method === 'DELETE') {
    const id = idParam(url, action);
    if (!id) return fail(res, 400, `cần ?${action}=<số>`);
    try {
      if (action === 'course') return await removeWithFiles(res, p, 'catalog_courses', 'l.course_id', id, 'không có khóa học này');
      if (action === 'lesson') return await removeWithFiles(res, p, 'catalog_lessons', 'l.id', id, 'không có bài này');
      const { rows: [a] } = await p.query('SELECT storage, key FROM catalog_assets WHERE id = $1', [id]);
      if (!a) return fail(res, 404, 'không có file này');
      if (a.storage === 'r2' && a.key) {
        const e = r2env();
        if (!r2ready(e)) return fail(res, 503, R2_MISSING);
        if (!(await r2delete(e, [a.key]))) return fail(res, 502, 'không xoá được file trên R2, thử lại sau');
      }
      await p.query('DELETE FROM catalog_assets WHERE id = $1', [id]);
      return send(res, 200, { ok: true });
    } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
  }

  let body;
  try { body = await readJson(req, action === 'import' ? 5 << 20 : 1 << 20); } catch { body = null; }
  if (!body || typeof body !== 'object' || Array.isArray(body)) return fail(res, 400, 'dữ liệu không hợp lệ hoặc quá lớn');

  const id = method === 'PATCH' ? idParam(url, action) : 0;
  if (method === 'PATCH' && !id) return fail(res, 400, `cần ?${action}=<số>`);

  try {
    if (action === 'course') {
      const title = text(body.title, MAX_TITLE);
      const sort = int(body.sort, -MAX_SORT, MAX_SORT, null);
      if (sort === undefined) return fail(res, 400, 'thứ tự không hợp lệ');
      if (method === 'POST') {
        const slug = typeof body.slug === 'string' ? body.slug.trim() : '';
        if (!SLUG_RE.test(slug)) return fail(res, 400, 'mã khóa học chỉ gồm chữ thường, số và dấu gạch ngang (tối đa 40 ký tự)');
        if (!title) return fail(res, 400, 'cần tên khóa học');
        const r = await p.query(`INSERT INTO catalog_courses (slug, title, sort) VALUES ($1, $2, $3) RETURNING ${COURSE_COLS}`,
          [slug, title, sort ?? 0]);
        return send(res, 201, { course: toCourse(r.rows[0]) });
      }
      if (!absent(body.title) && !title) return fail(res, 400, 'cần tên khóa học');
      const r = await p.query(
        `UPDATE catalog_courses SET title = coalesce($2, title), sort = coalesce($3, sort) WHERE id = $1 RETURNING ${COURSE_COLS}`,
        [id, title || null, sort]);
      return r.rowCount ? send(res, 200, { course: toCourse(r.rows[0]) }) : fail(res, 404, 'không có khóa học này');
    }

    if (action === 'lesson') {
      const num = int(body.num, 0, MAX_NUM, null);
      if (num === undefined) return fail(res, 400, 'số bài không hợp lệ');
      const title = text(body.title, MAX_TITLE);
      if (!absent(body.title) && !title) return fail(res, 400, 'cần tên bài');
      if (!absent(body.zh) && typeof body.zh !== 'string') return fail(res, 400, 'tên tiếng Trung không hợp lệ');
      const zh = absent(body.zh) ? null : text(body.zh, MAX_TITLE);
      if (!absent(body.visible) && typeof body.visible !== 'boolean') return fail(res, 400, 'trạng thái hiện/ẩn không hợp lệ');
      const visible = absent(body.visible) ? null : body.visible;
      const sort = int(body.sort, -MAX_SORT, MAX_SORT, null);
      if (sort === undefined) return fail(res, 400, 'thứ tự không hợp lệ');
      if (method === 'POST') {
        const courseId = int(body.courseId, 1, 2147483647, undefined);
        if (courseId === undefined) return fail(res, 400, 'mã khóa học (courseId) không hợp lệ');
        if (num === null) return fail(res, 400, 'số bài không hợp lệ');
        if (!title) return fail(res, 400, 'cần tên bài');
        const r = await p.query(
          `INSERT INTO catalog_lessons (course_id, num, title, zh, visible, sort) VALUES ($1, $2, $3, $4, $5, $6) RETURNING ${LESSON_COLS}`,
          [courseId, num, title, zh ?? '', visible ?? true, sort ?? 0]);
        return send(res, 201, { lesson: { ...toLesson(r.rows[0]), courseId: r.rows[0].course_id } });
      }
      const r = await p.query(
        `UPDATE catalog_lessons SET num = coalesce($2, num), title = coalesce($3, title), zh = coalesce($4, zh),
                visible = coalesce($5, visible), sort = coalesce($6, sort) WHERE id = $1 RETURNING ${LESSON_COLS}`,
        [id, num, title || null, zh, visible, sort]);
      return r.rowCount ? send(res, 200, { lesson: { ...toLesson(r.rows[0]), courseId: r.rows[0].course_id } }) : fail(res, 404, 'không có bài này');
    }

    if (action === 'upload' || action === 'asset') {
      const lessonId = int(body.lessonId, 1, 2147483647, undefined);
      if (lessonId === undefined) return fail(res, 400, 'mã bài (lessonId) không hợp lệ');
      if (!KINDS.includes(body.kind)) return fail(res, 400, 'loại file không hợp lệ');
      const name = text(body.name, MAX_NAME);
      if (!name) return fail(res, 400, 'cần tên file');
      const size = int(body.size, 0, MAX_SIZE, action === 'upload' ? undefined : 0);
      if (size === undefined) return fail(res, 400, 'dung lượng không hợp lệ');
      const storage = action === 'upload' ? 'r2' : body.storage;
      if (!STORAGES.includes(storage)) return fail(res, 400, 'nơi lưu không hợp lệ');
      if (storage === 'r2' && size > MAX_UPLOAD) return fail(res, 400, 'file quá 200 MB');

      let link = '';
      if (action === 'asset' && storage === 'repo') {
        link = text(body.url, MAX_URL);
        if (!validUrl(link)) return fail(res, 400, 'đường dẫn không hợp lệ');
      }
      if (action === 'asset' && storage === 'youtube') {
        link = youtube(text(body.url, MAX_URL));
        if (!link) return fail(res, 400, 'link YouTube không hợp lệ');
      }

      const { rows: [lesson] } = await p.query(
        'SELECT c.slug, l.num FROM catalog_lessons l JOIN catalog_courses c ON c.id = l.course_id WHERE l.id = $1', [lessonId]);
      if (!lesson) return fail(res, 404, 'không có bài này');
      const prefix = `${lesson.slug}/${pad2(lesson.num)}/`;

      let key = '';
      if (storage === 'r2') {
        const e = r2env();
        if (action === 'upload') {
          if (!r2ready(e)) return fail(res, 503, R2_MISSING);
          const type = TYPE_RE.test(text(body.type, 100)) ? text(body.type, 100) : 'application/octet-stream';
          key = `${prefix}${Date.now()}-${safeName(name)}`;
          return send(res, 200, {
            putUrl: r2url(e, 'PUT', key, 900), key, publicUrl: `${e.publicUrl}/${key}`, headers: { 'Content-Type': type },
          });
        }
        key = text(body.key, MAX_KEY);
        if (!key.startsWith(prefix) || !/^[A-Za-z0-9._\/-]+$/.test(key) || key.includes('..')) return fail(res, 400, 'key R2 không thuộc bài này');
        if (!e.publicUrl) return fail(res, 503, R2_MISSING);
        link = `${e.publicUrl}/${key}`;
      }

      const r = await p.query(
        `INSERT INTO catalog_assets (lesson_id, kind, name, size, url, storage, key) VALUES ($1, $2, $3, $4, $5, $6, $7) RETURNING ${ASSET_COLS}`,
        [lessonId, body.kind, name, String(size), link, storage, key]);
      return send(res, 201, { asset: { ...toAsset(r.rows[0]), lessonId } });
    }

    // import
    const { courses, error } = checkImport(body);
    if (error) return fail(res, 400, error);
    const n = await runImport(p, courses);
    return send(res, 200, { ok: true, ...n });
  } catch (e) {
    if (e?.code === '23505') return fail(res, 409, action === 'course' ? 'mã khóa học đã có' : 'số bài này đã có trong khóa học');
    if (e?.code === '23503') return fail(res, 404, action === 'lesson' ? 'không có khóa học này' : 'không có bài này');
    return fail(res, 500, 'lỗi ghi dữ liệu');
  }
}
