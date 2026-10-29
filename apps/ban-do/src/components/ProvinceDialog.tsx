'use client';

import { useState } from 'react';
import TripForm from './TripForm';
import { PinIcon } from './icons';
import { CLIP, REGION } from '@/lib/map-data';
import { fmtRange, nights, stars } from '@/lib/format';
import { inPeriod, scopeLabel, scopeShort } from '@/lib/period';
import { useDialog } from '@/lib/use-dialog';
import type { Level, Period, Province, ProvinceEntry, Status, Trip, TripDraft } from '@/lib/types';

const STATUSES: [Status, string][] = [
  ['visited', 'Đã đi'],
  ['wish', 'Muốn đi'],
  ['none', 'Chưa đánh dấu'],
];

interface Props {
  province: Province | null;
  entry: ProvinceEntry;
  level: Level;
  period: Period;
  /** Màn hẹp mở kiểu popup giữa màn, màn rộng mở kiểu bảng bên phải. */
  modal: boolean;
  /** Chưa đăng nhập thì chỉ đọc: giấu hết nút sửa, nút xoá và ô đánh dấu. */
  canEdit: boolean;
  onClose: () => void;
  onStatus: (status: Status) => void;
  onAdd: (data: TripDraft) => void;
  onUpdate: (id: number, data: TripDraft) => void;
  onRemove: (id: number) => void;
  onClearPeriod: () => void;
}

export default function ProvinceDialog({ province, modal, onClose, ...rest }: Props) {
  const { ref, onBackdropClick } = useDialog(Boolean(province), onClose, modal);

  return (
    <dialog id="dlg" ref={ref} onClick={onBackdropClick} aria-labelledby="dlg-title">
      {/* key theo mã tỉnh: đổi tỉnh là form đang mở dẹp đi, khỏi lẫn sang tỉnh mới */}
      {province && <Body key={province.code} province={province} onClose={onClose} {...rest} />}
    </dialog>
  );
}

type BodyProps = Omit<Props, 'modal'> & { province: Province };

