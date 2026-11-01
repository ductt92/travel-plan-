import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Bài Cấp 4 trở lên nằm ở src/data/lessons-N.json, tải khi cần. Module ảo này chỉ giữ phần tóm tắt từng bài
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
      for (const f of readdirSync(DATA).filter(f => /^lessons-\d+\.json$/.test(f)).sort()) {
        this.addWatchFile(DATA + f);
        for (const l of JSON.parse(readFileSync(DATA + f, 'utf8'))) {
          out.push({ id: l.id, lv: l.lv, no: l.no, title: l.title, zh: l.zh, tag: l.grammar[0]?.title || '', nw: l.words.length, ng: l.grammar.length });
        }
      }
      return `export default ${JSON.stringify(out)};`;
    },
    handleHotUpdate({ file, server }) {
      if (!/lessons-\d+\.json$/.test(file)) return;
      const m = server.moduleGraph.getModuleById(RID);
      if (m) server.moduleGraph.invalidateModule(m);
    }
  };
}

// App nằm ở /hoc-tieng-trung/ trên site; dùng HashRouter nên không cần cấu hình rewrite.
// /api chuyển sang `npm run dev:api` (Node + Go) khi chạy dev.
export default defineConfig({ plugins: [react(), lessonIndex()], base: '/hoc-tieng-trung/', server: { proxy: { '/api': 'http://127.0.0.1:3001' } } });
