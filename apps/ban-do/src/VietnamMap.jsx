import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { geoMercator, geoPath, geoArea } from 'd3-geo'
import raw from './data/provinces.json'

const W = 500
const H = 1020
const PAD = 14

/**
 * File dữ liệu theo chuẩn RFC 7946 (vòng ngoài ngược chiều kim đồng hồ), còn d3-geo
 * tính trên mặt cầu nên cần chiều ngược lại — không đảo thì mỗi tỉnh phủ kín quả địa cầu.
 */
const geo = {
  type: 'FeatureCollection',
  features: raw.features.map((f) => {
    const flip = (poly) => poly.map((ring) => [...ring].reverse())
    const g = f.geometry
    return {
      ...f,
      geometry: {
        ...g,
        coordinates:
          g.type === 'Polygon' ? flip(g.coordinates) : g.coordinates.map(flip),
      },
    }
  }),
}

/** Hình nào to nhất trong một MultiPolygon — dùng để đặt nhãn cho đúng đất liền. */
function mainland(feature) {
  if (feature.geometry.type !== 'MultiPolygon') return feature
  let best = null
  let bestArea = -1
  for (const coords of feature.geometry.coordinates) {
    const piece = { type: 'Feature', properties: {}, geometry: { type: 'Polygon', coordinates: coords } }
    const a = geoArea(piece)
    if (a > bestArea) {
      bestArea = a
      best = piece
    }
  }
  return best
}

