import { useEffect, useRef } from 'react';

/**
 * Nối một <dialog> thật với biến `open` của React.
 *
 * `modal` false là mở kiểu không-modal: không có nền mờ, trang phía sau vẫn bấm
 * được (dùng cho bảng tỉnh bên phải màn rộng) nhưng cũng không tự đóng bằng Esc.
 * Đổi `modal` lúc đang mở thì phải đóng rồi mở lại — mà sự kiện `close` chạy sau
 * một nhịp, nên cần cờ để lần đóng kỹ thuật đó không bị hiểu là người dùng đóng.
 */
export function useDialog(open: boolean, onClose: () => void, modal = true) {
  const ref = useRef<HTMLDialogElement>(null);
  const shownAsModal = useRef<boolean | null>(null);
  const selfClosing = useRef(false);

  useEffect(() => {
    const d = ref.current;
    if (!d) return;

    if (!open) {
      if (d.open) {
        selfClosing.current = true;
        d.close();
      }
      shownAsModal.current = null;
      return;
    }

    if (d.open && shownAsModal.current === modal) return;
    if (d.open) {
      selfClosing.current = true;
      d.close();
    }
    if (modal) d.showModal();
    else d.show();
    // showModal tự nhảy vào nút bấm được đầu tiên (thường là nút ✕); ô nào đánh dấu
    // data-autofocus thì nhường cho nó, để mở popup Tìm tỉnh là gõ được ngay
    d.querySelector<HTMLElement>('[data-autofocus]')?.focus();
    shownAsModal.current = modal;
  }, [open, modal]);

  useEffect(() => {
    const d = ref.current;
    if (!d) return;
    const handle = () => {
      if (selfClosing.current) {
        selfClosing.current = false;
        return;
      }
      onClose();
    };
    d.addEventListener('close', handle);
    return () => d.removeEventListener('close', handle);
  }, [onClose]);

  /**
   * Bấm ra vùng nền của popup thì đóng; bấm vào ruột popup thì không. Kiểu bảng
   * bên phải không có nền mờ nào để bấm ra, nên ở đó bỏ qua — lỡ tay chạm trúng
   * mép bảng mà nó đóng mất thì khó chịu.
   */
  const onBackdropClick = (ev: React.MouseEvent<HTMLDialogElement>) => {
    if (modal && ev.target === ref.current) onClose();
  };

  return { ref, onBackdropClick };
}
