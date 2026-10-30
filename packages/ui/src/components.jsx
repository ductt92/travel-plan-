import { createContext, useCallback, useContext, useRef, useState } from 'react';
import { Icon } from './Icon.jsx';

const cx = (...a) => a.filter(Boolean).join(' ');

/* Bố cục */
export function Stack({ gap = 12, as: Tag = 'div', className, style, ...rest }) {
  return <Tag className={cx('ui-stack', className)} style={{ gap, ...style }} {...rest} />;
}
export function Row({ gap = 16, between, align, wrap = true, as: Tag = 'div', className, style, ...rest }) {
  return <Tag className={cx('ui-row', className)} style={{ gap, justifyContent: between ? 'space-between' : undefined, alignItems: align, flexWrap: wrap ? 'wrap' : 'nowrap', ...style }} {...rest} />;
}

/* Nút: variant = primary | secondary | soft | light | danger | ghost; `as` để dùng với Link của router */
export function Button({ variant = 'secondary', size, icon, as: Tag = 'button', className, children, ...rest }) {
  const extra = Tag === 'button' && !rest.type ? { type: 'button' } : {};
  return (
    <Tag className={cx('ui-btn', `ui-btn--${variant}`, size === 'sm' && 'ui-btn--sm', className)} {...extra} {...rest}>
      {icon && <Icon name={icon} size={18} />}{children}
    </Tag>
  );
}
export function IconButton({ icon, label, variant, size = 44, className, as: Tag = 'button', ...rest }) {
  const extra = Tag === 'button' && !rest.type ? { type: 'button' } : {};
  return (
    <Tag className={cx('ui-iconbtn', variant && `ui-iconbtn--${variant}`, className)} aria-label={label} title={label} style={{ width: size, height: size }} {...extra} {...rest}>
      <Icon name={icon} size={Math.round(size * 0.42)} />
    </Tag>
  );
}
export function LinkButton({ icon, className, children, ...rest }) {
  return <button type="button" className={cx('ui-link', className)} {...rest}>{icon && <Icon name={icon} size={15} />}{children}</button>;
}

/* Bề mặt */
export function Card({ tone, pad = true, as: Tag = 'div', className, ...rest }) {
  return <Tag className={cx('ui-card', tone && `ui-card--${tone}`, pad && 'ui-card--pad', className)} {...rest} />;
}
export function Pill({ tone = 'grey', className, ...rest }) {
  return <span className={cx('ui-pill', `ui-pill--${tone}`, className)} {...rest} />;
}
export function Chip({ active, className, ...rest }) {
  return <button type="button" className={cx('ui-chip', active && 'is-on', className)} aria-pressed={active} {...rest} />;
}
export function Tag({ className, ...rest }) { return <span className={cx('ui-tag', className)} {...rest} />; }
export function Kbd(props) { return <kbd className="ui-kbd" {...props} />; }

/* Tiến độ: value từ 0 đến 1 */
export function ProgressBar({ value = 0, height = 6, label, className }) {
  return (
    <div className={cx('ui-bar', className)} style={{ height }} role="progressbar" aria-label={label} aria-valuemin={0} aria-valuemax={100} aria-valuenow={Math.round(value * 100)}>
      <i style={{ width: `${Math.min(100, Math.max(0, value * 100))}%` }} />
    </div>
  );
}

/* Tabs gạch chân: items = [{ id, label, done }] */
export function Tabs({ items, value, onChange, label }) {
  return (
    <nav className="ui-tabs" aria-label={label}>
      {items.map((t, i) => (
        <button key={t.id} type="button" className={value === t.id ? 'is-on' : ''} aria-current={value === t.id ? 'true' : undefined} onClick={() => onChange(t.id)}>
          {t.label}{t.done && <Icon name="check" size={16} className="ui-tabs__ok" strokeWidth="2.4" />}
        </button>
      ))}
    </nav>
  );
}

/* Ô tích có nhãn và công tắc */
export function Toggle({ id, checked, onChange, children }) {
  return <label className="ui-toggle" htmlFor={id}><input id={id} type="checkbox" checked={checked} onChange={e => onChange(e.target.checked)} />{children}</label>;
}
export function Switch({ checked, onChange, label, disabled }) {
  return <label className="ui-switch"><input type="checkbox" checked={checked} disabled={disabled} aria-label={label} onChange={e => onChange(e.target.checked)} /><span /></label>;
}
export function Field({ id, label, children }) {
  return <div className="ui-field"><label htmlFor={id}>{label}</label>{children}</div>;
}

