import { useState } from 'react';
import { Button, Modal, Password } from 'liquidglass-ui';
import { LockIcon } from './icons';

interface Props {
  open: boolean;
  onClose: () => void;
  /** Trả về null nếu mật khẩu đúng, còn lại là câu lỗi để hiện ra. */
  onSubmit: (pass: string) => Promise<string | null>;
}

export default function LoginDialog({ open, onClose, onSubmit }: Props) {
  return (
    <Modal open={open} onClose={onClose} footer={null} width={390} className="login">
      {open && <Body onClose={onClose} onSubmit={onSubmit} />}
    </Modal>
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
    <form className="login__form" onSubmit={submit}>
      <span className="login__ring" aria-hidden="true"><LockIcon size={23} width={1.7} /></span>
      <h3>Đăng nhập</h3>
      <p className="meta">
        Mật khẩu chung của hai đứa — cùng mã dùng cho trang Ngọc học tiếng Trung.
      </p>

      <Password
        data-autofocus size="lg" status={error ? 'error' : undefined}
        autoComplete="current-password" placeholder="Mật khẩu" aria-label="Mật khẩu"
        value={pass} onChange={e => setPass(e.target.value)}
      />
      <p className={`login__msg${error ? ' bad' : ''}`} role={error ? 'alert' : undefined}>
        {error ?? 'Đăng nhập rồi mới ghi và xoá được'}
      </p>

      <Button type="submit" variant="filled" color="primary" size="lg" block loading={busy} disabled={!pass}>
        {busy ? 'Đang kiểm…' : 'Vào'}
      </Button>
    </form>
  );
}
