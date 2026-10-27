// Nút trạng thái đồng bộ + ô nhập mã chung. Đặt ở header hoặc thanh bên của app.
import { useEffect, useRef, useState } from 'react';
import { BACKENDS, connect, disconnect, setBackend, useSyncStatus } from './index.js';
import './sync.css';

const LABEL = { off: 'Chưa đồng bộ', idle: 'Đang kết nối…', syncing: 'Đang đồng bộ…', ok: 'Đã đồng bộ', error: 'Lỗi đồng bộ', denied: 'Sai mã đồng bộ' };

function ago(t) {
  if (!t) return '';
  const s = Math.round((Date.now() - t) / 1000);
  return s < 60 ? 'vừa xong' : s < 3600 ? `${Math.round(s / 60)} phút trước` : new Date(t).toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
}

// Chọn bản API: Node.js hoặc Go (cùng hợp đồng, cùng dữ liệu)
function BackendPicker({ value }) {
  return (
    <fieldset className="sync__seg">
      <legend>Máy chủ API</legend>
      {BACKENDS.map(b => (
        <label key={b.id} className={value === b.id ? 'is-on' : ''}>
          <input type="radio" name="sync-backend" value={b.id} checked={value === b.id} onChange={() => setBackend(b.id)} />
          {b.label}
        </label>
      ))}
    </fieldset>
  );
}

export function SyncButton({ className = '' }) {
  const st = useSyncStatus();
  const [open, setOpen] = useState(false);
  const [code, setCode] = useState('');
  const [err, setErr] = useState('');
  const [busy, setBusy] = useState(false);
  const [end, setEnd] = useState(false); // khung mở sang trái khi nút nằm sát mép phải
  const box = useRef(null);

  useEffect(() => {
    if (!open) return;
    const close = e => { if (e.key === 'Escape' || (e.type === 'pointerdown' && !box.current?.contains(e.target))) setOpen(false); };
    document.addEventListener('pointerdown', close);
    document.addEventListener('keydown', close);
    return () => { document.removeEventListener('pointerdown', close); document.removeEventListener('keydown', close); };
  }, [open]);

  async function submit(e) {
    e.preventDefault();
    if (!code.trim()) return;
    setBusy(true);
    const error = await connect(code);
    setBusy(false);
    setErr(error);
    if (!error) { setCode(''); setOpen(false); }
  }

  const on = st.state !== 'off';
  return (
    <div className={`sync${end ? ' sync--end' : ''} ${className}`} ref={box}>
      <button type="button" className={`sync__btn is-${st.state}`} aria-expanded={open} onClick={() => { setEnd(box.current.getBoundingClientRect().left + 316 > window.innerWidth); setOpen(o => !o); }}>
        <span className="sync__dot" aria-hidden="true" />
        {LABEL[st.state]}
        {on && <span className="sync__tag">{st.backend === 'go' ? 'Go' : 'Node'}</span>}
      </button>
      {open && (
        <div className="sync__pop" role="dialog" aria-label="Đồng bộ dữ liệu">
          {on ? (
            <>
              <b>Đồng bộ đang bật</b>
              <p>Dữ liệu trên máy này được lưu lên mây và cập nhật với máy còn lại khoảng mỗi 10 giây.{st.at ? ` Lần gần nhất: ${ago(st.at)}.` : ''}</p>
              <BackendPicker value={st.backend} />
              {st.served && <p className="sync__small">Lần gọi gần nhất do bản <b>{st.served === 'go' ? 'Go' : 'Node.js'}</b> trả lời.</p>}
              {st.error && <p className="sync__err">{st.error}</p>}
              <button type="button" className="sync__ghost" onClick={() => { disconnect(); setOpen(false); }}>Tắt đồng bộ trên máy này</button>
            </>
          ) : (
            <form onSubmit={submit}>
              <b>Đồng bộ giữa hai máy</b>
              <p>Nhập mã chung của hai bạn. Mã chỉ lưu trong trình duyệt này.</p>
              <input type="password" autoComplete="off" placeholder="Mã đồng bộ" value={code} onChange={e => setCode(e.target.value)} autoFocus />
              <BackendPicker value={st.backend} />
              {err && <p className="sync__err">{err}</p>}
              <button type="submit" className="sync__primary" disabled={busy || !code.trim()}>{busy ? 'Đang kiểm tra…' : 'Bật đồng bộ'}</button>
            </form>
          )}
        </div>
      )}
    </div>
  );
}
