// Chạy cả hai bản API ở máy giống trên Vercel: npm run dev:api
//   /api/node/sync, /api/node/ai, /api/node/terms → backend/node (chạy ngay trong tiến trình này)
//   /api/go/sync,   /api/go/ai,   /api/go/terms   → backend/go qua `go run ./cmd/dev-api`
// Biến môi trường đọc từ .env.local ở gốc repo (không đưa lên git, mẫu ở .env.example).
import http from 'node:http';
import { spawn } from 'node:child_process';
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const envFile = new URL('../.env.local', import.meta.url);
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^(['"])(.*)\1$/, '$2');
  }
}
// nạp sau khi có biến môi trường
const { default: nodeSync } = await import('../backend/node/sync.js');
const { default: nodeAi } = await import('../backend/node/ai.js');
const { default: nodeTerms } = await import('../backend/node/terms.js');

const PORT = Number(process.env.API_PORT || 3001);
const GO_PORT = String(PORT + 1);
const go = spawn('go', ['run', './cmd/dev-api'], { cwd: root, env: { ...process.env, GO_API_PORT: GO_PORT }, stdio: 'inherit' });
process.on('exit', () => go.kill());
for (const sig of ['SIGINT', 'SIGTERM']) process.on(sig, () => process.exit());

const NODE_ROUTES = { '/api/node/sync': nodeSync, '/api/node/ai': nodeAi, '/api/node/terms': nodeTerms };

http.createServer((req, res) => {
  const path = req.url.split('?')[0];
  if (NODE_ROUTES[path]) return NODE_ROUTES[path](req, res);
  if (!path.startsWith('/api/go/')) { res.statusCode = 404; return res.end('không có route này'); }
  const up = http.request({ host: '127.0.0.1', port: GO_PORT, path: req.url, method: req.method, headers: req.headers }, r => {
    res.writeHead(r.statusCode, r.headers);
    r.pipe(res);
  });
  up.on('error', () => { res.statusCode = 502; res.end('{"error":"API Go chưa chạy xong, thử lại sau vài giây"}'); });
  req.pipe(up);
}).listen(PORT, '127.0.0.1', () => console.log(`API Node: http://localhost:${PORT}/api/node/{sync,ai,terms} (Go chuyển tiếp qua /api/go/...)`));
