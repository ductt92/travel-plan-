import { useCallback, useEffect, useState } from 'react';
import { ApiError, deleteNote, loadNotes, postNote, type LoveNote } from './api';

const seenKey = (user: string) => `ban-do-notes-seen:${user}`;
const readSeen = (user: string) => {
  try { return localStorage.getItem(seenKey(user)) || ''; } catch { return ''; }
};

/**
 * Lời nhắn của hai người. Nạp ngay khi đăng nhập để nút "Note tình yêu" báo được
 * có lời nhắn mới của người kia mà mình chưa đọc (mốc đã đọc giữ trong localStorage, theo từng tài khoản).
 */
export function useNotes(token: string, userName: string, onExpired: () => void) {
  const [notes, setNotes] = useState<LoveNote[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [seen, setSeen] = useState(() => readSeen(userName));

  const fail = useCallback((err: unknown) => {
    if (err instanceof ApiError && err.status === 401) {
      setError('Phiên đăng nhập đã hết. Đăng nhập lại nhé.');
      onExpired();
    } else setError(err instanceof Error ? err.message : 'Có lỗi, thử lại nhé.');
  }, [onExpired]);

  const reload = useCallback(() => {
    if (!token) return;
    setError(null);
    loadNotes(token).then(setNotes, fail);
  }, [token, fail]);

  useEffect(() => {
    setNotes(null);
    setSeen(readSeen(userName));
    reload();
  }, [reload, userName]);

  const add = useCallback(async (text: string) => {
    setError(null);
    try {
      const note = await postNote(token, text);
      setNotes(list => [note, ...(list ?? [])]);
      return true;
    } catch (err) { fail(err); return false; }
  }, [token, fail]);

  const remove = useCallback(async (id: number) => {
    setError(null);
    try {
      await deleteNote(token, id);
      setNotes(list => (list ?? []).filter(n => n.id !== id));
    } catch (err) { fail(err); }
  }, [token, fail]);

  /** Đánh dấu đã đọc hết tới lời nhắn mới nhất. */
  const markSeen = useCallback(() => {
    const top = notes?.[0]?.at;
    if (!top || !userName) return;
    try { localStorage.setItem(seenKey(userName), top); } catch { /* chế độ riêng tư */ }
    setSeen(top);
  }, [notes, userName]);

  const unread = (notes ?? []).filter(n => n.by !== userName && n.at > seen).length;

  return { notes, error, unread, seen, add, remove, reload, markSeen };
}