export default function VietnamMap({ selected, onSelect, statusOf, noteOf, isTrip = () => false, trips = [], selectedStop, onStop }) {
  const [hovered, setHovered] = useState(null)
  const [view, setView] = useState({ k: 1, x: 0, y: 0 })
  const drag = useRef(null)
  const svgRef = useRef(null)

  const { shapes, projection } = useMemo(() => {
    const projection = geoMercator().fitExtent(
      [[PAD, PAD], [W - PAD, H - PAD]],
      geo,
    )
    const path = geoPath(projection)
    const shapes = geo.features.map((f) => ({
      code: f.properties.code,
      name: f.properties.name,
      d: path(f),
      label: path.centroid(mainland(f)),
      area: path.area(f),
    }))
    return { shapes, projection }
  }, [])

  // Điểm dừng và đường đi của các chuyến, đã chiếu sang tọa độ SVG
  const tripLayer = useMemo(() => trips.map((t) => {
    const pt = Object.fromEntries(t.stops.map((s) => [s.id, projection([s.lng, s.lat])]))
    const legs = t.route.map(([a, b, kind], i) => {
      const [x1, y1] = pt[a], [x2, y2] = pt[b]
      // đường cong: chặng bay vòng ra biển (lệch sang phải), chặng đường bộ cong nhẹ
      const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1
      const bend = kind === 'flight' ? (i % 2 ? 0.16 : 0.3) : 0.35
      const sign = kind === 'flight' ? (dy > 0 ? -1 : 1) : (i % 2 ? 1 : -1)
      const cx = (x1 + x2) / 2 + sign * (-dy / len) * len * bend
      const cy = (y1 + y2) / 2 + sign * (dx / len) * len * bend
      return { d: `M${x1},${y1} Q${cx},${cy} ${x2},${y2}`, kind, mid: [(x1 + 2 * cx + x2) / 4, (y1 + 2 * cy + y2) / 4], key: `${t.id}-${i}` }
    })
    return { trip: t, pt, legs }
  }), [trips, projection])

  function zoomBy(factor, cx = W / 2, cy = H / 2) {
    setView((v) => {
      const k = Math.min(8, Math.max(1, v.k * factor))
      const ratio = k / v.k
      // giữ nguyên điểm dưới con trỏ khi phóng to
      return clamp({ k, x: cx - (cx - v.x) * ratio, y: cy - (cy - v.y) * ratio })
    })
  }

  function clamp({ k, x, y }) {
    const maxX = 0
    const minX = W - W * k
    const minY = H - H * k
    return { k, x: Math.min(maxX, Math.max(minX, x)), y: Math.min(0, Math.max(minY, y)) }
  }

  // Ctrl/⌘ + cuộn (hoặc chụm hai ngón trên trackpad) mới phóng to; cuộn thường để trang
  // tự trôi. React gắn onWheel kiểu passive nên preventDefault chỉ chạy khi tự addEventListener.
  const onWheel = useCallback((e) => {
    if (!e.ctrlKey && !e.metaKey) return
    e.preventDefault()
    const box = svgRef.current.getBoundingClientRect()
    const cx = ((e.clientX - box.left) / box.width) * W
    const cy = ((e.clientY - box.top) / box.height) * H
    zoomBy(e.deltaY < 0 ? 1.15 : 1 / 1.15, cx, cy)
  }, [])

  useEffect(() => {
    const el = svgRef.current
    el.addEventListener('wheel', onWheel, { passive: false })
    return () => el.removeEventListener('wheel', onWheel)
  }, [onWheel])

  function onPointerDown(e) {
    if (view.k === 1) return
    drag.current = { x: e.clientX, y: e.clientY, view, moved: false, box: e.currentTarget.getBoundingClientRect() }
    e.currentTarget.setPointerCapture(e.pointerId)
  }

  function onPointerMove(e) {
    const d = drag.current
    if (!d) return
    const sx = W / d.box.width
    const sy = H / d.box.height
    const dx = (e.clientX - d.x) * sx
    const dy = (e.clientY - d.y) * sy
    if (Math.abs(dx) + Math.abs(dy) > 3) d.moved = true
    setView(clamp({ k: d.view.k, x: d.view.x + dx, y: d.view.y + dy }))
  }

  function onPointerUp(e) {
    if (drag.current) e.currentTarget.releasePointerCapture?.(e.pointerId)
    drag.current = null
  }

  const selectedShape = shapes.find((s) => s.code === selected)
  const hoveredShape = shapes.find((s) => s.code === hovered)
  const activeShape = hoveredShape || selectedShape

  return (
    <div className="map-wrap">
      <ul className="legend">
        <li><i className="sw sw-trip" />Đã đến cùng nhau</li>
        <li><i className="sw sw-visited" />Đã đi</li>
        <li><i className="sw sw-wish" />Muốn đi</li>
        <li><i className="sw sw-route" />Chuyến đi</li>
      </ul>

      <svg
        className="map"
        ref={svgRef}
        viewBox={`0 0 ${W} ${H}`}
        role="group"
        aria-label="Bản đồ 34 tỉnh thành Việt Nam"
        onPointerDown={onPointerDown}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onPointerCancel={onPointerUp}
        style={{ cursor: view.k > 1 ? 'grab' : 'default', touchAction: view.k > 1 ? 'none' : 'pan-y' }}
      >
        <g transform={`translate(${view.x} ${view.y}) scale(${view.k})`}>
          {shapes.map((s) => {
            const status = statusOf(s.code)
            return (
              <path
                key={s.code}
                d={s.d}
                className={[
                  'province',
                  `is-${status}`,
                  isTrip(s.code) ? 'is-trip' : '',
                  hovered === s.code ? 'is-hovered' : '',
                ].join(' ')}
                strokeWidth={1 / view.k}
                tabIndex={0}
                role="button"
                aria-label={s.name}
                aria-pressed={selected === s.code}
                onMouseEnter={() => setHovered(s.code)}
                onMouseLeave={() => setHovered((h) => (h === s.code ? null : h))}
                onFocus={() => setHovered(s.code)}
                onBlur={() => setHovered((h) => (h === s.code ? null : h))}
                onClick={() => {
                  if (drag.current?.moved) return
                  onSelect(s.code)
                }}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault()
                    onSelect(s.code)
                  }
                }}
              />
            )
          })}

          {/* Viền vẽ riêng sau tất cả các tỉnh: cùng một <path> thì tỉnh liền kề vẽ sau
              sẽ đè mất một phần viền, khoanh không khép kín. */}
          {hoveredShape && hoveredShape.code !== selected ? (
            <path className="outline is-hover" d={hoveredShape.d} strokeWidth={1.6 / view.k} />
          ) : null}
          {selectedShape ? (
            <path className="outline is-selected" d={selectedShape.d} strokeWidth={2.4 / view.k} />
          ) : null}

          {tripLayer.map(({ trip, pt, legs }) => (
            <g key={trip.id} className="trip-layer">
              {legs.map((l) => (
                <path key={l.key} d={l.d} className={`route route--${l.kind}`} strokeWidth={(l.kind === 'flight' ? 1.6 : 2.2) / view.k} strokeDasharray={l.kind === 'flight' ? `${5 / view.k} ${4 / view.k}` : undefined} />
              ))}
              {legs.filter((l) => l.kind === 'flight').map((l) => (
                <text key={`p-${l.key}`} className="route-plane" x={l.mid[0]} y={l.mid[1]} fontSize={13 / view.k} dy={4 / view.k}>✈</text>
              ))}
              {trip.stops.map((s) => {
                const [x, y] = pt[s.id]
                const on = selectedStop === s.id
                const r = (s.kind === 'stay' ? 1 : 0.8) * (on ? 1.25 : 1) / view.k
                return (
                  <g key={s.id} className={`pin pin--${s.kind} ${on ? 'is-on' : ''}`} transform={`translate(${x} ${y}) scale(${r})`}
                    role="button" tabIndex={0} aria-label={`${s.name}, ${s.dates}`}
                    onClick={(e) => { e.stopPropagation(); onStop?.(s.id) }}
                    onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onStop?.(s.id) } }}>
                    {s.kind === 'stay'
                      ? <path className="pin-heart" d="M0 0 C-3 -4 -11 -7 -11 -14 C-11 -19 -7 -22 -4 -22 C-2 -22 -0.5 -21 0 -19 C0.5 -21 2 -22 4 -22 C7 -22 11 -19 11 -14 C11 -7 3 -4 0 0Z" />
                      : <circle className="pin-dot" r="5" />}
                    <g transform={`translate(${s.side === 'left' ? -14 : 14} ${s.kind === 'stay' ? -14 : 0})`}>
                      <text className="pin-label" textAnchor={s.side === 'left' ? 'end' : 'start'} dy="4">{s.name}</text>
                    </g>
                  </g>
                )
              })}
            </g>
          ))}

          {shapes.map((s) =>
            noteOf(s.code) ? (
              <circle
                key={`dot-${s.code}`}
                className="note-dot"
                cx={s.label[0]}
                cy={s.label[1] - 9 / view.k}
                r={2.6 / view.k}
              />
            ) : null,
          )}

          {shapes
            .filter((s) => s.area > 900 || view.k > 1.6)
            .map((s) => (
              <text
                key={`t-${s.code}`}
                className={`map-label is-${statusOf(s.code)}`}
                x={s.label[0]}
                y={s.label[1]}
                fontSize={9 / view.k}
                strokeWidth={2.4 / view.k}
              >
                {s.name}
              </text>
            ))}
        </g>
      </svg>

      <div className="map-tools">
        <button type="button" onClick={() => zoomBy(1.4)} aria-label="Phóng to">+</button>
        <button type="button" onClick={() => zoomBy(1 / 1.4)} aria-label="Thu nhỏ">−</button>
        <button type="button" onClick={() => setView({ k: 1, x: 0, y: 0 })} aria-label="Về mặc định">⤢</button>
      </div>

      <div className="map-hint" aria-live="polite">
        {activeShape ? activeShape.name : 'Bấm vào trái tim để xem kỷ niệm, bấm vào tỉnh để ghi chú'}
      </div>
    </div>
  )
}
