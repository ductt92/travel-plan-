import { useState } from 'react';
import { Button, Empty, IconButton, Popconfirm, Switch, Table, Tag, Tooltip, type TableColumn } from 'react-liquis-glass';
import { EditIcon, PlusIcon, TrashIcon, UploadIcon, VideoIcon } from 'react-liquis-glass/icons';
import { KINDS, fmtBytes, hasYoutube, lessonBytes } from '@/lib/format';
import type { Lesson } from '@/lib/types';

interface Props {
  lessons: Lesson[];
  onToggle: (l: Lesson, visible: boolean) => Promise<void>;
  onEdit: (l: Lesson) => void;
  onDelete: (l: Lesson) => Promise<void>;
  onFiles: (l: Lesson) => void;
  onYoutube: (l: Lesson) => void;
  onAdd: () => void;
}

/** Gom file theo loại: "Video 2 · 700 MB". Video YouTube tách riêng thành tag "YouTube". */
function KindTags({ lesson }: { lesson: Lesson }) {
  const own = lesson.assets.filter(a => a.storage !== 'youtube');
  const tags = KINDS.map(k => {
    const xs = own.filter(a => a.kind === k.value);
    return xs.length ? { ...k, n: xs.length, size: xs.reduce((s, a) => s + a.size, 0) } : null;
  }).filter(Boolean) as (typeof KINDS[number] & { n: number; size: number })[];
  if (!tags.length && !hasYoutube(lesson)) return <span className="muted">Chưa có</span>;
  return (
    <span className="kind-tags">
      {hasYoutube(lesson) && <Tag size="sm" color="danger" icon={<VideoIcon />}>YouTube</Tag>}
      {tags.map(t => (
        <Tag key={t.value} size="sm" color={t.color}>
          {t.label}{t.n > 1 ? ` ${t.n}` : ''} · {fmtBytes(t.size)}
        </Tag>
      ))}
    </span>
  );
}

function VisibleSwitch({ lesson, onToggle }: { lesson: Lesson; onToggle: Props['onToggle'] }) {
  const [busy, setBusy] = useState(false);
  return (
    <Switch
      size="sm" checked={lesson.visible} loading={busy}
      aria-label={`Hiện bài ${lesson.num} cho người học`}
      onChange={v => { setBusy(true); onToggle(lesson, v).finally(() => setBusy(false)); }}
    />
  );
}

export default function LessonTable({ lessons, onToggle, onEdit, onDelete, onFiles, onYoutube, onAdd }: Props) {
  const columns: TableColumn<Lesson>[] = [
    { key: 'num', title: 'Bài', width: 64, align: 'center', sorter: (a, b) => a.num - b.num, render: n => <b className="ui-num">{n}</b> },
    {
      key: 'title', title: 'Tên bài',
      render: (_, l) => (
        <div className={`lesson-name${l.visible ? '' : ' is-hidden'}`}>
          <span>{l.title}</span>
          {l.zh && <span className="hz" lang="zh">{l.zh}</span>}
        </div>
      ),
    },
    {
      key: 'assets', title: 'Tài liệu',
      render: (_, l) => (
        <button type="button" className="cell-btn" onClick={() => onFiles(l)} aria-label={`Xem ${l.assets.length} tài liệu của bài ${l.num}`}>
          <KindTags lesson={l} />
        </button>
      ),
    },
    {
      key: 'size', title: 'Dung lượng', align: 'right', width: 110,
      sorter: (a, b) => lessonBytes(a) - lessonBytes(b),
      render: (_, l) => <span className="ui-num nowrap">{lessonBytes(l) ? fmtBytes(lessonBytes(l)) : '—'}</span>,
    },
    { key: 'visible', title: 'Hiện', width: 70, align: 'center', render: (_, l) => <VisibleSwitch lesson={l} onToggle={onToggle} /> },
    {
      key: 'actions', title: <span className="ui-sr">Thao tác</span>, width: 176, align: 'right',
      render: (_, l) => (
        <span className="row-actions">
          <Tooltip title="Tài liệu & tải file lên">
            <IconButton size="sm" variant="text" icon={<UploadIcon />} aria-label={`Tải file lên bài ${l.num}`} onClick={() => onFiles(l)} />
          </Tooltip>
          <Tooltip title="Thêm video YouTube">
            <IconButton size="sm" variant="text" icon={<VideoIcon />} aria-label={`Thêm video YouTube cho bài ${l.num}`} onClick={() => onYoutube(l)} />
          </Tooltip>
          <Tooltip title="Sửa">
            <IconButton size="sm" variant="text" icon={<EditIcon />} aria-label={`Sửa bài ${l.num}`} onClick={() => onEdit(l)} />
          </Tooltip>
          <Popconfirm
            title={`Xoá bài ${l.num}?`}
            description={l.assets.length
              ? `Xoá luôn ${l.assets.length} mục tài liệu của bài; file trên R2 bị xoá theo, file trong repo và video YouTube vẫn còn. Không hoàn tác được.`
              : 'Bài chưa có tài liệu.'}
            okText="Xoá" okDanger placement="left" onConfirm={() => onDelete(l)}
          >
            <IconButton size="sm" variant="text" color="danger" icon={<TrashIcon />} aria-label={`Xoá bài ${l.num}`} />
          </Popconfirm>
        </span>
      ),
    },
  ];

  const rows = [...lessons].sort((a, b) => a.num - b.num || a.sort - b.sort);

  return (
    <Table
      className="lessons" columns={columns} dataSource={rows} rowKey="id" pagination={false} size="sm"
      emptyText={
        <Empty description="Giáo trình này chưa có bài nào.">
          <Button variant="filled" color="primary" icon={<PlusIcon />} onClick={onAdd}>Thêm bài đầu tiên</Button>
        </Empty>
      }
    />
  );
}
