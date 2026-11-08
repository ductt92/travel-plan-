import { Fragment, useEffect, useLayoutEffect, useRef, useState } from 'react';
import { Button, Modal, TextArea } from 'react-liquis-glass';
import { HeartIcon } from './icons';
import type { LoveNote } from '@/lib/api';

interface Props {
  open: boolean;
  userName: string;
  notes: LoveNote[] | null;
  error: string | null;
  /** Mốc đã đọc lúc mở popup, để tô những lời nhắn mới. */
  seen: string;
  onClose: () => void;
  onAdd: (text: string) => Promise<boolean>;
  onRemove: (id: number) => void;
  onRetry: () => void;
}

const MAX = 2000;

/** Người kia của người đang viết, để lời mời viết gọi đúng tên. */
const partner = (me: string) => (me === 'Ngọc' ? 'anh Đức' : me === 'Đức' ? 'Ngọc' : 'người thương');
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
    <Modal open={props.open} onClose={props.onClose} title="Note tình yêu" footer={null} width={600} className="bd-modal bd-notes">
      {props.open && <Body {...props} />}
    </Modal>
  );
}

function Body({ userName, notes, error, seen, onAdd, onRemove, onRetry }: Props) {
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  // giữ mốc đã đọc của lúc mở, để đánh dấu đã đọc rồi mà lời nhắn mới vẫn còn sáng tới khi đóng
  const [since] = useState(seen);
  const scroller = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLDivElement>(null);

  // cũ ở trên, mới ở dưới như một cuộc trò chuyện
  const list = notes ? [...notes].reverse() : null;

  // mở ra và mỗi khi có lời nhắn mới thì cuộn xuống cuối
  useLayoutEffect(() => {
    const el = scroller.current;
    if (el) el.scrollTop = el.scrollHeight;
  }, [notes?.length]);

  useEffect(() => { input.current?.querySelector('textarea')?.focus(); }, []);

  const send = async () => {
    const t = text.trim();
    if (!t || busy) return;
    setBusy(true);
    if (await onAdd(t)) setText('');
    setBusy(false);
  };

  let lastDay = '';

  return (
    <div className="dlg">
      <div className="dlg-head plain love-head">
        <p className="meta">
          <span className="love-lock">🔒</span> Chỉ hai đứa mình đọc được
          {notes && notes.length > 0 && <> · {notes.length} lời nhắn</>}
        </p>
      </div>

      <div className="dlg-body love-body" ref={scroller}>
        {error && (
          <p className="love-err" role="alert">
            {error} {!notes && <button type="button" className="link" onClick={onRetry}>Thử lại</button>}
          </p>
        )}
        {!list ? (
          !error && <p className="love-empty">Đang mở hộp thư…</p>
        ) : list.length === 0 ? (
          <div className="love-start">
            <span className="love-start__ic"><HeartIcon size={30} width={1.6} /></span>
            <p>Chưa có lời nhắn nào.<br />Viết lời nhắn đầu tiên cho {partner(userName)} đi 💌</p>
          </div>
        ) : (
          <ol className="love-thread">
            {list.map(n => {
              const d = new Date(n.at);
              const key = dayKey(d);
              const head = key !== lastDay;
              lastDay = key;
              const mine = n.by === userName;
              const fresh = !mine && n.at > since;
              return (
                <Fragment key={n.id}>
                  {head && <li className="love-day"><span>{dayLabel(d)}</span></li>}
                  <li className={`love-msg ${who(n.by)}${mine ? ' mine' : ''}${fresh ? ' fresh' : ''}`}>
                    <span className="love-ava" aria-hidden="true">{(n.by || '?').slice(0, 1)}</span>
                    <div className="love-bubble">
                      <div className="love-meta">
                        <b>{n.by || 'Ai đó'}</b>
                        {fresh && <span className="love-new">mới</span>}
                      </div>
                      <p>{n.text}</p>
                      <div className="love-foot">
                        <time dateTime={n.at} title={d.toLocaleString('vi-VN')}>
                          {clock(d)} · {d.toLocaleDateString('vi-VN')}
                        </time>
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
        <div className="love-compose__box" ref={input}>
          <TextArea
            className="note-in love-in" rows={2} maxLength={MAX}
            placeholder={`${userName} muốn nhắn gì cho ${partner(userName)}…`}
            aria-label="Viết lời nhắn"
            value={text} onChange={e => setText(e.target.value)}
            onKeyDown={e => {
              if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); void send(); }
            }}
          />
          <span className="love-hint">{text.length > MAX - 200 ? `${text.length}/${MAX}` : '⌘ + Enter để gửi'}</span>
        </div>
        <Button type="submit" variant="filled" color="primary" className="love-send" icon={<HeartIcon />}
          loading={busy} disabled={!text.trim()}>
          Gửi
        </Button>
      </form>
    </div>
  );
}
