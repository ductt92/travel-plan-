import 'server-only';
import { drizzle } from 'drizzle-orm/node-postgres';
import pg from 'pg';
import { databaseUrl } from '@/lib/env';
import * as schema from './schema';

export const hasDb = () => Boolean(databaseUrl());

type Client = ReturnType<typeof drizzle<typeof schema>>;

// dev chạy lại module mỗi lần sửa file, giữ pool ở global kẻo mở chồng kết nối
const store = globalThis as unknown as { __banDoPool?: pg.Pool; __banDoDb?: Client };

export function db(): Client {
  if (store.__banDoDb) return store.__banDoDb;

  const url = databaseUrl();
  if (!url) throw new Error('chưa cấu hình DATABASE_URL');

  // Neon bắt buộc TLS, Postgres chạy bằng Docker ở máy thì không — nhận biết như backend/node
  store.__banDoPool ??= new pg.Pool({
    connectionString: url,
    max: 4,
    ssl: /sslmode=require|neon\.tech/.test(url) ? { rejectUnauthorized: true } : false,
  });
  store.__banDoDb = drizzle(store.__banDoPool, { schema });
  return store.__banDoDb;
}
