// Nạp nội dung trang "Ngữ pháp qua tình huống" vào Neon:  node scripts/seed-grammar.mjs [file]
// Mặc định đọc hsk6/ngu-phap/data.json (bản dựng từ bai-giang/web/ngu-phap.json). Ghi đè cả bộ trong một transaction,
// bản cũ vẫn còn trong grammar_version. DATABASE_URL đọc từ .env.local ở gốc repo, giống scripts/dev-api.mjs.
import { readFileSync, existsSync } from 'node:fs';

const envFile = new URL('../.env.local', import.meta.url);
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^(['"])(.*)\1$/, '$2');
  }
}
const { save } = await import('../backend/node/grammar.js');

const file = process.argv[2] || new URL('../hsk6/ngu-phap/data.json', import.meta.url);
const body = JSON.parse(readFileSync(file, 'utf8'));
try {
  const r = await save(body);
  console.log(`Đã ghi ${r.count} tình huống, ${body.groups.length} nhóm (phiên bản ${r.version})`);
  process.exit(0);
} catch (e) {
  console.error('Không ghi được:', e.message);
  process.exit(1);
}
