// Bật/tắt giao diện kính cho cả site.
//
// Lựa chọn lưu ở localStorage['glass'] ('on' | 'off'), dùng chung cho mọi trang cùng
// tên miền (trang chủ, Hán Lộ, bản đồ, HSK 6, lớp học, sổ tay). Khi tắt, <html> có
// data-glass="off"; CSS của từng trang đổi mặt kính thành mặt đặc theo thuộc tính đó.
// Mặc định là bật nên lúc bật không cần thuộc tính nào. Trang tĩnh dùng bản không cần
// bundler ở packages/ui/static/glass.js (cùng khóa, cùng thuộc tính).
const KEY = 'glass';
const listeners = new Set();

function read() {
  try { return localStorage.getItem(KEY) !== 'off'; } catch { return true; }
}

function apply(on) {
  if (on) delete document.documentElement.dataset.glass;
  else document.documentElement.dataset.glass = 'off';
}

let current = read();
apply(current);

export function getGlass() {
  return current;
}

export function setGlass(on) {
  current = on;
  try { localStorage.setItem(KEY, on ? 'on' : 'off'); } catch { /* trình duyệt chặn bộ nhớ: chỉ đổi trang này */ }
  apply(on);
  listeners.forEach(fn => fn());
}

export function subscribe(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

// đổi ở tab khác thì tab này đổi theo
addEventListener('storage', e => {
  if (e.key !== KEY) return;
  current = read();
  apply(current);
  listeners.forEach(fn => fn());
});
