import { Fragment, useEffect, useLayoutEffect, useRef, useState } from 'react';
import { Modal } from 'react-liquis-glass';
import { HeartIcon } from './icons';
import type { LoveNote } from '@/lib/api';

interface Props {
  open: boolean;
  userName: string;
  notes: LoveNote[] | null;
  error: string | null;
  /** Mốc đã đọc lúc mở popup, để đánh dấu chỗ bắt đầu lời nhắn mới. */
  seen: string;
  onClose: () => void;
  onAdd: (text: string) => Promise<boolean>;
  onRemove: (id: number) => void;
  onRetry: () => void;
}

const MAX = 2000;

/** Người kia của người đang viết, để lời mời viết gọi đúng tên. */
const partner = (me: string) => (me === 'Ngọc' ? 'anh yêu' : me === 'Đức' ? 'em yêu' : 'người thương');
const who = (name: string) => (name === 'Đức' ? 'he' : name === 'Ngọc' ? 'she' : 'other');

const dayKey = (d: Date) => `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`;

/** "Hôm nay · Chủ Nhật, 8 tháng 11, 2026" */
function dayLabel(d: Date) {
  const full = d.toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
  const today = new Date();
  const yesterday = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1);
  if (dayKey(d) === dayKey(today)) return `Hôm nay · ${full}`;
  if (dayKey(d) === dayKey(yesterday)) return `Hôm qua · ${full}`;
  return full;
}

const clock = (d: Date) => d.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });

export default function NotesDialog(props: Props) {
  return (
    <Modal open={props.open} onClose={props.onClose} footer={null} width={560} className="bd-modal bd-notes">
      {props.open && <Body {...props} />}
    </Modal>
  );
}

function Body({ userName, notes, error, seen, onAdd, onRemove, onRetry }: Props) {
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  // giữ mốc đã đọc của lúc mở: đóng popup mới tính là đã đọc, nên vạch "mới" đứng yên tới lúc đó
  const [since] = useState(seen);
  const scroller = useRef<HTMLDivElement>(null);
  // lời nhắn có sẵn lúc mở: chỉ tin gửi thêm sau đó mới có hiệu ứng hiện ra
  // (đang tải thì chờ tới lúc có danh sách mới chụp lại)
  const initial = useRef<Set<number> | null>(null);
  if (notes && !initial.current) initial.current = new Set(notes.map(n => n.id));
  const area = useRef<HTMLTextAreaElement>(null);

  // cũ ở trên, mới ở dưới như một cuộc trò chuyện
  const list = notes ? [...notes].reverse() : null;
  const firstNew = list?.find(n => n.by !== userName && n.at > since)?.id;

  useLayoutEffect(() => {
    const el = scroller.current;
    if (el) el.scrollTop = el.scrollHeight;
  }, [notes?.length]);

  useEffect(() => { area.current?.focus(); }, []);

  // ô viết tự cao theo chữ, tới một mức thì cuộn
  useLayoutEffect(() => {
    const el = area.current;
    if (!el) return;
    el.style.height = 'auto';
    el.style.height = `${Math.min(el.scrollHeight + 2, 140)}px`;
    // chưa chạm mức cao nhất thì giấu thanh cuộn, không thì nó hiện thành một vạch thừa
    el.style.overflowY = el.scrollHeight + 2 > 140 ? 'auto' : 'hidden';
  }, [text]);

  const send = async () => {
    const t = text.trim();
    if (!t || busy) return;
    setBusy(true);
    if (await onAdd(t)) setText('');
    setBusy(false);
    area.current?.focus();
  };

  let lastDay = '';

  return (
    <div className="love">
      <header className="love-hd">
        <div className="love-pair" aria-hidden="true">
          <span className="love-ava he">Đ</span>
          <span className="love-pair__heart"><HeartIcon size={13} width={2.4} /></span>
          <span className="love-ava she">N</span>
        </div>
        <h2>Note tình yêu</h2>
        <p>Chỉ hai đứa mình đọc được{notes && notes.length > 0 ? ` · ${notes.length} lời nhắn` : ''}</p>
      </header>

      <div className="love-body" ref={scroller}>
        {error && (
          <p className="love-err" role="alert">
            {error} {!notes && <button type="button" className="link" onClick={onRetry}>Thử lại</button>}
          </p>
        )}
        {!list ? (
          !error && <p className="love-wait">Đang mở hộp thư…</p>
        ) : list.length === 0 ? (
          <div className="love-start">
            <span className="love-start__ic"><HeartIcon size={28} width={1.7} /></span>
            <p>Chưa có lời nhắn nào.</p>
            <p className="soft">Viết lời nhắn đầu tiên cho {partner(userName)} nhé</p>
          </div>
        ) : (
          <ol className="love-thread">
            {list.map((n, i) => {
              const d = new Date(n.at);
              const key = dayKey(d);
              const newDay = key !== lastDay;
              lastDay = key;
              const next = list[i + 1];
              // gom các tin liền nhau của cùng một người: chỉ tin cuối nhóm mới có hình đại diện
              const endOfRun = !next || next.by !== n.by || dayKey(new Date(next.at)) !== key;
              const mine = n.by === userName;
              return (
                <Fragment key={n.id}>
                  {newDay && <li className="love-day">{dayLabel(d)}</li>}
                  {n.id === firstNew && <li className="love-unread"><span>Lời nhắn mới</span></li>}
                  <li className={`love-msg ${who(n.by)}${mine ? ' mine' : ''}${endOfRun ? ' end' : ''}${initial.current && !initial.current.has(n.id) ? ' arrive' : ''}`}>
                    <span className="love-ava" aria-hidden="true">{endOfRun ? (n.by || '?').slice(0, 1) : ''}</span>
                    <div className="love-col">
                      <div className="love-bubble">{n.text}</div>
                      <div className="love-time">
                        {!mine && <b>{n.by || 'Ai đó'}</b>}
                        <time dateTime={n.at} title={d.toLocaleString('vi-VN')}>{clock(d)} · {d.toLocaleDateString('vi-VN')}</time>
                        {mine && (
                          <button type="button" className="love-del" aria-label="Xoá lời nhắn này"
                            onClick={() => { if (confirm('Xoá lời nhắn này?')) onRemove(n.id); }}>Xoá</button>
                        )}
                      </div>
                    </div>
                  </li>
                </Fragment>
              );
            })}
          </ol>
        )}
      </div>

      <form className="love-compose" onSubmit={e => { e.preventDefault(); void send(); }}>
        <textarea
          ref={area} rows={1} maxLength={MAX} aria-label="Viết lời nhắn"
          placeholder={`Nhắn cho ${partner(userName)} ❤️`}
          value={text} onChange={e => setText(e.target.value)}
          onKeyDown={e => {
            if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); void send(); }
          }}
        />
        <button type="submit" className="love-send" disabled={!text.trim() || busy} aria-label="Gửi lời nhắn" title="Gửi (⌘ + Enter)">
          <HeartIcon size={19} width={2.2} />
        </button>
      </form>
    </div>
  );
}
