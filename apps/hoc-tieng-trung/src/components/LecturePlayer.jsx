// Trình phát bài giảng: màn chiếu 16:9 kiểu bảng lớp học, lời giảng bằng giọng đọc
// (tiếng Việt giảng giải, tiếng Trung đọc mẫu), có phụ đề và thanh điều khiển.
// renderMode: dùng cho công cụ dựng video, hiện đúng một bước, không phát âm, không điều khiển.
// slide (kèm renderMode): hiện trọn một trang, đủ nội dung, không phụ đề (bảng của lớp học trực tiếp).
import { useEffect, useMemo, useRef, useState } from 'react';
import { Chip, Icon, IconButton, ProgressBar, useToast } from '@trang/ui';
import { LEVELS } from '../core/data.js';
import { plainHz } from '../core/pinyin.js';
import { buildLecture, stepParts } from '../core/lecture.js';
import { playClip, stopVoice } from '../core/speech.js';
import { markPart, activity } from '../core/store.js';
import { Py } from './Hanzi.jsx';
import './LecturePlayer.css';

const WHO_A = ['安', '梅'];
/** Màu avatar người nói: 安/梅 màu A, còn lại màu B */
export const whoTone = name => (WHO_A.includes(name) ? 'a' : 'b');
const RATES = [0.75, 1, 1.25];

/** Nội dung một trang chiếu ở mức hiện r */
function Slide({ sl, r, l }) {
  const L = LEVELS[l.lv];
  if (sl.kind === 'title') return (
    <div className="sl sl-title">
      <span className="s-eye">{L.name} · Bài {l.no}</span>
      <span className="s-hz s-xl">{l.zh}</span>
      <span className="s-h">{l.title}</span>
      {r >= 2 && <ul className="s-goals fade">{l.goal.map((g, i) => <li key={i}>{g}</li>)}</ul>}
    </div>
  );
  if (sl.kind === 'word') {
    const w = sl.w;
    return (
      <div className="sl sl-word">
        <span className="s-eye">Từ mới {sl.i + 1}/{sl.n}</span>
        <div className="s-wrow">
          <span className="s-hz s-huge">{w.hz}</span>
          {r >= 1 && <div className="s-wmeta fade"><Py w={w} className="s-py" /><span className="s-hv">{w.hv}</span><span className="s-vi">{w.vi}</span></div>}
        </div>
        {r >= 2 && <div className="s-ex fade"><span className="s-hz">{plainHz(w.ex)}</span><span className="py">{w.exPy}</span><span>{w.exVi}</span></div>}
      </div>
    );
  }
  if (sl.kind === 'tip') return (
    <div className="sl sl-tip"><span className="s-eye">Mẹo cho người Việt {sl.i + 1}/{sl.n}</span><p className="s-tip">{sl.t}</p></div>
  );
  if (sl.kind === 'grammar') {
    const g = sl.g;
    return (
      <div className="sl sl-gram">
        <span className="s-eye">Ngữ pháp {sl.gi + 1}/{sl.n}</span>
        <span className="s-h">{g.title}</span>
        <div className="s-formula">{g.formula.map((f, i) => <span key={i} className={i === g.key ? 'k' : ''}>{f}</span>)}</div>
        <div className="s-exs">
          {g.ex.slice(0, Math.max(0, r)).map((e, i) => <div key={i} className="s-gex fade"><span className="s-hz">{e[0]}</span><span className="py">{e[1]}</span><span>{e[2]}</span></div>)}
        </div>
        {r > g.ex.length && <p className="s-note fade">{g.note}</p>}
      </div>
    );
  }
  if (sl.kind === 'dialog') {
    // chỉ hiện tối đa 4 câu gần nhất cho vừa màn chiếu
    const n = Math.min(Math.max(0, r), sl.d.lines.length), from = Math.max(0, n - 4);
    return (
      <div className="sl sl-dlg">
        <span className="s-eye">Hội thoại {sl.di + 1}</span>
        <span className="s-h">{sl.d.title}</span>
        <div className="s-lines">
          {sl.d.lines.slice(from, n).map((x, k) => (
            <div key={from + k} className="s-line fade">
              <span className={`s-who ${whoTone(x[0])}`}>{[...x[0]][0]}</span>
              <div><span className="s-hz">{x[1]}</span><span className="py">{x[2]}</span><span>{x[3]}</span></div>
            </div>
          ))}
        </div>
      </div>
    );
  }
  return (
    <div className="sl sl-outro">
      <span className="s-eye">Tổng kết bài {l.no}</span>
      <span className="s-h">{l.title}</span>
      <div className="s-chips">{l.words.map(w => <span key={w.id}><b className="s-hz">{w.hz}</b> {w.vi}</span>)}</div>
      <p className="s-tip" style={{ fontSize: '2cqw' }}>{l.lecture.outro}</p>
    </div>
  );
}

