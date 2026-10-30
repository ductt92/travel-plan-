import { useState } from 'react';
import { Button, Input, Modal } from 'react-liquis-glass';
import { SearchIcon } from './icons';
import { noMark } from '@/lib/format';
import { REGION, provinces } from '@/lib/map-data';
import type { Entries, Level, Region } from '@/lib/types';

interface Props {
  open: boolean;
  entries: Entries;
  spotlight: string[];
  levelOf: (code: string) => Level;
  countOf: (code: string) => number;
  onClose: () => void;
  onApply: (codes: string[]) => void;
}

export default function FindDialog({ open, onClose, ...rest }: Props) {
  return (
    <Modal open={open} onClose={onClose} title="Tìm tỉnh" footer={null} width={580} className="bd-modal">
      {/* Modal chỉ dựng ruột khi đang mở (và lúc mờ dần khi đóng), nên mỗi lần mở là
          dựng lại: ô tìm trống, phần tích lấy lại từ những tỉnh đang chọn */}
      <Body onClose={onClose} {...rest} />
    </Modal>
  );
}

function Body({ entries, spotlight, levelOf, countOf, onApply }: Omit<Props, 'open'>) {
  const [q, setQ] = useState('');
  // đang tích trong popup, chỉ đổ sang bản đồ khi bấm xác nhận
  const [picked, setPicked] = useState<string[]>(spotlight);

  const s = noMark(q.trim());
  const groups = (Object.entries(REGION) as [Region, string][]).map(([id, label]) => ({
    label,
    hit: provinces.filter(p => p.region === id &&
      (!s || noMark(p.name).includes(s) || p.merged.some(m => noMark(m).includes(s)))),
  })).filter(g => g.hit.length);

  const toggle = (code: string, on: boolean) =>
    setPicked(prev => (on ? [...prev, code] : prev.filter(c => c !== code)));

  return (
    <div className="dlg">
      <div className="dlg-head plain">
        <p className="meta">Tích một hoặc vài tỉnh rồi xác nhận, bản đồ sẽ khoanh những tỉnh đó.</p>
        <Input
          className="search" type="search" data-autofocus allowClear variant="filled" size="lg"
          prefix={<SearchIcon />}
          placeholder="Gõ tên tỉnh, không dấu cũng được" aria-label="Tìm tỉnh"
          value={q} onChange={e => setQ(e.target.value)}
        />
      </div>

      <div className="dlg-body">
        <div>
          {groups.length === 0 && <div className="empty"><p>Không có tỉnh nào khớp.</p></div>}
          {groups.map(g => (
            <div className="pick-group" key={g.label}>
              <h5>{g.label}</h5>
              {g.hit.map(p => {
                const on = picked.includes(p.code);
                const n = countOf(p.code);
                return (
                  <label className={`pick-row${on ? ' on' : ''}`} key={p.code}>
                    <input type="checkbox" checked={on} onChange={e => toggle(p.code, e.target.checked)} />
                    <span className={`dot lv-${levelOf(p.code)}`} />
                    <span className="pick-name">{p.name}</span>
                    <span className="pick-n">
                      {n ? `${n} chuyến` : entries[p.code]?.status === 'wish' ? 'muốn đi' : ''}
                    </span>
                  </label>
                );
              })}
            </div>
          ))}
        </div>
      </div>

      <div className="dlg-acts">
        <span className="acts-note">
          {picked.length ? `Đã chọn ${picked.length} tỉnh` : 'Chưa chọn tỉnh nào'}
        </span>
        <Button onClick={() => setPicked([])}>Bỏ hết tích</Button>
        <Button
          variant="filled" color="primary"
          disabled={!picked.length && !spotlight.length}
          onClick={() => onApply(picked)}
        >Chọn tỉnh</Button>
      </div>
    </div>
  );
}
