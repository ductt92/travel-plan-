import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Bài Cấp 4 trở lên nằm ở src/data/lessons-N.json (Cấp 7–9 chia phần: lessons-7-p1.json, lessons-7-p2.json…), tải khi cần. Module ảo này chỉ giữ phần tóm tắt từng bài
// (tên, số từ, số điểm ngữ pháp) để lộ trình, trang cấp, bài tiếp theo hiện được mà không phải tải cả nội dung.
const DATA = fileURLToPath(new URL('./src/data/', import.meta.url));
function lessonIndex() {
  const ID = 'virtual:lesson-index', RID = '\0' + ID;
  return {
    name: 'lesson-index',
    resolveId: id => (id === ID ? RID : null),
    load(id) {
      if (id !== RID) return null;
      const out = [];
      for (const f of readdirSync(DATA).filter(f => /^lessons-\d+(-p\d+)?\.json$/.test(f)).sort()) {
        this.addWatchFile(DATA + f);
        for (const l of JSON.parse(readFileSync(DATA + f, 'utf8'))) {
          out.push({ id: l.id, lv: l.lv, no: l.no, title: l.title, zh: l.zh, tag: l.grammar[0]?.title || '', nw: l.words.length, ng: l.grammar.length });
        }
      }
      return `export default ${JSON.stringify(out)};`;
    },
    handleHotUpdate({ file, server }) {
      if (!/lessons-\d+(-p\d+)?\.json$/.test(file)) return;
      const m = server.moduleGraph.getModuleById(RID);
      if (m) server.moduleGraph.invalidateModule(m);
    }
  };
}

// App nằm ở /hoc-tieng-trung/ trên site; dùng HashRouter nên không cần cấu hình rewrite.
// /api chuyển sang `npm run dev:api` (Node + Go) khi chạy dev.
// Tách gói: dữ liệu bài Cấp 1–3 và thư viện thành file riêng. Chúng vẫn tải ngay (Vite gắn modulepreload nên
// tải song song với code app), nhưng ít đổi, nên sửa code rồi deploy thì trình duyệt giữ bản cache, không tải lại.
function manualChunks(id) {
  if (id.endsWith('/src/data/lessons.json')) return 'lessons-1-3';
  if (/node_modules\/(react|react-dom|react-router|react-router-dom|scheduler|@remix-run)\//.test(id)) return 'react';
  if (id.includes('node_modules/react-liquis-glass/')) return 'glass';
}

export default defineConfig({
  plugins: [react(), lessonIndex()],
  base: '/hoc-tieng-trung/',
  server: { proxy: { '/api': 'http://127.0.0.1:3001' } },
  // lessons-1-3 (~610 kB chưa nén) và lessons-6 (~700 kB chưa nén, ~380 kB gzip, chỉ tải khi mở Cấp 6) là dữ liệu bài,
  // không phải code, nên nâng ngưỡng cảnh báo cho vừa chúng
  build: { chunkSizeWarningLimit: 750, rollupOptions: { output: { manualChunks } } }
});
