// Các mảnh dùng chung cho bảng pinyin: trang Pinyin (views/PinyinView) và khung nổi (PinyinFab).
import { Link } from 'react-router-dom';
import { Icon } from '@trang/ui';
import { PINYIN } from '../core/data.js';
import { toneOf, markSyl } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import './PinyinKit.css';

export const PY_INITS = ['', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's'];
export const PY_FINALS = [
  ['a', 'o', 'e', '-i', 'er', 'ai', 'ei', 'ao', 'ou', 'an', 'en', 'ang', 'eng', 'ong'],
  ['i', 'ia', 'ie', 'iao', 'iu', 'ian', 'in', 'iang', 'ing', 'iong'],
  ['u', 'ua', 'uo', 'uai', 'ui', 'uan', 'un', 'uang', 'ueng'],
  ['ü', 'üe', 'üan', 'ün']
];
const PY_GROUPS = ['Vận mẫu đơn và kép', 'Vần bắt đầu bằng i', 'Vần bắt đầu bằng u', 'Vần bắt đầu bằng ü'];
// Âm tiết không có phụ âm đầu viết lại bằng y/w
const ZERO = { i: 'yi', ia: 'ya', ie: 'ye', iao: 'yao', iu: 'you', ian: 'yan', in: 'yin', iang: 'yang', ing: 'ying', iong: 'yong', u: 'wu', ua: 'wa', uo: 'wo', uai: 'wai', ui: 'wei', uan: 'wan', un: 'wen', uang: 'wang', ueng: 'weng', 'ü': 'yu', 'üe': 'yue', 'üan': 'yuan', 'ün': 'yun' };
const RETRO = ['zh', 'ch', 'sh', 'r', 'z', 'c', 's'];

/** Ghép thanh mẫu + vận mẫu thành âm tiết viết đúng chính tả; trả về [cách viết, khóa tra PINYIN] hoặc null */
export function spell(ini, fin) {
  let sp;
  if (!ini) { if (fin === '-i') return null; sp = ZERO[fin] || fin; }
  else if (fin === '-i') { if (!RETRO.includes(ini)) return null; sp = ini + 'i'; }
  else if (fin === 'i' && RETRO.includes(ini)) return null;
  else if (fin[0] === 'u' && ['j', 'q', 'x'].includes(ini)) return null; // ju/qu/xu thuộc hàng ü
  else if (fin[0] === 'ü' && ['j', 'q', 'x'].includes(ini)) sp = ini + fin.replace('ü', 'u');
  else sp = ini + fin;
  return [sp, sp.replace('ü', 'v')];
}

export const SYLLABLE_COUNT = PY_FINALS.flat().reduce((n, f) => n + PY_INITS.filter(i => { const r = spell(i, f); return r && PINYIN[r[1]]; }).length, 0);

// Đường nét thanh theo thang 5 bậc của Triệu Nguyên Nhậm: 55, 35, 214, 51
export const TONES = [
  { t: 1, mark: 'ā', name: 'Ngang', hint: 'cao, đều', pitch: [5, 5] },
  { t: 2, mark: 'á', name: 'Lên', hint: 'như dấu sắc', pitch: [3, 5] },
  { t: 3, mark: 'ǎ', name: 'Xuống – lên', hint: 'như dấu hỏi', pitch: [2, 1, 4] },
  { t: 4, mark: 'à', name: 'Xuống', hint: 'dứt khoát', pitch: [5, 1] }
];

function Contour({ pitch }) {
  const pts = pitch.map((p, i) => `${4 + (i * 40) / (pitch.length - 1)},${4 + (5 - p) * 6}`).join(' ');
  return (
    <svg className="pk-contour" viewBox="0 0 48 32" aria-hidden="true">
      {[1, 2, 3, 4, 5].map(l => <line key={l} x1="2" x2="46" y1={4 + (5 - l) * 6} y2={4 + (5 - l) * 6} />)}
      <polyline points={pts} />
    </svg>
  );
}

/** Chú thích 4 thanh; contour = vẽ thêm đường cao độ */
export function ToneLegend({ contour = false }) {
  return (
    <ul className={`pk-legend${contour ? ' pk-legend--big' : ''}`} aria-label="Bốn thanh điệu">
      {TONES.map(x => (
        <li key={x.t} className={`t${x.t}`}>
          <b>{x.mark}</b>
          <span><strong>Thanh {x.t}</strong> {x.name}<small>{x.hint}</small></span>
          {contour && <Contour pitch={x.pitch} />}
        </li>
      ))}
    </ul>
  );
}

