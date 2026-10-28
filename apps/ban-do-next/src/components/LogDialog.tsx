'use client';

import { Fragment } from 'react';
import WhenButton from './WhenButton';
import { BookIcon } from './icons';
import { byCode } from '@/lib/map-data';
import { monthOf, yearOf } from '@/lib/format';
import { scopeLabel } from '@/lib/period';
import { useDialog } from '@/lib/use-dialog';
import type { Period, Trip } from '@/lib/types';

export interface FeedRow { code: string; trip: Trip }

interface Props {
  open: boolean;
  rows: FeedRow[];
  period: Period;
  onClose: () => void;
  onPick: (code: string) => void;
  onOpenWhen: () => void;
  onClearPeriod: () => void;
}

export default function LogDialog({
  open, rows, period, onClose, onPick, onOpenWhen, onClearPeriod,
}: Props) {
  const { ref, onBackdropClick } = useDialog(open, onClose);
  const scope = scopeLabel(period);

  const sub = rows.length
    ? `${rows.length} chuyến${period.year ? ` trong ${scope}` : ', mới nhất trước'}`
    : period.year ? `Không có chuyến nào trong ${scope}` : 'Chưa có chuyến nào';

  let group: number | null = null;

  return (
    <dialog id="dlg-log" ref={ref} onClick={onBackdropClick} aria-labelledby="log-title">
      <div className="dlg">
        <div className="dlg-head plain">
          <div className="row">
            <div>
              <h3 id="log-title">Nhật ký</h3>
              <p className="meta">{sub}</p>
            </div>
            <button className="x" aria-label="Đóng" onClick={onClose}>✕</button>
          </div>
          <WhenButton period={period} onOpen={onOpenWhen} onClear={onClearPeriod} />
        </div>

        <div className="dlg-body">
          <div className="feed">
            {rows.length === 0 ? (
              <div className="empty">
                <BookIcon size={40} width={1.5} />
                <p>{period.year ? `Chưa có chuyến nào trong ${scope}.` : 'Chưa ghi chuyến nào.'}</p>
                {period.year !== null && (
                  <button className="btn primary" onClick={onClearPeriod}>Xem tất cả thời gian</button>
                )}
              </div>
            ) : rows.map(({ code, trip }) => {
              const y = yearOf(trip.from);
              const head = y !== group;
              group = y;
              return (
                <Fragment key={`${code}-${trip.id}`}>
                  {head && <div className="yr">{y ?? '—'}</div>}
                  <button className="feed-item" onClick={() => { onClose(); onPick(code); }}>
                    <span className="feed-when">{monthOf(trip.from)}</span>
                    <span className="feed-main">
                      <span className="feed-title">{byCode[code].name}</span>
                      <span className="feed-desc">
                        {trip.places.join(' · ') || trip.note.slice(0, 60)}
                      </span>
                    </span>
                  </button>
                </Fragment>
              );
            })}
          </div>
        </div>
      </div>
    </dialog>
  );
}
