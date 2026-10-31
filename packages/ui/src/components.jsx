import {
  Breadcrumb, Button as GlassButton, Card as GlassCard, Checkbox, IconButton as GlassIconButton, Progress,
  Switch as GlassSwitch, Tabs as GlassTabs, Tag as GlassTag, message
} from 'react-liquis-glass';
import { Icon } from './Icon.jsx';

const cx = (...a) => a.filter(Boolean).join(' ');

// Thẻ, nút, nhãn, tab, công tắc, thanh tiến độ, thông báo là component của react-liquis-glass; ở đây chỉ giữ
// props cũ của @trang/ui để các view không phải sửa. Nút nhận as={Link} to="/…" để chuyển trang.

/* Bố cục */
export function Stack({ gap = 12, as: Tag = 'div', className, style, ...rest }) {
  return <Tag className={cx('ui-stack', className)} style={{ gap, ...style }} {...rest} />;
}
export function Row({ gap = 16, between, align, wrap = true, as: Tag = 'div', className, style, ...rest }) {
  return <Tag className={cx('ui-row', className)} style={{ gap, justifyContent: between ? 'space-between' : undefined, alignItems: align, flexWrap: wrap ? 'wrap' : 'nowrap', ...style }} {...rest} />;
}

/* Nút: variant = primary | secondary | soft | light | danger | ghost; as={Link} to="/…" để chuyển trang */
const BUTTON = {
  primary: { variant: 'filled', color: 'primary' },
  secondary: { variant: 'glass' },
  soft: { variant: 'tinted', color: 'primary' },
  light: { variant: 'filled', className: 'ui-btn--light' },
  danger: { variant: 'filled', color: 'danger' },
  ghost: { variant: 'text' }
};
export function Button({ variant = 'secondary', size, icon, className, ...rest }) {
  const v = BUTTON[variant] || BUTTON.secondary;
  // cỡ mặc định của thư viện (38px) nhỏ hơn vùng chạm 44px của app, nên cỡ thường dùng lg, cỡ sm dùng md
  return (
    <GlassButton variant={v.variant} color={v.color} size={size === 'sm' ? 'md' : 'lg'}
      icon={icon && <Icon name={icon} size={18} />} className={cx('ui-btn', v.className, className)} {...rest} />
  );
}
const ICON_BUTTON = { plain: 'text', solid: 'filled', ondark: 'outline' };
export function IconButton({ icon, label, variant, size = 44, className, style, ...rest }) {
  return (
    <GlassIconButton variant={ICON_BUTTON[variant] || 'glass'} color={variant === 'solid' ? 'primary' : undefined}
      icon={<Icon name={icon} size={Math.round(size * 0.42)} />} aria-label={label} title={label}
      className={cx('ui-iconbtn', variant && `ui-iconbtn--${variant}`, className)} style={{ width: size, height: size, ...style }} {...rest} />
  );
}
export function LinkButton({ icon, className, ...rest }) {
  return <GlassButton variant="link" color="primary" size="sm" icon={icon && <Icon name={icon} size={15} />} className={cx('ui-link', className)} {...rest} />;
}

/* Bề mặt: Card của thư viện ở dạng bare (không có lớp .lg-card-body), vì nhiều chỗ đặt bố cục
   ui-stack/ui-row thẳng lên thẻ. tone = dark | muted | accent; thẻ tối và thẻ mờ không dùng mặt kính */
export function Card({ tone, pad = true, className, ...rest }) {
  return <GlassCard bare variant={tone === 'dark' || tone === 'muted' ? 'plain' : 'glass'}
    className={cx('ui-card', tone && `ui-card--${tone}`, pad && 'ui-card--pad', className)} {...rest} />;
}
const PILL = { jade: 'primary', seal: 'var(--seal)', grey: 'default' };
export function Pill({ tone = 'grey', ...rest }) {
  return tone === 'solid'
    ? <GlassTag variant="filled" color="primary" size="sm" {...rest} />
    : <GlassTag color={PILL[tone] || 'default'} size="sm" {...rest} />;
}
/* Chip là nút bấm được (lọc, chọn), nên dùng nút tròn của thư viện; đang chọn thì tô màu */
export function Chip({ active, className, ...rest }) {
  return <GlassButton shape="round" size="md" variant={active ? 'filled' : 'glass'} color={active ? 'primary' : undefined}
    aria-pressed={active} className={cx('ui-chip', className)} {...rest} />;
}
export function Tag(props) { return <GlassTag size="sm" {...props} />; }
export function Kbd(props) { return <kbd className="ui-kbd" {...props} />; }

/* Tiến độ: value từ 0 đến 1 */
export function ProgressBar({ value = 0, height = 6, label, className }) {
  return <Progress percent={Math.min(100, Math.max(0, value * 100))} size={height} showInfo={false} status="normal"
    aria-label={label} className={cx('ui-bar', className)} />;
}

/* Tabs gạch chân: items = [{ id, label, done }] */
export function Tabs({ items, value, onChange, label }) {
  return (
    <GlassTabs className="ui-tabs" aria-label={label} activeKey={value} onChange={onChange}
      items={items.map(t => ({ key: t.id, label: <>{t.label}{t.done && <Icon name="check" size={16} className="ui-tabs__ok" strokeWidth="2.4" />}</> }))} />
  );
}

/* Ô tích có nhãn và công tắc */
export function Toggle({ id, checked, onChange, children }) {
  return <Checkbox id={id} checked={checked} onChange={v => onChange(v)} className="ui-toggle">{children}</Checkbox>;
}
export function Switch({ checked, onChange, label, disabled }) {
  return <GlassSwitch checked={checked} disabled={disabled} aria-label={label} onChange={onChange} />;
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
// Breadcrumb của thư viện chỉ nhận href (chưa có as); app dùng HashRouter nên to="/x" thành href="#/x"
export function Breadcrumbs({ items }) {
  return <Breadcrumb className="ui-crumbs" items={items.map(it => ({ title: it.label, href: it.to != null ? `#${it.to}` : undefined }))} />;
}
export function StatTile({ label, value, sub }) {
  return <div className="ui-tile lg-glass"><span className="ui-muted" style={{ fontSize: 13 }}>{label}</span><b className="ui-num">{value}{sub && <small className="ui-muted"> {sub}</small>}</b></div>;
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

/* Thông báo nhanh: message của thư viện. Giữ <ToastProvider> và useToast()('Đã lưu') cho code cũ */
const toast = m => message.info(m, 2.2);
export function ToastProvider({ children }) { return children; }
export const useToast = () => toast;

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
