'use client';

import { useCallback, useRef, useState, useTransition } from 'react';
import {
  addTripAction, removeTripAction, setStatusAction, updateTripAction,
} from '@/app/actions';
import type { ActionResult, Entries, ProvinceEntry, Status, Trip, TripDraft } from './types';

const BLANK: ProvinceEntry = { status: 'none', trips: [] };

/**
 * Mỗi lần deploy, id của server action đổi theo. Trang mở từ trước đó gửi id cũ
 * lên và server không nhận ra — chỉ cần tải lại là xong, nên nói đúng câu đó thay
 * vì một lời "thử lại" chung chung.
 */
function failureText(err: unknown) {
  const msg = err instanceof Error ? err.message : String(err);
  return /server action/i.test(msg)
    ? 'Trang đang mở cũ hơn bản trên server. Tải lại trang rồi thử lại nhé.'
    : 'Không gọi được server, thay đổi chưa lưu. Kiểm tra mạng rồi thử lại.';
}

/**
 * Nhật ký chuyến đi và bốn cách sửa nó.
 *
 * Sửa hiện ra ngay rồi mới gửi lên server; server báo hỏng thì trả màn hình về
 * đúng như trước và hiện một dòng lỗi. Chưa cấu hình DATABASE_URL (`live` false)
 * thì chỉ sửa trên màn, tải lại là mất.
 */
export function useEntries(initial: Entries, live: boolean) {
  const [entries, setEntries] = useState<Entries>(initial);
  const [error, setError] = useState<string | null>(null);
  const [saving, startSaving] = useTransition();

  // bản mới nhất để tính bản vá kế tiếp mà không phải chờ React dựng lại
  const latest = useRef(entries);
  const write = useCallback((next: Entries) => {
    latest.current = next;
    setEntries(next);
  }, []);

  const entryOf = useCallback((code: string) => latest.current[code] ?? BLANK, []);

  const commit = useCallback(
    <T,>(before: Entries, send: () => Promise<ActionResult<T>>, done?: (value: T) => void) => {
      if (!live) return;
      startSaving(async () => {
        try {
          const res = await send();
          if (!res.ok) {
            write(before);
            setError(res.error);
            return;
          }
          done?.(res.value);
          setError(null);
        } catch (err) {
          // không bắt ở đây thì lời hứa vỡ ngay trong transition và React đánh sập
          // cả trang — mất chuyến đang xem chỉ vì rớt mạng một nhịp
          console.error('[ban-do] gọi server hỏng', err);
          write(before);
          setError(failureText(err));
        }
      });
    },
    [live, write],
  );

  const setStatus = useCallback((code: string, status: Status) => {
    const before = latest.current;
    write({ ...before, [code]: { ...(before[code] ?? BLANK), status } });
    commit(before, () => setStatusAction(code, status));
  }, [commit, write]);

  const addTrip = useCallback((code: string, data: TripDraft) => {
    const before = latest.current;
    const entry = before[code] ?? BLANK;
    // id tạm để dựng ngay; số âm nên không đụng id thật do Postgres cấp
    const tempId = -Date.now();
    write({
      ...before,
      [code]: { status: 'visited', trips: [...entry.trips, { ...data, id: tempId }] },
    });

    commit(before, () => addTripAction(code, data), saved => {
      const now = latest.current[code] ?? BLANK;
      write({
        ...latest.current,
        [code]: { ...now, trips: now.trips.map(t => (t.id === tempId ? saved : t)) },
      });
    });
  }, [commit, write]);

  const updateTrip = useCallback((code: string, id: number, data: TripDraft) => {
    const before = latest.current;
    const entry = before[code] ?? BLANK;
    const patch = (t: Trip) => (t.id === id ? { ...t, ...data } : t);
    write({ ...before, [code]: { ...entry, trips: entry.trips.map(patch) } });
    commit(before, () => updateTripAction(code, id, data));
  }, [commit, write]);

  const removeTrip = useCallback((code: string, id: number) => {
    const before = latest.current;
    const entry = before[code] ?? BLANK;
    write({ ...before, [code]: { ...entry, trips: entry.trips.filter(t => t.id !== id) } });
    commit(before, () => removeTripAction(code, id));
  }, [commit, write]);

  return {
    entries, entryOf, setStatus, addTrip, updateTrip, removeTrip,
    saving, error, clearError: useCallback(() => setError(null), []),
  };
}
