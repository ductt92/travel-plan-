import { useEffect, useRef, useState } from 'react';
import {
  Alert, Button, Descriptions, Drawer, Empty, IconButton, List, ListItem, Popconfirm, Progress, Select, Tag, Upload, message,
} from 'react-liquis-glass';
import { CloseIcon, ExternalLinkIcon, TrashIcon, UploadIcon, VideoIcon } from 'react-liquis-glass/icons';
import { ApiError, MAX_UPLOAD, deleteAsset, uploadAsset } from '@/lib/api';
import { KINDS, STORAGE_LABEL, fmtBytes, guessKind, kindInfo, lessonBytes } from '@/lib/format';
import type { Asset, AssetKind, Lesson } from '@/lib/types';

interface Props {
  lesson: Lesson | null;
  r2Configured: boolean;
  onClose: () => void;
  /** Gọi lại sau mỗi lần thêm/xoá file để nạp lại danh mục và dung lượng. */
  onChanged: () => Promise<void>;
  onAddYoutube: (l: Lesson) => void;
}

export default function AssetsDrawer({ lesson, onClose, ...rest }: Props) {
  // giữ bài cuối cùng để lúc trượt đóng vẫn còn nội dung
  const last = useRef<Lesson | null>(null);
  if (lesson) last.current = lesson;
  const shown = lesson ?? last.current;
  return (
    <Drawer
      open={!!lesson} onClose={onClose} size={480} className="assets-drawer"
      title={shown ? <>Bài {shown.num}: {shown.title}</> : null}
    >
      {shown && <Body key={shown.id} lesson={shown} {...rest} />}
    </Drawer>
  );
}

interface Item {
  uid: number;
  file: File;
  kind: AssetKind;
  status: 'ready' | 'uploading' | 'done' | 'error';
  percent: number;
  error?: string;
}

let seed = 0;
const storageColor = { repo: 'warning', r2: 'success', youtube: 'danger' } as const;

