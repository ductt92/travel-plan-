// Ô nhập mật khẩu kèm nút con mắt để xem lại mình vừa gõ gì.
//
// Dùng chung cho mọi chỗ gõ mật khẩu trong site (mã đồng bộ, mật khẩu bản đồ,
// khóa API), mà ba chỗ đó ba bộ màu khác nhau — nên component này cố tình không
// đụng tới hình thức ô nhập: nó chỉ lo chỗ đặt nút, còn viền, nền, bo góc vẫn do
// className của trang truyền vào.
import { forwardRef, useState } from 'react';
import { Icon } from './Icon.jsx';
import './password.css';

export const PasswordInput = forwardRef(function PasswordInput({ className = '', ...rest }, ref) {
  const [shown, setShown] = useState(false);
  const label = shown ? 'Ẩn mật khẩu' : 'Hiện mật khẩu';

  return (
    <span className="ui-pw">
      <input
        {...rest}
        ref={ref}
        type={shown ? 'text' : 'password'}
        className={`ui-pw__in ${className}`.trim()}
      />
      <button
        type="button" className="ui-pw__eye" onClick={() => setShown(s => !s)}
        aria-label={label} aria-pressed={shown} title={label}
      >
        <Icon name={shown ? 'eyeOff' : 'eye'} size={18} />
      </button>
    </span>
  );
});
