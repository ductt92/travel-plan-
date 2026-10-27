import { useEffect, useRef, useState } from 'react'
import { STATUSES } from './store.js'

const fmt = new Intl.DateTimeFormat('vi-VN', { dateStyle: 'short', timeStyle: 'short' })

/** App gắn key={code} nên mỗi tỉnh là một instance riêng — rời tỉnh là unmount, xả nốt bản nháp. */
export default function ProvincePanel({ province, entry, onChange, onClose }) {
  const [draft, setDraft] = useState(entry.note)
  const latest = useRef(null)
  latest.current = { draft, saved: entry.note, onChange }

  // gõ xong 350ms mới lưu, khỏi ghi localStorage mỗi phím
  useEffect(() => {
    if (draft === entry.note) return
    const t = setTimeout(() => onChange({ note: draft }), 350)
    return () => clearTimeout(t)
  }, [draft, entry.note])

  // đổi tỉnh hoặc đóng tab giữa chừng: lưu ngay phần đang gõ dở
  useEffect(() => {
    const flush = () => {
      const { draft: d, saved, onChange: save } = latest.current
      if (d !== saved) save({ note: d })
    }
    window.addEventListener('pagehide', flush)
    return () => {
      window.removeEventListener('pagehide', flush)
      flush()
    }
  }, [])

  const saved = draft === entry.note

  return (
    <div className="card panel">
      <div className="panel-head">
        <div>
          <h2>{province.name}</h2>
          <p className="sub">
            {province.isCity ? 'Thành phố trực thuộc trung ương' : 'Tỉnh'}
            {province.merged.length ? ` · trước 2025: ${province.merged.join(', ')}` : ''}
          </p>
        </div>
        <button type="button" className="close" onClick={onClose} aria-label="Đóng">×</button>
      </div>

      <div className="status-row" role="group" aria-label="Trạng thái">
        {STATUSES.map((s) => (
          <button
            key={s.id}
            type="button"
            className={`status is-${s.id} ${entry.status === s.id ? 'on' : ''}`}
            aria-pressed={entry.status === s.id}
            onClick={() => onChange({ status: s.id })}
          >
            {s.label}
          </button>
        ))}
      </div>

      <label className="note-label" htmlFor="note">Ghi chú</label>
      <textarea
        id="note"
        className="note"
        value={draft}
        onChange={(e) => setDraft(e.target.value)}
        onBlur={() => draft !== entry.note && onChange({ note: draft })}
        placeholder={`Đi đâu, ăn gì, đi với ai ở ${province.name}…`}
        rows={9}
      />

      <p className="saved-at">
        {saved
          ? entry.updatedAt
            ? `Đã lưu ${fmt.format(entry.updatedAt)}`
            : 'Chưa có ghi chú'
          : 'Đang lưu…'}
      </p>
    </div>
  )
}
