// GET/PUT /api/node/grammar
//
// Trang "Ngữ pháp qua tình huống" (hsk6/ngu-phap/) đọc nhóm bài và các tình huống từ đây.
// Mỗi tình huống là một dòng grammar_case, nội dung giữ nguyên dạng JSON trang dùng (data); grp/ord để sắp xếp.
// GET ai cũng đọc được. PUT {groups, cases} cần mật khẩu (APP_SECRET hoặc HSK6_PASS): ghi đè cả bộ trong một
// transaction và lưu bản sao vào grammar_version để khôi phục được (bản mới nhất là bản đang dùng).
import { authorizedHsk6, db, fail, readJson, send } from './common.js';

const TABLES = `
CREATE TABLE IF NOT EXISTS grammar_group (
  id   text PRIMARY KEY,
  name text NOT NULL,
  ord  integer NOT NULL
);
CREATE TABLE IF NOT EXISTS grammar_case (
  id         text PRIMARY KEY,
  grp        text NOT NULL REFERENCES grammar_group ON DELETE CASCADE,
  ord        integer NOT NULL,
  data       jsonb NOT NULL,
  updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS grammar_version (
  id         bigserial PRIMARY KEY,
  groups     jsonb NOT NULL,
  cases      jsonb NOT NULL,
  count      integer NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
)`;

let tables = null;
async function pool() {
  const p = await db();
  tables ||= p.query(TABLES).catch(e => { tables = null; throw e; });
  await tables;
  return p;
}

const MAX_CASES = 300;
const MAX_BODY = 3 << 20;
const GROUP_ID = /^[A-Z][A-Z0-9]{0,3}$/;
const CASE_ID = /^[a-z0-9-]{1,40}$/;
const str = (v, max) => typeof v === 'string' && v.trim() !== '' && v.length <= max;

// Trả thông báo lỗi đầu tiên, hoặc null nếu dữ liệu đúng định dạng (bản Go: checkGrammar trong backend/go/grammar.go)
export function check(body) {
  const { groups, cases } = body || {};
  if (!Array.isArray(groups) || !groups.length || groups.length > 20) return 'cần 1–20 nhóm';
  const gids = new Set();
  for (const g of groups) {
    if (!GROUP_ID.test(g?.id) || gids.has(g.id)) return `mã nhóm không hợp lệ hoặc trùng: ${g?.id}`;
    if (!str(g.name, 80)) return `nhóm ${g.id} thiếu tên`;
    gids.add(g.id);
  }
  if (!Array.isArray(cases) || !cases.length || cases.length > MAX_CASES) return `cần 1–${MAX_CASES} tình huống`;
  const ids = new Set();
  for (const c of cases) {
    if (!c || typeof c !== 'object' || Array.isArray(c)) return 'tình huống phải là đối tượng';
    if (!CASE_ID.test(c.id) || ids.has(c.id)) return `mã tình huống không hợp lệ hoặc trùng: ${c.id}`;
    if (!gids.has(c.g)) return `tình huống ${c.id} thuộc nhóm không có: ${c.g}`;
    if (!str(c.title, 300)) return `tình huống ${c.id} thiếu tiêu đề`;
    if (!Array.isArray(c.quiz) || !c.quiz.length) return `tình huống ${c.id} chưa có câu hỏi`;
    for (const q of c.quiz) {
      if (!Array.isArray(q?.opts) || q.opts.length < 2 || !Number.isInteger(q.a) || q.a < 0 || q.a >= q.opts.length)
        return `tình huống ${c.id} có câu hỏi sai đáp án`;
    }
    ids.add(c.id);
  }
  return null;
}

async function load(p) {
  const [g, c, v] = await Promise.all([
    p.query('SELECT id, name FROM grammar_group ORDER BY ord'),
    p.query('SELECT c.data FROM grammar_case c JOIN grammar_group g ON g.id = c.grp ORDER BY g.ord, c.ord'),
    p.query('SELECT max(id) AS id, max(created_at) AS at FROM grammar_version')
  ]);
  return { version: Number(v.rows[0].id || 0), updatedAt: v.rows[0].at, groups: g.rows, cases: c.rows.map(r => r.data) };
}

async function replace(p, { groups, cases }) {
  const c = await p.connect();
  try {
    await c.query('BEGIN');
    await c.query('DELETE FROM grammar_case');
    await c.query('DELETE FROM grammar_group');
    await c.query(`INSERT INTO grammar_group (id, name, ord) SELECT * FROM jsonb_to_recordset($1) AS x(id text, name text, ord integer)`,
      [JSON.stringify(groups.map((g, i) => ({ id: g.id, name: g.name.trim(), ord: i })))]);
    // thứ tự trong nhóm giữ đúng thứ tự gửi lên
    const order = {};
    await c.query(`INSERT INTO grammar_case (id, grp, ord, data) SELECT id, grp, ord, data FROM jsonb_to_recordset($1) AS x(id text, grp text, ord integer, data jsonb)`,
      [JSON.stringify(cases.map(k => ({ id: k.id, grp: k.g, ord: (order[k.g] = (order[k.g] ?? -1) + 1), data: k })))]);
    const { rows } = await c.query('INSERT INTO grammar_version (groups, cases, count) VALUES ($1, $2, $3) RETURNING id, created_at',
      [JSON.stringify(groups), JSON.stringify(cases), cases.length]);
    await c.query('COMMIT');
    return { version: Number(rows[0].id), count: cases.length, updatedAt: rows[0].created_at };
  } catch (e) {
    await c.query('ROLLBACK').catch(() => {});
    throw e;
  } finally { c.release(); }
}

// Ghi cả bộ từ dòng lệnh (scripts/seed-grammar.mjs), kiểm tra giống PUT
export async function save(body) {
  const err = check(body);
  if (err) throw new Error(err);
  return replace(await pool(), body);
}

export default async function grammar(req, res) {
  if (req.method !== 'GET' && req.method !== 'PUT') { res.setHeader('Allow', 'GET, PUT'); return fail(res, 405, 'chỉ hỗ trợ GET và PUT'); }
  if (req.method === 'PUT' && !authorizedHsk6(req)) return fail(res, 401, 'sai mật khẩu');
  let p;
  try { p = await pool(); } catch { return fail(res, 503, 'không kết nối được cơ sở dữ liệu'); }
  if (req.method === 'GET') {
    try { return send(res, 200, await load(p)); } catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
  }
  let body;
  try { body = await readJson(req, MAX_BODY); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
  const err = check(body);
  if (err) return fail(res, 400, err);
  try { return send(res, 200, await replace(p, body)); } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
}
