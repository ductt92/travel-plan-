// Tập viết: mô phỏng thứ tự nét và tự viết bằng Hanzi Writer
import { useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import HanziWriter from 'hanzi-writer';
import { Button, Card, Field, PageHeader, Row, Stack, useToast } from '@trang/ui';
import { LESSONS, WORDS } from '../core/data.js';
import { syls, toneOf } from '../core/pinyin.js';
import { useStore, activity, lessonDoneCount, nextLesson } from '../core/store.js';
import { Hz, Hv, SayButton } from '../components/Hanzi.jsx';
import './WriteView.css';

let lastCh = '好'; // nhớ chữ đang tập khi rời trang
const cssVar = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const isHan = c => /\p{Script=Han}/u.test(c);

/** Bài đang học: bài kế tiếp chưa xong, không có thì bài gần nhất đã mở */
function currentLesson() {
  const nl = nextLesson();
  return (nl?.kind === 'lesson' && nl.l) || LESSONS.filter(l => lessonDoneCount(l.id) > 0).slice(-1)[0] || LESSONS[0];
}

export function WriteView() {
  const S = useStore();
  const { ch: param } = useParams();
  const ch = param && isHan([...param][0]) ? [...param][0] : lastCh;
  lastCh = ch;
  const nav = useNavigate();
  const toast = useToast();
  const box = useRef(null), writer = useRef(null);
  const [outline, setOutline] = useState(true);
  const outlineRef = useRef(outline); outlineRef.current = outline;
  const [msg, setMsg] = useState('');
  const [err, setErr] = useState('');
  const [strokes, setStrokes] = useState(0);
  const [inp, setInp] = useState(ch);

  // Tạo writer cho chữ hiện tại; dọn khi đổi chữ hoặc rời trang
  useEffect(() => {
    const el = box.current; if (!el) return;
    let alive = true;
    setMsg(''); setErr(''); setStrokes(0); setInp(ch);
    const size = Math.min(300, el.parentElement.clientWidth) - 8;
    el.innerHTML = '';
    const w = HanziWriter.create(el, ch, {
      width: size, height: size, padding: 14, showOutline: outlineRef.current, strokeAnimationSpeed: 1, delayBetweenStrokes: 220,
      strokeColor: cssVar('--ink'), radicalColor: cssVar('--seal'), outlineColor: cssVar('--line-2'), highlightColor: cssVar('--jade'), drawingColor: cssVar('--jade'),
      onLoadCharDataError: () => { if (alive) { el.innerHTML = ''; setErr('Không tìm thấy dữ liệu nét cho chữ này.'); } }
    });
    writer.current = w;
    HanziWriter.loadCharacterData(ch).then(d => { if (alive && d) setStrokes(d.strokes.length); }).catch(() => {});
    w.animateCharacter();
    return () => {
      alive = false;
      try { w.cancelQuiz(); w.pauseAnimation(); } catch (e) { /* bỏ qua */ }
      writer.current = null; el.innerHTML = '';
    };
  }, [ch]);

  const animate = () => { writer.current?.cancelQuiz(); writer.current?.animateCharacter(); setMsg(''); };
  const loop = () => { writer.current?.cancelQuiz(); writer.current?.loopCharacterAnimation(); };
  const quiz = () => {
    if (!writer.current) return;
    setMsg('Viết từng nét theo đúng thứ tự…');
    writer.current.quiz({
      onMistake: s => setMsg(`Nét ${s.strokeNum + 1} chưa đúng, thử lại nhé.`),
      onCorrectStroke: s => setMsg(`Đúng nét ${s.strokeNum + 1}. Còn ${s.strokesRemaining} nét.`),
      onComplete: s => { setMsg(s.totalMistakes ? `Hoàn thành, sai ${s.totalMistakes} lần. Viết lại để nhớ hơn.` : 'Tuyệt vời! Bạn viết đúng toàn bộ các nét.'); activity(); }
    });
  };
  const toggleOutline = () => {
    const on = !outline; setOutline(on);
    on ? writer.current?.showOutline() : writer.current?.hideOutline();
  };
  const go = c => nav(`/write/${encodeURIComponent(c)}`);
  const submit = () => {
    const c = [...inp.trim()].find(isHan);
    if (!c) { toast('Hãy nhập một chữ Hán'); return; }
    go(c);
  };

  // Thông tin chữ: từ chứa chữ, pinyin và Hán Việt của riêng chữ đó
  const w = WORDS.find(x => x.hz === ch) || WORDS.find(x => x.hz.includes(ch));
  const chars = w ? [...w.hz] : [], idx = chars.indexOf(ch);
  const hvChar = w && w.hv.split(' ').length === chars.length ? w.hv.split(' ')[idx] : null;
  const pyChar = w && syls(w).length === chars.length ? syls(w)[idx] : null;
  const learned = [...new Set(WORDS.filter(x => S.cards[x.id]).flatMap(x => [...x.hz]))];
  const lessonChars = [...new Set((currentLesson()?.words || []).flatMap(x => [...x.hz]))];
  const sugg = list => (
    <div className="sugg">
      {list.map(c => <button key={c} type="button" className={c === ch ? 'on' : ''} aria-label={`Tập viết ${c}`} aria-current={c === ch ? 'true' : undefined} onClick={() => go(c)}>{c}</button>)}
    </div>
  );

  return (
    <>
      <PageHeader eyebrow="Tập viết 写字" title="Luyện viết theo thứ tự nét" sub="Xem mô phỏng từng nét, rồi tự viết lên ô chữ điền. Nét sai sẽ được gợi ý lại." />
      <div className="writer-grid">
        <Card as="section" className="ui-stack" style={{ flex: '1 1 340px', alignItems: 'center', gap: 18, minWidth: 0 }}>
          <div className="tzg">
            {/* Ô chữ điền: đường kẻ đỏ chia ô */}
            <svg className="bg" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
              <g style={{ stroke: 'var(--grid)' }} strokeWidth=".6" strokeDasharray="2 2" fill="none">
                <line x1="50" y1="0" x2="50" y2="100" /><line x1="0" y1="50" x2="100" y2="50" />
                <line x1="0" y1="0" x2="100" y2="100" /><line x1="100" y1="0" x2="0" y2="100" />
              </g>
            </svg>
            <div className="hw" ref={box} aria-label={`Ô tập viết chữ ${ch}`} />
            {err && <p className="hw-err ui-muted">{err}</p>}
          </div>
          <Row gap={8} style={{ justifyContent: 'center' }}>
            <Button variant="primary" icon="play" onClick={animate}>Xem nét</Button>
            <Button icon="loop" onClick={loop}>Lặp lại</Button>
            <Button variant="soft" icon="hand" onClick={quiz}>Tự viết</Button>
            <Button icon="eye" onClick={toggleOutline} aria-pressed={!outline}>{outline ? 'Ẩn chữ mờ' : 'Hiện chữ mờ'}</Button>
          </Row>
          <p className="ui-muted" style={{ minHeight: 24, textAlign: 'center' }} aria-live="polite">{msg}</p>
        </Card>
        <Stack as="section" gap={18} style={{ flex: '1 1 300px', minWidth: 0 }}>
          <Card className="ui-stack" style={{ gap: 10 }}>
            <Row between><Hz size={64} style={{ lineHeight: 1 }}>{ch}</Hz><SayButton text={ch} /></Row>
            {pyChar && <span className={`ui-py t${toneOf(pyChar)}`} style={{ fontSize: 22 }}>{pyChar}</span>}
            {hvChar && <Hv>Hán Việt: {hvChar}</Hv>}
            {w
              ? <span>Trong từ <Link to={`/dict/${encodeURIComponent(w.id)}`}><Hz>{w.hz}</Hz></Link>: {w.vi}</span>
              : <span className="ui-muted">Chữ này chưa có trong các bài đã soạn.</span>}
            <span className="ui-muted ui-num">{strokes ? `${strokes} nét · nét bộ thủ tô màu đỏ` : ''}</span>
          </Card>
          <Field id="wr-in" label="Nhập một chữ Hán bất kỳ">
            <Row gap={8} wrap={false}>
              <input id="wr-in" className="ui-input ui-hz" maxLength={2} value={inp} onChange={e => setInp(e.target.value)}
                onKeyDown={e => { if (e.key === 'Enter' && !e.nativeEvent.isComposing) submit(); }}
                style={{ fontSize: 22, textAlign: 'center', maxWidth: 120 }} />
              <Button variant="primary" onClick={submit}>Tập viết</Button>
            </Row>
          </Field>
          <Stack gap={8}><span className="ui-eyebrow">Chữ trong bài đang học</span>{sugg(lessonChars)}</Stack>
          {learned.length > 0 && <Stack gap={8}><span className="ui-eyebrow">Chữ đã học ({learned.length})</span>{sugg(learned.slice(0, 40))}</Stack>}
        </Stack>
      </div>
    </>
  );
}
