// Nút nổi góc dưới bên phải: mở bảng pinyin ở bất kỳ trang nào (trừ chính trang Pinyin).
// Khung chia theo nhóm vần cho gọn, có chú thích 4 thanh và thẻ chi tiết âm tiết đang chọn.
import { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Icon } from '@trang/ui';
import { PINYIN } from '../core/data.js';
import { say } from '../core/speech.js';
import { GroupTabs, PinyinTable, SyllableCard, ToneLegend } from './PinyinKit.jsx';
import './PinyinFab.css';

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
