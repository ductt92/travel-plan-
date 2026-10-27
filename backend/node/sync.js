// GET/PUT /api/node/sync?key=<khóa>
//
// Mỗi khóa localStorage của các app (bản đồ, tiến độ học) là một dòng trong bảng docs.
// Ghi theo kiểu khóa lạc quan: client gửi kèm base (phiên bản nó đang có); nếu máy khác
// đã ghi trước thì trả 409 kèm bản mới nhất để client gộp rồi gửi lại.
import { authorized, db, fail, readJson, send } from './common.js';

// Chỉ nhận các khóa đã biết để không ai ghi rác vào DB
const ALLOWED = new Set([
  'dadiqua-trip', // dấu tích địa điểm đã ghé trong chuyến đi
  'da-di-qua-v1', // trạng thái + ghi chú từng tỉnh
  'hanlo-v2'      // tiến độ học tiếng Trung
]);

// pg trả bigint dạng chuỗi: đổi về số cho giống bản Go
const toDoc = (key, row) => row
  ? { key, data: row.data, version: Number(row.version), updatedAt: row.updated_at }
  : { key, data: null, version: 0, updatedAt: null };

async function load(p, key) {
  const { rows } = await p.query('SELECT data, version, updated_at FROM docs WHERE key = $1', [key]);
  return toDoc(key, rows[0]);
}

// Ghi khi phiên bản trên DB vẫn bằng base; ok=false nghĩa là xung đột và doc là bản hiện tại
async function save(p, key, data, base) {
  const json = JSON.stringify(data);
  const { rows } = base === 0
    ? await p.query(`INSERT INTO docs (key, data, version) VALUES ($1, $2, 1)
        ON CONFLICT (key) DO NOTHING RETURNING version, updated_at`, [key, json])
    : await p.query(`UPDATE docs SET data = $2, version = version + 1, updated_at = now()
        WHERE key = $1 AND version = $3 RETURNING version, updated_at`, [key, json, base]);
  if (!rows.length) return { ok: false, doc: await load(p, key) };
  return { ok: true, doc: { key, data, version: Number(rows[0].version), updatedAt: rows[0].updated_at } };
}

export default async function sync(req, res) {
  if (!authorized(req)) return fail(res, 401, 'sai mã đồng bộ');
  const key = new URL(req.url, 'http://x').searchParams.get('key');
  if (!ALLOWED.has(key)) return fail(res, 400, 'khóa không hợp lệ');

  let p;
  try { p = await db(); } catch { return fail(res, 503, 'không kết nối được cơ sở dữ liệu'); }

  if (req.method === 'GET') {
    try { return send(res, 200, await load(p, key)); } catch { return fail(res, 500, 'lỗi đọc dữ liệu'); }
  }
  if (req.method === 'PUT') {
    let body;
    try { body = await readJson(req); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
    const base = Number(body?.base ?? 0);
    if (body?.data == null || !Number.isInteger(base) || base < 0) return fail(res, 400, 'dữ liệu không hợp lệ');
    try {
      const { ok, doc } = await save(p, key, body.data, base);
      return send(res, ok ? 200 : 409, doc); // 409: máy khác đã ghi trước, trả bản mới nhất
    } catch { return fail(res, 500, 'lỗi ghi dữ liệu'); }
  }
  res.setHeader('Allow', 'GET, PUT');
  return fail(res, 405, 'chỉ hỗ trợ GET và PUT');
}
