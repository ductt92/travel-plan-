// Gốc giao diện kính: bọc app trong ConfigProvider của react-liquis-glass.
//
// Màu nhấn mặc định là var(--accent) của chính app, nên mỗi trang giữ tông riêng
// mà không phải lặp lại mã màu. Sáng/tối theo :root[data-theme] nếu trang có đặt,
// còn không thì theo cài đặt của máy — giống tokens.css. Nhãn có sẵn của thư viện
// (Đóng, Hủy, hiện mật khẩu…) bằng tiếng Việt.
import { useEffect, useState, useSyncExternalStore } from 'react';
import { Button, ConfigProvider, viVN } from 'react-liquis-glass';
import { MoonIcon, SparklesIcon, SunIcon } from 'react-liquis-glass/icons';
import 'react-liquis-glass/styles.css';
import './glass.css';
import { getGlass, setGlass, subscribe } from './glass-mode.js';
import { getThemeMode, setThemeMode, subscribeTheme } from './theme-mode.js';

export { getGlass, setGlass, getThemeMode, setThemeMode };

const dark = matchMedia('(prefers-color-scheme: dark)');

function currentTheme() {
  const set = document.documentElement.dataset.theme;
  return set === 'dark' || set === 'light' ? set : dark.matches ? 'dark' : 'light';
}

function useTheme() {
  const [theme, setTheme] = useState(currentTheme);
  useEffect(() => {
    const update = () => setTheme(currentTheme());
    dark.addEventListener('change', update);
    const obs = new MutationObserver(update);
    obs.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    return () => { dark.removeEventListener('change', update); obs.disconnect(); };
  }, []);
  return theme;
}

const ROOT = { display: 'contents', font: 'inherit', color: 'inherit' };

export function GlassRoot({ accent = 'var(--accent)', children, ...tokens }) {
  // display:contents để lớp bọc không chen vào bố cục của app (biến CSS vẫn kế thừa);
  // .lg-root còn đặt phông, cỡ chữ, màu chữ cho mọi thứ bên trong — trả lại cho app,
  // component của thư viện tự đặt lấy kiểu chữ của nó
  return (
    <ConfigProvider theme={useTheme()} accent={accent} locale={viVN} style={ROOT} {...tokens}>
      {children}
    </ConfigProvider>
  );
}

/** true khi giao diện kính đang bật (theo nút bật/tắt dùng chung cả site). */
export function useGlass() {
  return useSyncExternalStore(subscribe, getGlass);
}

/** Nút bật/tắt kính. `compact` chỉ hiện biểu tượng (vẫn có nhãn cho trình đọc màn hình). */
export function GlassToggle({ compact = false, className = '', ...rest }) {
  const on = useGlass();
  const label = on ? 'Tắt Liquis glass' : 'Bật Liquis glass';
  return (
    <Button
      variant="glass" size="sm" {...rest}
      className={`glass-toggle ${className}`.trim()}
      icon={<SparklesIcon />}
      aria-pressed={on} aria-label={compact ? label : undefined} title={label}
      onClick={() => setGlass(!on)}
    >
      {!compact && <>Liquis glass: {on ? 'on' : 'off'} <span className="glass-toggle__dot" aria-hidden="true" /></>}
    </Button>
  );
}

const THEME_NEXT = { auto: 'light', light: 'dark', dark: 'auto' };
const THEME_LABEL = { auto: 'Theo máy', light: 'Sáng', dark: 'Tối' };

/** 'auto' | 'light' | 'dark' — lựa chọn sáng/tối dùng chung cả site */
export function useThemeMode() {
  return useSyncExternalStore(subscribeTheme, getThemeMode);
}

/** Nút đổi giao diện: Theo máy → Sáng → Tối → Theo máy. Biểu tượng theo giao diện đang hiện. */
export function ThemeToggle({ compact = false, className = '', ...rest }) {
  const mode = useThemeMode();
  const shown = useTheme();
  const label = `Giao diện: ${THEME_LABEL[mode]} (bấm để đổi sang ${THEME_LABEL[THEME_NEXT[mode]]})`;
  return (
    <Button
      variant="glass" size="sm" {...rest}
      className={`theme-toggle ${className}`.trim()}
      icon={shown === 'dark' ? <MoonIcon /> : <SunIcon />}
      aria-label={compact ? label : undefined} title={label}
      onClick={() => setThemeMode(THEME_NEXT[mode])}
    >
      {!compact && <>Giao diện: {THEME_LABEL[mode]}</>}
    </Button>
  );
}
