// Tiện ích pinyin và chữ Hán
export const MARKS = { a: 'āáǎà', e: 'ēéěè', i: 'īíǐì', o: 'ōóǒò', u: 'ūúǔù', 'ü': 'ǖǘǚǜ' };

/** Thanh điệu của một âm tiết có dấu: 1–4, 5 = thanh nhẹ */
export function toneOf(s) {
  for (const ch of s.toLowerCase()) for (const b in MARKS) { const i = MARKS[b].indexOf(ch); if (i >= 0) return i + 1; }
  return 5;
}
/** Bỏ dấu thanh: hǎo → hao */
export function bareSyl(s) {
  let o = '';
  for (const ch of s) { let r = ch; for (const b in MARKS) if (MARKS[b].includes(ch)) r = b; o += r; }
  return o;
}
/** Đặt dấu thanh t (1–5) lên âm tiết không dấu theo quy tắc a/e > ou > nguyên âm cuối */
export function markSyl(base, t) {
  if (t === 5) return base;
  let i = base.indexOf('a'); if (i < 0) i = base.indexOf('e');
  if (i < 0 && base.includes('ou')) i = base.indexOf('o');
  if (i < 0) for (let k = base.length - 1; k >= 0; k--) if ('aeiouü'.includes(base[k])) { i = k; break; }
  return i < 0 ? base : base.slice(0, i) + MARKS[base[i]][t - 1] + base.slice(i + 1);
}
export const syls = w => w.py.split(' ');
export const pyText = w => syls(w).join('');
/** Bỏ dấu tiếng Việt và pinyin để tìm kiếm không dấu */
export const fold = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
/** Câu ví dụ lưu dạng token tách bằng | */
export const plainHz = ex => ex.replace(/\|/g, '');
export const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
export const pickOne = a => a[Math.floor(Math.random() * a.length)];
export const fmtN = n => n.toLocaleString('vi-VN');
