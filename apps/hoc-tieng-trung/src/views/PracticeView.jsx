// Luyện tập: chọn phạm vi, làm bài 5 dạng câu hỏi, xem kết quả
import { useEffect, useRef, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { Button, EmptyState, Icon, IconButton, Row, Stack, PageHeader } from '@trang/ui';
import { LEVELS, LESSONS, WORDS, lessonById } from '../core/data.js';
import { syls, pyText, toneOf, bareSyl, markSyl, plainHz, shuffle, pickOne } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { useStore, getState, update, lessonDoneCount, setLessonScore, recordAnswer } from '../core/store.js';
import { Hz, Py, Hv, SayButton } from '../components/Hanzi.jsx';
import './PracticeView.css';

/* Từ trong phạm vi luyện tập */
function scopeWords(scope, id) {
  if (scope === 'lesson') return lessonById(id)?.words || [];
  if (scope === 'level') return WORDS.filter(w => w.lv === +id);
  if (scope === 'learned') return WORDS.filter(w => getState().cards[w.id]);
  return WORDS;
}
/** Pinyin nhiễu: đổi thanh của 1–2 âm tiết */
function pyVariants(w) {
  const ss = syls(w), right = ss.join(''), out = new Set();
  for (let k = 0; k < 60 && out.size < 3; k++) {
    const v = ss.slice(); const n = ss.length === 1 ? 1 : 1 + Math.floor(Math.random() * Math.min(2, ss.length));
    shuffle([...ss.keys()]).slice(0, n).forEach(i => { const cur = toneOf(ss[i]); v[i] = markSyl(bareSyl(ss[i]), pickOne([1, 2, 3, 4].filter(x => x !== cur))); });
    const s = v.join(''); if (s !== right) out.add(s);
  }
  return [...out];
}
/** Tạo n câu hỏi, xoay vòng 5 dạng */
function makeQuestions(words, n) {
  const pool = shuffle(words), qs = [], types = ['meaning', 'pinyin', 'listen', 'hanzi', 'order'];
  for (let i = 0; i < n; i++) {
    const w = pool[i % pool.length];
    let type = types[i % types.length];
    if (type === 'order' && w.ex.split('|').length < 3) type = 'meaning';
    const others = shuffle((words.length >= 4 ? words : WORDS).filter(x => x.hz !== w.hz && x.vi !== w.vi)).slice(0, 3);
    const q = { type, w };
    if (type === 'pinyin') q.opts = shuffle([pyText(w), ...pyVariants(w)]);
    else if (type === 'order') {
      const toks = w.ex.split('|'); let sh;
      do { sh = shuffle(toks.map((t, i) => ({ t, i }))); } while (sh.map(x => x.t).join('') === toks.join('') && toks.length > 1);
      q.toks = sh; q.answer = toks.join('');
    } else q.opts = shuffle([w, ...others]);
    qs.push(q);
  }
  return shuffle(qs);
}
const startQuiz = (scope, id) => {
  const words = scopeWords(scope, id);
  return { qs: words.length ? makeQuestions(words, scope === 'level' ? 20 : 10) : [], i: 0, ok: 0, res: [], answered: false, picked: null, order: [], finished: false };
};

export function PracticeView() {
  const { scope, id } = useParams();
  if (!scope) return <PracticeHome />;
  return <Quiz key={`${scope}/${id ?? ''}`} scope={scope} id={id ?? ''} />;
}

function PracticeHome() {
  const S = useStore();
  const learned = WORDS.filter(w => S.cards[w.id]).length;
  if (!LESSONS.length) return <EmptyState title="Chưa tải được dữ liệu bài học"><p className="ui-muted">Kiểm tra dữ liệu bài học rồi tải lại trang.</p></EmptyState>;
  const recent = LESSONS.filter(l => lessonDoneCount(l.id) > 0).slice(-1)[0] || LESSONS[0];
  return (
    <>
      <PageHeader eyebrow="Luyện tập" title="Chọn phạm vi luyện tập" sub="Mỗi lượt trộn các dạng: chọn nghĩa, chọn pinyin đúng thanh, nghe rồi chọn chữ, chọn chữ theo nghĩa, sắp xếp câu." />
      <div className="choices">
        <Link className="choice" to={`/practice/lesson/${recent.id}`}>
          <span className="ui-eyebrow">Bài gần nhất</span><b style={{ fontSize: 17 }}>{LEVELS[recent.lv].name} · {recent.title}</b>
          <span className="ui-muted" style={{ fontSize: 14 }}>10 câu · {recent.words.length} từ</span>
        </Link>
        <Link className="choice" to="/practice/learned" aria-disabled={learned ? undefined : 'true'} tabIndex={learned ? undefined : -1}>
          <span className="ui-eyebrow">Từ đã học</span><b style={{ fontSize: 17 }}>Tất cả từ trong bộ ôn tập</b>
          <span className="ui-muted" style={{ fontSize: 14 }}>{learned ? `10 câu · ${learned} từ` : 'Chưa có từ nào, hãy học một bài trước'}</span>
        </Link>
        {[1, 2].map(n => (
          <Link key={n} className="choice" to={`/practice/level/${n}`}>
            <span className="ui-eyebrow">Kiểm tra cuối cấp</span><b style={{ fontSize: 17 }}>{LEVELS[n].name}</b>
            <span className="ui-muted" style={{ fontSize: 14 }}>20 câu · đạt 80% để hoàn thành cấp{S.passed[n] ? ` · đã đạt ${S.passed[n]}%` : ''}</span>
          </Link>
        ))}
      </div>
      <Stack as="section">
        <h2 style={{ fontSize: 18 }}>Theo từng bài</h2>
        <Row gap={8}>{LESSONS.map(l => <Link key={l.id} className="ui-chip" to={`/practice/lesson/${l.id}`}>{l.lv}.{l.no} {l.title}</Link>)}</Row>
      </Stack>
    </>
  );
}

function Quiz({ scope, id }) {
  useStore();
  const [P, setP] = useState(() => startQuiz(scope, id));
  const set = patch => setP(p => ({ ...p, ...patch }));
  const q = P.qs[P.i];

  // Câu dạng nghe: tự đọc khi hiện câu
  useEffect(() => {
    if (!q || P.finished || P.answered || q.type !== 'listen') return;
    const t = setTimeout(() => say(q.w.hz), 250);
    return () => clearTimeout(t);
  }, [P.qs, P.i, P.finished]); // eslint-disable-line react-hooks/exhaustive-deps

  const answer = (ok, patch) => { recordAnswer(ok); set({ ...patch, answered: true, res: [...P.res, ok], ok: P.ok + (ok ? 1 : 0) }); };
  const pick = v => {
    if (P.answered) return;
    answer(q.type === 'pinyin' ? v === pyText(q.w) : v === q.w.id, { picked: v }); // so khớp theo w.id
    if (q.type !== 'listen') say(q.w.hz);
  };
  const check = () => {
    const s = P.order.map(i => q.toks.find(x => x.i === i).t).join('');
    answer(s === q.answer, {});
    say(plainHz(q.w.ex));
  };
  const next = () => {
    const i = P.i + 1;
    if (i >= P.qs.length) {
      const pct = Math.round(P.ok / P.qs.length * 100);
      if (scope === 'lesson') setLessonScore(id, pct);
      if (scope === 'level' && pct >= 80) update(s => { s.passed[id] = Math.max(pct, s.passed[id] || 0); });
      set({ i, answered: false, picked: null, order: [], finished: true });
    } else set({ i, answered: false, picked: null, order: [] });
    window.scrollTo(0, 0);
  };

  // Enter: sang câu tiếp theo
  const live = useRef(); live.current = { P, next };
  useEffect(() => {
    const onKey = e => {
      if (e.key !== 'Enter' || e.target.closest?.('input,textarea,select,button,a')) return;
      const { P, next } = live.current;
      if (!P.finished && P.answered) { e.preventDefault(); next(); }
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, []);

  if (!P.qs.length || !q && !P.finished) return (
    <EmptyState title="Chưa có từ để luyện" actions={<Button as={Link} variant="primary" to="/practice">Chọn phạm vi khác</Button>}>
      <p className="ui-muted">Học một bài và thêm từ vào ôn tập trước.</p>
    </EmptyState>
  );

  const l = scope === 'lesson' ? lessonById(id) : null;
  const title = l ? `${LEVELS[l.lv].name} · Bài ${l.no} · ${l.title}` : scope === 'level' ? `Kiểm tra cuối ${LEVELS[id]?.name ?? 'cấp'}` : 'Từ đã học';
  const back = scope === 'lesson' ? `/lesson/${id}` : scope === 'level' ? `/level/${id}` : '/practice';
  if (P.finished) return <Result P={P} scope={scope} id={id} title={title} back={back} again={() => setP(startQuiz(scope, id))} />;

  const w = q.w;
  const optCls = o => {
    if (!P.answered) return '';
    const right = q.type === 'pinyin' ? o === pyText(w) : o.id === w.id;
    const picked = q.type === 'pinyin' ? o === P.picked : o.id === P.picked;
    return right ? 'right' : picked ? 'wrong' : '';
  };
  const opt = (o, children) => (
    <button key={q.type === 'pinyin' ? o : o.id} type="button" className={`opt ${optCls(o)}`} disabled={P.answered} onClick={() => pick(q.type === 'pinyin' ? o : o.id)}>{children}</button>
  );

  let prompt = null, body = null;
  if (q.type === 'meaning') {
    prompt = <><span className="ui-eyebrow">Chọn nghĩa đúng</span>
      <Row gap={14} style={{ justifyContent: 'center' }}><span className="prompt-hz">{w.hz}</span><SayButton text={w.hz} label="Nghe" /></Row></>;
    body = <div className="opts wide">{q.opts.map(o => opt(o, <>{o.vi}</>))}</div>;
  }
  if (q.type === 'hanzi') {
    prompt = <><span className="ui-eyebrow">Chọn chữ Hán có nghĩa</span><h2 style={{ fontSize: 28, textAlign: 'center' }}>“{w.vi}”</h2></>;
    body = <div className="opts">{q.opts.map(o => opt(o, <><Hz>{o.hz}</Hz></>))}</div>;
  }
  if (q.type === 'listen') {
    prompt = <><span className="ui-eyebrow">Nghe rồi chọn</span><h2 style={{ fontSize: 24, textAlign: 'center' }}>Bạn nghe thấy từ nào?</h2>
      <Row gap={12} align="flex-end" style={{ justifyContent: 'center' }}>
        <button type="button" className="playbig" aria-label="Phát lại" onClick={() => say(w.hz)}><Icon name="sound" size={38} /></button>
        <button type="button" className="slowbtn" aria-label="Phát chậm" onClick={() => say(w.hz, 0.65)}>0.6×</button>
      </Row></>;
    body = <div className="opts">{q.opts.map(o => opt(o, <><Hz>{o.hz}</Hz>{P.answered && <Py w={o} />}</>))}</div>;
  }
  if (q.type === 'pinyin') {
    prompt = <><span className="ui-eyebrow">Chọn pinyin đúng thanh điệu</span>
      <Row gap={14} style={{ justifyContent: 'center' }}><span className="prompt-hz">{w.hz}</span></Row>
      <p className="ui-muted" style={{ textAlign: 'center' }}>{w.vi}</p></>;
    body = <div className="opts">{q.opts.map(o => opt(o, <><span className="ui-py">{o}</span></>))}</div>;
  }
  if (q.type === 'order') {
    prompt = <><span className="ui-eyebrow">Sắp xếp thành câu đúng</span><h2 style={{ fontSize: 26 }}>{w.exVi}</h2></>;
    const placed = P.order.map(i => q.toks.find(x => x.i === i));
    body = <>
      <div className="slot" aria-label="Câu trả lời của bạn">
        {placed.length ? placed.map(x => (
          <button key={x.i} type="button" className="tok" disabled={P.answered} onClick={() => set({ order: P.order.filter(k => k !== x.i) })}>{x.t}</button>
        )) : <span className="ui-muted" style={{ fontSize: 14 }}>Chạm vào các từ bên dưới theo đúng thứ tự…</span>}
      </div>
      <div className="bank" aria-label="Các từ để chọn">
        {q.toks.map(x => (
          <button key={x.i} type="button" className={`tok ${P.order.includes(x.i) ? 'used' : ''}`} disabled={P.answered}
            onClick={() => !P.order.includes(x.i) && set({ order: [...P.order, x.i] })}>{x.t}</button>
        ))}
      </div>
      {!P.answered && (
        <Row between style={{ paddingTop: 16, borderTop: '1px solid var(--line)' }}>
          <Button icon="undo" onClick={() => set({ order: [] })}>Làm lại</Button>
          <Button variant="primary" disabled={P.order.length !== q.toks.length} onClick={check}>Kiểm tra</Button>
        </Row>
      )}
    </>;
  }

  const ok = P.res[P.res.length - 1];
  return (
    <div className="qz">
      <Row gap={14} wrap={false}>
        <IconButton as={Link} to={back} icon="x" label="Thoát luyện tập" style={{ width: 44, height: 44, color: 'var(--ink-2)' }} />
        <Stack gap={6} style={{ flex: 1, minWidth: 0 }}>
          <Row between wrap={false} style={{ fontSize: 14 }}>
            <b style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{title}</b>
            <span className="ui-muted ui-num" style={{ whiteSpace: 'nowrap' }}>Câu {P.i + 1}/{P.qs.length}</span>
          </Row>
          <div className="segs" style={{ gridTemplateColumns: `repeat(${P.qs.length},minmax(0,1fr))` }} aria-hidden="true">
            {P.qs.map((_, i) => <i key={i} className={i < P.res.length ? (P.res[i] ? 'ok' : 'no') : i === P.i ? 'cur' : ''} />)}
          </div>
        </Stack>
      </Row>
      <Stack gap={14}>{prompt}</Stack>
      {body}
      {P.answered && (
        <div className={`fb ${ok ? 'ok' : 'no'}`} aria-live="polite">
          <h3>{ok ? 'Chính xác!' : 'Chưa đúng'}</h3>
          {q.type === 'order'
            ? <p><Hz size={20}>{plainHz(w.ex)}</Hz><br /><span className="ui-py ui-muted">{w.exPy}</span></p>
            : <p><Hz size={22}>{w.hz}</Hz> <b><Py w={w} /></b> · <Hv>{w.hv}</Hv> · <b>{w.vi}</b></p>}
          {q.type === 'pinyin' && (
            <p className="ui-muted" style={{ fontSize: 14 }}>Thanh điệu: {syls(w).map(s => `${s} = ${toneOf(s) === 5 ? 'thanh nhẹ' : 'thanh ' + toneOf(s)}`).join(', ')}.</p>
          )}
          <Button variant="primary" style={{ alignSelf: 'flex-start' }} onClick={next}>{P.i + 1 < P.qs.length ? 'Câu tiếp theo' : 'Xem kết quả'}</Button>
        </div>
      )}
    </div>
  );
}

function Result({ P, scope, id, title, back, again }) {
  const pct = Math.round(P.ok / P.qs.length * 100);
  const note = scope !== 'level' ? '' : pct >= 80 ? `Bạn đã đạt yêu cầu hoàn thành ${LEVELS[id]?.name}.` : 'Cần đạt 80% để hoàn thành cấp. Ôn lại các bài rồi thử lại nhé.';
  const wrong = [...new Map(P.qs.filter((q, i) => !P.res[i]).map(q => [q.w.hz, q.w])).values()];
  return (
    <div className="qz">
      <EmptyState glyph={pct >= 80 ? '优' : pct >= 60 ? '良' : '加油'} glyphColor={pct >= 80 ? 'var(--jade)' : 'var(--seal)'}
        actions={<>
          <Button onClick={again}>Luyện lại</Button>
          <Button as={Link} variant="primary" to={back}>{scope === 'lesson' ? 'Về bài học' : 'Xong'}</Button>
        </>}>
        <span className="ui-eyebrow">{title}</span>
        <h1 style={{ fontSize: 28 }} className="ui-num">{P.ok}/{P.qs.length} câu đúng · {pct}%</h1>
        {note && <p className="ui-muted">{note}</p>}
        {wrong.length > 0 && (
          <Stack gap={8} style={{ width: '100%', maxWidth: 520, textAlign: 'left' }}>
            <span className="ui-eyebrow">Từ cần xem lại</span>
            {wrong.map(w => (
              <Row key={w.id} between style={{ padding: '8px 12px', borderRadius: 10, background: 'var(--surface-2)' }}>
                <span><Hz size={20}>{w.hz}</Hz> <Py w={w} /></span><span>{w.vi}</span>
              </Row>
            ))}
          </Stack>
        )}
      </EmptyState>
    </div>
  );
}
