// Chạy trang lớp học ở máy giống trên Vercel:  node lop-hoc/dev.mjs  → http://localhost:8780/lop-hoc/
//   /lop-hoc/              trang lớp học (index.html)
//   /lop-hoc/lessons.json  danh sách slide, tính từ hsk6/ (trên Vercel do scripts/build.mjs ghi sẵn)
//   /hsk6/…                slide các bài
//   /api/node/lop-hoc      ký token Ably (backend/node/lophoc.js), cần ABLY_API_KEY và TEACHER_PASS trong .env.local
// Chưa có khóa Ably thì thêm ?local=1 vào link để các tab cùng máy nói chuyện với nhau mà không cần Ably.
import { createServer } from 'node:http';
import { existsSync, readFileSync } from 'node:fs';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { lessons } from './lessons.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const envFile = join(root, '.env.local');
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^(['"])(.*)\1$/, '$2');
  }
}
const { default: lopHoc } = await import('../backend/node/lophoc.js');

const PORT = Number(process.env.PORT || 8780);
const TYPES = { '.html': 'text/html; charset=utf-8', '.json': 'application/json', '.jpg': 'image/jpeg', '.png': 'image/png',
  '.webp': 'image/webp', '.mp3': 'audio/mpeg', '.mp4': 'video/mp4', '.js': 'text/javascript', '.css': 'text/css' };
const HSK6 = join(root, 'hsk6');

const server = createServer(async (req, res) => {
  const path = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  try {
    if (path === '/' || path === '/lop-hoc') { res.writeHead(302, { Location: '/lop-hoc/' }); return res.end(); }
    if (path === '/lop-hoc/' || path === '/lop-hoc/index.html') {
      res.writeHead(200, { 'Content-Type': TYPES['.html'] });
      return res.end(await readFile(join(root, 'lop-hoc', 'index.html')));
    }
    if (path === '/lop-hoc/lessons.json') {
      res.writeHead(200, { 'Content-Type': TYPES['.json'] });
      return res.end(JSON.stringify(lessons(HSK6)));
    }
    if (path === '/api/node/lop-hoc') return lopHoc(req, res);
    if (path.startsWith('/hsk6/')) {
      const file = normalize(join(root, path));
      if (file.startsWith(HSK6 + sep)) {
        const body = await readFile(file);
        res.writeHead(200, { 'Content-Type': TYPES[extname(file)] || 'application/octet-stream' });
        return res.end(body);
      }
    }
  } catch { /* rơi xuống 404 */ }
  res.writeHead(404).end('không có');
});
server.on('error', err => {
  if (err.code !== 'EADDRINUSE') throw err;
  console.error(`Cổng ${PORT} đang có server khác chạy — tắt nó (lsof -ti tcp:${PORT} | xargs kill) hoặc đổi cổng: PORT=8781 node lop-hoc/dev.mjs`);
  process.exit(1);
});
server.listen(PORT, () => {
  const ably = process.env.ABLY_API_KEY ? 'có' : 'CHƯA CÓ (dùng ?local=1 để thử)';
  console.log(`Lớp học: http://localhost:${PORT}/lop-hoc/   khóa Ably: ${ably}`);
});
