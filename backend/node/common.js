// Bản Node của API (bản Go nằm ở backend/go, cùng hợp đồng).
// Các file trong api/node/ chỉ là lối vào mỏng để Vercel tạo function, logic nằm ở đây.
//
// Biến môi trường:
//   DATABASE_URL    chuỗi kết nối Postgres (Neon trên Vercel, Docker ở máy)
//   APP_SECRET      mã chung, client gửi qua header X-App-Secret
//   HSK6_PASS       mật khẩu riêng của trang hsk6, dùng thay APP_SECRET cho /terms và /ai
//   GEMINI_API_KEY  khóa Gemini cho /api/node/ai (dự phòng: GROQ_API_KEY, OPENROUTER_API_KEY, MISTRAL_API_KEY, xem ai.js)
import { timingSafeEqual } from 'node:crypto';
import pg from 'pg';

let pool = null;
let ready = null;

// Một pool dùng lại giữa các lần gọi khi function còn "ấm"; tạo bảng ở lần đầu.
// Bảng docs dùng chung với bản Go nên đổi qua lại không mất dữ liệu.
export async function db() {
  if (!process.env.DATABASE_URL) throw new Error('chưa cấu hình DATABASE_URL');
  if (!pool) {
    const url = process.env.DATABASE_URL;
    pool = new pg.Pool({ connectionString: url, max: 4, ssl: /sslmode=require|neon\.tech/.test(url) ? { rejectUnauthorized: true } : false });
    ready = pool.query(`CREATE TABLE IF NOT EXISTS docs (
      key        text PRIMARY KEY,
      data       jsonb NOT NULL,
      version    bigint NOT NULL,
      updated_at timestamptz NOT NULL DEFAULT now()
    )`).catch(e => { pool = null; throw e; });
  }
  await ready;
  return pool;
}

export function send(res, status, body) {
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Backend', 'node');
  res.statusCode = status;
  res.end(JSON.stringify(body));
}

export const fail = (res, status, error) => send(res, status, { error });

// So sánh thời gian hằng để không lộ mã qua thời gian phản hồi
function matches(value, req) {
  const secret = Buffer.from(value || '');
  const got = Buffer.from(String(req.headers['x-app-secret'] || ''));
  return secret.length > 0 && got.length === secret.length && timingSafeEqual(got, secret);
}
export const authorized = req => matches(process.env.APP_SECRET, req);
// API của trang hsk6 (thuật ngữ, AI): mã chung APP_SECRET hoặc mật khẩu riêng của trang HSK6_PASS (cho Ngọc)
export const authorizedHsk6 = req => authorized(req) || matches(process.env.HSK6_PASS, req);

// Vercel đã parse sẵn req.body khi là JSON; chạy ở máy thì tự đọc luồng
export async function readJson(req, limit = 1 << 20) {
  if (req.body !== undefined) return typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  // gom Buffer rồi mới giải mã: cộng chuỗi từng mẩu sẽ cắt đôi chữ nhiều byte (chữ Hán, tiếng Việt) ở ranh giới mẩu
  const chunks = [];
  let size = 0;
  for await (const chunk of req) {
    size += chunk.length;
    if (size > limit) throw new Error('quá lớn');
    chunks.push(chunk);
  }
  const raw = Buffer.concat(chunks).toString('utf8');
  return raw ? JSON.parse(raw) : {};
}
