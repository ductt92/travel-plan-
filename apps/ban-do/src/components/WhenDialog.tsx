import { useState } from 'react';
import { pad } from '@/lib/format';
import { allYears, tripMonths, tripsOfYear } from '@/lib/period';
import { useDialog } from '@/lib/use-dialog';
import type { Entries, Period } from '@/lib/types';

const YEAR_MIN = 2000;

interface Props {
  open: boolean;
  period: Period;
  entries: Entries;
  onClose: () => void;
  onPick: (year: number | null, month: number | null) => void;
}

export default function WhenDialog({ open, onClose, ...rest }: Props) {
  const { ref, onBackdropClick } = useDialog(open, onClose);

  return (
    <dialog id="dlg-when" ref={ref} onClick={onBackdropClick} aria-labelledby="when-title">
      {/* chỉ dựng khi mở, nên mỗi lần mở là năm đang xem quay về năm đang lọc */}
      {open && <Body onClose={onClose} {...rest} />}
    </dialog>
  );
}

function Body({ period, entries, onClose, onPick }: Omit<Props, 'open'>) {
  const [pickYear, setPickYear] = useState(
    () => period.year || allYears(entries)[0] || new Date().getFullYear(),
  );
  const yearMax = new Date().getFullYear() + 2;
  const has = tripMonths(entries);
  const n = tripsOfYear(entries, pickYear);

  const choose = (year: number | null, month: number | null) => {
    onPick(year, month);
    onClose();
  };

  return (
    <div className="dlg">
      <div className="dlg-head plain">
        <div className="row">
          <div>
            <h3 id="when-title">Chọn thời gian</h3>
            <p className="meta">
              Một tháng hay cả năm đều được — bản đồ, thống kê và nhật ký lọc theo đúng khoảng đó.
            </p>
          </div>
          <button className="x" aria-label="Đóng" onClick={onClose}>✕</button>
        </div>
      </div>

      <div className="dlg-body">
        <div className="ym">
          <button
            type="button" aria-label="Năm trước"
            disabled={pickYear <= YEAR_MIN} onClick={() => setPickYear(y => y - 1)}
          >‹</button>
          <b>{pickYear}</b>
          <button
            type="button" aria-label="Năm sau"
            disabled={pickYear >= yearMax} onClick={() => setPickYear(y => y + 1)}
          >›</button>
        </div>

        <button
          type="button"
          className={`whole${period.year === pickYear && !period.month ? ' on' : ''}`}
          onClick={() => choose(pickYear, null)}
        >Cả năm {pickYear}</button>

        <div className="months" role="group" aria-label="Chọn tháng">
          {Array.from({ length: 12 }, (_, i) => i + 1).map(m => {
            const on = period.year === pickYear && period.month === m;
            return (
              <button
                key={m} type="button" className={on ? 'on' : ''} aria-pressed={on}
                onClick={() => choose(pickYear, m)}
              >
                Tháng {m}
                {has.has(`${pickYear}-${pad(m)}`) && <i />}
              </button>
            );
          })}
        </div>
      </div>

      <div className="dlg-acts">
        <span className="acts-note">
          {n ? `${pickYear} có ${n} chuyến` : `${pickYear} chưa có chuyến nào`}
        </span>
        <button type="button" className="btn" onClick={() => choose(null, null)}>
          Tất cả thời gian
        </button>
      </div>
    </div>
  );
}
