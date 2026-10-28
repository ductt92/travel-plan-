// GET/PUT /api/node/terms
//
// Thuật ngữ du lịch của trang "Ngọc học tiếng Trung" (hsk6/), mỗi thuật ngữ một dòng trong bảng term.
// GET ai cũng đọc được (nội dung học, không bí mật); ?versions là lịch sử phiên bản, ?version=N là bản sao của bản N.
// PUT cần mã đồng bộ và GHI ĐÈ toàn bộ bằng danh sách gửi lên (trang tự gộp khi chọn "thêm vào"):
// xóa hết thuật ngữ cũ rồi ghi danh sách mới trong một transaction, mỗi lần ghi thêm một dòng term_upload
// kèm bản sao cả danh sách, nên bản nào cũng khôi phục được.
// Trang đọc file Excel và chuẩn hóa (TERM_BE trong BaiGiang/web/template.html), server kiểm tra lại từng trường.
import { authorized, db, fail, readJson, send } from './common.js';

const TABLES = `
CREATE TABLE IF NOT EXISTS term (
  key      text PRIMARY KEY,
  zh       text NOT NULL,
  pinyin   text NOT NULL,
  vi       text NOT NULL,
  grp      text NOT NULL,
  majors   jsonb NOT NULL,
  sessions text[] NOT NULL,
  n        integer NOT NULL
);
CREATE TABLE IF NOT EXISTS term_upload (
  id           bigserial PRIMARY KEY,
  file_name    text NOT NULL,
  summary_name text NOT NULL,
  sheets       jsonb NOT NULL,
  count        integer NOT NULL,
  created_at   timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE term_upload ADD COLUMN IF NOT EXISTS mode text NOT NULL DEFAULT 'replace';
ALTER TABLE term_upload ADD COLUMN IF NOT EXISTS terms jsonb`;

let tables = null;
async function pool() {
  const p = await db();
  tables ||= p.query(TABLES).catch(e => { tables = null; throw e; });
  await tables;
  return p;
}

const MAX_TERMS = 5000;
const str = (v, max, required) => typeof v === 'string' && v.length <= max && (!required || v.trim() !== '');
const int = v => Number.isInteger(v) && v >= 0 && v < 2 ** 31;
const DATE = /^\d{4}-\d{2}-\d{2}$/;
// replace: ghi đè bằng file; add: trang đã gộp file vào danh sách cũ; restore: khôi phục một bản cũ
const MODES = ['replace', 'add', 'restore'];
const MAX_VERSIONS = 100;

// Trả thông báo lỗi đầu tiên, hoặc null nếu dữ liệu đúng định dạng
export function check(body) {
  if (!body || typeof body !== 'object') return 'dữ liệu không hợp lệ';
  if (!str(body.fileName, 200, true)) return 'thiếu tên file';
  if (!str(body.summaryName, 200, true)) return 'thiếu tên sheet tổng hợp';
  if (body.mode !== undefined && !MODES.includes(body.mode)) return 'cách ghi không hợp lệ';
  if (!Array.isArray(body.sheets) || body.sheets.length > 50 || !body.sheets.every(s => str(s, 200, true))) return 'danh sách sheet không hợp lệ';
  const terms = body.terms;
  if (!Array.isArray(terms) || !terms.length) return 'file không có thuật ngữ nào';
  if (terms.length > MAX_TERMS) return `tối đa ${MAX_TERMS} thuật ngữ`;
  const seen = new Set();
  for (const [i, t] of terms.entries()) {
    const at = `thuật ngữ thứ ${i + 1}`;
    if (!t || typeof t !== 'object') return `${at}: không hợp lệ`;
    if (!str(t.key, 200, true) || !str(t.zh, 200, true)) return `${at}: thiếu chữ Hán`;
    if (seen.has(t.key)) return `${at}: trùng "${t.key}"`;
    seen.add(t.key);
    if (!str(t.pinyin, 300) || !str(t.vi, 1000) || !str(t.group, 200)) return `${at} (${t.zh}): pinyin, nghĩa hoặc nhóm không hợp lệ`;
    if (!int(t.n)) return `${at} (${t.zh}): thứ tự không hợp lệ`;
    if (!Array.isArray(t.majors) || t.majors.length > 20 || !t.majors.every(m => m && str(m.name, 200, true) && str(m.group, 200) && int(m.n)))
      return `${at} (${t.zh}): chuyên ngành không hợp lệ`;
    if (!Array.isArray(t.sessions) || t.sessions.length > 100 || !t.sessions.every(d => typeof d === 'string' && DATE.test(d)))
      return `${at} (${t.zh}): buổi học không hợp lệ`;
  }
  return null;
}

