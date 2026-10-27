// Tra từ: tìm theo chữ Hán, pinyin (có/không dấu), Hán Việt, tiếng Việt
import { useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Button, Chip, Icon, LinkButton, PageHeader, Pill, Row, Stack, Tag, Card, useToast } from '@trang/ui';
import { WORDS, WMAP, byHz } from '../core/data.js';
import { syls, pyText, toneOf, fold, plainHz } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { useStore, getState, addCards, activity, fmtWait } from '../core/store.js';
import { Hz, Py, Hv, SayButton } from '../components/Hanzi.jsx';
import './DictView.css';

const FILTERS = [[0, 'Tất cả'], [1, 'Cấp 1'], [2, 'Cấp 2'], [-1, 'Từ đã học']];
const memo = { q: '', lv: 0, sel: null }; // giữ ô tìm và bộ lọc khi rời trang

function searchWords(query, lv) {
  const raw = query.trim(), q = fold(raw), cards = getState().cards;
  let r = WORDS.filter(w => !lv || (lv === -1 ? cards[w.id] : w.lv === lv));
  if (q) r = r.filter(w => w.hz.includes(raw) || fold(pyText(w)).includes(q.replace(/\s/g, '')) || fold(w.py).includes(q) || fold(w.hv).includes(q) || fold(w.vi).includes(q));
  return r;
}
/** Tô đậm phần khớp (so khớp không dấu) bằng <mark> */
function Hl({ text, q }) {
  q = q.trim(); if (!q) return text;
  const f = fold(text), i = f.indexOf(fold(q));
  if (i < 0 || f.length !== text.length) return text;
  return <>{text.slice(0, i)}<mark>{text.slice(i, i + q.length)}</mark>{text.slice(i + q.length)}</>;
}
const pickSel = s => (s ? (WMAP[s] ? s : byHz(s)?.id || null) : null);

export function DictView() {
  const S = useStore();
  const { sel: param } = useParams();
  const nav = useNavigate();
  const toast = useToast();
  const [q, setQ] = useState(memo.q);
  const [lv, setLv] = useState(memo.lv);
  const [sel, setSel] = useState(() => pickSel(param) || memo.sel);
  const detail = useRef(null);
  useEffect(() => { const s = pickSel(param); if (s) setSel(s); }, [param]);
  useEffect(() => { Object.assign(memo, { q, lv, sel }); }, [q, lv, sel]);

  const r = searchWords(q, lv);
  const cur = sel && r.find(w => w.id === sel) ? sel : r[0]?.id || null;
  const w = WMAP[cur];
  const askAi = text => nav('/ai', { state: { q: text } });
  const choose = id => {
    setSel(id);
    if (window.innerWidth < 900) setTimeout(() => detail.current?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 0);
  };

  return (
    <>
      <PageHeader eyebrow="Tra từ 词典" title="Tra từ" extra={<Button as={Link} to="/pinyin" icon="grid">Bảng pinyin</Button>} />
      <Stack gap={12}>
        <label htmlFor="dq" style={{ fontSize: 14, color: 'var(--ink-2)' }}>Gõ chữ Hán, pinyin (có hoặc không dấu), âm Hán Việt hoặc nghĩa tiếng Việt</label>
        <div className="search">
          <Icon name="search" size={22} style={{ color: 'var(--muted)', flex: 'none' }} />
          <input id="dq" type="search" autoComplete="off" value={q} onChange={e => setQ(e.target.value)} placeholder="ví dụ: màu, yanse, 颜色, nhan sắc" />
          <span className="ui-muted ui-num" style={{ fontSize: 13, whiteSpace: 'nowrap' }}>{r.length} kết quả</span>
        </div>
        <Row gap={8} role="group" aria-label="Lọc">
          {FILTERS.map(([v, t]) => <Chip key={v} active={lv === v} onClick={() => setLv(v)}>{t}</Chip>)}
        </Row>
      </Stack>
      <Row gap={24} align="flex-start">
        <Card as="section" pad={false} style={{ flex: '1 1 400px', minWidth: 0, overflow: 'hidden' }} aria-label="Kết quả">
          {r.length ? r.slice(0, 60).map(x => (
            <button key={x.id} type="button" className={`res ${x.id === cur ? 'on' : ''}`} aria-pressed={x.id === cur} onClick={() => choose(x.id)}>
              <Hz>{x.hz}</Hz>
              <Stack gap={0} style={{ minWidth: 0 }}>
                <span><Py w={x} size={16} /> <Hv>· <Hl text={x.hv} q={q} /></Hv></span>
                <span><Hl text={x.vi} q={q} /></span>
              </Stack>
              <Tag>Cấp {x.lv}</Tag>
            </button>
          )) : (
            <div className="ui-empty">
              <p className="ui-muted">Không tìm thấy “{q}” trong các bài đã soạn.</p>
              <Button variant="soft" icon="ai" onClick={() => askAi(`Giải thích từ tiếng Trung cho “${q}”: chữ Hán, pinyin, âm Hán Việt, nghĩa và 2 câu ví dụ.`)}>Hỏi AI</Button>
            </div>
          )}
        </Card>
        <article ref={detail} className="ui-card ui-card--pad ui-stack" style={{ flex: '1 1 360px', minWidth: 0, gap: 16 }} aria-live="polite">
          {w ? <Detail w={w} S={S} askAi={askAi} add={() => { addCards([w]); activity(); toast('Đã thêm vào ôn tập'); }} /> : <p className="ui-muted">Chọn một từ để xem chi tiết.</p>}
        </article>
      </Row>
    </>
  );
}

