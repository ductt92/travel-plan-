// Gốc giao diện kính: bọc app trong ConfigProvider của react-liquis-glass.
//
// Màu nhấn mặc định là var(--accent) của chính app, nên mỗi trang giữ tông riêng
// mà không phải lặp lại mã màu. Sáng/tối theo :root[data-theme] nếu trang có đặt,
// còn không thì theo cài đặt của máy — giống tokens.css. Nhãn có sẵn của thư viện
// (Đóng, Hủy, hiện mật khẩu…) bằng tiếng Việt.
import { useEffect, useState, useSyncExternalStore } from 'react';
import { Button, ConfigProvider, viVN } from 'react-liquis-glass';
import { SparklesIcon } from 'react-liquis-glass/icons';
import 'react-liquis-glass/styles.css';
import './glass.css';
import { getGlass, setGlass, subscribe } from './glass-mode.js';

export { getGlass, setGlass };

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
  const label = on ? 'Tắt hiệu ứng kính' : 'Bật hiệu ứng kính';
  return (
    <Button
      variant="glass" size="sm" {...rest}
      className={`glass-toggle ${className}`.trim()}
      icon={<SparklesIcon />}
      aria-pressed={on} aria-label={compact ? label : undefined} title={label}
      onClick={() => setGlass(!on)}
    >
      {!compact && <>Kính <span className="glass-toggle__dot" aria-hidden="true" /></>}
    </Button>
  );
}
