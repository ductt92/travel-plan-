import { useState } from 'react';
import { Button, Modal, Password } from 'react-liquis-glass';
import { LockIcon } from 'react-liquis-glass/icons';

interface Props {
  open: boolean;
  onClose: () => void;
  /** Câu lỗi hiện sẵn khi mở lại (server vừa báo 401). */
  initialError?: string | null;
  /** Trả về null nếu mật khẩu đúng, còn lại là câu lỗi để hiện ra. */
  onSubmit: (pass: string) => Promise<string | null>;
}

export default function LoginDialog({ open, ...rest }: Props) {
  return (
    <Modal open={open} onClose={rest.onClose} footer={null} width={390} className="login">
      {open && <Body {...rest} />}
    </Modal>
  );
}

function Body({ onClose, onSubmit, initialError = null }: Omit<Props, 'open'>) {
  const [pass, setPass] = useState('');
  const [error, setError] = useState<string | null>(initialError);
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
      <span className="login__ring" aria-hidden="true"><LockIcon size={23} strokeWidth={1.7} /></span>
      <h2 className="login__title">Đăng nhập</h2>
      <p className="login__meta">Trang quản lý học liệu chỉ dành cho người soạn bài. Dùng mật khẩu chung của site.</p>

      <Password
        data-autofocus size="lg" status={error ? 'error' : undefined}
        autoComplete="current-password" placeholder="Mật khẩu" aria-label="Mật khẩu"
        aria-describedby="login-msg" value={pass} onChange={e => setPass(e.target.value)}
      />
      <p id="login-msg" className={`login__msg${error ? ' bad' : ''}`} role={error ? 'alert' : undefined}>
        {error ?? 'Mật khẩu được nhớ trên máy này cho lần sau.'}
      </p>

      <Button type="submit" variant="filled" color="primary" size="lg" block loading={busy} disabled={!pass}>
        {busy ? 'Đang kiểm…' : 'Vào'}
      </Button>
    </form>
  );
}
