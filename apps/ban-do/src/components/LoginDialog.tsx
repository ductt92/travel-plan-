import { useState } from 'react';
import { useDialog } from '@/lib/use-dialog';

interface Props {
  open: boolean;
  onClose: () => void;
  /** Trả về null nếu mật khẩu đúng, còn lại là câu lỗi để hiện ra. */
  onSubmit: (pass: string) => Promise<string | null>;
}

export default function LoginDialog({ open, onClose, onSubmit }: Props) {
  const { ref, onBackdropClick } = useDialog(open, onClose);

  return (
    <dialog id="dlg-login" ref={ref} onClick={onBackdropClick} aria-labelledby="login-title">
      {open && <Body onClose={onClose} onSubmit={onSubmit} />}
    </dialog>
  );
}

function Body({ onClose, onSubmit }: Omit<Props, 'open'>) {
  const [pass, setPass] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const submit = (ev: React.FormEvent) => {
    ev.preventDefault();
    setError(null);
    setBusy(true);
    onSubmit(pass)
      .then(err => (err ? setError(err) : onClose()))
      .finally(() => setBusy(false));
  };

  return (
    <form className="dlg" onSubmit={submit}>
      <div className="dlg-head plain">
        <div className="row">
          <div>
            <h3 id="login-title">Đăng nhập</h3>
            <p className="meta">
              Mật khẩu chung của hai đứa — cùng mã dùng cho trang Ngọc học tiếng Trung.
            </p>
          </div>
          <button type="button" className="x" aria-label="Đóng" onClick={onClose}>✕</button>
        </div>
        <input
          className="search" type="password" data-autofocus
          autoComplete="current-password" placeholder="Mật khẩu" aria-label="Mật khẩu"
          value={pass} onChange={e => setPass(e.target.value)}
        />
      </div>

      <div className="dlg-acts">
        <span className={`acts-note${error ? ' bad' : ''}`}>
          {error ?? 'Đăng nhập rồi mới ghi và xoá được'}
        </span>
        <button type="submit" className="btn primary" disabled={busy || !pass}>
          {busy ? 'Đang kiểm…' : 'Vào'}
        </button>
      </div>
    </form>
  );
}
