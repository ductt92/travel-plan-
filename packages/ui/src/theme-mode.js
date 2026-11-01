// Giao diện sáng / tối cho cả site, giống glass-mode.js.
//
// Lựa chọn lưu ở localStorage['theme']: 'light' | 'dark', không có là theo cài đặt của máy.
// Khi chọn, <html> có data-theme="light|dark"; tokens.css và GlassRoot đổi màu theo thuộc tính đó.
// Trang đặt sẵn data-theme trước khi vẽ (script nhỏ trong index.html) để khỏi nháy.
const KEY = 'theme';
const listeners = new Set();

function read() {
  try { const v = localStorage.getItem(KEY); return v === 'light' || v === 'dark' ? v : 'auto'; } catch { return 'auto'; }
}

function apply(mode) {
  if (mode === 'auto') delete document.documentElement.dataset.theme;
  else document.documentElement.dataset.theme = mode;
}

let current = read();
apply(current);

/** 'auto' | 'light' | 'dark' */
export function getThemeMode() {
  return current;
}

export function setThemeMode(mode) {
  current = mode;
  try { mode === 'auto' ? localStorage.removeItem(KEY) : localStorage.setItem(KEY, mode); } catch { /* chỉ đổi trang này */ }
  apply(mode);
  listeners.forEach(fn => fn());
}

export function subscribeTheme(fn) {
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
