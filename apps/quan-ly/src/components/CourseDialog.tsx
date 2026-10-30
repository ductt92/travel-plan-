import { useState } from 'react';
import { Button, Form, FormItem, Input, InputNumber, Modal } from 'react-liquis-glass';
import type { Course, CourseDraft } from '@/lib/types';

interface Props {
  open: boolean;
  /** Có course là sửa (slug khóa lại), không có là thêm mới. */
  course?: Course | null;
  defaultSort: number;
  takenSlugs: string[];
  onClose: () => void;
  onSubmit: (d: CourseDraft) => Promise<void>;
}

const SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export default function CourseDialog({ open, course, onClose, ...rest }: Props) {
  return (
    <Modal open={open} onClose={onClose} title={course ? 'Sửa giáo trình' : 'Thêm giáo trình'} footer={null} width={460}>
      {open && <Body course={course} onClose={onClose} {...rest} />}
    </Modal>
  );
}

function Body({ course, defaultSort, takenSlugs, onClose, onSubmit }: Omit<Props, 'open'>) {
  const [slug, setSlug] = useState(course?.slug ?? '');
  const [title, setTitle] = useState(course?.title ?? '');
  const [sort, setSort] = useState<number | null>(course?.sort ?? defaultSort);
  const [tried, setTried] = useState(false);
  const [busy, setBusy] = useState(false);

  const slugErr = course ? null
    : !slug ? 'Cần có mã.'
    : !SLUG.test(slug) ? 'Chỉ chữ thường không dấu, số và gạch nối, ví dụ hsk6-thuong.'
    : takenSlugs.includes(slug) ? 'Mã này đã có.'
    : null;
  const titleErr = title.trim() ? null : 'Cần có tên.';

  const submit = (ev: React.FormEvent) => {
    ev.preventDefault();
    setTried(true);
    if (slugErr || titleErr) return;
    setBusy(true);
    onSubmit({ slug, title: title.trim(), sort: sort ?? undefined })
      .then(onClose, () => {})
      .finally(() => setBusy(false));
  };

  return (
    <Form onSubmit={submit} noValidate>
      <FormItem
        label="Mã (slug)" required={!course}
        status={tried && slugErr ? 'error' : undefined}
        help={tried && slugErr ? slugErr : course ? 'Mã dùng trong đường dẫn, không đổi được.' : 'Ví dụ: hsk1, hsk6-ha, dinh-thach.'}
      >
        <Input
          data-autofocus={!course || undefined} value={slug} disabled={!!course} autoComplete="off" spellCheck={false}
          placeholder="hsk1" onChange={e => setSlug(e.target.value.toLowerCase().replace(/\s+/g, '-'))}
        />
      </FormItem>
      <FormItem label="Tên giáo trình" required status={tried && titleErr ? 'error' : undefined} help={tried && titleErr ? titleErr : undefined}>
        <Input data-autofocus={course ? true : undefined} value={title} placeholder="HSK 6 — Quyển Thượng" onChange={e => setTitle(e.target.value)} />
      </FormItem>
      <FormItem label="Thứ tự" help="Số nhỏ đứng trước.">
        <InputNumber value={sort} min={0} step={1} precision={0} onChange={setSort} />
      </FormItem>
      <div className="dialog-actions">
        <Button variant="glass" onClick={onClose}>Hủy</Button>
        <Button type="submit" variant="filled" color="primary" loading={busy}>{course ? 'Lưu' : 'Thêm'}</Button>
      </div>
    </Form>
  );
}
