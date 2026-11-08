import { useCallback, useRef, useState } from 'react';
import { ApiError, deleteTrip, patchTrip, postTrip, putStatus } from './api';
import type { Entries, ProvinceEntry, Status, Trip, TripDraft } from './types';

const BLANK: ProvinceEntry = { status: 'none', trips: [] };

function message(err: unknown) {
  if (err instanceof ApiError && err.status === 401) return 'Phiên đăng nhập đã hết. Đăng nhập lại nhé.';
  return err instanceof Error ? err.message : 'Không lưu được, thử lại nhé.';
}

/**
 * Nhật ký chuyến đi và bốn cách sửa nó.
 *
 * Sửa hiện ra ngay rồi mới gửi lên API; server báo hỏng thì trả màn hình về đúng
 * như trước và hiện một dòng lỗi. Chưa đăng nhập (`token` rỗng) thì không gửi gì cả —
 * nút sửa cũng đã ẩn, đây chỉ là chốt cuối cho chắc.
 */
export function useEntries(initial: Entries, token: string, onExpired: () => void) {
  const [entries, setEntries] = useState<Entries>(initial);
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(0);

  // bản mới nhất để tính bản vá kế tiếp mà không phải chờ React dựng lại
  const latest = useRef(entries);
  const write = useCallback((next: Entries) => {
    latest.current = next;
    setEntries(next);
  }, []);

  const entryOf = useCallback((code: string) => latest.current[code] ?? BLANK, []);

  const commit = useCallback(
    <T,>(before: Entries, send: () => Promise<T>, done?: (value: T) => void) => {
      if (!token) return;
      setSaving(n => n + 1);
      send().then(
        value => {
          done?.(value);
          setError(null);
        },
        (err: unknown) => {
          write(before);
          setError(message(err));
          if (err instanceof ApiError && err.status === 401) onExpired();
        },
      ).finally(() => setSaving(n => n - 1));
    },
    [token, write, onExpired],
  );

  const setStatus = useCallback((code: string, status: Status) => {
    const before = latest.current;
    write({ ...before, [code]: { ...(before[code] ?? BLANK), status } });
    commit(before, () => putStatus(token, code, status));
  }, [commit, token, write]);

  const addTrip = useCallback((code: string, data: TripDraft) => {
    const before = latest.current;
    const entry = before[code] ?? BLANK;
    // id tạm để dựng ngay; số âm nên không đụng id thật do Postgres cấp
    const tempId = -Date.now();
    write({
      ...before,
      [code]: { status: 'visited', trips: [...entry.trips, { ...data, id: tempId }] },
    });

    commit(before, () => postTrip(token, code, data), saved => {
      const now = latest.current[code] ?? BLANK;
      write({
        ...latest.current,
        [code]: { ...now, trips: now.trips.map(t => (t.id === tempId ? saved : t)) },
      });
    });
  }, [commit, token, write]);

  const updateTrip = useCallback((code: string, id: number, data: TripDraft) => {
    const before = latest.current;
    const entry = before[code] ?? BLANK;
    const patch = (t: Trip) => (t.id === id ? { ...t, ...data } : t);
    write({ ...before, [code]: { ...entry, trips: entry.trips.map(patch) } });
    // server trả lại chuyến kèm tên người sửa: thay vào để hiện "… sửa"
    commit(before, () => patchTrip(token, code, id, data), saved => {
      const now = latest.current[code] ?? BLANK;
      write({ ...latest.current, [code]: { ...now, trips: now.trips.map(t => (t.id === id ? saved : t)) } });
    });
  }, [commit, token, write]);

  /** Xoá chờ server xác nhận rồi mới gỡ khỏi màn hình, để popup xác nhận quay vòng đúng lúc đang xoá. */
  const removeTrip = useCallback(async (code: string, id: number) => {
    if (!token) return;
    try {
      await deleteTrip(token, code, id);
      const now = latest.current;
      const entry = now[code] ?? BLANK;
      write({ ...now, [code]: { ...entry, trips: entry.trips.filter(t => t.id !== id) } });
      setError(null);
    } catch (err) {
      setError(message(err));
      if (err instanceof ApiError && err.status === 401) onExpired();
    }
  }, [token, write, onExpired]);

  return {
    entries, entryOf, setStatus, addTrip, updateTrip, removeTrip,
    saving: saving > 0,
    error,
    clearError: useCallback(() => setError(null), []),
  };
}
