// Gốc giao diện kính: bọc app trong ConfigProvider của liquidglass-ui.
//
// Màu nhấn mặc định là var(--accent) của chính app, nên mỗi trang giữ tông riêng
// mà không phải lặp lại mã màu. Sáng/tối theo :root[data-theme] nếu trang có đặt,
// còn không thì theo cài đặt của máy — giống tokens.css. Nhãn có sẵn của thư viện
// (Đóng, Hủy, hiện mật khẩu…) bằng tiếng Việt.
import { useEffect, useState } from 'react';
import { ConfigProvider, viVN } from 'liquidglass-ui';
import 'liquidglass-ui/styles.css';

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
