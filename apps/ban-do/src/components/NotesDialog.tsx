import { useState } from 'react';
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

function when(iso: string) {
  const d = new Date(iso);
  const mins = Math.round((Date.now() - +d) / 60000);
  if (mins < 1) return 'vừa xong';
  if (mins < 60) return `${mins} phút trước`;
  if (mins < 24 * 60) return `${Math.round(mins / 60)} giờ trước`;
  const time = d.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
  return `${time} · ${d.toLocaleDateString('vi-VN', { day: 'numeric', month: 'numeric', year: 'numeric' })}`;
}

export default function NotesDialog(props: Props) {
  return (
    <Modal open={props.open} onClose={props.onClose} title="Note tình yêu" footer={null} width={560} className="bd-modal bd-notes">
      {props.open && <Body {...props} />}
    </Modal>
  );
}

function Body({ userName, notes, error, seen, onAdd, onRemove, onRetry }: Props) {
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  // giữ mốc đã đọc của lúc mở, để đánh dấu đã đọc rồi mà lời nhắn mới vẫn còn sáng tới khi đóng
  const [since] = useState(seen);

  const send = async () => {
    const t = text.trim();
    if (!t || busy) return;
    setBusy(true);
    if (await onAdd(t)) setText('');
    setBusy(false);
  };

  return (
    <div className="dlg">
      <div className="dlg-head plain">
        <p className="meta">Chỉ hai đứa mình đọc được. Thi thoảng ghé vào để lại một lời nhắn nhé 💌</p>
        <form className="love-form" onSubmit={e => { e.preventDefault(); void send(); }}>
          <TextArea
            data-autofocus className="note-in love-in" rows={3} maxLength={MAX}
            placeholder={`${userName} muốn nhắn gì cho ${partner(userName)}…`}
            value={text} onChange={e => setText(e.target.value)}
            onKeyDown={e => {
              if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); void send(); }
            }}
          />
          <div className="love-acts">
            <span className="love-hint">{text.length > MAX - 200 ? `${text.length}/${MAX}` : '⌘ + Enter để gửi'}</span>
            <Button type="submit" variant="filled" color="primary" icon={<HeartIcon />} loading={busy} disabled={!text.trim()}>
              Gửi lời nhắn
            </Button>
          </div>
        </form>
      </div>

      <div className="dlg-body">
        {error && (
          <p className="love-err" role="alert">
            {error} {!notes && <button type="button" className="link" onClick={onRetry}>Thử lại</button>}
          </p>
        )}
        {!notes ? (
          !error && <p className="love-empty">Đang mở hộp thư…</p>
        ) : notes.length === 0 ? (
          <div className="empty">
            <HeartIcon size={40} width={1.5} />
            <p>Chưa có lời nhắn nào. Viết lời nhắn đầu tiên đi!</p>
          </div>
        ) : (
          <ul className="love-list">
            {notes.map(n => {
              const mine = n.by === userName;
              const fresh = !mine && n.at > since;
              return (
                <li key={n.id} className={`love-card${n.by === 'Đức' ? ' he' : n.by === 'Ngọc' ? ' she' : ''}${fresh ? ' fresh' : ''}`}>
                  <div className="love-top">
                    <b>{n.by || 'Ai đó'}</b>
                    {fresh && <span className="love-new">mới</span>}
                    <span className="love-when" title={new Date(n.at).toLocaleString('vi-VN')}>{when(n.at)}</span>
                    {mine && (
                      <button type="button" className="love-del" aria-label="Xoá lời nhắn này"
                        onClick={() => { if (confirm('Xoá lời nhắn này?')) onRemove(n.id); }}>✕</button>
                    )}
                  </div>
                  <p>{n.text}</p>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );
}
