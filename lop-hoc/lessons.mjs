// Danh sách bài có slide trong hsk6/ cho trang lớp học:
//   [{ id: 'bai21', title: 'Bài 21: Cửa hàng tương lai', zh: '未来商店',
//      slides: ['/hsk6/bai21/slides/s-01.jpg', …], titles: ['Bài 21: Cửa hàng tương lai', 'Mục tiêu bài học', …],
//      sections: ['', 'Mở đầu', …] }]
// Tên bài và tiêu đề slide lấy từ slides/titles.json (BaiGiang/build_site.py ghi ra); thiếu file thì để trống.
// Dùng chung cho scripts/build.mjs (ghi dist/lop-hoc/lessons.json) và dev.mjs (chạy ở máy).
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

function titles(dir) {
  try { return JSON.parse(readFileSync(join(dir, 'titles.json'), 'utf8')); } catch { return {}; }
}

export function lessons(hsk6Dir) {
  return readdirSync(hsk6Dir)
    .filter(d => /^bai\d+$/.test(d) && existsSync(join(hsk6Dir, d, 'slides')))
    .sort()
    .map(id => {
      const dir = join(hsk6Dir, id, 'slides');
      const t = titles(dir);
      const slides = readdirSync(dir).filter(f => f.endsWith('.jpg')).sort().map(f => `/hsk6/${id}/slides/${f}`);
      const info = slides.map((_, i) => t.slides?.[i] || {});
      return { id, title: t.title || '', zh: t.zh || '', slides,
        titles: info.map(s => s.title || ''), sections: info.map(s => s.section || '') };
    })
    .filter(l => l.slides.length);
}
