'use client';

import { useState, useTransition } from 'react';
import { signInAction } from '@/app/auth-actions';
import { useDialog } from '@/lib/use-dialog';

interface Props {
  open: boolean;
  onClose: () => void;
  /** Đăng nhập xong thì nạp lại trang để server dựng lại với quyền sửa. */
  onDone: () => void;
}

export default function LoginDialog({ open, onClose, onDone }: Props) {
  const { ref, onBackdropClick } = useDialog(open, onClose);

  return (
    <dialog id="dlg-login" ref={ref} onClick={onBackdropClick} aria-labelledby="login-title">
      {open && <Body onClose={onClose} onDone={onDone} />}
    </dialog>
  );
}

function Body({ onClose, onDone }: Omit<Props, 'open'>) {
  const [pass, setPass] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [busy, start] = useTransition();

  const submit = (ev: React.FormEvent) => {
    ev.preventDefault();
    setError(null);
    start(async () => {
      try {
        const res = await signInAction(pass);
        if (res.ok) {
          setPass('');
          onDone();
        } else {
          setError(res.error);
        }
      } catch (err) {
        console.error('[ban-do] đăng nhập hỏng', err);
        setError('Không gọi được server. Thử lại nhé.');
      }
    });
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
        <span className={`acts-note${error ? ' bad' : ''}`}>{error ?? 'Đăng nhập rồi mới ghi và xoá được'}</span>
        <button type="submit" className="btn primary" disabled={busy || !pass}>
          {busy ? 'Đang kiểm…' : 'Vào'}
        </button>
      </div>
    </form>
  );
}
