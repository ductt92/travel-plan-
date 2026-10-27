// POST /api/node/ai  { model?, system?, contents: [{role, parts:[{text}]}] } → { text }
// Gọi Gemini bằng khóa giấu trên server, người dùng chỉ cần mã đồng bộ chung.
import { authorized, fail, readJson, send } from './common.js';

const MODEL_RE = /^gemini-[\w.-]{1,40}$/;
const DEFAULT_MODEL = 'gemini-2.5-flash';
const MAX_TURNS = 16;
const MAX_CHARS = 8000;

const cut = s => [...String(s ?? '')].slice(0, MAX_CHARS).join('');

// Chỉ chuyển tiếp đúng dạng hội thoại, cắt bớt để không ai dùng API làm proxy tùy ý
function clean(body) {
  const contents = (Array.isArray(body?.contents) ? body.contents : []).slice(-MAX_TURNS).map(c => ({
    role: c?.role === 'model' ? 'model' : 'user',
    parts: [{ text: cut(c?.parts?.[0]?.text) }]
  }));
  const system = cut(body?.system).trim();
  const model = MODEL_RE.test(body?.model) ? body.model : DEFAULT_MODEL;
  return { contents, system, model };
}

export default async function ai(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return fail(res, 405, 'chỉ hỗ trợ POST'); }
  if (!authorized(req)) return fail(res, 401, 'sai mã đồng bộ');
  const key = process.env.GEMINI_API_KEY;
  if (!key) return fail(res, 503, 'server chưa cấu hình GEMINI_API_KEY');

  let body;
  try { body = await readJson(req); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
  const { contents, system, model } = clean(body);
  if (!contents.length || contents[0].role !== 'user') return fail(res, 400, 'hội thoại phải bắt đầu bằng câu hỏi');

  try {
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
      body: JSON.stringify({ ...(system && { systemInstruction: { parts: [{ text: system }] } }), contents }),
      signal: AbortSignal.timeout(25000)
    });
    const data = await r.json().catch(() => ({}));
    if (!r.ok) return fail(res, 502, data.error?.message || `Gemini trả lỗi ${r.status}`);
    const text = data.candidates?.[0]?.content?.parts?.map(p => p.text).join('') || '';
    return send(res, 200, { text });
  } catch (e) {
    return fail(res, 504, `không gọi được Gemini: ${e.message}`);
  }
}
