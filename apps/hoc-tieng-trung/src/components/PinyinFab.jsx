// Nút nổi góc dưới bên phải: mở bảng pinyin ở bất kỳ trang nào (trừ chính trang Pinyin).
import { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Icon } from '@trang/ui';
import { PinyinChart } from '../views/PinyinView.jsx';
import './PinyinFab.css';

export function PinyinFab() {
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);
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
  return (
    <>
      <button type="button" className="pyfab" onClick={() => setOpen(true)} aria-haspopup="dialog" aria-label="Mở bảng pinyin">
        <span className="pyfab__hz" aria-hidden="true">拼</span>
        <span className="pyfab__txt">Pinyin</span>
      </button>
      <dialog ref={dlg} className="pysheet" aria-labelledby="pysheet-t" onClose={() => setOpen(false)}
        onClick={e => { if (e.target === e.currentTarget) setOpen(false); }}>
        <div className="pysheet__in">
          <header className="pysheet__head">
            <div>
              <span className="ui-eyebrow">Bảng chữ cái · 拼音表</span>
              <h2 id="pysheet-t">Bảng pinyin</h2>
            </div>
            <Link className="ui-link pysheet__more" to="/pinyin">Mở trang đầy đủ</Link>
            <button type="button" className="pysheet__x" onClick={() => setOpen(false)} aria-label="Đóng bảng pinyin"><Icon name="x" /></button>
          </header>
          <p className="ui-muted pysheet__hint">Bấm một âm tiết để nghe chữ mẫu và xem 4 thanh.</p>
          {open && <PinyinChart />}
        </div>
      </dialog>
    </>
  );
}
