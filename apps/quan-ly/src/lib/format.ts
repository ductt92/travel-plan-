import type { AssetKind, Lesson } from './types';

const UNITS = ['B', 'KB', 'MB', 'GB', 'TB'];

/** '1,2 GB', '350 MB' — dấu phẩy thập phân kiểu Việt, cơ số 1024 như các trang quản trị. */
export function fmtBytes(n: number) {
  if (!Number.isFinite(n) || n <= 0) return '0 B';
  const i = Math.min(UNITS.length - 1, Math.floor(Math.log(n) / Math.log(1024)));
  const v = n / 1024 ** i;
  const digits = i === 0 || v >= 100 ? 0 : 1;
  return `${v.toLocaleString('vi-VN', { maximumFractionDigits: digits })} ${UNITS[i]}`;
}

export const pct = (used: number, limit: number) => (limit > 0 ? Math.min(100, (used / limit) * 100) : 0);

export const KINDS: { value: AssetKind; label: string; color: string }[] = [
  { value: 'video', label: 'Video', color: 'primary' },
  { value: 'slides', label: 'Slide', color: 'warning' },
  { value: 'audio', label: 'Audio', color: 'info' },
  { value: 'pdf', label: 'PDF', color: 'var(--t4)' },
  { value: 'other', label: 'Khác', color: 'default' },
];
export const kindInfo = (k: AssetKind) => KINDS.find(x => x.value === k) ?? KINDS[4];

/** Đoán loại theo mime, thiếu mime thì theo đuôi file. */
export function guessKind(file: { name: string; type: string }): AssetKind {
  const t = file.type;
  const ext = file.name.split('.').pop()?.toLowerCase() ?? '';
  if (t.startsWith('video/') || ['mp4', 'webm', 'mov', 'mkv', 'm4v'].includes(ext)) return 'video';
  if (t.startsWith('image/') || ['png', 'jpg', 'jpeg', 'webp', 'gif', 'svg', 'avif'].includes(ext)) return 'slides';
  if (t.startsWith('audio/') || ['mp3', 'm4a', 'wav', 'ogg', 'aac', 'flac'].includes(ext)) return 'audio';
  if (t === 'application/pdf' || ext === 'pdf') return 'pdf';
  return 'other';
}

// video YouTube nằm trên YouTube, không tính vào dung lượng của mình
export const lessonBytes = (l: Lesson) => l.assets.reduce((s, a) => s + (a.storage === 'youtube' ? 0 : a.size), 0);
export const hasYoutube = (l: Lesson) => l.assets.some(a => a.storage === 'youtube');
export const STORAGE_LABEL = { repo: 'Repo', r2: 'R2', youtube: 'YouTube' } as const;
export const lessonsBytes = (ls: Lesson[]) => ls.reduce((s, l) => s + lessonBytes(l), 0);
