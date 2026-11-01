import { useState } from 'react';
import { Button, Input, Modal, Password } from 'react-liquis-glass';
import { LockIcon } from 'react-liquis-glass/icons';

interface Props {
  open: boolean;
  onClose: () => void;
  /** Câu hiện sẵn khi mở (vd. server vừa báo 401). */
  initialError?: string | null;
  /** Trả về null nếu đăng nhập được, còn lại là câu lỗi để hiện ra. */
  onSubmit: (username: string, password: string) => Promise<string | null>;
}

// chọn nhanh tên; gõ tay tên khác (tài khoản mới sau này) vẫn được
const QUICK = ['Đức', 'Ngọc'];

export default function LoginDialog({ open, ...rest }: Props) {
  return (
    <Modal open={open} onClose={rest.onClose} footer={null} width={390} className="login">
      {open && <Body {...rest} />}
    </Modal>
  );
}

function Body({ onClose, onSubmit, initialError = null }: Omit<Props, 'open'>) {
  const [name, setName] = useState('');
  const [pass, setPass] = useState('');
  const [error, setError] = useState<string | null>(initialError);
  const [busy, setBusy] = useState(false);

  const submit = (ev: React.FormEvent) => {
    ev.preventDefault();
    setError(null);
    setBusy(true);
    onSubmit(name, pass)
      .then(err => (err ? setError(err) : onClose()))
      .finally(() => setBusy(false));
  };

  return (
    <form className="login__form" onSubmit={submit}>
      <span className="login__ring" aria-hidden="true"><LockIcon size={23} strokeWidth={1.7} /></span>
      <h2 className="login__title">Đăng nhập</h2>
      <p className="login__meta">Mỗi người một tài khoản: thêm hay sửa gì cũng ghi tên người đó. Dùng chung với trang bản đồ.</p>

      <div className="login__who" role="group" aria-label="Chọn nhanh tài khoản">
        {QUICK.map(n => (
          <Button key={n} size="sm" variant={name === n ? 'filled' : 'tinted'} color="primary" onClick={() => setName(n)}>{n}</Button>
        ))}
      </div>
      <Input
        data-autofocus size="lg" autoComplete="username" placeholder="Tên đăng nhập" aria-label="Tên đăng nhập"
        value={name} onChange={e => setName(e.target.value)}
      />
      <Password
        className="login__pass" size="lg" status={error ? 'error' : undefined}
        autoComplete="current-password" placeholder="Mật khẩu" aria-label="Mật khẩu"
        aria-describedby="login-msg" value={pass} onChange={e => setPass(e.target.value)}
      />
      <p id="login-msg" className={`login__msg${error ? ' bad' : ''}`} role={error ? 'alert' : undefined}>
        {error ?? 'Phiên đăng nhập được nhớ trên máy này cho lần sau.'}
      </p>

      <Button type="submit" variant="filled" color="primary" size="lg" block loading={busy} disabled={!name.trim() || !pass}>
        {busy ? 'Đang kiểm…' : 'Vào'}
      </Button>
    </form>
  );
}
