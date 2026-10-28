import { date, index, integer, jsonb, pgEnum, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

export const provinceStatus = pgEnum('province_status', ['none', 'visited', 'wish']);

/**
 * Một dòng cho mỗi tỉnh đã được đụng tới. Tỉnh chưa đánh dấu và chưa có chuyến nào
 * thì không có dòng — 34 tỉnh vốn đã nằm sẵn trong provinces.json, bảng này chỉ giữ
 * phần người dùng thêm vào.
 */
export const provinces = pgTable('provinces', {
  code: text('code').primaryKey(),
  status: provinceStatus('status').notNull().default('none'),
  updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
});

export const trips = pgTable('trips', {
  id: serial('id').primaryKey(),
  provinceCode: text('province_code').notNull().references(() => provinces.code, { onDelete: 'cascade' }),
  // null là chưa rõ ngày; kiểu date của Postgres không mang múi giờ nên không lệch ngày
  fromDate: date('from_date'),
  toDate: date('to_date'),
  // 'with' là từ khoá SQL nên cột đặt tên khác
  companions: text('companions').notNull().default(''),
  rate: integer('rate').notNull().default(0),
  places: jsonb('places').$type<string[]>().notNull().default([]),
  note: text('note').notNull().default(''),
  createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
  updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
}, t => [
  index('trips_province_idx').on(t.provinceCode),
  index('trips_from_idx').on(t.fromDate),
]);

export type TripRow = typeof trips.$inferSelect;
export type ProvinceRow = typeof provinces.$inferSelect;
