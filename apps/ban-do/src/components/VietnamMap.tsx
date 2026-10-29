import { useMemo } from 'react';
import { byCode, provinces } from '@/lib/map-data';
import type { Level, Province } from '@/lib/types';

interface Props {
  width: number;
  height: number;
  levelOf: (code: string) => Level;
  countOf: (code: string) => number;
  hovered: string | null;
  selected: string | null;
  spotlight: string[];
  onHover: (code: string | null) => void;
  onPick: (code: string) => void;
}

/**
 * Xếp nhãn: duyệt tỉnh từ lớn đến nhỏ, thử vài vị trí quanh tâm, chỗ nào chưa
 * đụng nhãn đã đặt thì lấy. Chen quá thì bỏ nhãn, tên vẫn hiện ở dòng dưới bản đồ.
 */
const TRY = [[0, 0], [0, -10], [0, 11], [-16, 0], [16, 0], [0, -20], [0, 21], [-22, -9], [22, -9]];

interface Box { x1: number; x2: number; y1: number; y2: number }
interface Label { p: Province; x: number; y: number; n: number }

function layoutLabels(countOf: (code: string) => number): Label[] {
  const placed: Box[] = [];
  const hit = (a: Box, b: Box) => !(a.x2 < b.x1 || b.x2 < a.x1 || a.y2 < b.y1 || b.y2 < a.y1);
  const out: Label[] = [];

  for (const p of [...provinces].sort((a, b) => b.area - a.area)) {
    if (p.area < 700) continue;
    const n = countOf(p.code);
    const w = p.name.length * 4.5 + (n > 1 ? 13 : 0);
    for (const [dx, dy] of TRY) {
      const x = p.lx + dx;
      const y = p.ly + dy;
      const box = { x1: x - w / 2 - 2, x2: x + w / 2 + 2, y1: y - 7, y2: y + 3 };
      if (placed.some(q => hit(box, q))) continue;
      placed.push(box);
      out.push({ p, x, y, n });
      break;
    }
  }
  return out;
}

export default function VietnamMap({
  width, height, levelOf, countOf, hovered, selected, spotlight, onHover, onPick,
}: Props) {
  const labels = useMemo(() => layoutLabels(countOf), [countOf]);
  const spots = useMemo(() => new Set(spotlight), [spotlight]);

  // viền vẽ sau toàn bộ các tỉnh nên không bị tỉnh bên cạnh đè mất một đoạn
  const rings: { code: string; cls: string }[] = [];
  for (const code of spotlight) if (code !== selected) rings.push({ code, cls: 'spot' });
  if (hovered && hovered !== selected) rings.push({ code: hovered, cls: 'hov' });
  if (selected) rings.push({ code: selected, cls: 'sel' });

  return (
    <svg
      className="map"
      id="map"
      viewBox={`0 0 ${width} ${height}`}
      role="group"
      aria-label="Bản đồ 34 tỉnh thành Việt Nam"
    >
      <g id="country">
        {provinces.map(p => (
          <path
            key={p.code}
            d={p.d}
            className={`province lv-${levelOf(p.code)}${spots.size && !spots.has(p.code) ? ' faded' : ''}`}
            tabIndex={0}
            role="button"
            aria-label={p.name}
            onPointerEnter={() => onHover(p.code)}
            onPointerLeave={() => onHover(null)}
            onFocus={() => onHover(p.code)}
            onBlur={() => onHover(null)}
            onClick={() => onPick(p.code)}
            onKeyDown={ev => {
              if (ev.key !== 'Enter' && ev.key !== ' ') return;
              ev.preventDefault();
              onPick(p.code);
            }}
          />
        ))}
      </g>

      <g>
        {rings.map(({ code, cls }) => (
          <path key={`${cls}-${code}`} d={byCode[code].d} className={`outline ${cls}`} />
        ))}
      </g>

      <g>
        {labels.map(({ p, x, y, n }) => {
          const lv = levelOf(p.code);
          const bright = lv === 'wish' || (typeof lv === 'number' && lv >= 2);
          // huy hiệu số chuyến cho tỉnh đi nhiều lần
          const cx = x - 6 + p.name.length * 2.25 + 7;
          return (
            <g key={p.code}>
              <text className={`lbl${bright ? ' on' : ''}`} x={n > 1 ? x - 6 : x} y={y}>
                {p.name}
              </text>
              {n > 1 && (
                <>
                  <circle className="badge" cx={cx} cy={y - 3} r={5} />
                  <text className="badge-n" x={cx} y={y - 0.9}>{n}</text>
                </>
              )}
            </g>
          );
        })}
      </g>
    </svg>
  );
}
