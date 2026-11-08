import { useCallback, useEffect, useState } from 'react';
import { getSession, onSessionChange, refreshSession, signIn, signOut } from '@trang/ui/auth';
import TravelMap from './components/TravelMap';
import { loadEntries } from './lib/api';
import { mapData } from './lib/map-data';
import type { Entries } from './lib/types';

const EMPTY: Entries = {};

/**
 * Bản đồ dựng ngay từ ranh giới tỉnh có sẵn (map-data), không chờ API; nhật ký về thì điền vào.
 * Chưa có nhật ký (đang tải hoặc API hỏng) thì bản đồ ở chế độ chỉ xem, vì sửa lúc đó là sửa trên
 * một bản trống. Đăng nhập bằng tài khoản (Đức, Ngọc…) qua @trang/ui/auth, dùng chung phiên với
 * trang quản lý; mỗi lần mở trang hỏi lại server xem phiên còn dùng được không, đổi mật khẩu bên
 * server là lần sau vào sẽ tự rơi về chế độ chỉ xem.
 */
export default function App() {
  const [entries, setEntries] = useState<Entries | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [session, setSession] = useState(getSession);

  const load = useCallback(() => {
    setLoadError(null);
    loadEntries().then(setEntries, (err: Error) => setLoadError(err.message));
  }, []);

  useEffect(load, [load]);

  // đăng nhập/đăng xuất ở trang quản lý (tab khác) cũng cập nhật ở đây
  useEffect(() => onSessionChange(setSession), []);
  useEffect(() => { void refreshSession(); }, []);

  return (
    <>
      {/* key đổi khi nhật ký về để TravelMap dựng lại với dữ liệu thật (useEntries chỉ đọc initial lúc đầu) */}
      <TravelMap
        key={entries ? 'loaded' : 'empty'}
        width={mapData.W}
        height={mapData.H}
        initial={entries ?? EMPTY}
        token={entries ? session?.token ?? '' : ''}
        userName={session?.user.name ?? ''}
        onSignIn={signIn}
        onSignOut={signOut}
      />
      {/* .toast đặt left:50% nên tự co về nửa màn; max-content cho nó rộng theo chữ, max-width của .toast vẫn chặn */}
      {!entries && (
        loadError ? (
          <div className="toast" role="alert" style={{ width: 'max-content' }}>
            <span><b>Không đọc được nhật ký.</b> {loadError}</span>
            <button type="button" onClick={load} style={{ color: 'var(--accent)', fontSize: 13.5, fontWeight: 600 }}>
              Thử lại
            </button>
          </div>
        ) : (
          <div className="toast muted" role="status" style={{ width: 'max-content' }}>Đang mở nhật ký…</div>
        )
      )}
    </>
  );
}
