// Danh sách bài có slide trong hsk6/ cho trang lớp học: [{ id: 'bai21', slides: ['/hsk6/bai21/slides/s-01.jpg', …] }]
// Dùng chung cho scripts/build.mjs (ghi dist/lop-hoc/lessons.json) và dev.mjs (chạy ở máy).
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

export function lessons(hsk6Dir) {
  return readdirSync(hsk6Dir)
    .filter(d => /^bai\d+$/.test(d) && existsSync(join(hsk6Dir, d, 'slides')))
    .sort()
    .map(id => ({
      id,
      slides: readdirSync(join(hsk6Dir, id, 'slides')).filter(f => f.endsWith('.jpg')).sort().map(f => `/hsk6/${id}/slides/${f}`)
    }))
    .filter(l => l.slides.length);
}
