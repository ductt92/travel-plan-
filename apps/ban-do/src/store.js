import { useCallback, useEffect, useRef, useState } from 'react'
import { changed, track } from '@trang/sync'

const KEY = 'da-di-qua-v1'
track(KEY) // đồng bộ giữa máy của Ngọc và Đức khi đã nhập mã

/** Trạng thái mỗi tỉnh: 'none' | 'visited' (đã đi) | 'wish' (muốn đi) */
export const STATUSES = [
  { id: 'visited', label: 'Đã đi', color: 'var(--visited)' },
  { id: 'wish', label: 'Muốn đi', color: 'var(--wish)' },
  { id: 'none', label: 'Chưa đánh dấu', color: 'var(--blank)' },
]

const empty = { status: 'none', note: '', updatedAt: null }

function read() {
  try {
    const parsed = JSON.parse(localStorage.getItem(KEY) || '{}')
    return parsed && typeof parsed === 'object' ? parsed : {}
  } catch {
    return {}
  }
}

/**
 * Ghi chú + trạng thái từng tỉnh. Ghi thẳng localStorage ngay trong lúc sửa (không
 * chờ effect) để đóng tab giữa chừng vẫn không mất chữ.
 */
export function useProvinceNotes() {
  const [entries, setEntries] = useState(read)
  const live = useRef(entries)

  // máy kia sửa (qua đồng bộ) hoặc tab khác sửa thì nạp lại
  useEffect(() => {
    const onStorage = (e) => {
      if (e.key !== KEY) return
      live.current = read()
      setEntries(live.current)
    }
    window.addEventListener('storage', onStorage)
    return () => window.removeEventListener('storage', onStorage)
  }, [])

  const write = useCallback((next) => {
    live.current = next
    setEntries(next)
    try {
      localStorage.setItem(KEY, JSON.stringify(next))
    } catch {
      /* hết chỗ hoặc trình duyệt chặn: app vẫn chạy hết phiên này */
    }
    changed(KEY)
  }, [])

  const get = useCallback((code) => entries[code] || empty, [entries])

  const patch = useCallback(
    (code, changes) => {
      const prev = live.current
      const merged = { ...(prev[code] || empty), ...changes, updatedAt: Date.now() }
      if (merged.status === 'none' && !merged.note.trim()) {
        const { [code]: _drop, ...rest } = prev
        write(rest)
      } else {
        write({ ...prev, [code]: merged })
      }
    },
    [write],
  )

  return { entries, get, patch, replaceAll: write }
}

export { KEY as STORAGE_KEY, empty as emptyEntry }
