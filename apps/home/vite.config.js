import { readFileSync } from 'node:fs';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Số liệu trên các thẻ tính lúc build từ dữ liệu trong repo, nên tự khớp sau mỗi lần thêm bài hay đăng video.
// Cùng nguồn với scripts/seed-catalog.mjs (trang quản lý): Hán Lộ mỗi cấp một giáo trình, HSK 6 hai quyển, 顶石中文.
const read = p => JSON.parse(readFileSync(new URL(p, import.meta.url), 'utf8'));
const lessons = read('../hoc-tieng-trung/src/data/lessons.json');
const youtube = read('../hoc-tieng-trung/src/data/youtube.json');
const mp4 = read('../hoc-tieng-trung/public/video/index.json').filter(f => !youtube[f]);   // bài chưa lên YouTube
const published = Object.values(read('../../bai-giang/web/published.json'));
const ds = published.filter(l => String(l.id).startsWith('ds')).length;
const levels = new Set(lessons.map(l => l.lv)).size;
const STATS = {
  zh: { lessons: lessons.length, words: lessons.reduce((s, l) => s + l.words.length, 0), levels,
    youtube: Object.keys(youtube).length, videos: Object.keys(youtube).length + mp4.length },
  hsk6: {
    lessons: published.length, ds,
    words: published.reduce((s, l) => s + (l.vocab?.length || 0), 0),
    hours: published.reduce((s, l) => s + l.chapters.reduce((t, c) => t + c.dur, 0), 0) / 3600,
  },
  courses: levels + 2 + (ds ? 1 : 0),
};

// Trang chủ nằm ở gốc site: dist/index.html
export default defineConfig({ plugins: [react()], base: '/', define: { __STATS__: JSON.stringify(STATS) } });