function Detail({ w, S, askAi, add }) {
  const chars = [...w.hz], hvs = w.hv.split(' '), pys = syls(w);
  const card = S.cards[w.id];
  return (
    <>
      <Row between align="flex-start">
        <Stack gap={4}><Hz size={56} style={{ lineHeight: 1.1 }}>{w.hz}</Hz><Py w={w} size={22} /></Stack>
        <SayButton text={w.hz} size={48} />
      </Row>
      <Stack gap={2}><Hv>Hán Việt: {w.hv}</Hv><b style={{ fontSize: 20 }}>{w.vi}</b></Stack>
      <div className="parts">
        {chars.map((c, i) => (
          <Link key={i} className="part" to={`/write/${encodeURIComponent(c)}`}>
            <Hz>{c}</Hz>
            <Stack gap={0} style={{ fontSize: 13 }}>
              {hvs.length === chars.length && <b style={{ fontSize: 14 }}>{hvs[i]}</b>}
              {pys.length === chars.length && <span className={`ui-py t${toneOf(pys[i])}`}>{pys[i]}</span>}
              <span className="ui-muted">Tập viết</span>
            </Stack>
          </Link>
        ))}
      </div>
      <Stack gap={6}>
        <span className="ui-eyebrow">Ví dụ</span>
        <div className="ex">
          <Row between wrap={false}><Hz>{plainHz(w.ex)}</Hz><LinkButton icon="play" onClick={() => say(plainHz(w.ex))}>Nghe</LinkButton></Row>
          <span className="ui-py">{w.exPy}</span><span>{w.exVi}</span>
        </div>
      </Stack>
      <Row between style={{ paddingTop: 14, borderTop: '1px solid var(--line)' }}>
        {card
          ? <Pill tone="jade">Đang ôn · lần tới sau {fmtWait(Math.max(0, card.due - Date.now()))}</Pill>
          : <Button variant="soft" icon="plus" onClick={add}>Thêm vào ôn tập</Button>}
        <Row gap={4}>
          <Link className="ui-link" to={`/lesson/${w.lesson}`}>Xem trong bài</Link>
          <LinkButton icon="ai" onClick={() => askAi(`Giải thích chi tiết từ ${w.hz} (${pyText(w)}): cách dùng, từ gần nghĩa, 3 câu ví dụ có pinyin và nghĩa tiếng Việt.`)}>Hỏi AI</LinkButton>
        </Row>
      </Row>
    </>
  );
}
