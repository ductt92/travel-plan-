// Các chuyến đi đã ghi trong sổ tay Travel plan (travel/). Mỗi điểm dừng có tọa độ để cắm ghim trên bản đồ,
// danh sách địa điểm lấy từ src/data/trip-2026-10.json (trích từ travel/index.html).
import { useCallback, useEffect, useState } from 'react'
import places from './data/trip-2026-10.json'

export const TRIPS = [
  {
    id: '2026-10',
    title: 'Tam Đảo & Đà Lạt',
    dates: '3 – 11/10/2026',
    href: '../travel/',
    stops: [
      { id: 'noibai', name: 'Nội Bài', province: 'ha-noi', lat: 21.2187, lng: 105.8042, dates: 'Đón 3/10 · về 11/10', kind: 'airport', side: 'left' },
      { id: 'tamdao', name: 'Tam Đảo', province: 'phu-tho', lat: 21.4558, lng: 105.6461, dates: '3 – 4/10', kind: 'stay', side: 'left' },
      { id: 'dalat', name: 'Đà Lạt', province: 'lam-dong', lat: 11.9404, lng: 108.4583, dates: '4 – 11/10', kind: 'stay', side: 'right' }
    ],
    // đường đi theo thứ tự: đón ở Nội Bài → Tam Đảo → Nội Bài → bay Đà Lạt → bay về Nội Bài
    route: [['noibai', 'tamdao', 'road'], ['tamdao', 'noibai', 'road'], ['noibai', 'dalat', 'flight'], ['dalat', 'noibai', 'flight']],
    places
  }
]
export const placesOf = (trip, stopId) => trip.places.filter(p => p.stop === stopId)
/** Các tỉnh có điểm dừng của một chuyến: { mã tỉnh: [điểm dừng] } */
export function tripProvinces() {
  const out = {}
  for (const t of TRIPS) for (const s of t.stops) (out[s.province] ||= []).push({ trip: t, stop: s })
  return out
}

/** Dấu tích "đã ghé" dùng chung với trang Travel plan (cùng tên miền nên chung localStorage khóa dadiqua-trip) */
const TICKS = 'dadiqua-trip'
function readTicks() {
  try { return JSON.parse(localStorage.getItem(TICKS) || '{}') || {} } catch { return {} }
}
export function useTripTicks() {
  const [ticks, setTicks] = useState(readTicks)
  useEffect(() => {
    // tích ở tab Travel plan đang mở song song thì bản đồ cập nhật theo
    const onStorage = e => { if (e.key === TICKS) setTicks(readTicks()) }
    window.addEventListener('storage', onStorage)
    return () => window.removeEventListener('storage', onStorage)
  }, [])
  const toggle = useCallback(id => {
    setTicks(prev => {
      const next = { ...prev }
      if (next[id]) delete next[id]; else next[id] = true
      try { localStorage.setItem(TICKS, JSON.stringify(next)) } catch { /* bỏ qua */ }
      return next
    })
  }, [])
  return { ticks, toggle }
}
