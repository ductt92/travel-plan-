// Đưa danh mục khóa học có sẵn trong repo lên trang quản lý (POST /api/<node|go>/quan-ly?import).
//   node scripts/seed-catalog.mjs [--dry] [--url http://127.0.0.1:3001/api/node/quan-ly] [--hsk ../../HSK]
//   --dry  chỉ in tóm tắt (khóa, bài, file, dung lượng), không gửi gì
//   --hsk  thư mục repo HSK (lấy tên bài HSK 6 từ BaiGiang/web/catalog.json khi bài chưa có slides/titles.json)
// Mã APP_SECRET lấy từ biến môi trường hoặc .env.local. Chạy lại bao nhiêu lần cũng được: khóa và bài được
// ghi gộp, file 'repo' của từng bài được thay mới, file R2 và link YouTube giữ nguyên.
//
// Nguồn:
//   hsk1–3       apps/hoc-tieng-trung/src/data/lessons.json (Hán Lộ); video public/video/bai-giang-cap<lv>-bai<NN>.mp4,
//                giọng đọc public/audio/<khóa>.mp3 (khóa băm của câu, mỗi file tính cho bài đầu tiên dùng câu đó)
//   hsk6-thuong  bài 1–20, hsk6-ha bài 21–40: hsk6/baiNN/{vid/*.mp4, slides/*.jpg, audio/*.mp3}, gộp mỗi loại một dòng
//   dingshi      顶石中文: hsk6/ds<chủ đề><bài>/ (cùng cấu trúc), số bài = chủ đề×10 + bài (ds21 → 21) để chạy lại không lệch
// Sau khi nhập: gắn link YouTube của video Hán Lộ (apps/hoc-tieng-trung/src/data/youtube.json), bài đã có link đó thì bỏ qua.
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { register } from 'node:module';
import { join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const args = process.argv.slice(2);
const opt = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : undefined; };
const DRY = args.includes('--dry');
const URL_ = opt('--url') || 'http://127.0.0.1:3001/api/node/quan-ly';
const HSK = opt('--hsk') || process.env.HSK_DIR || join(root, '..', '..', 'HSK');

const readJson = file => { try { return JSON.parse(readFileSync(file, 'utf8')); } catch { return null; } };
const size = file => statSync(file).size;
const pad2 = n => String(n).padStart(2, '0');
const files = (dir, ext) => (existsSync(dir) ? readdirSync(dir).filter(f => f.endsWith(ext)).sort() : []);

// ---- Hán Lộ ----

// Node 18 chưa import thẳng được JSON không kèm assert: đổi .json thành module "export default …"
// để dùng lại đúng buildLecture của app (danh sách câu đọc phải khớp từng chữ thì mới ra khóa file)
register('data:text/javascript,' + encodeURIComponent(`import { readFile } from 'node:fs/promises';
export async function load(url, ctx, next) {
  if (url.endsWith('.json')) return { format: 'module', shortCircuit: true, source: 'export default ' + await readFile(new URL(url), 'utf8') };
  return next(url, ctx);
}`));
const core = join(root, 'apps', 'hoc-tieng-trung', 'src', 'core');
const { LESSONS } = await import(pathToFileURL(join(core, 'data.js')));
const { buildLecture, stepParts } = await import(pathToFileURL(join(core, 'lecture.js')));
const { plainHz } = await import(pathToFileURL(join(core, 'pinyin.js')));

/** Khóa file âm thanh, giống audioKey trong apps/hoc-tieng-trung/src/core/speech.js */
function audioKey(lang, text) {
  let h1 = 0x811c9dc5, h2 = 5381;
  for (const x of new TextEncoder().encode(lang + '|' + text)) { h1 = Math.imul(h1 ^ x, 0x01000193) >>> 0; h2 = (Math.imul(h2, 33) + x) >>> 0; }
  return h1.toString(16).padStart(8, '0') + h2.toString(16).padStart(8, '0');
}

// cùng danh sách câu với AllTextsView (src/views/ToolViews.jsx), tách theo bài
function lessonTexts(l) {
  const keys = new Set();
  const add = (lang, text) => { text = (text || '').trim(); if (text) keys.add(audioKey(lang, text)); };
  buildLecture(l).steps.forEach(st => stepParts(st).forEach(p => add(p.lang, p.text)));
  l.words.forEach(w => { add('zh', w.hz); add('zh', plainHz(w.ex)); });
  l.grammar.forEach(g => g.ex.forEach(e => add('zh', e[0])));
  l.dialogs.forEach(d => d.lines.forEach(x => add('zh', x[1])));
  return keys;
}

