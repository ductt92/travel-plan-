import { useState } from 'react';
import { Button, Form, FormItem, Input, Modal } from 'react-liquis-glass';
import { ApiError } from '@/lib/api';
import type { Lesson } from '@/lib/types';

interface Props {
  lesson: Lesson | null;
  onClose: () => void;
  /** Ném ApiError 400 khi server thấy link không phải YouTube. */
  onSubmit: (name: string, url: string) => Promise<void>;
}

// kiểm sơ ở trình duyệt cho đỡ một lượt gọi; server mới là nơi kiểm và chuẩn hóa thật
const LOOKS_YT = /^(https?:\/\/)?([a-z0-9-]+\.)*(youtube\.com|youtu\.be|youtube-nocookie\.com)\//i;

export default function YoutubeDialog({ lesson, onClose, onSubmit }: Props) {
  return (
    <Modal open={!!lesson} onClose={onClose} title={lesson ? `Thêm video YouTube — bài ${lesson.num}` : ''} footer={null} width={500}>
      {lesson && <Body lesson={lesson} onClose={onClose} onSubmit={onSubmit} />}
    </Modal>
  );
}

function Body({ lesson, onClose, onSubmit }: { lesson: Lesson } & Omit<Props, 'lesson'>) {
  const [url, setUrl] = useState('');
  const [name, setName] = useState(lesson.title);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const submit = (ev: React.FormEvent) => {
    ev.preventDefault();
    const link = url.trim();
    if (!link) return setError('Dán link video vào đây.');
    if (!LOOKS_YT.test(link)) return setError('Link này không giống link YouTube (youtube.com/watch?v=… hoặc youtu.be/…).');
    setError(null);
    setBusy(true);
    onSubmit(name.trim() || lesson.title, link)
      .then(onClose, (err: Error) => {
        // 400 là lỗi của link, hiện ngay dưới ô; lỗi khác App đã báo bằng toast
        if (err instanceof ApiError && err.status === 400) setError(err.message);
      })
      .finally(() => setBusy(false));
  };

  return (
    <Form onSubmit={submit} noValidate>
      <FormItem
        label="Link YouTube" required status={error ? 'error' : undefined}
        help={error ?? 'Video để chế độ Công khai hoặc Không công khai (unlisted) thì người học mới xem được.'}
      >
        <Input
          data-autofocus type="url" inputMode="url" autoComplete="off" spellCheck={false}
          placeholder="https://youtu.be/…" value={url} onChange={e => setUrl(e.target.value)}
        />
      </FormItem>
      <FormItem label="Tên hiển thị" help="Mặc định là tên bài.">
        <Input value={name} onChange={e => setName(e.target.value)} />
      </FormItem>
      <div className="dialog-actions">
        <Button variant="glass" onClick={onClose}>Hủy</Button>
        <Button type="submit" variant="filled" color="primary" loading={busy}>Thêm video</Button>
      </div>
    </Form>
  );
}
