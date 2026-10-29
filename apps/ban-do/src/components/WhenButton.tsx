'use client';

import { CalendarIcon, ChevronIcon } from './icons';
import type { Period } from '@/lib/types';

/** Nút mở bộ chọn thời gian, kèm nút ✕ bỏ lọc khi đang lọc. */
export default function WhenButton({
  period, onOpen, onClear,
}: { period: Period; onOpen: () => void; onClear: () => void }) {
  const label = period.year
    ? period.month ? `Tháng ${period.month}/${period.year}` : `Năm ${period.year}`
    : 'Tất cả thời gian';

  return (
    <div className="when">
      <button type="button" className={`when-btn${period.year ? ' on' : ''}`} onClick={onOpen}>
        <CalendarIcon />
        <span>{label}</span>
        <ChevronIcon />
      </button>
      {period.year !== null && (
        <button
          type="button" className="when-clear"
          title="Bỏ lọc thời gian" aria-label="Bỏ lọc thời gian"
          onClick={onClear}
        >✕</button>
      )}
    </div>
  );
}
