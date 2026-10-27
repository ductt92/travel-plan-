// Bảng pinyin: thanh mẫu × vận mẫu; bấm một âm tiết để nghe chữ mẫu và xem 4 dấu thanh.
import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { Card, EmptyState, Icon, Row, Stack } from '@trang/ui';
import { PINYIN } from '../core/data.js';
import { toneOf, markSyl } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { SayButton } from '../components/Hanzi.jsx';
import './PinyinView.css';

const PY_INITS = ['', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's'];
const PY_FINALS = [
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
function spell(ini, fin) {
  let sp;
  if (!ini) { if (fin === '-i') return null; sp = ZERO[fin] || fin; }
  else if (fin === '-i') { if (!RETRO.includes(ini)) return null; sp = ini + 'i'; }
  else if (fin === 'i' && RETRO.includes(ini)) return null;
  else if (fin[0] === 'u' && ['j', 'q', 'x'].includes(ini)) return null; // ju/qu/xu thuộc hàng ü
  else if (fin[0] === 'ü' && ['j', 'q', 'x'].includes(ini)) sp = ini + fin.replace('ü', 'u');
  else sp = ini + fin;
  return [sp, sp.replace('ü', 'v')];
}

/** Khung chi tiết âm tiết đang chọn */
function Detail({ sp, v }) {
  const [ch, py, vi] = v;
  return (
    <Card as="section" className="ui-row" style={{ gap: 24, alignItems: 'center', flexWrap: 'wrap' }} aria-label={`Âm tiết ${sp}`}>
      <Stack gap={2} style={{ minWidth: 120 }}>
        <span className="ui-eyebrow">Âm tiết</span>
        <b className="ui-py" style={{ fontSize: 34 }}>{sp}</b>
      </Stack>
      <Row gap={10}>
        {[1, 2, 3, 4].map(t => <span key={t} className={`ui-py t${t} pyd-tone`}>{markSyl(sp, t)}</span>)}
      </Row>
      <Row gap={12} style={{ marginLeft: 'auto' }}>
        <span className="ui-hz" style={{ fontSize: 44, lineHeight: 1 }}>{ch}</span>
        <Stack gap={0}>
          <span className={`ui-py t${toneOf(py)}`} style={{ fontSize: 18 }}>{py}</span>
          <span className="ui-muted" style={{ fontSize: 14 }}>{vi}</span>
        </Stack>
        <SayButton text={ch} />
        <Link className="ui-link" to={`/write/${encodeURIComponent(ch)}`}><Icon name="brush" size={15} />Tập viết</Link>
      </Row>
    </Card>
  );
}

export function PinyinView() {
  const [sel, setSel] = useState(null); // [cách viết, khóa]
  const box = useRef(null);
  useEffect(() => { if (sel) box.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, [sel]);

  if (!PINYIN || !Object.keys(PINYIN).length) return (
    <EmptyState title="Chưa tải được bảng pinyin"><p className="ui-muted">Thiếu file dữ liệu pinyin.</p></EmptyState>
  );
  const pick = r => { setSel(r); say(PINYIN[r[1]][0]); };

  return (
    <>
      <Stack as="header" gap={6}>
        <span className="ui-eyebrow">Bảng chữ cái tiếng Trung · 拼音表</span>
        <h1 style={{ fontSize: 30 }}>Bảng pinyin</h1>
        <p className="ui-muted" style={{ maxWidth: '68ch' }}>Tiếng Trung không có bảng chữ cái như tiếng Việt. Người học dùng pinyin: 21 thanh mẫu (phụ âm đầu) ghép với các vận mẫu (phần vần), cộng 4 thanh điệu. Bấm vào một âm tiết để nghe chữ mẫu và xem cách đánh dấu 4 thanh.</p>
      </Stack>

      <div ref={box} style={{ scrollMarginTop: 16 }}>{sel && <Detail sp={sel[0]} v={PINYIN[sel[1]]} />}</div>

      <Card pad={false} style={{ overflow: 'hidden' }}>
        <div className="pyc-wrap">
          <table className="pyc-t">
            <thead>
              <tr>
                <th scope="col" className="pyc-h pyc-corner">Vần \ Phụ âm</th>
                {PY_INITS.map(i => <th key={i || '0'} scope="col" className="pyc-h">{i || <span className="ui-muted">—</span>}</th>)}
              </tr>
            </thead>
            {PY_FINALS.map((grp, gi) => (
              <tbody key={gi}>
                <tr><th colSpan={PY_INITS.length + 1} className="pyc-g">{PY_GROUPS[gi]}</th></tr>
                {grp.map(f => (
                  <tr key={f}>
                    <th scope="row" className="pyc-f">{f}</th>
                    {PY_INITS.map(i => {
                      const r = spell(i, f);
                      if (!r || !PINYIN[r[1]]) return <td key={i || '0'} />;
                      const on = sel && sel[1] === r[1];
                      return (
                        <td key={i || '0'}>
                          <button type="button" className={`pyc${on ? ' is-on' : ''}`} aria-pressed={on} onClick={() => pick(r)}>{r[0]}</button>
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            ))}
          </table>
        </div>
      </Card>

      <section className="pyc-rules">
        <Card className="ui-stack" style={{ gap: 6 }}><b>Quy tắc viết y, w</b><p className="ui-muted" style={{ fontSize: 14 }}>Vần bắt đầu bằng i, u, ü mà đứng một mình thì viết lại: i → yi, ia → ya; u → wu, uo → wo; ü → yu, üe → yue.</p></Card>
        <Card className="ui-stack" style={{ gap: 6 }}><b>Hai chấm trên ü</b><p className="ui-muted" style={{ fontSize: 14 }}>Sau j, q, x và y thì ü bỏ hai chấm nhưng vẫn đọc là ü: ju, qu, xu, yu. Chỉ n, l giữ hai chấm: nü, lü.</p></Card>
        <Card className="ui-stack" style={{ gap: 6 }}><b>Vần viết tắt</b><p className="ui-muted" style={{ fontSize: 14 }}>iou viết thành iu (liù), uei thành ui (guì), uen thành un (lùn). Vần “-i” sau zh, ch, sh, r, z, c, s không đọc là “i” mà kéo dài phụ âm.</p></Card>
      </section>
      <p className="ui-muted" style={{ fontSize: 14 }}>Xem thêm cách phát âm từng nhóm phụ âm và quy tắc biến điệu ở <Link to="/l0">Cấp 0 · Nhập môn</Link>.</p>
    </>
  );
}
