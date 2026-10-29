export const pad = (n: number) => String(n).padStart(2, '0');

const parse = (s: string) => {
  const [y, m, d] = s.split('-').map(Number);
  return new Date(y, m - 1, d);
};

/** '03/10/2026', '03–04/10/2026' hay '30/09 – 02/10/2026' tuỳ chuyến dài ngắn. */
export function fmtRange(from: string, to: string) {
  if (!from) return 'Chưa rõ ngày';
  const a = parse(from);
  const b = to ? parse(to) : a;
  const sameMonth = a.getMonth() === b.getMonth() && a.getFullYear() === b.getFullYear();
  if (+a === +b) return `${pad(a.getDate())}/${pad(a.getMonth() + 1)}/${a.getFullYear()}`;
  if (sameMonth) return `${pad(a.getDate())}–${pad(b.getDate())}/${pad(b.getMonth() + 1)}/${b.getFullYear()}`;
  return `${pad(a.getDate())}/${pad(a.getMonth() + 1)} – ${pad(b.getDate())}/${pad(b.getMonth() + 1)}/${b.getFullYear()}`;
}

export function nights(from: string, to: string) {
  if (!from || !to) return '';
  const n = Math.round((+parse(to) - +parse(from)) / 86400000);
  return n > 0 ? `${n + 1} ngày ${n} đêm` : '';
}

export const stars = (n: number) => (n ? '★'.repeat(n) + '☆'.repeat(5 - n) : '');

/**
 * Bỏ dấu để gõ 'da nang' vẫn ra 'Đà Nẵng'. Phải hạ chữ thường trước: 'Đ' hoa không
 * tách dấu được bằng NFD, để nguyên thì 'Đà Nẵng' ra 'đa nang' chứ không ra 'da nang'.
 */
export const noMark = (s: string) =>
  s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd');

/** 'Tháng 10' / 'năm 2026' — nhãn ngắn cho ô ngày tháng trong nhật ký. */
export const monthOf = (from: string) => (from ? `Tháng ${+from.slice(5, 7)}` : '—');
export const yearOf = (from: string) => (from ? +from.slice(0, 4) : null);
