import { useCallback, useEffect, useState } from 'react';
import { Button } from 'react-liquis-glass';
import { getSession, onSessionChange, refreshSession, signIn, signOut } from '@trang/ui/auth';
import TravelMap from './components/TravelMap';
import { loadEntries } from './lib/api';
import { mapData } from './lib/map-data';
import type { Entries } from './lib/types';

/**
 * Nạp nhật ký từ API rồi mới dựng bản đồ. Đăng nhập bằng tài khoản (Đức, Ngọc…) qua @trang/ui/auth,
 * dùng chung phiên với trang quản lý; mỗi lần mở trang hỏi lại server xem phiên còn dùng được không,
 * đổi mật khẩu bên server là lần sau vào sẽ tự rơi về chế độ chỉ xem.
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

  if (!entries) {
    return (
      <div className="wrap">
        <p className={`note-bar${loadError ? ' warn' : ''}`}>
          <span>{loadError ? '⚠️' : '🗺️'}</span>
          <span>{loadError ? <><b>Không đọc được nhật ký.</b> {loadError}</> : 'Đang mở nhật ký…'}</span>
        </p>
        {loadError && (
          <p style={{ textAlign: 'center' }}>
            <Button variant="filled" color="primary" onClick={load}>Thử lại</Button>
          </p>
        )}
      </div>
    );
  }

  return (
    <TravelMap
      width={mapData.W}
      height={mapData.H}
      initial={entries}
      token={session?.token ?? ''}
      userName={session?.user.name ?? ''}
      onSignIn={signIn}
      onSignOut={signOut}
    />
  );
}
