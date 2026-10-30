import type { InputHTMLAttributes, Ref, ReactElement } from 'react';

/**
 * Ô nhập mật khẩu kèm nút hiện/ẩn; `type` do component tự đặt nên không nhận.
 * Nhận thêm data-* để chỗ gọi đánh dấu được ô cần tự focus (xem use-dialog).
 */
export declare function PasswordInput(
  props: Omit<InputHTMLAttributes<HTMLInputElement>, 'type'>
    & { ref?: Ref<HTMLInputElement> }
    & { [data: `data-${string}`]: unknown },
): ReactElement;
