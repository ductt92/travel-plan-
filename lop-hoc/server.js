// Bản thử lớp học trực tiếp: 1 giáo viên + vài học sinh.
// Server chỉ làm mối WebRTC (video đi thẳng giữa các máy) và chuyển nét vẽ, chat, giơ tay qua Socket.IO.
//
// Chạy:  node server.js        → http://localhost:8780
// Biến môi trường: PORT (mặc định 8780), TEACHER_PASS (mật khẩu giáo viên, mặc định "giaovien")
import { createServer } from 'node:http';
import { existsSync } from 'node:fs';
import { readFile, readdir } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';
import { Server } from 'socket.io';

const HERE = fileURLToPath(new URL('.', import.meta.url));
// Slide các bài đã dựng: trong repo da-di-qua là ../hsk6, ở thư mục làm bài là ../BaiGiang/site
const SITE = [process.env.SLIDES_DIR, join(HERE, '..', 'hsk6'), join(HERE, '..', 'BaiGiang', 'site')]
  .find(d => d && existsSync(d)) || join(HERE, '..', 'hsk6');
const PORT = Number(process.env.PORT || 8780);
const TEACHER_PASS = process.env.TEACHER_PASS || 'giaovien';
const TYPES = { '.html': 'text/html; charset=utf-8', '.jpg': 'image/jpeg', '.js': 'text/javascript' };

// Danh sách bài có slide: [{id, slides: ['/slides/bai21/s-01.jpg', …]}]
async function lessons() {
  const out = [];
  for (const id of (await readdir(SITE)).filter(d => /^bai\d+$/.test(d)).sort()) {
    const files = (await readdir(join(SITE, id, 'slides')).catch(() => [])).filter(f => f.endsWith('.jpg')).sort();
    if (files.length) out.push({ id, slides: files.map(f => `/slides/${id}/${f}`) });
  }
  return out;
}

const http = createServer(async (req, res) => {
  const path = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  try {
    if (path === '/' || path === '/index.html') {
      res.writeHead(200, { 'Content-Type': TYPES['.html'] });
      return res.end(await readFile(join(HERE, 'index.html')));
    }
    if (path === '/api/lessons') {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify(await lessons()));
    }
    const m = path.match(/^\/slides\/(bai\d+)\/([\w-]+\.jpg)$/);
    if (m) {
      const file = normalize(join(SITE, m[1], 'slides', m[2]));
      res.writeHead(200, { 'Content-Type': TYPES[extname(file)], 'Cache-Control': 'max-age=3600' });
      return res.end(await readFile(file));
    }
  } catch { /* rơi xuống 404 */ }
  res.writeHead(404).end('không có');
});

const io = new Server(http, { maxHttpBufferSize: 1e6 });

// Trạng thái từng phòng, chỉ giữ trong bộ nhớ (tắt server là mất — đủ cho bản thử)
// room = { lesson, slide, strokes: {"<lesson>:<slide>": [stroke…]}, chat: [], people: Map<socketId, person> }
const rooms = new Map();
const room = id => {
  if (!rooms.has(id)) rooms.set(id, { lesson: null, slide: 0, strokes: {}, chat: [], people: new Map() });
  return rooms.get(id);
};
const pageKey = r => `${r.lesson || 'trang'}:${r.slide}`;
const peopleOf = r => [...r.people.values()];