function Body({
  province, entry, level, period, canEdit,
  onClose, onStatus, onAdd, onUpdate, onRemove, onClearPeriod,
}: BodyProps) {
  /** id chuyến đang sửa, 'new' nếu đang thêm, null nếu không mở form nào. */
  const [editing, setEditing] = useState<number | 'new' | null>(null);

  const shown = entry.trips.filter(t => inPeriod(t, period));
  const list = [...shown].sort((a, b) => (b.from || '').localeCompare(a.from || ''));
  const outside = entry.trips.length - shown.length;
  const scope = scopeLabel(period);

  const [bx, by, bw, bh] = province.bb;
  const m = Math.max(bw, bh) * 0.06;
  const vw = bw + m * 2;
  const vh = bh + m * 2;

  const tint = level === 'wish' ? 'var(--wish)' : level === 0 ? 'var(--blank-hi)' : 'var(--v2)';

  const save = (data: TripDraft) => {
    if (editing === 'new') onAdd(data);
    else if (typeof editing === 'number') onUpdate(editing, data);
    setEditing(null);
  };

  return (
    <div className="dlg">
      <div className="dlg-head" style={{ '--tint': tint } as React.CSSProperties}>
        <svg
          className="silh" aria-hidden="true"
          viewBox={`${bx - m} ${by - m} ${vw} ${vh}`}
          style={{ aspectRatio: (vw / vh).toFixed(3) }}
        >
          <path d={province.d} />
        </svg>

        <div className="row">
          <div>
            <h3 id="dlg-title">{province.name}</h3>
            <p className="meta">
              {[
                province.isCity ? 'Thành phố trực thuộc trung ương' : 'Tỉnh',
                REGION[province.region],
                province.merged.length ? `trước 2025: ${province.merged.join(', ')}` : '',
              ].filter(Boolean).join(' · ')}
            </p>
          </div>
          <button className="x" aria-label="Đóng" onClick={onClose}>✕</button>
        </div>

        <div className="seg">
          {(canEdit ? STATUSES : STATUSES.filter(([id]) => id === entry.status)).map(([id, label]) => (
            <button
              key={id}
              className={`s-${id}${entry.status === id ? ' on' : ''}`}
              disabled={!canEdit}
              onClick={() => onStatus(id)}
            >{label}</button>
          ))}
        </div>
      </div>

      <div className="dlg-body">
        <div className="sec-head">
          <h4>{shown.length ? `${shown.length} chuyến đi${period.year ? ` · ${scopeShort(period)}` : ''}` : 'Chuyến đi'}</h4>
          {canEdit && editing !== 'new' && (
            <button className="add" onClick={() => setEditing('new')}>＋ Thêm chuyến</button>
          )}
        </div>

        {canEdit && editing !== null && (
          <TripForm
            trip={editing === 'new' ? null : entry.trips.find(t => t.id === editing) ?? null}
            onCancel={() => setEditing(null)}
            onSave={save}
          />
        )}

        {!list.length && editing !== 'new' ? (
          <div className="empty">
            <PinIcon />
            <p>
              {outside ? (
                `Không có chuyến nào ở đây trong ${scope}.`
              ) : canEdit ? (
                <>Chưa ghi chuyến nào ở đây.<br />Đi ngày nào, ghé những đâu, thấy thế nào?</>
              ) : (
                'Chưa ghi chuyến nào ở đây.'
              )}
            </p>
            {(outside || canEdit) && (
              <button
                className="btn primary"
                onClick={outside ? onClearPeriod : () => setEditing('new')}
              >
                {outside ? `Xem cả ${entry.trips.length} chuyến` : 'Ghi chuyến đầu tiên'}
              </button>
            )}
          </div>
        ) : (
          <>
            {/* đang lọc mà tỉnh này còn chuyến ngoài khoảng thì nói rõ, kèm lối bỏ lọc */}
            {period.year && outside > 0 && (
              <div className="filter-note">
                <span>Đang xem <b>{scope}</b> — còn {outside} chuyến ở lúc khác.</span>
                <button onClick={onClearPeriod}>Xem cả {entry.trips.length} chuyến</button>
              </div>
            )}
            <ol className="tl">
              {list.filter(t => t.id !== editing).map(t => (
                <li className="tl-item" key={t.id}>
                  <span className="tl-dot" />
                  <TripCard
                    trip={t}
                    canEdit={canEdit}
                    onEdit={() => setEditing(t.id)}
                    onRemove={() => {
                      if (window.confirm('Xoá chuyến này?')) onRemove(t.id);
                    }}
                  />
                </li>
              ))}
            </ol>
          </>
        )}
      </div>

      <p className="dlg-foot">Bản thật: mỗi chuyến là một bản ghi trong database, kèm ảnh và vị trí.</p>
    </div>
  );
}

function TripCard({ trip, canEdit, onEdit, onRemove }: {
  trip: Trip; canEdit: boolean; onEdit: () => void; onRemove: () => void;
}) {
  const [all, setAll] = useState(false);
  const clip = trip.places.length > CLIP && !all;

  return (
    <article className="trip">
      <div className="trip-top">
        <span className="trip-date">{fmtRange(trip.from, trip.to)}</span>
        <span className="trip-len">{nights(trip.from, trip.to)}</span>
      </div>

      {trip.rate > 0 && (
        <span className="stars" title={`${trip.rate}/5 sao`}>{stars(trip.rate)}</span>
      )}
      {trip.with && <p className="trip-with">Đi cùng {trip.with}</p>}

      {trip.places.length > 0 && (
        <div className="places" {...(clip ? { 'data-clip': '' } : {})}>
          {trip.places.map(x => <span className="place" key={x}>{x}</span>)}
          {clip && (
            <button type="button" className="more" onClick={() => setAll(true)}>
              +{trip.places.length - CLIP} nữa
            </button>
          )}
        </div>
      )}

      {trip.note && <p className="trip-note">{trip.note}</p>}

      {canEdit && (
        <div className="trip-acts">
          <button onClick={onEdit}>Sửa</button>
          <button className="del" onClick={onRemove}>Xoá</button>
        </div>
      )}
    </article>
  );
}
