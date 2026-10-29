import { useId, useState } from 'react';
import type { Trip, TripDraft } from '@/lib/types';

interface Props {
  /** Chuyến đang sửa, null là đang thêm mới. */
  trip: Trip | null;
  onCancel: () => void;
  onSave: (data: TripDraft) => void;
}

export default function TripForm({ trip, onCancel, onSave }: Props) {
  const id = useId();
  const [from, setFrom] = useState(trip?.from ?? '');
  const [to, setTo] = useState(trip?.to ?? '');
  const [withWho, setWithWho] = useState(trip?.with ?? '');
  const [rate, setRate] = useState(trip?.rate ?? 0);
  const [note, setNote] = useState(trip?.note ?? '');
  const [places, setPlaces] = useState<string[]>(trip?.places ?? []);
  const [typing, setTyping] = useState('');

  const addPlace = () => {
    const v = typing.trim();
    if (v && !places.includes(v)) setPlaces([...places, v]);
    setTyping('');
  };

  return (
    <form
      className="form"
      onSubmit={ev => {
        ev.preventDefault();
        onSave({ from, to, with: withWho.trim(), rate, places, note: note.trim() });
      }}
    >
      <div className="grid2">
        <div>
          <label htmlFor={`${id}-from`}>Đi ngày</label>
          <input
            className="inp" type="date" id={`${id}-from`} autoFocus
            value={from} onChange={e => setFrom(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor={`${id}-to`}>Đến ngày</label>
          <input
            className="inp" type="date" id={`${id}-to`}
            value={to} onChange={e => setTo(e.target.value)}
          />
        </div>
      </div>

      <div className="field">
        <label htmlFor={`${id}-with`}>Đi cùng ai</label>
        <input
          className="inp" id={`${id}-with`} placeholder="Ngọc, nhóm công ty, đi một mình…"
          value={withWho} onChange={e => setWithWho(e.target.value)}
        />
      </div>

      <div className="field">
        <label htmlFor={`${id}-place`}>Đã ghé những đâu</label>
        <div className="chips-in">
          {places.map((name, i) => (
            <span className="place" key={name}>
              {name}
              <button
                type="button" aria-label={`Bỏ ${name}`}
                onClick={() => setPlaces(places.filter((_, j) => j !== i))}
              >✕</button>
            </span>
          ))}
          <input
            id={`${id}-place`} placeholder="Gõ tên rồi Enter…"
            value={typing}
            onChange={e => setTyping(e.target.value)}
            onKeyDown={ev => {
              if (ev.key === 'Enter' || ev.key === ',') {
                ev.preventDefault();
                addPlace();
              } else if (ev.key === 'Backspace' && !typing && places.length) {
                setPlaces(places.slice(0, -1));
              }
            }}
          />
        </div>
      </div>

      <div className="field">
        <label>Thấy thế nào <span className="opt">không bắt buộc</span></label>
        <div className="rate">
          {[1, 2, 3, 4, 5].map(n => (
            <button
              key={n} type="button" className={n <= rate ? 'on' : ''} aria-label={`${n} sao`}
              onClick={() => setRate(rate === n ? 0 : n)}
            >★</button>
          ))}
        </div>
      </div>

      <div className="field">
        <label htmlFor={`${id}-note`}>Trải nghiệm</label>
        <textarea
          className="inp" id={`${id}-note`}
          placeholder="Ăn gì, ở đâu, lần sau quay lại thì làm gì khác…"
          value={note} onChange={e => setNote(e.target.value)}
        />
      </div>

      <div className="form-acts">
        <button type="button" className="btn" onClick={onCancel}>Huỷ</button>
        <button type="submit" className="btn primary">{trip ? 'Lưu thay đổi' : 'Thêm chuyến'}</button>
      </div>
    </form>
  );
}
