import { useCallback, useEffect, useRef, useState } from 'react';
import { Button } from 'react-liquis-glass';
import { TrashIcon } from 'react-liquis-glass/icons';

export interface ConfirmOptions {
  title: string;
  content?: React.ReactNode;
  okText?: string;
  /** Việc cần làm khi bấm đồng ý; popup quay vòng chờ tới khi xong rồi mới đóng. */
  onOk: () => Promise<unknown>;
}

/**
 * Popup xác nhận trước khi xoá, có trạng thái đang xoá.
 *
 * Dùng <dialog> thật mở bằng showModal(): bảng tỉnh trên điện thoại cũng là <dialog> nằm ở
 * lớp trên cùng của trình duyệt, popup thường (z-index) sẽ bị nó che; mở sau thì nằm trên nó.
 */
export function useConfirm() {
  const [opts, setOpts] = useState<ConfirmOptions | null>(null);
  const [busy, setBusy] = useState(false);
  const ref = useRef<HTMLDialogElement>(null);

  useEffect(() => {
    const d = ref.current;
    if (!d) return;
    if (opts && !d.open) d.showModal();
    if (!opts && d.open) d.close();
  }, [opts]);

  const close = useCallback(() => { if (!busy) setOpts(null); }, [busy]);

  const ok = async () => {
    if (!opts || busy) return;
    setBusy(true);
    try { await opts.onOk(); } catch { /* lỗi đã hiện ở chỗ gọi */ }
    setBusy(false);
    setOpts(null);
  };

  const node = (
    <dialog
      ref={ref} className="confirm" aria-labelledby="confirm-title"
      // Esc: đóng popup này thôi, đừng để popup bên dưới (Modal của thư viện) nghe thấy rồi đóng theo
      onKeyDown={e => { if (e.key === 'Escape') e.stopPropagation(); }}
      onCancel={e => { e.preventDefault(); close(); }}
      onClick={e => { if (e.target === ref.current) close(); }}
    >
      {opts && (
        <div className="confirm__box" tabIndex={-1} autoFocus>
          <span className="confirm__ic" aria-hidden="true"><TrashIcon /></span>
          <h3 id="confirm-title">{opts.title}</h3>
          {opts.content && <p>{opts.content}</p>}
          <div className="confirm__acts">
            <Button onClick={close} disabled={busy}>Huỷ</Button>
            <Button variant="filled" color="danger" loading={busy} onClick={ok}>
              {busy ? 'Đang xoá…' : (opts.okText ?? 'Xoá')}
            </Button>
          </div>
        </div>
      )}
    </dialog>
  );

  return [node, setOpts] as const;
}