/** Thẻ âm tiết đang chọn: chữ mẫu lớn, 4 thanh, nút tập viết */
export function SyllableCard({ sel }) {
  if (!sel) return (
    <div className="pyf pyf--empty">
      <span className="pyf__ghost" aria-hidden="true">音</span>
      <div>
        <b>Chọn một âm tiết bên dưới</b>
        <p>Nghe chữ mẫu và xem âm tiết đó ở cả 4 thanh.</p>
      </div>
    </div>
  );
  const [sp, key] = sel;
  const [ch, py, vi] = PINYIN[key];
  return (
    <div className="pyf" aria-live="polite">
      <button type="button" className="pyf__hz" onClick={() => say(ch)} aria-label={`Nghe ${ch}`}>
        <span lang="zh">{ch}</span>
        <Icon name="sound" size={16} />
      </button>
      <div className="pyf__main">
        <span className="pyf__label">Âm tiết</span>
        <b className="pyf__sp">{sp}</b>
        <span className="pyf__ex"><span className={`t${toneOf(py)}`}>{py}</span> · {vi}</span>
      </div>
      <div className="pyf__tones" role="group" aria-label="Bốn thanh">
        {[1, 2, 3, 4].map(t => <span key={t} className={`pyf__tone t${t}`}>{markSyl(sp, t)}</span>)}
      </div>
      <Link className="pyf__write" to={`/write/${encodeURIComponent(ch)}`}><Icon name="brush" size={15} />Tập viết</Link>
    </div>
  );
}

export const GROUP_TABS = [
  { id: 0, label: 'a o e', sub: 'Vần đơn, kép' },
  { id: 1, label: 'i', sub: 'Bắt đầu bằng i' },
  { id: 2, label: 'u', sub: 'Bắt đầu bằng u' },
  { id: 3, label: 'ü', sub: 'Bắt đầu bằng ü' },
  { id: null, label: 'Tất cả', sub: 'Cả bảng' }
];

export function GroupTabs({ value, onChange }) {
  return (
    <div className="pk-tabs" role="tablist" aria-label="Nhóm vần">
      {GROUP_TABS.map(t => (
        <button key={String(t.id)} type="button" role="tab" aria-selected={value === t.id} className={value === t.id ? 'is-on' : ''} onClick={() => onChange(t.id)}>
          <b>{t.label}</b><small>{t.sub}</small>
        </button>
      ))}
    </div>
  );
}

/** Bảng thanh mẫu × vận mẫu. group: chỉ số nhóm vần (null = tất cả); sel: [cách viết, khóa] đang chọn */
export function PinyinTable({ group = null, sel, onPick }) {
  const groups = group == null ? PY_FINALS.map((g, i) => [g, i]) : [[PY_FINALS[group], group]];
  // chỉ giữ các cột phụ âm có ít nhất một âm tiết trong nhóm đang xem
  const inits = PY_INITS.filter(i => groups.some(([g]) => g.some(f => { const r = spell(i, f); return r && PINYIN[r[1]]; })));
  return (
    <div className="pk-table" role="tabpanel">
      <div className="pyc-wrap">
        <table className="pyc-t">
          <thead>
            <tr>
              <th scope="col" className="pyc-h pyc-corner">Vần \ Phụ âm</th>
              {inits.map(i => <th key={i || '0'} scope="col" className="pyc-h">{i || <span className="pk-none">—</span>}</th>)}
            </tr>
          </thead>
          {groups.map(([grp, gi]) => (
            <tbody key={gi}>
              {group == null && <tr><th colSpan={inits.length + 1} className="pyc-g">{PY_GROUPS[gi]}</th></tr>}
              {grp.map(f => (
                <tr key={f}>
                  <th scope="row" className="pyc-f">{f}</th>
                  {inits.map(i => {
                    const r = spell(i, f);
                    if (!r || !PINYIN[r[1]]) return <td key={i || '0'} />;
                    const on = sel && sel[1] === r[1];
                    return (
                      <td key={i || '0'}>
                        <button type="button" className={`pyc${on ? ' is-on' : ''}`} aria-pressed={on} onClick={() => onPick(r)}>{r[0]}</button>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          ))}
        </table>
      </div>
    </div>
  );
}