function hanLo() {
  const pub = join(root, 'apps', 'hoc-tieng-trung', 'public');
  const audioDir = join(pub, 'audio');
  const have = new Set(files(audioDir, '.mp3').map(f => f.slice(0, -4)));
  const taken = new Set();
  const list = LESSONS.slice().sort((a, b) => a.lv - b.lv || a.no - b.no);
  const courses = new Map();
  for (const l of list) {
    const assets = [];
    const video = `bai-giang-cap${l.lv}-bai${pad2(l.no)}.mp4`;
    if (existsSync(join(pub, 'video', video))) {
      assets.push({ kind: 'video', name: video, size: size(join(pub, 'video', video)), url: `/hoc-tieng-trung/video/${video}` });
    }
    // một câu có thể xuất hiện ở nhiều bài: file chỉ tính cho bài đầu tiên để tổng dung lượng không bị đếm trùng
    const mine = [...lessonTexts(l)].filter(k => have.has(k) && !taken.has(k));
    mine.forEach(k => taken.add(k));
    if (mine.length) {
      assets.push({ kind: 'audio', name: `${mine.length} câu giọng đọc`,
        size: mine.reduce((s, k) => s + size(join(audioDir, `${k}.mp3`)), 0), url: '/hoc-tieng-trung/audio/' });
    }
    const slug = `hsk${l.lv}`;
    if (!courses.has(slug)) courses.set(slug, { slug, title: `HSK ${l.lv} · Hán Lộ`, sort: l.lv * 10, lessons: [] });
    courses.get(slug).lessons.push({ num: l.no, title: l.title, zh: l.zh || '', assets });
  }
  // câu dùng chung (nhập môn, thanh điệu…) không thuộc bài nào
  const rest = [...have].filter(k => !taken.has(k));
  return { courses: [...courses.values()], rest: { count: rest.length, bytes: rest.reduce((s, k) => s + size(join(audioDir, `${k}.mp3`)), 0) } };
}

// ---- HSK 6 ----

/** Một bài HSK 6 / 顶石中文 trong hsk6/<dir>/: tên lấy từ slides/titles.json, mỗi loại file gộp một dòng */
function folder(dirName, num, known) {
  const dir = join(root, 'hsk6', dirName);
  const t = readJson(join(dir, 'slides', 'titles.json'));
  const m = (t?.title || '').match(/^Bài\s*[\d.]+\s*[:：]\s*(.+)$/);
  const title = m?.[1]?.trim() || known?.vi || `Bài ${num}`;
  const zh = t?.zh || known?.zh || '';
  const assets = [];
  for (const [kind, sub, ext, label] of [['video', 'vid', '.mp4', 'đoạn video'], ['slides', 'slides', '.jpg', 'ảnh slide'], ['audio', 'audio', '.mp3', 'file âm thanh']]) {
    const list = files(join(dir, sub), ext);
    if (list.length) assets.push({ kind, name: `${list.length} ${label}`, size: list.reduce((s, f) => s + size(join(dir, sub, f)), 0), url: `/hsk6/${dirName}/` });
  }
  return { num, title, zh, assets };
}

function hsk6() {
  const catalog = readJson(join(HSK, 'BaiGiang', 'web', 'catalog.json'));
  if (!catalog) console.warn(`(không đọc được ${join(HSK, 'BaiGiang', 'web', 'catalog.json')}, bài chưa có titles.json sẽ chỉ có số bài)`);
  const known = new Map();
  for (const b of catalog?.books || []) for (const u of b.units || []) for (const l of u.lessons || []) known.set(l.n, l);

  const lesson = n => folder(`bai${pad2(n)}`, n, known.get(n));
  const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => lesson(a + i));
  // 顶石中文: thư mục ds11, ds12, ds21…, tên bài dạng "Bài 1.1: …" thì giữ "1.1 · …"
  const ds = files(join(root, 'hsk6'), '').filter(d => /^ds\d{2}$/.test(d)).map(d => {
    const l = folder(d, Number(d.slice(2)));
    return { ...l, title: `${d[2]}.${d[3]} · ${l.title}` };
  });
  return [
    { slug: 'hsk6-thuong', title: 'HSK 6 · Quyển Thượng', sort: 60, lessons: range(1, 20) },
    { slug: 'hsk6-ha', title: 'HSK 6 · Quyển Hạ', sort: 61, lessons: range(21, 40) },
    ...(ds.length ? [{ slug: 'dingshi', title: '顶石中文', sort: 62, lessons: ds }] : []),
  ];
}