/* Khối nội dung */
export function PageHeader({ eyebrow, title, sub, extra, size = 30 }) {
  return (
    <header className="ui-row ui-pagehead">
      <div className="ui-stack" style={{ gap: 6, minWidth: 0 }}>
        {eyebrow && <span className="ui-eyebrow">{eyebrow}</span>}
        <h1 style={{ fontSize: size }}>{title}</h1>
        {sub && <p className="ui-muted" style={{ maxWidth: '64ch' }}>{sub}</p>}
      </div>
      {extra}
    </header>
  );
}
export function Breadcrumbs({ items, LinkComponent = 'a' }) {
  return (
    <nav className="ui-crumbs" aria-label="Vị trí">
      {items.map((it, i) => (
        <span key={i} className="ui-crumbs__i">
          {i > 0 && <span aria-hidden="true">/</span>}
          {it.to ? <LinkComponent to={it.to} href={it.to}>{it.label}</LinkComponent> : <span style={{ color: i === items.length - 1 ? 'var(--ink)' : undefined }}>{it.label}</span>}
        </span>
      ))}
    </nav>
  );
}
export function StatTile({ label, value, sub }) {
  return <div className="ui-tile"><span className="ui-muted" style={{ fontSize: 13 }}>{label}</span><b className="ui-num">{value}{sub && <small className="ui-muted"> {sub}</small>}</b></div>;
}
export function EmptyState({ glyph, title, children, actions, glyphColor }) {
  return (
    <Card className="ui-empty">
      {glyph && <span className="ui-hz ui-empty__glyph" style={{ color: glyphColor }}>{glyph}</span>}
      {title && <h2 style={{ fontSize: 22 }}>{title}</h2>}
      {children}
      {actions && <Row style={{ justifyContent: 'center' }}>{actions}</Row>}
    </Card>
  );
}

/* Thông báo nhanh: bọc app trong <ToastProvider>, gọi useToast()('Đã lưu') */
const ToastCtx = createContext(() => {});
export function ToastProvider({ children }) {
  const [msg, setMsg] = useState('');
  const t = useRef();
  const show = useCallback(m => { setMsg(m); clearTimeout(t.current); t.current = setTimeout(() => setMsg(''), 2200); }, []);
  return <ToastCtx.Provider value={show}>{children}<div className="ui-toast" role="status" hidden={!msg}>{msg}</div></ToastCtx.Provider>;
}
export const useToast = () => useContext(ToastCtx);

/* Khung app: thanh bên trên desktop, thanh tab dưới trên điện thoại.
   nav = [{ to, label, short, icon, badge, active }], LinkComponent = Link của router.
   mobileBar: thanh nhỏ đầu trang chỉ hiện trên điện thoại, thay chỗ cho thanh bên bị ẩn */
export function AppShell({ brand, nav, sideExtra, footer, mobileBar, LinkComponent = 'a', children }) {
  const L = LinkComponent;
  return (
    <div className="ui-app">
      <aside className="ui-side" aria-label="Thanh bên">
        {brand}
        <nav className="ui-nav" aria-label="Điều hướng chính">
          {nav.map(n => (
            <L key={n.to} to={n.to} href={n.to} className={n.active ? 'is-on' : ''} aria-current={n.active ? 'page' : undefined}>
              <Icon name={n.icon} />{n.label}{n.badge ? <span className="ui-badge ui-num">{n.badge}</span> : null}
            </L>
          ))}
        </nav>
        {sideExtra}
        {footer}
      </aside>
      <main className="ui-main"><div className="ui-wrap">{mobileBar && <div className="ui-mbar">{mobileBar}</div>}{children}</div></main>
      <nav className="ui-tabbar" aria-label="Điều hướng chính" style={{ gridTemplateColumns: `repeat(${nav.filter(n => !n.desktopOnly).length},minmax(0,1fr))` }}>
        {nav.filter(n => !n.desktopOnly).map(n => (
          <L key={n.to} to={n.to} href={n.to} className={n.active ? 'is-on' : ''} aria-current={n.active ? 'page' : undefined}>
            <Icon name={n.icon} size={22} />{n.short || n.label}{n.badge ? <span className="ui-dot ui-num">{n.badge}</span> : null}
          </L>
        ))}
      </nav>
    </div>
  );
}
export function Brand({ mark, title, sub, href = '#', LinkComponent = 'a' }) {
  const L = LinkComponent;
  return <L className="ui-brand" to={href} href={href}><span className="ui-brand__mark">{mark}</span><span><b>{title}</b><small>{sub}</small></span></L>;
}
