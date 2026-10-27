// Nút nổi góc dưới bên phải: mở bảng pinyin ở bất kỳ trang nào (trừ chính trang Pinyin).
// Khung chia theo nhóm vần cho gọn, có chú thích 4 thanh và thẻ chi tiết âm tiết đang chọn.
import { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Icon } from '@trang/ui';
import { PINYIN } from '../core/data.js';
import { toneOf, markSyl } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { PinyinTable } from '../views/PinyinView.jsx';
import './PinyinFab.css';

const TABS = [
  { id: 0, label: 'a o e', sub: 'Vần đơn, kép' },
  { id: 1, label: 'i', sub: 'Bắt đầu bằng i' },
  { id: 2, label: 'u', sub: 'Bắt đầu bằng u' },
  { id: 3, label: 'ü', sub: 'Bắt đầu bằng ü' },
  { id: null, label: 'Tất cả', sub: 'Cả bảng' }
];
const TONES = [
  { t: 1, mark: 'ā', name: 'Ngang', hint: 'cao, đều' },
  { t: 2, mark: 'á', name: 'Lên', hint: 'như dấu sắc' },
  { t: 3, mark: 'ǎ', name: 'Xuống – lên', hint: 'như dấu hỏi' },
  { t: 4, mark: 'à', name: 'Xuống', hint: 'dứt khoát' }
];

// Thẻ âm tiết đang chọn: chữ mẫu lớn, 4 thanh bấm để nghe
function Focus({ sel }) {
  if (!sel) return (
    <div className="pyf pyf--empty">
      <span className="pyf__ghost" aria-hidden="true">音</span>
      <div>
        <b>Chọn một âm tiết bên dưới</b>
        <p>Nghe chữ mẫu và xem âm tiết đó ở cả 4 thanh.</p>
      </div>
    </div>
  );
  const [sp, key] = sel;
  const [ch, py, vi] = PINYIN[key];
  return (
    <div className="pyf" aria-live="polite">
      <button type="button" className="pyf__hz" onClick={() => say(ch)} aria-label={`Nghe ${ch}`}>
        <span lang="zh">{ch}</span>
        <Icon name="sound" size={16} />
      </button>
      <div className="pyf__main">
        <span className="pyf__label">Âm tiết</span>
        <b className="pyf__sp">{sp}</b>
        <span className="pyf__ex"><span className={`t${toneOf(py)}`}>{py}</span> · {vi}</span>
      </div>
      <div className="pyf__tones" role="group" aria-label="Bốn thanh">
        {[1, 2, 3, 4].map(t => <span key={t} className={`pyf__tone t${t}`}>{markSyl(sp, t)}</span>)}
      </div>
      <Link className="pyf__write" to={`/write/${encodeURIComponent(ch)}`}><Icon name="brush" size={15} />Tập viết</Link>
    </div>
  );
}

export function PinyinFab() {
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);
  const [tab, setTab] = useState(0);
  const [sel, setSel] = useState(null);
  const dlg = useRef(null);

  // <dialog> lo phần khóa tiêu điểm, nút Esc và lớp phủ
  useEffect(() => {
    const d = dlg.current;
    if (!d) return;
    if (open && !d.open) d.showModal();
    if (!open && d.open) d.close();
  }, [open]);
  useEffect(() => setOpen(false), [pathname]);

  if (pathname.startsWith('/pinyin')) return null;
  const pick = r => { setSel(r); say(PINYIN[r[1]][0]); };

  return (
    <>
      <button type="button" className="pyfab" onClick={() => setOpen(true)} aria-haspopup="dialog" aria-label="Mở bảng pinyin">
        <span className="pyfab__hz" aria-hidden="true">拼</span>
        <span className="pyfab__txt">Pinyin</span>
      </button>
      <dialog ref={dlg} className="pysheet" aria-labelledby="pysheet-t" onClose={() => setOpen(false)}
        onClick={e => { if (e.target === e.currentTarget) setOpen(false); }}>
        <div className="pysheet__grip" aria-hidden="true" />
        <header className="pysheet__head">
          <span className="pysheet__seal" aria-hidden="true">拼<br />音</span>
          <div className="pysheet__title">
            <span className="pysheet__eyebrow">Bảng chữ cái tiếng Trung</span>
            <h2 id="pysheet-t">Bảng pinyin</h2>
          </div>
          <button type="button" className="pysheet__x" onClick={() => setOpen(false)} aria-label="Đóng bảng pinyin"><Icon name="x" /></button>
        </header>

        <div className="pysheet__body">
          <ul className="pysheet__legend" aria-label="Bốn thanh điệu">
            {TONES.map(x => (
              <li key={x.t} className={`t${x.t}`}>
                <b>{x.mark}</b>
                <span><strong>Thanh {x.t}</strong> {x.name}<small>{x.hint}</small></span>
              </li>
            ))}
          </ul>

          {open && <Focus sel={sel} />}

          <div className="pysheet__tabs" role="tablist" aria-label="Nhóm vần">
            {TABS.map(t => (
              <button key={String(t.id)} type="button" role="tab" aria-selected={tab === t.id} className={tab === t.id ? 'is-on' : ''} onClick={() => setTab(t.id)}>
                <b>{t.label}</b><small>{t.sub}</small>
              </button>
            ))}
          </div>

          <div className="pysheet__table" role="tabpanel">
            {open && <PinyinTable group={tab} sel={sel} onPick={pick} />}
          </div>

          <p className="pysheet__foot">
            <Icon name="grid" size={15} /> Muốn xem quy tắc viết y, w và ü? <Link to="/pinyin">Mở trang Bảng pinyin</Link>
          </p>
        </div>
      </dialog>
    </>
  );
}
