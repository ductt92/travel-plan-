// Ôn tập: thẻ ghi nhớ, lặp lại ngắt quãng (khóa thẻ = id từ)
import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, EmptyState, Kbd, Pill, ProgressBar, Row, Stack } from '@trang/ui';
import { LEVELS, WMAP } from '../core/data.js';
import { plainHz, shuffle } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { useStore, update, activity, dueCards, schedule, fmtWait, nextLesson } from '../core/store.js';
import { Hz, Py, Hv } from '../components/Hanzi.jsx';
import './ReviewView.css';

const RATES = [[1, 'Quên'], [2, 'Khó'], [3, 'Nhớ'], [4, 'Dễ']];
const fresh = (S, extra) => ({ queue: extra ? shuffle(Object.keys(S.cards)).slice(0, 20) : dueCards(), flipped: false, done: 0, extra });

export function ReviewView() {
  const S = useStore();
  const [RV, setRV] = useState(() => fresh(S, false));
  const total = Object.keys(S.cards).length;
  const key = RV.queue[0];

  const flip = () => {
    if (!RV.flipped) say(key); // lật sang mặt sau thì đọc chữ
    setRV(r => ({ ...r, flipped: !r.flipped }));
  };
  const rate = r => {
    const k = RV.queue[0];
    update(s => { s.cards[k] = schedule(s.cards[k], r); });
    activity();
    // chấm Quên/Khó thì thẻ quay lại cuối hàng (trừ khi đang ôn thêm)
    setRV(v => {
      const q = v.queue.slice(1);
      if (r <= 2 && !v.extra) return { ...v, queue: [...q, k], flipped: false };
      return { ...v, queue: q, flipped: false, done: v.done + 1 };
    });
  };

  // Phím tắt: Space lật, 1–4 chấm, R nghe lại
  const live = useRef(); live.current = { RV, flip, rate };
  useEffect(() => {
    const onKey = e => {
      if (e.target.closest?.('input,textarea,select')) return;
      if ((e.code === 'Space' || e.key === 'Enter') && e.target.closest?.('button,a')) return;
      const { RV, flip, rate } = live.current;
      if (!RV.queue.length || e.metaKey || e.ctrlKey || e.altKey) return;
      if (e.code === 'Space') { e.preventDefault(); flip(); }
      else if (RV.flipped && e.key.length === 1 && '1234'.includes(e.key)) rate(+e.key);
      else if (e.key === 'r' || e.key === 'R') say(RV.queue[0]);
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, []);

  if (!total) {
    const nl = nextLesson();
    return (
      <EmptyState glyph="卡" title="Chưa có thẻ nào để ôn"
        actions={<Button as={Link} variant="primary" to={nl?.l ? `/lesson/${nl.l.id}` : '/level/1'}>Học bài mới</Button>}>
        <p className="ui-muted" style={{ maxWidth: '48ch' }}>Thẻ được tạo khi bạn học xong phần Từ mới của một bài. Hệ thống sẽ hẹn lịch ôn: từ hay quên sẽ quay lại sớm hơn.</p>
      </EmptyState>
    );
  }
  if (!key || !S.cards[key]) {
    const now = Date.now();
    const next = Object.values(S.cards).map(c => c.due).filter(d => d > now).sort((a, b) => a - b)[0];
    return (
      <EmptyState glyph="好" glyphColor="var(--jade)" title={RV.done ? `Đã ôn xong ${RV.done} thẻ` : 'Không có thẻ đến hạn'}
        actions={<>
          <Button onClick={() => setRV(fresh(S, true))}>Ôn thêm 20 thẻ ngẫu nhiên</Button>
          <Button as={Link} variant="primary" to="/">Về lộ trình</Button>
        </>}>
        <p className="ui-muted">{next ? `Thẻ tiếp theo đến hạn sau ${fmtWait(next - now)}.` : ''} Bạn có {total} thẻ trong bộ ôn tập.</p>
      </EmptyState>
    );
  }

  const w = WMAP[key], c = S.cards[key];
  // Đếm thẻ trong hàng: mới, học lại (khoảng < 1 ngày), ôn
  const cnt = { neu: 0, re: 0, rv: 0 };
  RV.queue.forEach(k => { const x = S.cards[k]; if (!x) return; if (x.reps === 0 && !x.lapses) cnt.neu++; else if (x.ivl < 1) cnt.re++; else cnt.rv++; });
  const all = RV.done + RV.queue.length;

  return (
    <div className="fc-wrap">
      <Row between>
        <Stack gap={2}><span className="ui-eyebrow">{RV.extra ? 'Ôn thêm' : 'Ôn tập hôm nay'}</span><h1 style={{ fontSize: 22 }}>Thẻ ghi nhớ</h1></Stack>
        <Row gap={6} style={{ fontSize: 13 }}>
          <Pill tone="jade" className="ui-num">Mới {cnt.neu}</Pill>
          <Pill tone="seal" className="ui-num">Học lại {cnt.re}</Pill>
          <Pill tone="grey" className="ui-num">Ôn {cnt.rv}</Pill>
        </Row>
      </Row>
      <Row gap={10}>
        <ProgressBar value={RV.done / all} label="Tiến độ ôn tập" />
        <span className="ui-muted ui-num" style={{ fontSize: 13 }}>{RV.done}/{all}</span>
      </Row>
      <button type="button" className={`flip ${RV.flipped ? 'on' : ''}`} onClick={flip} aria-label={RV.flipped ? 'Mặt sau thẻ' : `Lật thẻ ${w.hz}`}>
        <div className="flip-in">
          <div className="face" aria-hidden={RV.flipped}>
            <span className="ui-eyebrow corner">{LEVELS[w.lv].name} · Bài {w.lesson.split('-')[1]}</span>
            <span className="big">{w.hz}</span>
            <span className="ui-muted" style={{ fontSize: 14 }}>Bạn có nhớ pinyin và nghĩa? Chạm để lật</span>
          </div>
          <div className="face back" aria-hidden={!RV.flipped}>
            <Hz size={56} style={{ lineHeight: 1.1 }}>{w.hz}</Hz>
            <span style={{ fontSize: 28, fontWeight: 500 }}><Py w={w} /></span>
            <Hv style={{ fontSize: 13 }}>{w.hv}</Hv>
            <b style={{ fontSize: 22 }}>{w.vi}</b>
            <div className="ex" style={{ width: '100%', maxWidth: 520, textAlign: 'left' }}>
              <Hz>{plainHz(w.ex)}</Hz><span className="ui-py">{w.exPy}</span><span>{w.exVi}</span>
            </div>
          </div>
        </div>
      </button>
      <Row gap={10} style={{ justifyContent: 'center' }}>
        <Button icon="sound" onClick={() => say(w.hz)}>Nghe</Button>
        {!RV.flipped && <Button variant="primary" icon="flip" onClick={flip}>Lật thẻ</Button>}
      </Row>
      {RV.flipped && (
        <div className="rates" role="group" aria-label="Bạn nhớ từ này đến mức nào?">
          {RATES.map(([r, t]) => (
            <button key={r} type="button" className={`rate r${r}`} onClick={() => rate(r)}>
              {t}<small>{fmtWait(schedule(c, r).due - Date.now())}</small>
            </button>
          ))}
        </div>
      )}
      <p className="ui-muted" style={{ fontSize: 13, textAlign: 'center', display: 'flex', flexWrap: 'wrap', gap: 6, justifyContent: 'center', alignItems: 'center' }}>
        Phím tắt: <Kbd>Space</Kbd> lật thẻ · <Kbd>1</Kbd>–<Kbd>4</Kbd> chấm mức nhớ · <Kbd>R</Kbd> nghe lại
      </p>
    </div>
  );
}