async function load(p) {
  const up = (await p.query('SELECT id, file_name, summary_name, sheets, count, created_at FROM term_upload ORDER BY id DESC LIMIT 1')).rows[0];
  const { rows } = await p.query('SELECT key, zh, pinyin, vi, grp, majors, sessions, n FROM term ORDER BY n, key');
  return {
    version: up ? Number(up.id) : 0,
    fileName: up?.file_name ?? null,
    summaryName: up?.summary_name ?? null,
    sheets: up?.sheets ?? [],
    updatedAt: up?.created_at ?? null,
    terms: rows.map(r => ({ key: r.key, zh: r.zh, pinyin: r.pinyin, vi: r.vi, group: r.grp, majors: r.majors, sessions: r.sessions, n: r.n })),
  };
}

async function versions(p) {
  const { rows } = await p.query(`SELECT id, file_name, mode, count, created_at, terms IS NOT NULL AS saved
    FROM term_upload ORDER BY id DESC LIMIT ${MAX_VERSIONS}`);
  return { versions: rows.map(r => ({ version: Number(r.id), fileName: r.file_name, mode: r.mode, count: r.count, createdAt: r.created_at, saved: r.saved })) };
}

async function snapshot(p, id) {
  const r = (await p.query('SELECT id, file_name, summary_name, sheets, mode, created_at, terms FROM term_upload WHERE id = $1', [id])).rows[0];
  if (!r?.terms) return null;
  return { version: Number(r.id), fileName: r.file_name, summaryName: r.summary_name, sheets: r.sheets, mode: r.mode, updatedAt: r.created_at, terms: r.terms };
}

// Ghi đè trong một transaction: lỗi giữa chừng thì giữ nguyên danh sách cũ
async function replace(p, body) {
  const c = await p.connect();
  try {
    await c.query('BEGIN');
    // sao lưu bản đang có: bản mới nhất ghi từ trước khi có lịch sử (chưa có bản sao) thì chép danh sách hiện tại vào
    await c.query(`UPDATE term_upload SET terms = (SELECT COALESCE(jsonb_agg(jsonb_build_object('key', key, 'zh', zh, 'pinyin', pinyin,
        'vi', vi, 'group', grp, 'majors', majors, 'sessions', sessions, 'n', n) ORDER BY n, key), '[]') FROM term)
      WHERE id = (SELECT max(id) FROM term_upload) AND terms IS NULL`);
    await c.query('DELETE FROM term');
    await c.query(`INSERT INTO term (key, zh, pinyin, vi, grp, majors, sessions, n)
      SELECT x.key, x.zh, x.pinyin, x.vi, x."group", x.majors, x.sessions, x.n
      FROM jsonb_to_recordset($1::jsonb) AS x(key text, zh text, pinyin text, vi text, "group" text, majors jsonb, sessions text[], n integer)`,
      [JSON.stringify(body.terms)]);
    const { rows } = await c.query(`INSERT INTO term_upload (file_name, summary_name, sheets, count, mode, terms)
      VALUES ($1, $2, $3, $4, $5, $6) RETURNING id, created_at`,
      [body.fileName, body.summaryName, JSON.stringify(body.sheets), body.terms.length, body.mode || 'replace', JSON.stringify(body.terms)]);
    await c.query('COMMIT');
    return { version: Number(rows[0].id), count: body.terms.length, updatedAt: rows[0].created_at };
  } catch (e) {
    await c.query('ROLLBACK').catch(() => {});
    throw e;
  } finally {
    c.release();
  }
}

export default async function terms(req, res) {
  if (req.method !== 'GET' && req.method !== 'PUT') {
    res.setHeader('Allow', 'GET, PUT');
    return fail(res, 405, 'chỉ hỗ trợ GET và PUT');
  }
  if (req.method === 'PUT' && !authorized(req)) return fail(res, 401, 'sai mã đồng bộ');

  let p;
  try { p = await pool(); } catch { return fail(res, 503, 'không kết nối được cơ sở dữ liệu'); }

  if (req.method === 'GET') {
    const q = new URL(req.url, 'http://localhost').searchParams;
    try {
      if (q.has('versions')) return send(res, 200, await versions(p));
      if (q.has('version')) {
        const id = Number(q.get('version'));
        const snap = Number.isInteger(id) && id > 0 ? await snapshot(p, id) : null;
        return snap ? send(res, 200, snap) : fail(res, 404, 'không có bản sao của phiên bản này');
      }
      return send(res, 200, await load(p));
    } catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
  }
  let body;
  try { body = await readJson(req, 4 << 20); } catch { return fail(res, 400, 'dữ liệu không hợp lệ hoặc quá lớn'); }
  const err = check(body);
  if (err) return fail(res, 400, err);
  try { return send(res, 200, await replace(p, body)); } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
}
