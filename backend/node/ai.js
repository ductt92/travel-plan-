// POST /api/node/ai  { model?, provider?, system?, contents: [{role, parts:[{text}]}] } → { text, provider, model }
// Gọi AI bằng khóa giấu trên server, người dùng chỉ cần mã đồng bộ chung.
// Nhiều nhà cung cấp có gói miễn phí, thử lần lượt: hết lượt (429), quá tải, lỗi hay quá giờ thì chuyển sang cái kế tiếp.
// Chỉ dùng cái nào có khóa trong biến môi trường; đổi thứ tự bằng AI_ORDER (vd "groq,gemini"), đổi model bằng <TÊN>_MODELS,
// đổi địa chỉ (proxy, máy chủ thử) bằng <TÊN>_BASE_URL.
import { authorized, fail, readJson, send } from './common.js';

const MODEL_RE = /^gemini-[\w.-]{1,40}$/;
const MAX_TURNS = 16;
const MAX_CHARS = 8000;
const TIMEOUT = 20000;  // mỗi lần gọi một model
const BUDGET = 50000;   // cả chuỗi, dưới maxDuration 60 s trong vercel.json
const COOLDOWN = 60000; // model hết lượt thì bỏ qua một phút (chỉ trong function đang "ấm")

const list = (v, d) => (v || d).split(',').map(s => s.trim()).filter(Boolean);
const cut = s => [...String(s ?? '')].slice(0, MAX_CHARS).join('');

// Gemini: mỗi model có hạn mức miễn phí riêng nên thử lần lượt từng model. Còn lại theo chuẩn chat/completions của OpenAI.
const PROVIDERS = {
  gemini: { name: 'Gemini', key: 'GEMINI_API_KEY', base: 'https://generativelanguage.googleapis.com/v1beta', models: () => list(process.env.GEMINI_MODELS, 'gemini-2.5-flash,gemini-2.5-flash-lite') },
  groq: { name: 'Groq', key: 'GROQ_API_KEY', base: 'https://api.groq.com/openai/v1', models: () => list(process.env.GROQ_MODELS, 'llama-3.3-70b-versatile') },
  openrouter: { name: 'OpenRouter', key: 'OPENROUTER_API_KEY', base: 'https://openrouter.ai/api/v1', models: () => list(process.env.OPENROUTER_MODELS, 'meta-llama/llama-3.3-70b-instruct:free') },
  mistral: { name: 'Mistral', key: 'MISTRAL_API_KEY', base: 'https://api.mistral.ai/v1', models: () => list(process.env.MISTRAL_MODELS, 'mistral-small-latest') },
};
const ORDER = 'gemini,groq,openrouter,mistral';
const cooldown = new Map();
const baseOf = id => process.env[`${id.toUpperCase()}_BASE_URL`] || PROVIDERS[id].base;

// Chỉ chuyển tiếp đúng dạng hội thoại, cắt bớt để không ai dùng API làm proxy tùy ý
function clean(body) {
  const contents = (Array.isArray(body?.contents) ? body.contents : []).slice(-MAX_TURNS).map(c => ({
    role: c?.role === 'model' ? 'model' : 'user',
    parts: [{ text: cut(c?.parts?.[0]?.text) }]
  }));
  const system = cut(body?.system).trim();
  return { contents, system };
}

const failure = (status, message) => Object.assign(new Error(message), { status });
// model "suy nghĩ" (Qwen, DeepSeek…) có thể trả kèm <think>…</think>, bỏ đi để chỉ còn câu trả lời
const answer = s => String(s || '').replace(/<think>[\s\S]*?<\/think>/g, '').trim();

async function callGemini(key, model, { system, contents }, signal) {
  const r = await fetch(`${baseOf('gemini')}/models/${encodeURIComponent(model)}:generateContent`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
    body: JSON.stringify({ ...(system && { systemInstruction: { parts: [{ text: system }] } }), contents }),
    signal
  });
  const data = await r.json().catch(() => ({}));
  if (!r.ok) throw failure(r.status, data.error?.message || `lỗi ${r.status}`);
  return answer(data.candidates?.[0]?.content?.parts?.map(p => p.text).join(''));
}

async function callOpenAI(id, key, model, { system, contents }, signal) {
  const messages = [...(system ? [{ role: 'system', content: system }] : []),
    ...contents.map(c => ({ role: c.role === 'model' ? 'assistant' : 'user', content: c.parts[0].text }))];
  const r = await fetch(`${baseOf(id)}/chat/completions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${key}` },
    body: JSON.stringify({ model, messages, temperature: 0.2 }),
    signal
  });
  const data = await r.json().catch(() => ({}));
  if (!r.ok) throw failure(r.status, data.error?.message || data.message || `lỗi ${r.status}`);
  return answer(data.choices?.[0]?.message?.content);
}

export default async function ai(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return fail(res, 405, 'chỉ hỗ trợ POST'); }
  if (!authorized(req)) return fail(res, 401, 'sai mã đồng bộ');

  let body;
  try { body = await readJson(req); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
  const input = clean(body);
  if (!input.contents.length || input.contents[0].role !== 'user') return fail(res, 400, 'hội thoại phải bắt đầu bằng câu hỏi');

  // provider: chỉ dùng một nhà cung cấp (để thử từng khóa); không có thì theo AI_ORDER
  const order = PROVIDERS[body?.provider] ? [body.provider] : list(process.env.AI_ORDER, ORDER).filter(id => PROVIDERS[id]);
  const start = Date.now(), errors = [];
  let tried = 0, limited = 0;
  for (const id of order) {
    const p = PROVIDERS[id], key = process.env[p.key];
    if (!key) continue;
    let models = p.models();
    if (id === 'gemini' && MODEL_RE.test(body?.model)) models = [body.model, ...models.filter(m => m !== body.model)];
    for (const model of models) {
      const left = BUDGET - (Date.now() - start);
      if (left < 3000) break;
      tried++;
      if ((cooldown.get(`${id}:${model}`) || 0) > Date.now()) { limited++; errors.push(`${p.name} ${model}: vừa hết lượt, đang chờ`); continue; }
      try {
        const signal = AbortSignal.timeout(Math.min(TIMEOUT, left));
        const text = id === 'gemini' ? await callGemini(key, model, input, signal) : await callOpenAI(id, key, model, input, signal);
        if (!text) throw failure(502, 'trả về rỗng');
        return send(res, 200, { text, provider: id, model });
      } catch (e) {
        if (e.status === 429) { limited++; cooldown.set(`${id}:${model}`, Date.now() + COOLDOWN); }
        errors.push(`${p.name} ${model}: ${String(e.status === 429 ? 'hết lượt' : e.message).slice(0, 160)}`);
      }
    }
  }
  if (!tried) return fail(res, 503, `server chưa cấu hình khóa AI nào (${Object.values(PROVIDERS).map(p => p.key).join(', ')})`);
  return fail(res, limited === tried ? 429 : 502, `các AI đều chưa trả lời được: ${errors.join('; ')}`);
}
