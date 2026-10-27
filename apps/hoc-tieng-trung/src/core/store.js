// Tiến độ học lưu trong localStorage (khóa hanlo-v2, giống bản HTML cũ nên không mất tiến độ).
// Đọc trong component: const S = useStore(); ghi: update(s => { ... }).
import { useSyncExternalStore } from 'react';
import { changed, track } from '@trang/sync';
import { LESSONS, LEVELS, WMAP, NPARTS, lessonsOf, hasContent } from './data.js';

const KEY = 'hanlo-v2';
export const DEF = { cards: {}, lessons: {}, l0: false, passed: {}, days: [], today: { date: '', n: 0 }, stats: { ans: 0, ok: 0 }, showPy: true, showVi: true, ai: { key: '', model: 'gemini-2.5-flash' } };
const clone = o => JSON.parse(JSON.stringify(o));

let S = (() => {
  try {
    const r = localStorage.getItem(KEY);
    if (r) { const d = JSON.parse(r); return { ...clone(DEF), ...d, ai: { ...DEF.ai, ...(d.ai || {}) } }; }
  } catch (e) { /* trình duyệt chặn lưu trữ */ }
  return clone(DEF);
})();
const subs = new Set();
let version = 0;
function emit() { version++; subs.forEach(f => f()); }
function persist() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { /* bỏ qua */ } changed(KEY); }

// Đồng bộ tiến độ giữa các máy (khi đã nhập mã). Khóa API Gemini riêng không đưa lên server.
track(KEY, {
  strip: d => { if (!d) return d; const { ai, ...rest } = d; return { ...rest, ai: { model: ai?.model || DEF.ai.model } }; },
  keep: (next, local) => ({ ...next, ai: { ...DEF.ai, ...(local?.ai || {}) } })
});
window.addEventListener('storage', e => {
  if (e.key !== KEY) return;
  try { const d = JSON.parse(localStorage.getItem(KEY)); if (d) { S = { ...clone(DEF), ...d, ai: { ...DEF.ai, ...(d.ai || {}) } }; emit(); } } catch (err) { /* bỏ qua */ }
});

/** Sửa trạng thái tại chỗ rồi lưu và báo cho component vẽ lại */
export function update(fn) { fn(S); persist(); emit(); }
export function getState() { return S; }
export function resetAll() { const ai = S.ai; S = clone(DEF); S.ai = ai; persist(); emit(); }
/** Hook: trả về S và vẽ lại mỗi khi S đổi */
export function useStore() {
  useSyncExternalStore(f => { subs.add(f); return () => subs.delete(f); }, () => version);
  return S;
}

/* Ngày học, chuỗi ngày, mục tiêu ngày */
export const dayKey = (d = new Date()) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
export const GOAL = 30;
export function activity() {
  update(s => {
    const k = dayKey();
    if (!s.days.includes(k)) s.days.push(k);
    if (s.today.date !== k) s.today = { date: k, n: 0 };
    s.today.n++;
  });
}
export function streak() {
  const set = new Set(S.days); const d = new Date();
  if (!set.has(dayKey(d))) d.setDate(d.getDate() - 1);
  let n = 0; while (set.has(dayKey(d))) { n++; d.setDate(d.getDate() - 1); }
  return n;
}
export const todayN = () => (S.today.date === dayKey() ? S.today.n : 0);

/* Tiến độ bài học: 5 phần (Bài giảng, Từ mới, Ngữ pháp, Hội thoại, Luyện tập) */
export const lessonParts = id => (S.lessons[id]?.parts || Array(NPARTS).fill(false));
export const lessonDoneCount = id => lessonParts(id).filter(Boolean).length;
export const lessonDone = id => lessonDoneCount(id) === NPARTS;
export function markPart(id, i) {
  if (lessonParts(id)[i]) return;
  update(s => { const p = s.lessons[id] || (s.lessons[id] = { parts: Array(NPARTS).fill(false), score: null }); p.parts[i] = true; });
}
export function setLessonScore(id, pct) {
  update(s => { const p = s.lessons[id] || (s.lessons[id] = { parts: Array(NPARTS).fill(false), score: null }); p.score = pct; p.parts[4] = true; });
}
export function levelStats(n) {
  const ls = lessonsOf(n);
  return { done: ls.filter(l => lessonDone(l.id)).length, content: ls.length, total: ls.length };
}
/** Bài nên học tiếp: Nhập môn trước, sau đó bài đầu tiên chưa xong */
export function nextLesson() {
  if (!S.l0) return { kind: 'l0' };
  const l = LESSONS.find(x => !lessonDone(x.id));
  return l ? { kind: 'lesson', l } : null;
}
/** Trạng thái thẻ cấp: soon | done | active | test | open */
export function levelStatus(n) {
  if (!hasContent(n)) return 'soon';
  if (n === 0) return S.l0 ? 'done' : 'active';
  if (S.passed[n]) return 'done';
  const nl = nextLesson();
  if (nl && nl.kind === 'lesson' && nl.l.lv === n) return 'active';
  const st = levelStats(n);
  return st.done === st.content ? 'test' : 'open';
}
export { LEVELS };

/* Ôn tập ngắt quãng (kiểu SM-2 rút gọn). Khóa thẻ = id từ "bài:chữ" */
export const MIN = 60e3, DAY = 864e5;
export function addCards(words) {
  let n = 0; const now = Date.now();
  update(s => words.forEach(w => { if (!s.cards[w.id]) { s.cards[w.id] = { due: now, ivl: 0, ease: 2.5, reps: 0, lapses: 0 }; n++; } }));
  return n;
}
export const dueCards = () => Object.entries(S.cards).filter(([k, c]) => WMAP[k] && c.due <= Date.now()).sort((a, b) => a[1].due - b[1].due).map(([k]) => k);
/** Lịch ôn mới của thẻ c khi chấm mức r: 1 Quên, 2 Khó, 3 Nhớ, 4 Dễ */
export function schedule(c, r) {
  const n = { ...c }, now = Date.now();
  if (r === 1) { n.ivl = 0; n.due = now + MIN; n.ease = Math.max(1.3, c.ease - 0.2); n.lapses++; n.reps = 0; return n; }
  if (r === 2) { n.ease = Math.max(1.3, c.ease - 0.15); if (c.reps === 0 || c.ivl < 1) { n.ivl = 0; n.due = now + 6 * MIN; } else { n.ivl = Math.max(1, c.ivl * 1.2); n.due = now + n.ivl * DAY; } n.reps++; return n; }
  if (r === 3) n.ivl = (c.reps === 0 || c.ivl < 1) ? 1 : c.ivl * c.ease;
  if (r === 4) { n.ivl = c.reps === 0 ? 4 : Math.max(c.ivl, 1) * c.ease * 1.3; n.ease = c.ease + 0.15; }
  n.ivl = Math.round(n.ivl * 10) / 10; n.due = now + n.ivl * DAY; n.reps++; return n;
}
export function fmtWait(ms) {
  const m = Math.round(ms / MIN);
  if (m < 60) return m <= 1 ? '< 1 phút' : `${m} phút`;
  const d = ms / DAY; if (d < 1) return `${Math.round(m / 60)} giờ`;
  if (d < 30) return `${Math.round(d)} ngày`;
  return `${Math.round(d / 30)} tháng`;
}
/** Ghi nhận một câu trả lời luyện tập */
export function recordAnswer(ok) { update(s => { s.stats.ans++; if (ok) s.stats.ok++; }); activity(); }
