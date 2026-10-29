import TravelMap from '@/components/TravelMap';
import { canSignIn, signedIn } from '@/lib/auth';
import { hasDb } from '@/db/client';
import { loadEntries } from '@/db/queries';
import { mapData } from '@/lib/map-data';
import { seed } from '@/lib/seed';
import type { Entries } from '@/lib/types';

// nhật ký đọc từ database mỗi lần vào trang, không dựng sẵn lúc build
export const dynamic = 'force-dynamic';

/**
 * Trang chạy trên server: lấy nhật ký rồi giao cho phần tương tác.
 *
 * Chưa cấu hình DATABASE_URL thì vẫn mở được bằng dữ liệu mẫu, nhưng nói rõ là
 * sửa gì cũng không lưu. Có cấu hình mà đọc hỏng thì để trống chứ không bày dữ
 * liệu mẫu ra — nhìn vào tưởng mất sạch còn tệ hơn.
 */
export default async function Page() {
  let mode: 'db' | 'nodb' | 'error' = 'nodb';
  let entries: Entries = seed;

  if (hasDb()) {
    try {
      entries = await loadEntries();
      mode = 'db';
    } catch (err) {
      console.error('[ban-do] không đọc được database', err);
      entries = {};
      mode = 'error';
    }
  }

  // chưa nối database thì sửa gì cũng chỉ nằm trong bộ nhớ trang, khoá lại cũng vô nghĩa
  const canEdit = mode === 'nodb' ? true : await signedIn();

  return (
    <TravelMap
      width={mapData.W}
      height={mapData.H}
      initial={entries}
      mode={mode}
      canEdit={canEdit}
      canSignIn={mode !== 'nodb' && canSignIn()}
    />
  );
}
