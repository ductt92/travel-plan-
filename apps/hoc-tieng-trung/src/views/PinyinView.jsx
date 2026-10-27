// Trang Bảng pinyin: 4 thanh điệu, phụ âm đầu theo nhóm (bấm để nghe), bảng ghép âm tiết, quy tắc viết.
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { EmptyState, Icon } from '@trang/ui';
import { PINYIN } from '../core/data.js';
import { say } from '../core/speech.js';
import { GroupTabs, PinyinTable, PY_FINALS, PY_INITS, SYLLABLE_COUNT, SyllableCard, ToneLegend, spell } from '../components/PinyinKit.jsx';
import './PinyinView.css';

// Phụ âm đầu theo vị trí phát âm; ghép với vần quen dùng khi đọc bảng: bo po mo fo, de te ne le…
const INIT_GROUPS = [
  { name: 'Âm môi', fin: 'o', inits: ['b', 'p', 'm', 'f'], note: 'Hai môi (f: môi chạm răng). p bật hơi mạnh, b thì không.' },
  { name: 'Đầu lưỡi giữa', fin: 'e', inits: ['d', 't', 'n', 'l'], note: 'd gần “t” tiếng Việt; t bật hơi như “th”.' },
  { name: 'Gốc lưỡi', fin: 'e', inits: ['g', 'k', 'h'], note: 'g gần “c”; k bật hơi; h xát ở cuống họng, gần “kh”.' },
  { name: 'Mặt lưỡi', fin: 'i', inits: ['j', 'q', 'x'], note: 'Mặt lưỡi áp vòm cứng, môi dẹt. q bật hơi.' },
  { name: 'Quặt lưỡi', fin: '-i', inits: ['zh', 'ch', 'sh', 'r'], note: 'Cong đầu lưỡi lên vòm miệng. ch bật hơi.' },
  { name: 'Đầu lưỡi trước', fin: '-i', inits: ['z', 'c', 's'], note: 'Đầu lưỡi chạm sau răng trên. c bật hơi, như “ts”.' }
];

const RULES = [
  { title: 'Quy tắc viết y, w', body: <>Vần bắt đầu bằng i, u, ü mà đứng một mình thì viết lại: <em>i → yi</em>, <em>ia → ya</em>; <em>u → wu</em>, <em>uo → wo</em>; <em>ü → yu</em>, <em>üe → yue</em>.</> },
  { title: 'Hai chấm trên ü', body: <>Sau j, q, x và y thì ü bỏ hai chấm nhưng vẫn đọc là ü: <em>ju, qu, xu, yu</em>. Chỉ n, l giữ hai chấm: <em>nü, lü</em>.</> },
  { title: 'Vần viết tắt', body: <><em>iou → iu</em> (liù), <em>uei → ui</em> (guì), <em>uen → un</em> (lùn). Vần “-i” sau zh, ch, sh, r, z, c, s không đọc là “i” mà kéo dài phụ âm.</> }
];

function Initials() {
  return (
    <div className="pv-inits">
      {INIT_GROUPS.map(g => (
        <article key={g.name} className="pv-init">
          <header><b>{g.name}</b><span>{g.inits.length} âm</span></header>
          <div className="pv-init__keys">
            {g.inits.map(i => {
              const r = spell(i, g.fin);
              const v = r && PINYIN[r[1]];
              return (
                <button key={i} type="button" className="pv-key" onClick={() => v && say(v[0])} disabled={!v} aria-label={v ? `${i}: nghe ${r[0]} (${v[0]})` : i}>
                  <b>{i}</b>{r && <small>{r[0]}</small>}
                </button>
              );
            })}
          </div>
          <p>{g.note}</p>
        </article>
      ))}
    </div>
  );
}

export function PinyinView() {
  const [tab, setTab] = useState(0);
  const [sel, setSel] = useState(null);

  if (!PINYIN || !Object.keys(PINYIN).length) return (
    <EmptyState title="Chưa tải được bảng pinyin"><p className="ui-muted">Thiếu file dữ liệu pinyin.</p></EmptyState>
  );
  const pick = r => { setSel(r); say(PINYIN[r[1]][0]); };
  const stats = [
    [PY_INITS.length - 1, 'thanh mẫu', 'phụ âm đầu'],
    [PY_FINALS.flat().length, 'vận mẫu', 'phần vần'],
    [4, 'thanh điệu', 'và 1 thanh nhẹ'],
    [SYLLABLE_COUNT, 'âm tiết', 'trong bảng']
  ];

  return (
    <div className="pv">
      <header className="pv-hero">
        <span className="pv-hero__seal" aria-hidden="true">拼<br />音</span>
        <div className="pv-hero__text">
          <span className="pv-eyebrow">Bảng chữ cái tiếng Trung · 拼音表</span>
          <h1>Bảng pinyin</h1>
          <p>Tiếng Trung không có bảng chữ cái như tiếng Việt. Người học dùng <b>pinyin</b>: phụ âm đầu ghép với phần vần, rồi thêm một trong bốn thanh. Bấm vào bất kỳ âm nào để nghe.</p>
        </div>
        <dl className="pv-stats">
          {stats.map(([n, label, sub]) => (
            <div key={label}><dt>{label}<small>{sub}</small></dt><dd>{n}</dd></div>
          ))}
        </dl>
        <span className="pv-hero__bg" aria-hidden="true">拼音</span>
      </header>

      <section className="pv-sec" aria-labelledby="pv-tones">
        <div className="pv-sec__head"><span className="pv-num">1</span><div><h2 id="pv-tones">Bốn thanh điệu</h2><p>Cùng một âm tiết, đổi thanh là đổi nghĩa: mā 妈 mẹ, mǎ 马 ngựa.</p></div></div>
        <ToneLegend contour />
      </section>

      <section className="pv-sec" aria-labelledby="pv-inits">
        <div className="pv-sec__head"><span className="pv-num">2</span><div><h2 id="pv-inits">Phụ âm đầu</h2><p>Chia theo chỗ đặt lưỡi và môi. Bấm từng phím để nghe cách đọc khi học bảng.</p></div></div>
        <Initials />
      </section>

      <section className="pv-sec" aria-labelledby="pv-table">
        <div className="pv-sec__head"><span className="pv-num">3</span><div><h2 id="pv-table">Bảng ghép âm tiết</h2><p>Hàng là vần, cột là phụ âm đầu. Chọn nhóm vần rồi bấm một ô.</p></div></div>
        <div className="pv-play">
          <SyllableCard sel={sel} />
          <GroupTabs value={tab} onChange={setTab} />
          <PinyinTable group={tab} sel={sel} onPick={pick} />
        </div>
      </section>

      <section className="pv-sec" aria-labelledby="pv-rules">
        <div className="pv-sec__head"><span className="pv-num">4</span><div><h2 id="pv-rules">Quy tắc viết cần nhớ</h2><p>Ba điểm hay nhầm khi đọc và viết pinyin.</p></div></div>
        <div className="pv-rules">
          {RULES.map((r, i) => (
            <article key={r.title} className="pv-rule">
              <span className="pv-rule__n">0{i + 1}</span>
              <b>{r.title}</b>
              <p>{r.body}</p>
            </article>
          ))}
        </div>
      </section>

      <Link className="pv-next" to="/l0">
        <span className="pv-next__hz" aria-hidden="true">声</span>
        <span><b>Học kỹ hơn ở Cấp 0 · Nhập môn</b><small>Cách phát âm từng nhóm phụ âm và quy tắc biến điệu</small></span>
        <Icon name="arrow" />
      </Link>
    </div>
  );
}
