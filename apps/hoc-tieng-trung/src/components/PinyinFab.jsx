// Nút nổi góc dưới bên phải: mở bảng pinyin ở bất kỳ trang nào (trừ chính trang Pinyin).
// Khung chia theo nhóm vần cho gọn, có chú thích 4 thanh và thẻ chi tiết âm tiết đang chọn.
import { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Icon, IconButton } from '@trang/ui';
import { PINYIN } from '../core/data.js';
import { say } from '../core/speech.js';
import { GroupTabs, PinyinTable, SyllableCard, ToneLegend } from './PinyinKit.jsx';
import './PinyinFab.css';

// Thứ bấm được nằm dưới nút nổi: nút, link, ô nhập… Thẻ lớn bấm được (thẻ cấp, thẻ bài) thì bỏ qua,
// vì nút chỉ che một góc thẻ, vẫn bấm được phần còn lại.
const CONTROL = 'a,button,input,select,textarea,label,summary,[role="button"],[role="tab"],[tabindex]:not([tabindex="-1"])';
function coversControl(fab) {
  const r = fab.getBoundingClientRect();
  if (!r.width) return false;
  const pts = [[r.left + r.width / 2, r.top + r.height / 2], [r.left + 6, r.top + 6], [r.right - 6, r.top + 6], [r.left + 6, r.bottom - 6], [r.right - 6, r.bottom - 6]];
  for (const [x, y] of pts) {
    for (const el of document.elementsFromPoint(x, y)) {
      if (fab.contains(el)) continue;
      const c = el.closest(CONTROL);
      if (!c || c.closest('.ui-tabbar')) continue;
      const b = c.getBoundingClientRect();
      if (b.width * b.height < r.width * r.height * 4) return true;
    }
  }
  return false;
}

/** Nút nổi che mất nút khác (nút của trình phát bài giảng…) thì tạm lánh đi; cuộn qua là hiện lại */
function useAway(ref, on) {
  const [away, setAway] = useState(false);
  useEffect(() => {
    if (!on) return;
    let raf = 0;
    const check = () => { raf = 0; if (ref.current) setAway(coversControl(ref.current)); };
    const soon = () => { if (!raf) raf = requestAnimationFrame(check); };
    check();
    // nội dung đổi mà không cuộn (đổi tab, mở bài) thì lần kiểm tra định kỳ bắt được
    const t = setInterval(soon, 700);
    addEventListener('scroll', soon, { passive: true });
    addEventListener('resize', soon);
    return () => { clearInterval(t); cancelAnimationFrame(raf); removeEventListener('scroll', soon); removeEventListener('resize', soon); };
  }, [ref, on]);
  return on && away;
}

export function PinyinFab() {
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);
  const [tab, setTab] = useState(0);
  const [sel, setSel] = useState(null);
  const dlg = useRef(null);
  const fab = useRef(null);
  const away = useAway(fab, !open && !pathname.startsWith('/pinyin'));

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
      <button type="button" ref={fab} className={`pyfab${away ? ' is-away' : ''}`} onClick={() => setOpen(true)} aria-haspopup="dialog" aria-label="Mở bảng pinyin">
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
          <IconButton icon="x" label="Đóng bảng pinyin" className="pysheet__x" onClick={() => setOpen(false)} />
        </header>

        <div className="pysheet__body">
          <ToneLegend />

          {open && <SyllableCard sel={sel} />}

          <GroupTabs value={tab} onChange={setTab} />

          {open && <PinyinTable group={tab} sel={sel} onPick={pick} />}

          <p className="pysheet__foot">
            <Icon name="grid" size={15} /> Muốn xem quy tắc viết y, w và ü? <Link to="/pinyin">Mở trang Bảng pinyin</Link>
          </p>
        </div>
      </dialog>
    </>
  );
}
