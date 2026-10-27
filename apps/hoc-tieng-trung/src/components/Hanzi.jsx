// Component riêng của app học: hiển thị chữ Hán, pinyin tô màu theo thanh, thẻ từ.
import { Link } from 'react-router-dom';
import { Icon, IconButton, LinkButton, Pill } from '@trang/ui';
import { syls, toneOf, plainHz } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { useStore } from '../core/store.js';

/** Chữ Hán với font Noto Serif SC */
export function Hz({ children, size, className = '', style, ...rest }) {
  return <span className={`ui-hz ${className}`} style={{ fontSize: size, ...style }} {...rest}>{children}</span>;
}
/** Pinyin của một từ, mỗi âm tiết tô màu theo thanh điệu (class t1..t5) */
export function Py({ w, text, size, className = '' }) {
  const parts = text ? text.split(' ') : syls(w);
  return <span className={`ui-py ${className}`} style={{ fontSize: size }}>{parts.map((s, i) => <span key={i} className={`t${toneOf(s)}`}>{s}</span>)}</span>;
}
/** Âm Hán Việt viết hoa nhỏ */
export function Hv({ children, style }) { return <span className="hv" style={style}>{children}</span>; }
/** Nút loa đọc một câu tiếng Trung */
export function SayButton({ text, label, size = 44, variant }) {
  return <IconButton icon="sound" label={label || `Nghe ${text}`} size={size} variant={variant} onClick={() => say(text)} />;
}

/** Thẻ từ mới: chữ, pinyin, Hán Việt, nghĩa, câu ví dụ, nút nghe và tập viết */
export function WordCard({ w }) {
  const S = useStore();
  return (
    <article className="word">
      <div className="word__top">
        <div className="ui-stack" style={{ gap: 2 }}>
          <Hz className="word__hz">{w.hz}</Hz>
          {S.showPy && <Py w={w} size={17} />}
        </div>
        <SayButton text={w.hz} />
      </div>
      <div className="ui-stack" style={{ gap: 0 }}><Hv>{w.hv}</Hv><b style={{ fontSize: 16 }}>{w.vi}</b></div>
      <Example zh={plainHz(w.ex)} py={w.exPy} vi={w.exVi} />
      <div className="word__act">
        <LinkButton icon="play" onClick={() => say(plainHz(w.ex))}>Nghe câu</LinkButton>
        <Link className="ui-link" to={`/write/${encodeURIComponent([...w.hz][0])}`}><Icon name="brush" size={15} />Tập viết</Link>
        {S.cards[w.id] && <Pill tone="jade" style={{ marginLeft: 'auto', alignSelf: 'center' }}>Đang ôn</Pill>}
      </div>
    </article>
  );
}
/** Câu ví dụ: chữ Hán, pinyin, nghĩa (ẩn/hiện theo cài đặt) */
export function Example({ zh, py, vi, size = 17 }) {
  const S = useStore();
  return (
    <div className="ex">
      <Hz size={size}>{zh}</Hz>
      {S.showPy && py && <span className="ui-py ex__py">{py}</span>}
      {S.showVi && vi && <span>{vi}</span>}
    </div>
  );
}