function Body({ lesson, r2Configured, onChanged, onAddYoutube }: Omit<Props, 'onClose' | 'lesson'> & { lesson: Lesson }) {
  const [queue, setQueue] = useState<Item[]>([]);
  const [r2Missing, setR2Missing] = useState(false);
  const [running, setRunning] = useState(false);
  const abort = useRef<AbortController | null>(null);
  useEffect(() => () => abort.current?.abort(), []);

  const patch = (uid: number, p: Partial<Item>) => setQueue(q => q.map(it => (it.uid === uid ? { ...it, ...p } : it)));

  const accept = (file: File) => {
    if (file.size > MAX_UPLOAD) {
      message.error(`${file.name} nặng ${fmtBytes(file.size)}, quá giới hạn ${fmtBytes(MAX_UPLOAD)} mỗi file.`);
      return false;
    }
    setQueue(q => [...q, { uid: ++seed, file, kind: guessKind(file), status: 'ready', percent: 0 }]);
    // Upload chỉ dùng để chọn file; danh sách và tiến độ do mình vẽ để còn chọn loại
    return false;
  };

  const start = async () => {
    const todo = queue.filter(it => it.status === 'ready' || it.status === 'error');
    if (!todo.length) return;
    setRunning(true);
    abort.current = new AbortController();
    let ok = 0;
    for (const it of todo) {
      if (abort.current.signal.aborted) break;
      patch(it.uid, { status: 'uploading', percent: 0, error: undefined });
      try {
        await uploadAsset(lesson.id, it.file, it.kind, p => patch(it.uid, { percent: p }), abort.current.signal);
        patch(it.uid, { status: 'done', percent: 100 });
        ok++;
        setR2Missing(false);
      } catch (err) {
        const e = err as ApiError;
        patch(it.uid, { status: 'error', error: e.message });
        if (e.status === 503) {
          // server chưa có R2: các file sau cũng sẽ hỏng y vậy, dừng luôn
          setR2Missing(true);
          break;
        }
      }
    }
    setRunning(false);
    if (ok) {
      message.success(`Đã tải lên ${ok} file.`);
      await onChanged();
      setQueue(q => q.filter(it => it.status !== 'done'));
    }
  };

  const remove = (a: Asset) =>
    deleteAsset(a.id).then(
      () => { message.success(`Đã xoá ${a.name}.`); return onChanged(); },
      (err: Error) => { message.error(err.message); },
    );

  const assets = [...lesson.assets].sort((a, b) => KINDS.findIndex(k => k.value === a.kind) - KINDS.findIndex(k => k.value === b.kind));
  const pending = queue.filter(it => it.status !== 'done');

  return (
    <div className="drawer-body">
      <Descriptions
        column={2}
        items={[
          { label: 'Tiếng Trung', children: lesson.zh ? <span className="hz" lang="zh">{lesson.zh}</span> : '—' },
          { label: 'Trạng thái', children: lesson.visible ? 'Đang hiện' : 'Đang ẩn' },
          { label: 'Số tài liệu', children: lesson.assets.length },
          { label: 'Dung lượng', children: fmtBytes(lessonBytes(lesson)) },
        ]}
      />

      <section aria-labelledby="up-title" className="drawer-sec">
        <div className="drawer-sec__head">
          <h3 id="up-title">Tải file lên</h3>
          <Button size="sm" variant="tinted" icon={<VideoIcon />} onClick={() => onAddYoutube(lesson)}>Thêm video YouTube</Button>
        </div>
        {(r2Missing || !r2Configured) && (
          <Alert
            type={r2Missing ? 'error' : 'warning'} showIcon
            title={r2Missing ? 'Server chưa cấu hình Cloudflare R2' : 'Cloudflare R2 chưa được cấu hình'}
            description={
              r2Missing
                ? 'Server trả lời 503: chưa có chỗ chứa file nên chưa tải lên được. Đặt các biến môi trường R2 cho server API rồi triển khai lại. Vẫn sửa danh mục, gắn video YouTube và xoá mục cũ bình thường.'
                : 'Tải file lên cần R2. Video bài giảng có thể gắn bằng link YouTube trong lúc chờ.'
            }
          />
        )}
        <Upload
          multiple disabled={running} showList={false} beforeUpload={accept}
          hint={`Video, slide (ảnh), audio, PDF — tối đa ${fmtBytes(MAX_UPLOAD)} mỗi file`}
        />
        {pending.length > 0 && (
          <ul className="queue" aria-label="File chờ tải lên">
            {pending.map(it => (
              <li key={it.uid} className={`queue__item${it.status === 'error' ? ' is-error' : ''}`}>
                <div className="queue__top">
                  <span className="queue__name" title={it.file.name}>{it.file.name}</span>
                  <span className="queue__size">{fmtBytes(it.file.size)}</span>
                  <IconButton
                    size="sm" variant="text" icon={<CloseIcon />} aria-label={`Bỏ ${it.file.name}`}
                    disabled={it.status === 'uploading'} onClick={() => setQueue(q => q.filter(x => x.uid !== it.uid))}
                  />
                </div>
                <div className="queue__bottom">
                  {/* Select của thư viện chưa nhận aria-label, nên đặt tên cho cả nhóm */}
                  <span role="group" aria-label={`Loại tài liệu của ${it.file.name}`} className="queue__kind">
                    <Select<AssetKind>
                      size="sm" value={it.kind} disabled={it.status === 'uploading'}
                      options={KINDS.map(k => ({ value: k.value, label: k.label }))}
                      onChange={v => v && patch(it.uid, { kind: v })}
                    />
                  </span>
                  {it.status === 'uploading'
                    ? <Progress percent={it.percent} size="sm" status="active" />
                    : <span className="queue__state" role={it.status === 'error' ? 'alert' : undefined}>
                        {it.status === 'error' ? it.error : 'Chờ tải lên'}
                      </span>}
                </div>
              </li>
            ))}
          </ul>
        )}
        {pending.length > 0 && (
          <div className="queue__actions">
            {running
              ? <Button variant="glass" onClick={() => abort.current?.abort()}>Hủy</Button>
              : <Button variant="glass" onClick={() => setQueue([])}>Bỏ hết</Button>}
            <Button variant="filled" color="primary" icon={<UploadIcon />} loading={running} onClick={start}>
              {running ? 'Đang tải lên…' : `Tải lên ${pending.length} file`}
            </Button>
          </div>
        )}
      </section>

      <section aria-labelledby="list-title" className="drawer-sec">
        <h3 id="list-title">Tài liệu của bài</h3>
        {assets.length === 0 ? (
          <Empty description="Bài này chưa có tài liệu nào." />
        ) : (
          <List size="sm" className="asset-list">
            {assets.map(a => {
              const k = kindInfo(a.kind);
              return (
                <ListItem
                  key={a.id}
                  prefix={<Tag size="sm" color={k.color}>{k.label}</Tag>}
                  title={<a href={a.url} target="_blank" rel="noreferrer" className="asset-link">{a.name}<ExternalLinkIcon aria-hidden="true" /><span className="ui-sr"> (mở tab mới)</span></a>}
                  description={
                    <span className="asset-meta">
                      <Tag size="sm" variant="outline" color={storageColor[a.storage]}>{STORAGE_LABEL[a.storage]}</Tag>
                      <span>{a.storage === 'youtube' ? '—' : fmtBytes(a.size)}</span>
                      {a.createdAt && <span>{new Date(a.createdAt).toLocaleDateString('vi-VN')}</span>}
                    </span>
                  }
                  extra={
                    <Popconfirm
                      title={`Xoá ${a.name}?`}
                      description={
                        a.storage === 'r2' ? 'File trên Cloudflare R2 cũng bị xoá luôn, không hoàn tác được.'
                        : a.storage === 'youtube' ? 'Chỉ gỡ link khỏi bài. Video vẫn còn trên YouTube.'
                        : 'Chỉ xoá mục trong danh mục. File vẫn nằm trong repo, muốn giảm dung lượng phải xoá trong git.'
                      }
                      okText="Xoá" okDanger placement="left" onConfirm={() => remove(a)}
                    >
                      <IconButton size="sm" variant="text" color="danger" icon={<TrashIcon />} aria-label={`Xoá ${a.name}`} />
                    </Popconfirm>
                  }
                />
              );
            })}
          </List>
        )}
      </section>
    </div>
  );
}
