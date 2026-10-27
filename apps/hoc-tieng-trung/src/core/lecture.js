// Dựng kịch bản bài giảng từ dữ liệu bài: danh sách trang (slides) và các bước đọc (steps).
// Mỗi bước: { s: chỉ số trang, lang: 'vi' | 'zh' | 'mix', text, reveal: mức hiện nội dung trên trang }.
import { LEVELS } from './data.js';
import { plainHz } from './pinyin.js';

const CJK_RUN = /([㐀-鿿　-〿！-？“”…·]+)/;
export const PINYIN_ONLY = /\S*[āǎēěīǐōǒūǔǖǘǚǜ]\S*/g;

/** Tách câu lẫn Việt – Trung thành các đoạn để đọc bằng hai giọng */
export function splitMix(text) {
  return text.split(CJK_RUN).map(t => t.trim()).filter(Boolean)
    .map(t => (CJK_RUN.test(t) && /[㐀-鿿]/.test(t) ? { lang: 'zh', text: t } : { lang: 'vi', text: t.replace(PINYIN_ONLY, '').replace(/\s+/g, ' ').trim() }))
    .filter(p => /[\p{L}\p{N}]/u.test(p.text));
}
/** Các đoạn thực sự được đọc cho một bước */
export function stepParts(st) {
  if (st.lang === 'mix') return splitMix(st.text);
  return [{ lang: st.lang, text: st.lang === 'vi' ? st.text.replace(PINYIN_ONLY, '').trim() : st.text }];
}

export function buildLecture(l) {
  const slides = [], steps = [], L = LEVELS[l.lv];
  const add = sl => { slides.push(sl); return slides.length - 1; };
  const say = (s, lang, text, reveal = 0) => { if (text) steps.push({ s, lang, text, reveal }); };
  let s = add({ kind: 'title', ch: 'Mở đầu' });
  say(s, 'vi', `${L.name}, bài ${l.no}. ${l.title}.`); say(s, 'zh', l.zh, 1); say(s, 'vi', l.lecture.intro, 1);
  say(s, 'vi', 'Học xong bài này, bạn có thể: ' + l.goal.join('. ') + '.', 2);
  l.words.forEach((w, i) => {
    s = add({ kind: 'word', w, i, n: l.words.length, ch: i === 0 ? 'Từ mới' : null });
    say(s, 'zh', w.hz, 0); say(s, 'vi', `${w.vi}. Âm Hán Việt: ${w.hv}.`, 1); say(s, 'zh', w.hz, 1);
    say(s, 'vi', 'Ví dụ.', 2); say(s, 'zh', plainHz(w.ex), 2); say(s, 'vi', w.exVi, 2);
  });
  l.lecture.tips.forEach((t, i) => { s = add({ kind: 'tip', t, i, n: l.lecture.tips.length, ch: i === 0 ? 'Mẹo nhớ' : null }); say(s, 'mix', t, 0); });
  l.grammar.forEach((g, gi) => {
    s = add({ kind: 'grammar', g, gi, n: l.grammar.length, ch: gi === 0 ? 'Ngữ pháp' : null });
    say(s, 'mix', `Ngữ pháp ${gi + 1}. ${g.title}.`, 0);
    g.ex.forEach((e, k) => { say(s, 'zh', e[0], k + 1); say(s, 'vi', e[2], k + 1); });
    say(s, 'mix', g.note, g.ex.length + 1);
  });
  l.dialogs.forEach((d, di) => {
    s = add({ kind: 'dialog', d, di, ch: di === 0 ? 'Hội thoại' : null });
    say(s, 'vi', `Hội thoại ${di + 1}. ${d.title}.`, 0);
    d.lines.forEach((x, k) => { say(s, 'zh', x[1], k + 1); say(s, 'vi', x[3], k + 1); });
  });
  s = add({ kind: 'outro', ch: 'Tổng kết' });
  say(s, 'vi', l.lecture.outro, 0);
  return { slides, steps };
}

/** Kịch bản dạng chữ để dựng video với người dẫn ảo */
export function lectureScript(l, { slides, steps }) {
  const out = [`BÀI GIẢNG · ${LEVELS[l.lv].name} · Bài ${l.no}: ${l.title} (${l.zh})`, ''];
  let last = -1;
  steps.forEach(st => {
    if (st.s !== last) { const sl = slides[st.s]; last = st.s; out.push('', `--- Trang ${st.s + 1}${sl.ch ? ' · ' + sl.ch : ''} ---`); }
    out.push(`${st.lang === 'zh' ? '[Đọc tiếng Trung]' : '[Giảng]'} ${st.text}`);
  });
  return out.join('\n');
}
