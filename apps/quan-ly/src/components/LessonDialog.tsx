import { useState } from 'react';
import { Button, Form, FormItem, Input, InputNumber, Modal, Switch } from 'react-liquis-glass';
import type { Lesson, LessonDraft } from '@/lib/types';

interface Props {
  open: boolean;
  lesson?: Lesson | null;
  courseTitle: string;
  defaultNum: number;
  takenNums: number[];
  onClose: () => void;
  onSubmit: (d: LessonDraft) => Promise<void>;
}

export default function LessonDialog({ open, lesson, courseTitle, onClose, ...rest }: Props) {
  const title = lesson ? `Sửa bài ${lesson.num}` : `Thêm bài — ${courseTitle}`;
  return (
    <Modal open={open} onClose={onClose} title={title} footer={null} width={480}>
      {open && <Body lesson={lesson} onClose={onClose} {...rest} />}
    </Modal>
  );
}

function Body({ lesson, defaultNum, takenNums, onClose, onSubmit }: Omit<Props, 'open' | 'courseTitle'>) {
  const [num, setNum] = useState<number | null>(lesson?.num ?? defaultNum);
  const [title, setTitle] = useState(lesson?.title ?? '');
  const [zh, setZh] = useState(lesson?.zh ?? '');
  const [visible, setVisible] = useState(lesson?.visible ?? true);
  const [tried, setTried] = useState(false);
  const [busy, setBusy] = useState(false);

  const numErr = num == null || num < 1 ? 'Số bài từ 1 trở lên.'
    : num !== lesson?.num && takenNums.includes(num) ? `Đã có bài ${num} trong giáo trình này.`
    : null;
  const titleErr = title.trim() ? null : 'Cần có tên bài.';

  const submit = (ev: React.FormEvent) => {
    ev.preventDefault();
    setTried(true);
    if (numErr || titleErr) return;
    setBusy(true);
    onSubmit({ num: num!, title: title.trim(), zh: zh.trim(), visible })
      .then(onClose, () => {})
      .finally(() => setBusy(false));
  };

  return (
    <Form onSubmit={submit} noValidate>
      <div className="form-row">
        <FormItem label="Bài số" required status={tried && numErr ? 'error' : undefined} help={tried && numErr ? numErr : undefined} className="form-row__num">
          <InputNumber value={num} min={1} step={1} precision={0} onChange={setNum} />
        </FormItem>
        <FormItem label="Tên bài (tiếng Việt)" required status={tried && titleErr ? 'error' : undefined} help={tried && titleErr ? titleErr : undefined} className="form-row__grow">
          <Input data-autofocus value={title} placeholder="Chào hỏi" onChange={e => setTitle(e.target.value)} />
        </FormItem>
      </div>
      <FormItem label="Tên tiếng Trung" help="Không bắt buộc.">
        <Input value={zh} lang="zh" className="hz-input" placeholder="你好" onChange={e => setZh(e.target.value)} />
      </FormItem>
      <FormItem label="Hiện cho người học" htmlFor="lesson-visible">
        <Switch id="lesson-visible" checked={visible} onChange={setVisible} aria-label="Hiện cho người học" />
      </FormItem>
      <div className="dialog-actions">
        <Button variant="glass" onClick={onClose}>Hủy</Button>
        <Button type="submit" variant="filled" color="primary" loading={busy}>{lesson ? 'Lưu' : 'Thêm bài'}</Button>
      </div>
    </Form>
  );
}
