// POST /api/node/lop-hoc  { room, clientId, pass? } → TokenRequest của Ably
//
// Trang lớp học trực tiếp (lop-hoc/) không có server riêng: nét vẽ, chat và làm mối video đi qua Ably.
// Ở đây chỉ ký "phiếu xin token" bằng khóa Ably giấu trên server, cho vào đúng một kênh lop:<phòng>.
// clientId "gv-…" là giáo viên (mật khẩu là HSK6_PASS của Ngọc, hoặc mã chung APP_SECRET), "hs-…" là học sinh.
// Ably gắn clientId vào mọi tin nhắn, nên máy khác tin được tin nào thật sự do giáo viên gửi (đổi slide, tắt mic, giao bút…).
//
// Biến môi trường: ABLY_API_KEY (dạng "appId.keyId:secret"), HSK6_PASS, APP_SECRET
import { createHmac, randomBytes, timingSafeEqual } from 'node:crypto';
import { fail, readJson, send } from './common.js';

const ROOM_RE = /^[a-z0-9-]{1,32}$/;
const CLIENT_RE = /^(gv|hs)-[a-z0-9]{8,32}$/;
const TTL = 60 * 60 * 1000; // hết hạn thì thư viện Ably tự xin lại

const same = (a, b) => {
  const x = Buffer.from(String(a ?? '')), y = Buffer.from(String(b ?? ''));
  return x.length > 0 && x.length === y.length && timingSafeEqual(x, y);
};

// Ký giống hệt Auth.createTokenRequest của thư viện Ably (bản Go: backend/go/lophoc.go)
export function tokenRequest(key, clientId, room, timestamp = Date.now(), nonce = randomBytes(16).toString('hex')) {
  const [keyName, secret] = key.split(':');
  const capability = JSON.stringify({ [`lop:${room}`]: ['presence', 'publish', 'subscribe'] });
  const text = [keyName, TTL, capability, clientId, timestamp, nonce, ''].join('\n');
  const mac = createHmac('sha256', secret).update(text).digest('base64');
  return { keyName, ttl: TTL, capability, clientId, timestamp, nonce, mac };
}

export default async function lopHoc(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return fail(res, 405, 'chỉ hỗ trợ POST'); }
  const key = process.env.ABLY_API_KEY;
  if (!key || !key.includes(':')) return fail(res, 503, 'server chưa cấu hình ABLY_API_KEY');

  let body;
  try { body = await readJson(req, 4096); } catch { return fail(res, 400, 'dữ liệu không hợp lệ'); }
  const room = String(body?.room ?? ''), clientId = String(body?.clientId ?? '');
  if (!ROOM_RE.test(room) || !CLIENT_RE.test(clientId)) return fail(res, 400, 'mã phòng hoặc mã người dùng không hợp lệ');
  if (clientId.startsWith('gv-')) {
    // giáo viên dùng chung mật khẩu với trang hsk6 (giống authorizedHsk6, nhưng mật khẩu gửi trong body)
    const pass = body?.pass;
    if (!same(pass, process.env.HSK6_PASS) && !same(pass, process.env.APP_SECRET)) return fail(res, 401, 'Sai mật khẩu giáo viên');
  }
  return send(res, 200, tokenRequest(key, clientId, room));
}
