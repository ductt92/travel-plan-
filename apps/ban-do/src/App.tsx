import { useCallback, useEffect, useState } from 'react';
import { Button } from 'react-liquis-glass';
import TravelMap from './components/TravelMap';
import { checkPass, loadEntries, rememberPass, savedPass } from './lib/api';
import { mapData } from './lib/map-data';
import type { Entries } from './lib/types';

/**
 * Nạp nhật ký từ API rồi mới dựng bản đồ. Mật khẩu giữ trong localStorage; mỗi lần
 * mở trang hỏi lại server xem còn đúng không, đổi mật khẩu bên server là lần sau
 * vào sẽ tự rơi về chế độ chỉ xem.
 */
export default function App() {
  const [entries, setEntries] = useState<Entries | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [pass, setPass] = useState(savedPass);

  const load = useCallback(() => {
    setLoadError(null);
    loadEntries().then(setEntries, (err: Error) => setLoadError(err.message));
  }, []);

  useEffect(load, [load]);

  useEffect(() => {
    if (!pass) return;
    checkPass(pass).then(err => {
      if (!err) return;
      rememberPass('');
      setPass('');
    });
  }, [pass]);

  const signIn = useCallback(async (raw: string) => {
    const typed = raw.trim();
    const err = await checkPass(typed);
    if (err) return err;
    rememberPass(typed);
    setPass(typed);
    return null;
  }, []);

  const signOut = useCallback(() => {
    rememberPass('');
    setPass('');
  }, []);

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
      pass={pass}
      onSignIn={signIn}
      onSignOut={signOut}
    />
  );
}
