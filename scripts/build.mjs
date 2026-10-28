// Build toàn site vào dist/:
//   dist/                  ← apps/home (trang chủ)
//   dist/hoc-tieng-trung/  ← apps/hoc-tieng-trung (kèm public/audio, public/video)
//   dist/ban-do/           ← apps/ban-do (bản đồ "đã đi qua")
//   dist/travel/           ← travel/ (trang tĩnh, chưa chuyển sang React)
//   dist/hsk6/             ← hsk6/ (trang tĩnh "Ngọc học tiếng Trung", dựng sẵn bằng BaiGiang/build_site.py)
//   dist/lop-hoc/          ← lop-hoc/index.html + lessons.json (lớp học trực tiếp, slide lấy từ /hsk6/)
import { execSync } from 'node:child_process';
import { cpSync, rmSync, mkdirSync, writeFileSync } from 'node:fs';
import { lessons } from '../lop-hoc/lessons.mjs';

const run = cmd => execSync(cmd, { stdio: 'inherit' });
rmSync('dist', { recursive: true, force: true });
run('npm -w apps/home run build');
run('npm -w apps/hoc-tieng-trung run build');
run('npm -w apps/ban-do run build');
mkdirSync('dist', { recursive: true });
cpSync('apps/home/dist', 'dist', { recursive: true });
cpSync('apps/hoc-tieng-trung/dist', 'dist/hoc-tieng-trung', { recursive: true });
cpSync('apps/ban-do/dist', 'dist/ban-do', { recursive: true });
cpSync('travel', 'dist/travel', { recursive: true, filter: src => !src.endsWith('README.md') });
cpSync('hsk6', 'dist/hsk6', { recursive: true });
mkdirSync('dist/lop-hoc', { recursive: true });
cpSync('lop-hoc/index.html', 'dist/lop-hoc/index.html');
writeFileSync('dist/lop-hoc/lessons.json', JSON.stringify(lessons('hsk6')));
console.log('\nĐã build xong vào dist/');
