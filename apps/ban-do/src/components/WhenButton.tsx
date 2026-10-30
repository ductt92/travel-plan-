import { Button } from 'react-liquis-glass';
import { CloseIcon } from 'react-liquis-glass/icons';
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
      {/* đang lọc thì tô đặc màu nhấn, nhìn qua là biết bản đồ đang không hiện hết */}
      <Button
        variant={period.year ? 'filled' : 'glass'} color={period.year ? 'primary' : 'default'}
        className="when-btn tool-key" icon={<CalendarIcon />} onClick={onOpen}
      >
        <span>{label}</span>
        <ChevronIcon />
      </Button>
      {period.year !== null && (
        <Button
          size="sm" shape="circle" className="when-clear" icon={<CloseIcon />}
          title="Bỏ lọc thời gian" aria-label="Bỏ lọc thời gian"
          onClick={onClear}
        />
      )}
    </div>
  );
}
