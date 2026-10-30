export type AssetKind = 'video' | 'slides' | 'audio' | 'pdf' | 'other';
export type Storage = 'repo' | 'r2' | 'youtube';

export interface Asset {
  id: number;
  kind: AssetKind;
  name: string;
  size: number;
  url: string;
  storage: Storage;
  key: string;
  createdAt: string;
}

export interface Lesson {
  id: number;
  num: number;
  title: string;
  zh: string;
  visible: boolean;
  sort: number;
  assets: Asset[];
}

export interface Course {
  id: number;
  slug: string;
  title: string;
  sort: number;
  lessons: Lesson[];
}

export interface Usage {
  dbBytes: number;
  dbLimitBytes: number;
  r2Bytes: number;
  r2LimitBytes: number;
  repoBytes: number;
  /** Số video gắn link YouTube (không tốn chỗ của mình). */
  youtubeCount?: number;
}

export interface Catalog {
  courses: Course[];
  usage: Usage;
  r2: { configured: boolean; publicUrl: string };
}

export interface CourseDraft { slug: string; title: string; sort?: number }
export interface LessonDraft { num: number; title: string; zh?: string; visible?: boolean; sort?: number }
