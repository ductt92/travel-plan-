import { useState } from 'react';
import { PasswordInput } from '@trang/ui/password';
import { LockIcon } from './icons';
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
    <dialog
      id="dlg-login" className="glass sheen" ref={ref}
      onClick={onBackdropClick} aria-labelledby="login-title"
    >
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
    <form className="lg" onSubmit={submit}>
      <button type="button" className="x" aria-label="Đóng" onClick={onClose}>✕</button>

      <span className="lg-ring" aria-hidden="true"><LockIcon size={23} width={1.7} /></span>
      <h3 id="login-title">Đăng nhập</h3>
      <p className="meta">
        Mật khẩu chung của hai đứa — cùng mã dùng cho trang Ngọc học tiếng Trung.
      </p>

      <PasswordInput
        className="lg-inp" data-autofocus
        autoComplete="current-password" placeholder="Mật khẩu" aria-label="Mật khẩu"
        value={pass} onChange={e => setPass(e.target.value)}
      />
      <p className={`lg-msg${error ? ' bad' : ''}`} role={error ? 'alert' : undefined}>
        {error ?? 'Đăng nhập rồi mới ghi và xoá được'}
      </p>

      <button type="submit" className="lg-go" disabled={busy || !pass}>
        {busy ? 'Đang kiểm…' : 'Vào'}
      </button>
    </form>
  );
}