export function LecturePlayer({ lesson, renderMode = false, startStep = 0, slide = null }) {
  const { slides, steps } = useMemo(() => buildLecture(lesson), [lesson]);
  const N = steps.length;
  const [i, setI] = useState(() => (renderMode ? Math.max(0, Math.min(+startStep || 0, N - 1)) : 0));
  const [playing, setPlaying] = useState(false);
  const [rate, setRate] = useState(1);
  const [subs, setSubs] = useState(true);
  const [nonce, setNonce] = useState(0); // tăng để phát lại bước hiện tại (tua về đúng chỗ đang đứng)
  const tok = useRef(0);
  const box = useRef(null);
  const toast = useToast();

  // đổi bài thì về đầu
  useEffect(() => { if (!renderMode) { setI(0); setPlaying(false); } }, [lesson.id, renderMode]);
  // ở renderMode luôn bám theo startStep
  useEffect(() => { if (renderMode) setI(Math.max(0, Math.min(+startStep || 0, N - 1))); }, [renderMode, startStep, N]);

  // Phát bước i khi đang chạy; dừng/tua/đổi tốc độ/unmount thì token đổi và giọng tắt
  useEffect(() => {
    if (!playing || renderMode || i >= N) return;
    const t = ++tok.current;
    stopVoice();
    const parts = stepParts(steps[i]);
    const next = k => {
      if (t !== tok.current) return;
      if (k >= parts.length) {
        if (i + 1 >= N) { setPlaying(false); setI(N); markPart(lesson.id, 0); activity(); toast('Đã xem hết bài giảng'); }
        else setI(i + 1);
        return;
      }
      const p = parts[k];
      playClip(p.lang, p.text, rate, () => setTimeout(() => next(k + 1), (p.lang === 'zh' ? 450 : 250) / rate));
    };
    const start = setTimeout(() => next(0), 90);
    return () => { clearTimeout(start); tok.current++; stopVoice(); };
  }, [playing, i, rate, nonce, renderMode, N, steps, lesson.id, toast]);

  if (!N) return null;
  const ended = !renderMode && i >= N;
  const step = steps[Math.min(i, N - 1)];
  const chapters = slides.map((x, k) => (x.ch ? [x.ch, k] : null)).filter(Boolean);
  const cur = chapters.filter(c => c[1] <= step.s).pop();
  const whole = renderMode && slide != null ? slides[Math.max(0, Math.min(+slide || 0, slides.length - 1))] : null;

  const seekSlide = s => { const k = steps.findIndex(x => x.s === s); if (k >= 0) { setI(k); setNonce(n => n + 1); } };
  const toggle = () => {
    if (playing) setPlaying(false);
    else { if (i >= N) setI(0); setPlaying(true); }
  };
  const prev = () => { const first = steps.findIndex(x => x.s === step.s); seekSlide(i > first + 1 ? step.s : Math.max(0, step.s - 1)); };
  const next = () => { if (step.s + 1 < slides.length) seekSlide(step.s + 1); };
  const full = () => {
    if (document.fullscreenElement) document.exitFullscreen();
    else if (box.current?.requestFullscreen) box.current.requestFullscreen().catch(() => toast('Không mở được toàn màn hình'));
    else toast('Không mở được toàn màn hình');
  };

  return (
    <section className={`lec${renderMode ? ' lec--render' : ''}`} ref={box}>
      <div className="stage" aria-live="off">
        <Slide key={whole ? `w${slide}` : step.s} sl={whole || slides[step.s]} r={whole || ended ? 99 : step.reveal} l={lesson} />
        {subs && !ended && !whole && <div className={`s-sub${step.lang === 'zh' ? ' zh' : ''}`}>{step.text}</div>}
        {!playing && !renderMode && (
          <button type="button" className="s-cover" onClick={toggle} aria-label={ended ? 'Xem lại' : 'Phát bài giảng'}>
            <span><Icon name={ended ? 'loop' : 'play'} /></span>
          </button>
        )}
      </div>
      {!renderMode && (
        <div className="lec-bar">
          <IconButton icon="back" label="Phần trước" onClick={prev} />
          <IconButton icon={playing ? 'pause' : 'play'} label={playing ? 'Tạm dừng' : 'Phát'} className="lec-main" size={52} onClick={toggle} />
          <IconButton icon="chev" label="Phần sau" onClick={next} />
          <div className="lec-prog">
            <ProgressBar value={Math.min(1, i / N)} label="Tiến độ bài giảng" />
            <span className="ui-muted ui-num" style={{ fontSize: 12, whiteSpace: 'nowrap' }}>Trang {step.s + 1}/{slides.length}</span>
          </div>
          <div className="ui-row" style={{ gap: 6, flexWrap: 'wrap' }}>
            {chapters.map(([c, k]) => <Chip key={k} active={cur && cur[1] === k} onClick={() => seekSlide(k)}>{c}</Chip>)}
          </div>
          <div className="ui-row" style={{ gap: 6, marginLeft: 'auto' }}>
            <label className="ui-sr" htmlFor="lec-rate">Tốc độ</label>
            <select id="lec-rate" className="ui-chip lec-rate" value={rate} onChange={e => setRate(+e.target.value)}>
              {RATES.map(v => <option key={v} value={v}>{v}×</option>)}
            </select>
            <Chip active={subs} onClick={() => setSubs(v => !v)}>Phụ đề</Chip>
            <IconButton icon="full" label="Toàn màn hình" onClick={full} />
          </div>
        </div>
      )}
    </section>
  );
}
