import { useEffect, useMemo, useRef, useState } from 'react'
import VietnamMap from './VietnamMap.jsx'
import ProvincePanel from './ProvincePanel.jsx'
import { useProvinceNotes } from './store.js'
import meta from './data/provinces.meta.json'
import { TRIPS, tripProvinces, useTripTicks } from './trips.js'
import { TripCard, StopPanel } from './TripPanels.jsx'
import { SyncButton } from '@trang/sync'

const REGIONS = [
  { id: 'bac', label: 'Miền Bắc' },
  { id: 'trung', label: 'Miền Trung' },
  { id: 'nam', label: 'Miền Nam' },
]

const byCode = Object.fromEntries(meta.map((p) => [p.code, p]))
const TRIP_PROV = tripProvinces()
const trip = TRIPS[0]

function noDiacritics(s) {
  return s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').toLowerCase()
}

export default function App() {
  const { entries, get, patch, replaceAll } = useProvinceNotes()
  const [selected, setSelected] = useState(null)
  const [stop, setStop] = useState(null)
  const { ticks, toggle } = useTripTicks()
  const [query, setQuery] = useState('')
  const fileInput = useRef(null)

  const stats = useMemo(() => {
    const list = Object.values(entries)
    const been = new Set([...Object.keys(TRIP_PROV), ...Object.entries(entries).filter(([, e]) => e.status === 'visited').map(([c]) => c)])
    return {
      been: been.size,
      places: TRIPS.reduce((n, t) => n + t.places.filter((p) => ticks[p.id]).length, 0),
      visited: list.filter((e) => e.status === 'visited').length,
      wish: list.filter((e) => e.status === 'wish').length,
      notes: list.filter((e) => e.note.trim()).length,
    }
  }, [entries, ticks])

  const filtered = useMemo(() => {
    const q = noDiacritics(query.trim())
    if (!q) return meta
    return meta.filter(
      (p) => noDiacritics(p.name).includes(q) || p.merged.some((m) => noDiacritics(m).includes(q)),
    )
  }, [query])

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === 'Escape') { setSelected(null); setStop(null) }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  function exportJson() {
    const blob = new Blob([JSON.stringify(entries, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `ban-do-du-lich-${new Date().toISOString().slice(0, 10)}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  async function importJson(file) {
    try {
      const data = JSON.parse(await file.text())
      const clean = {}
      for (const [code, value] of Object.entries(data)) {
        if (!byCode[code] || !value || typeof value !== 'object') continue
        clean[code] = {
          status: ['visited', 'wish'].includes(value.status) ? value.status : 'none',
          note: typeof value.note === 'string' ? value.note : '',
          updatedAt: typeof value.updatedAt === 'number' ? value.updatedAt : null,
        }
      }
      replaceAll(clean)
    } catch {
      alert('File không đọc được — cần đúng file JSON đã xuất từ app này.')
    }
  }

  return (
    <div className="app">
      <header className="top">
        <div className="top-bar">
          <a className="home-link" href="../">← Trang chủ</a>
          <SyncButton />
        </div>
        <div className="hero">
          <p className="eyebrow">Ngọc <span className="heart" aria-hidden="true">♥</span> Đức · 34 tỉnh thành Việt Nam</p>
          <h1>Bản đồ du lịch của <em>Ngọc và Đức</em></h1>
          <p className="lede">Mỗi trái tim là một nơi hai người đã đến cùng nhau. Bấm vào trái tim để xem lại từng quán ăn, từng điểm chơi trong chuyến.</p>
        </div>
        <div className="counts">
          <span className="stat"><b>{stats.been}</b><small>tỉnh đã đến</small></span>
          <span className="stat"><b>{TRIPS.length}</b><small>chuyến đi</small></span>
          <span className="stat"><b>{stats.places}</b><small>nơi đã ghé</small></span>
          <span className="stat"><b>{stats.wish}</b><small>tỉnh muốn đi</small></span>
        </div>
      </header>

      <main className="layout">
        <section className="map-col">
          <VietnamMap
            selected={selected}
            onSelect={(code) => { setStop(null); setSelected((cur) => (cur === code ? null : code)) }}
            statusOf={(code) => get(code).status}
            isTrip={(code) => !!TRIP_PROV[code]}
            trips={TRIPS}
            selectedStop={stop}
            onStop={(id) => { setSelected(null); setStop((cur) => (cur === id ? null : id)) }}
            noteOf={(code) => get(code).note.trim().length > 0}
          />
        </section>

        <aside className="side">
          {stop ? (
            <StopPanel trip={trip} stop={trip.stops.find((s) => s.id === stop)} ticks={ticks} onToggle={toggle} onClose={() => setStop(null)} />
          ) : null}
          {!stop && selected && TRIP_PROV[selected] ? (
            <div className="card trip-banner">
              <span aria-hidden="true">♥</span>
              <p>Đã đến cùng nhau trong chuyến <b>{trip.title}</b>:{' '}
                {TRIP_PROV[selected].map(({ stop: s }) => (
                  <button key={s.id} type="button" className="link" onClick={() => { setSelected(null); setStop(s.id) }}>{s.name}</button>
                ))}
              </p>
            </div>
          ) : null}
          {stop ? null : selected ? (
            <ProvincePanel
              key={selected}
              province={byCode[selected]}
              entry={get(selected)}
              onChange={(changes) => patch(selected, changes)}
              onClose={() => setSelected(null)}
            />
          ) : (
            <TripCard trip={trip} ticks={ticks} selectedStop={stop} onStop={(id) => setStop(id)} />
          )}

          <div className="card list-card">
            <input
              className="search"
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Tìm tỉnh (gõ không dấu cũng được)"
              aria-label="Tìm tỉnh"
            />
            <div className="list">
              {REGIONS.map((r) => {
                const items = filtered.filter((p) => p.region === r.id)
                if (!items.length) return null
                return (
                  <div key={r.id} className="list-group">
                    <h3>{r.label}</h3>
                    {items.map((p) => {
                      const e = get(p.code)
                      return (
                        <button
                          key={p.code}
                          type="button"
                          className={`row is-${e.status} ${selected === p.code ? 'is-selected' : ''}`}
                          onClick={() => setSelected(p.code)}
                        >
                          <span className={`dot ${TRIP_PROV[p.code] ? 'is-trip' : ''}`} />
                          <span className="row-name">{p.name}</span>
                          {e.note.trim() ? <span className="row-note">✎</span> : null}
                        </button>
                      )
                    })}
                  </div>
                )
              })}
              {filtered.length === 0 ? <p className="empty">Không có tỉnh nào khớp.</p> : null}
            </div>
          </div>

          <div className="card io">
            <button type="button" className="ghost" onClick={exportJson}>Xuất file</button>
            <button type="button" className="ghost" onClick={() => fileInput.current?.click()}>Nhập file</button>
            <input
              ref={fileInput}
              type="file"
              accept="application/json,.json"
              hidden
              onChange={(e) => {
                const f = e.target.files?.[0]
                if (f) importJson(f)
                e.target.value = ''
              }}
            />
          </div>
        </aside>
      </main>
    </div>
  )
}
