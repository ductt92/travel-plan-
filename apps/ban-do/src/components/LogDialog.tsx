import { Fragment } from 'react';
import { Button, Modal } from 'react-liquis-glass';
import WhenButton from './WhenButton';
import { BookIcon } from './icons';
import { byCode } from '@/lib/map-data';
import { monthOf, yearOf } from '@/lib/format';
import { scopeLabel } from '@/lib/period';
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
  const scope = scopeLabel(period);

  const sub = rows.length
    ? `${rows.length} chuyến${period.year ? ` trong ${scope}` : ', mới nhất trước'}`
    : period.year ? `Không có chuyến nào trong ${scope}` : 'Chưa có chuyến nào';

  let group: number | null = null;

  return (
    <Modal open={open} onClose={onClose} title="Nhật ký" footer={null} width={580} className="bd-modal bd-log">
      <div className="dlg">
        <div className="dlg-head plain">
          <p className="meta">{sub}</p>
          <WhenButton period={period} onOpen={onOpenWhen} onClear={onClearPeriod} />
        </div>

        <div className="dlg-body">
          <div className="feed">
            {rows.length === 0 ? (
              <div className="empty">
                <BookIcon size={40} width={1.5} />
                <p>{period.year ? `Chưa có chuyến nào trong ${scope}.` : 'Chưa ghi chuyến nào.'}</p>
                {period.year !== null && (
                  <Button variant="filled" color="primary" onClick={onClearPeriod}>Xem tất cả thời gian</Button>
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
    </Modal>
  );
}