// ---- gửi ----

const hl = hanLo();
const payload = { courses: [...hl.courses, ...hsk6()] };
const body = JSON.stringify(payload);

const mb = n => `${(n / 1048576).toFixed(1)} MB`;
let total = 0;
for (const c of payload.courses) {
  const assets = c.lessons.flatMap(l => l.assets);
  const bytes = assets.reduce((s, a) => s + a.size, 0);
  total += bytes;
  const withFiles = c.lessons.filter(l => l.assets.length).length;
  console.log(`${c.slug.padEnd(12)} ${c.title.padEnd(22)} ${String(c.lessons.length).padStart(3)} bài (${withFiles} có file)  ${String(assets.length).padStart(3)} file  ${mb(bytes).padStart(9)}`);
}
console.log(`Tổng: ${payload.courses.length} khóa, ${payload.courses.reduce((s, c) => s + c.lessons.length, 0)} bài, `
  + `${payload.courses.reduce((s, c) => s + c.lessons.reduce((t, l) => t + l.assets.length, 0), 0)} file, ${mb(total)}`);
console.log(`Giọng đọc Hán Lộ dùng chung, không thuộc bài nào: ${hl.rest.count} file, ${mb(hl.rest.bytes)}`);
console.log(`Dữ liệu gửi đi: ${(body.length / 1024).toFixed(1)} KB`);
if (DRY) process.exit(0);

let secret = process.env.APP_SECRET;
if (!secret && existsSync(join(root, '.env.local'))) {
  const m = readFileSync(join(root, '.env.local'), 'utf8').match(/^\s*APP_SECRET\s*=\s*(.*?)\s*$/m);
  secret = m?.[1].replace(/^(['"])(.*)\1$/, '$2');
}
if (!secret) { console.error('Thiếu APP_SECRET (biến môi trường hoặc .env.local)'); process.exit(1); }

const res = await fetch(`${URL_}${URL_.includes('?') ? '&' : '?'}import`, {
  method: 'POST', headers: { 'Content-Type': 'application/json', 'X-App-Secret': secret }, body,
});
const out = await res.json().catch(() => ({}));
if (!res.ok) { console.error(`Lỗi ${res.status}: ${out.error || 'không rõ'}`); process.exit(1); }
console.log(`Đã ghi (${res.headers.get('x-backend')}): ${out.courses} khóa, ${out.lessons} bài, ${out.assets} file`);

// ---- link YouTube của video Hán Lộ ----

const yt = readJson(join(root, 'apps', 'hoc-tieng-trung', 'src', 'data', 'youtube.json')) || {};
const headers = { 'Content-Type': 'application/json', 'X-App-Secret': secret };
const cat = await fetch(URL_, { headers }).then(r => r.json());
let added = 0;
for (const [file, id] of Object.entries(yt)) {
  const [, lv, no] = file.match(/cap(\d+)-bai(\d+)/) || [];
  const l = cat.courses?.find(c => c.slug === `hsk${lv}`)?.lessons.find(x => x.num === Number(no));
  const link = `https://www.youtube.com/watch?v=${id}`;
  if (!l || l.assets.some(a => a.storage === 'youtube' && a.url === link)) continue;
  const r = await fetch(`${URL_}${URL_.includes('?') ? '&' : '?'}asset`, {
    method: 'POST', headers, body: JSON.stringify({ lessonId: l.id, kind: 'video', name: 'Video bài giảng (YouTube)', size: 0, storage: 'youtube', url: link }),
  });
  if (r.ok) added++; else console.error(`Lỗi gắn YouTube ${file}: ${r.status}`);
}
console.log(`Link YouTube: thêm ${added}, tổng ${Object.keys(yt).length} video Hán Lộ`);
