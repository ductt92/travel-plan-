import { useState } from 'react';
import { Button, Input, Modal, Password } from 'react-liquis-glass';
import { LockIcon } from './icons';

interface Props {
  open: boolean;
  onClose: () => void;
  /** Trả về null nếu đăng nhập được, còn lại là câu lỗi để hiện ra. */
  onSubmit: (username: string, password: string) => Promise<string | null>;
}

// chọn nhanh tên; gõ tay tên khác (tài khoản mới sau này) vẫn được
const QUICK = ['Đức', 'Ngọc'];

export default function LoginDialog({ open, onClose, onSubmit }: Props) {
  return (
    <Modal open={open} onClose={onClose} footer={null} width={390} className="login">
      {open && <Body onClose={onClose} onSubmit={onSubmit} />}
    </Modal>
  );
}

function Body({ onClose, onSubmit }: Omit<Props, 'open'>) {
  const [name, setName] = useState('');
  const [pass, setPass] = useState('');
  const [error, setError] = useState<string | null>(null);
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
      <span className="login__ring" aria-hidden="true"><LockIcon size={23} width={1.7} /></span>
      <h3>Đăng nhập</h3>
      <p className="meta">
        Mỗi người một tài khoản: chuyến nào thêm hay sửa sẽ ghi tên người đó. Dùng chung với trang quản lý.
      </p>

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
        value={pass} onChange={e => setPass(e.target.value)}
      />
      <p className={`login__msg${error ? ' bad' : ''}`} role={error ? 'alert' : undefined}>
        {error ?? 'Đăng nhập rồi mới ghi và xoá được'}
      </p>

      <Button type="submit" variant="filled" color="primary" size="lg" block loading={busy} disabled={!name.trim() || !pass}>
        {busy ? 'Đang kiểm…' : 'Vào'}
      </Button>
    </form>
  );
}
