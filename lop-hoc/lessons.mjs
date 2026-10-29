// Danh sách bài cho trang lớp học, gộp hai nguồn:
//   - Hán Lộ (apps/hoc-tieng-trung, HSK 3.0 cấp 1–3): slide là trang bài giảng của app, nhúng qua
//     /hoc-tieng-trung/#/slide/<bài>/<trang> (kind 'frame')
//   - HSK 6 của Ngọc (hsk6/<bài>/slides/*.jpg, dựng bằng BaiGiang/build_site.py): slide là ảnh (kind 'img')
// Mỗi bài: { id, group: 'HSK 1', source, kind, title: 'HSK 1 · Bài 1 · Xin chào', zh, slides: [url…], titles: [tiêu đề slide…], sections: [phần…] }
// Dùng chung cho scripts/build.mjs (ghi dist/lop-hoc/lessons.json) và dev.mjs (chạy ở máy).
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const readJson = file => { try { return JSON.parse(readFileSync(file, 'utf8')); } catch { return null; } };

// Thứ tự trang phải khớp buildLecture() trong apps/hoc-tieng-trung/src/core/lecture.js:
// mở đầu → từng từ mới → mẹo nhớ → ngữ pháp → hội thoại → tổng kết
function hanLo(root) {
  const raw = readJson(join(root, 'apps', 'hoc-tieng-trung', 'src', 'data', 'lessons.json')) || [];
  return raw.map(l => {
    const pages = [[`Bài ${l.no}: ${l.title}`, 'Mở đầu']];
    l.words.forEach((w, i) => pages.push([`Từ mới ${i + 1}/${l.words.length}: ${w[0]} (${w[1]}) – ${w[3]}`, 'Từ mới']));
    l.lecture.tips.forEach((_, i) => pages.push([`Mẹo nhớ ${i + 1}/${l.lecture.tips.length}`, 'Mẹo nhớ']));
    l.grammar.forEach((g, i) => pages.push([`Ngữ pháp ${i + 1}: ${g.title}`, 'Ngữ pháp']));
    l.dialogs.forEach((d, i) => pages.push([`Hội thoại ${i + 1}: ${d.title}`, 'Hội thoại']));
    pages.push(['Tổng kết', 'Tổng kết']);
    return {
      id: `hl-${l.id}`, group: `HSK ${l.lv}`, source: 'Hán Lộ', kind: 'frame',
      title: `HSK ${l.lv} · Bài ${l.no} · ${l.title}`, zh: l.zh,
      slides: pages.map((_, i) => `/hoc-tieng-trung/#/slide/${l.id}/${i}`),
      titles: pages.map(p => p[0]), sections: pages.map(p => p[1])
    };
  });
}

// Tên bài và tiêu đề slide lấy từ slides/titles.json; thiếu file thì để trống
function hsk6(root) {
  const dir = join(root, 'hsk6');
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter(d => /^bai\d+$/.test(d) && existsSync(join(dir, d, 'slides')))
    .sort()
    .map(id => {
      const sdir = join(dir, id, 'slides');
      const t = readJson(join(sdir, 'titles.json')) || {};
      const slides = readdirSync(sdir).filter(f => f.endsWith('.jpg')).sort().map(f => `/hsk6/${id}/slides/${f}`);
      const info = slides.map((_, i) => t.slides?.[i] || {});
      // "Bài 21: Cửa hàng tương lai" → "HSK 6 · Bài 21 · Cửa hàng tương lai"
      const m = (t.title || '').match(/^Bài\s*(\d+)\s*[:：]\s*(.+)$/);
      return { id, group: 'HSK 6', source: 'Giáo trình chuẩn HSK 6', kind: 'img',
        title: m ? `HSK 6 · Bài ${m[1]} · ${m[2]}` : `HSK 6 · Bài ${Number(id.slice(3))}`, zh: t.zh || '', slides,
        titles: info.map(s => s.title || ''), sections: info.map(s => s.section || '') };
    })
    .filter(l => l.slides.length);
}

export function lessons(root) {
  return [...hanLo(root), ...hsk6(root)];
}
