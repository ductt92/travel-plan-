import { placesOf } from './trips.js'

const DAY_LABEL = d => (d ? `${d}/10` : 'Ngoài lịch')

/** Thẻ chuyến đi: các điểm dừng, số nơi đã ghé, link sang sổ tay Travel plan */
export function TripCard({ trip, ticks, selectedStop, onStop }) {
  const done = trip.places.filter(p => ticks[p.id]).length
  return (
    <div className="card trip-card">
      <div className="trip-head">
        <span className="eyebrow">Chuyến đi · {trip.dates}</span>
        <h2>{trip.title}</h2>
        <div className="trip-prog">
          <div className="bar"><i style={{ width: `${(done / trip.places.length) * 100}%` }} /></div>
          <span>{done}/{trip.places.length} nơi đã ghé</span>
        </div>
      </div>
      <ol className="stops">
        {trip.stops.map((s, i) => {
          const list = placesOf(trip, s.id)
          const d = list.filter(p => ticks[p.id]).length
          return (
            <li key={s.id}>
              <button type="button" className={`stop ${selectedStop === s.id ? 'is-on' : ''}`} onClick={() => onStop(s.id)}>
                <span className={`stop-ic stop-ic--${s.kind}`} aria-hidden="true">{s.kind === 'stay' ? '♥' : '✈'}</span>
                <span className="stop-txt"><b>{s.name}</b><small>{s.dates}</small></span>
                {list.length ? <span className="stop-n">{d}/{list.length}</span> : null}
              </button>
              {i < trip.stops.length - 1 ? <span className="stop-line" aria-hidden="true" /> : null}
            </li>
          )
        })}
      </ol>
      <a className="trip-link" href={trip.href}>Mở sổ tay chuyến đi →</a>
    </div>
  )
}

/** Bảng chi tiết một điểm dừng: các quán và nơi chơi, tích "đã ghé" đồng bộ với Travel plan */
export function StopPanel({ trip, stop, ticks, onToggle, onClose }) {
  const list = placesOf(trip, stop.id)
  const groups = [['choi', 'Chơi'], ['an', 'Ăn']].map(([cat, label]) => [label, list.filter(p => p.cat === cat)])
  const done = list.filter(p => ticks[p.id]).length
  return (
    <div className="card panel stop-panel">
      <div className="panel-head">
        <div>
          <p className="eyebrow">{trip.title} · {stop.dates}</p>
          <h2>{stop.kind === 'stay' ? '♥ ' : '✈ '}{stop.name}</h2>
          {list.length ? <p className="sub">{done}/{list.length} nơi đã ghé · tích ở đây hay ở sổ tay đều được</p> : null}
        </div>
        <button type="button" className="close" onClick={onClose} aria-label="Đóng">×</button>
      </div>
      {!list.length ? (
        <p className="sub">Điểm đón và tiễn ở sân bay: đón Ngọc lúc 17:45 ngày 3/10, bay về ngày 11/10.</p>
      ) : groups.map(([label, items]) => items.length ? (
        <div key={label} className="pl-group">
          <h3>{label} <span>{items.filter(p => ticks[p.id]).length}/{items.length}</span></h3>
          <ul className="pl-list">
            {items.map(p => (
              <li key={p.id}>
                <label className={`pl ${ticks[p.id] ? 'is-done' : ''}`}>
                  <input type="checkbox" checked={!!ticks[p.id]} onChange={() => onToggle(p.id)} />
                  <span className="pl-box" aria-hidden="true" />
                  <span className="pl-txt"><b>{p.name}</b>{p.note ? <small>{p.note}</small> : null}</span>
                  <span className={`pl-day ${p.inPlan ? '' : 'is-extra'}`}>{DAY_LABEL(p.day)}</span>
                </label>
              </li>
            ))}
          </ul>
        </div>
      ) : null)}
      <a className="trip-link" href={trip.href}>Xem lịch từng ngày trong sổ tay →</a>
    </div>
  )
}