io.on('connection', socket => {
  let r = null, me = null, roomId = null;
  const isTeacher = () => me?.role === 'teacher';
  const canDraw = () => isTeacher() || me?.draw;
  const update = () => io.to(roomId).emit('people', peopleOf(r));

  socket.on('join', ({ room: id, name, role, pass }, ack) => {
    if (me) return;
    id = String(id || '').trim().toLowerCase().slice(0, 32);
    name = String(name || '').trim().slice(0, 30);
    if (!id || !name) return ack({ error: 'Cần nhập tên và mã phòng' });
    if (role === 'teacher' && pass !== TEACHER_PASS) return ack({ error: 'Sai mật khẩu giáo viên' });
    r = room(id); roomId = id;
    if (r.people.size >= 6) return ack({ error: 'Phòng đã đủ 6 người' });
    me = { id: socket.id, name, role: role === 'teacher' ? 'teacher' : 'student', hand: false, draw: false, mic: true, cam: true };
    // những người đã ở trong phòng: người mới sẽ gọi WebRTC tới từng người
    const others = peopleOf(r);
    r.people.set(socket.id, me);
    socket.join(id);
    ack({ me, others, lesson: r.lesson, slide: r.slide, strokes: r.strokes[pageKey(r)] || [], chat: r.chat.slice(-100) });
    socket.to(id).emit('joined', me);
    update();
  });

  // Làm mối WebRTC: chuyển nguyên offer/answer/ICE tới đúng người
  socket.on('signal', ({ to, data }) => {
    if (me && r.people.has(to)) io.to(to).emit('signal', { from: socket.id, data });
  });

  // Trạng thái mic/cam/giơ tay của chính mình
  socket.on('status', s => {
    if (!me) return;
    for (const k of ['hand', 'mic', 'cam']) if (typeof s[k] === 'boolean') me[k] = s[k];
    update();
  });

  // Giáo viên: đổi bài/slide, cho học sinh vẽ, tắt mic học sinh, hạ tay
  socket.on('goto', ({ lesson, slide }) => {
    if (!isTeacher()) return;
    r.lesson = lesson || null;
    r.slide = Math.max(0, Number(slide) || 0);
    io.to(roomId).emit('goto', { lesson: r.lesson, slide: r.slide, strokes: r.strokes[pageKey(r)] || [] });
  });
  socket.on('allow-draw', ({ id, on }) => {
    const p = isTeacher() && r.people.get(id);
    if (p) { p.draw = !!on; update(); }
  });
  socket.on('mute', ({ id }) => {
    if (isTeacher() && r.people.has(id)) io.to(id).emit('muted');
  });
  socket.on('lower-hand', ({ id }) => {
    const p = isTeacher() && r.people.get(id);
    if (p) { p.hand = false; update(); }
  });

  // Nét vẽ: tọa độ chuẩn hóa 0..1 theo khung slide. Gửi từng đoạn để người khác thấy ngay khi đang vẽ.
  socket.on('stroke:start', s => {
    if (!canDraw()) return;
    const stroke = { id: String(s.id).slice(0, 40), by: socket.id, color: String(s.color).slice(0, 20),
      width: Math.min(40, Number(s.width) || 3), points: Array.isArray(s.points) ? s.points.slice(0, 2000) : [] };
    (r.strokes[pageKey(r)] ||= []).push(stroke);
    socket.to(roomId).emit('stroke:start', stroke);
  });
  socket.on('stroke:points', ({ id, points }) => {
    if (!canDraw()) return;
    const st = (r.strokes[pageKey(r)] || []).find(x => x.id === id && x.by === socket.id);
    if (!st || !Array.isArray(points) || st.points.length > 5000) return;
    st.points.push(...points.slice(0, 500));
    socket.to(roomId).emit('stroke:points', { id, points });
  });
  socket.on('undo', () => {
    if (!canDraw()) return;
    const list = r.strokes[pageKey(r)] || [];
    // giáo viên xóa nét mới nhất của bất kỳ ai, học sinh chỉ xóa nét của mình
    for (let i = list.length - 1; i >= 0; i--) {
      if (isTeacher() || list[i].by === socket.id) {
        const [gone] = list.splice(i, 1);
        io.to(roomId).emit('remove', gone.id);
        break;
      }
    }
  });
  socket.on('clear', () => {
    if (!isTeacher()) return;
    r.strokes[pageKey(r)] = [];
    io.to(roomId).emit('clear');
  });

  socket.on('chat', text => {
    if (!me) return;
    text = String(text || '').trim().slice(0, 500);
    if (!text) return;
    const msg = { name: me.name, role: me.role, text, at: Date.now() };
    r.chat.push(msg);
    if (r.chat.length > 200) r.chat.shift();
    io.to(roomId).emit('chat', msg);
  });

  socket.on('disconnect', () => {
    if (!me) return;
    r.people.delete(socket.id);
    io.to(roomId).emit('left', socket.id);
    update();
    if (!r.people.size) setTimeout(() => { if (!r.people.size) rooms.delete(roomId); }, 10 * 60 * 1000);
  });
});

http.on('error', err => {
  if (err.code !== 'EADDRINUSE') throw err;
  console.error(`Cổng ${PORT} đang có server khác chạy (có thể chính lớp học này đã bật sẵn) — mở thẳng http://localhost:${PORT}`);
  console.error(`Muốn chạy lại thì tắt server cũ:  lsof -ti tcp:${PORT} | xargs kill   — hoặc đổi cổng:  PORT=8781 npm start`);
  process.exit(1);
});
http.listen(PORT, () => console.log(`Lớp học thử: http://localhost:${PORT}  (mật khẩu giáo viên: ${TEACHER_PASS})`));
