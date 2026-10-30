// Video bài giảng: trình phát lớn ở trên kèm bộ nút (câu trước/sau, tốc độ, lặp câu, nhảy theo phần và theo slide),
// danh sách bài chia theo cấp bên dưới.
// Video đã đăng YouTube (src/data/youtube.json: tên file → mã video) phát qua YouTube IFrame API;
// bài chưa có mã thì phát file mp4 trong public/video (index.json là danh sách file).
// Mốc thời gian từng bước đọc lấy từ src/data/video-timing.json (tools/make_video.py ghi ra).
import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Breadcrumbs, Button, Row, Stack } from '@trang/ui';
import { LESSONS, LEVELS } from '../core/data.js';
import { buildLecture } from '../core/lecture.js';
import YT_IDS from '../data/youtube.json';
import TIMING from '../data/video-timing.json';
import { Hz } from '../components/Hanzi.jsx';
import './VideosView.css';

const BASE = import.meta.env.BASE_URL;
const LIST = LESSONS.slice().sort((a, b) => a.lv - b.lv || a.no - b.no);
const LVS = [...new Set(LIST.map(l => l.lv))];
const file = l => `bai-giang-cap${l.lv}-bai${String(l.no).padStart(2, '0')}.mp4`;
const RATES = [0.75, 1, 1.25, 1.5];
const fmt = t => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, '0')}`;

let ytReady;
/** Nạp YouTube IFrame API một lần */
const loadYT = () => ytReady || (ytReady = new Promise(res => {
  if (window.YT?.Player) return res(window.YT);
  const prev = window.onYouTubeIframeAPIReady;
  window.onYouTubeIframeAPIReady = () => { prev?.(); res(window.YT); };
  const s = document.createElement('script'); s.src = 'https://www.youtube.com/iframe_api'; document.head.append(s);
}));

/** Tên ngắn của một slide bài giảng để làm nút */
function slideLabel(sl) {
  switch (sl.kind) {
    case 'title': return 'Mở đầu';
    case 'word': return sl.w.hz;
    case 'tip': return `Mẹo ${sl.i + 1}`;
    case 'grammar': return sl.g.title;
    case 'dialog': return sl.d.title;
    default: return 'Tổng kết';
  }
}

/** Trình phát (YouTube hoặc mp4) và bộ nút điều khiển của một bài */
function Player({ lesson, yt, src, autoplay, onEnded }) {
  const box = useRef(null), p = useRef(null), loopRef = useRef(null), ended = useRef(onEnded);
  ended.current = onEnded;
  const [t, setT] = useState(0), [dur, setDur] = useState(0), [playing, setPlaying] = useState(false);
  const [rate, setRate] = useState(1), [loop, setLoop] = useState(null), [ready, setReady] = useState(false);
  loopRef.current = loop;

  const { slides, steps } = useMemo(() => buildLecture(lesson), [lesson]);
  const starts = TIMING[lesson.id];
  const timed = !!starts && starts.length === steps.length;
  const slideAt = useMemo(() => {             // giây bắt đầu của mỗi slide = bước đầu tiên của slide đó
    const a = []; if (timed) steps.forEach((st, i) => { if (a[st.s] == null) a[st.s] = starts[i]; }); return a;
  }, [steps, starts, timed]);
  const sections = useMemo(() => slides.reduce((a, sl, i) => (sl.ch ? [...a, { name: sl.ch, from: i }] : a), []), [slides]);

  // gắn trình phát; bọc về chung một giao diện { time, seek, rate, play, pause, duration }
  useEffect(() => {
    let dead = false, yp = null, v = null;
    const host = box.current;
    if (yt) {
      const div = document.createElement('div'); host.append(div);
      loadYT().then(YT => {
        if (dead) return;
        yp = new YT.Player(div, {
          videoId: yt, host: 'https://www.youtube-nocookie.com',
          playerVars: { rel: 0, playsinline: 1, autoplay: autoplay ? 1 : 0, modestbranding: 1 },
          events: {
            onReady: () => {
              p.current = { time: () => yp.getCurrentTime(), seek: s => yp.seekTo(s, true), rate: r => yp.setPlaybackRate(r),
                play: () => yp.playVideo(), pause: () => yp.pauseVideo(), duration: () => yp.getDuration() };
              setReady(true);
            },
            onStateChange: e => { setPlaying(e.data === 1); if (e.data === 0) ended.current(); },
          },
        });
      });
    } else {
      v = document.createElement('video');
      Object.assign(v, { src, preload: 'metadata', playsInline: true, controls: true });
      v.onplay = () => setPlaying(true); v.onpause = () => setPlaying(false); v.onended = () => ended.current();
      host.append(v);
      p.current = { time: () => v.currentTime, seek: s => { v.currentTime = s; }, rate: r => { v.playbackRate = r; },
        play: () => v.play().catch(() => {}), pause: () => v.pause(), duration: () => v.duration || 0 };
      setReady(true);
      if (autoplay) v.play().catch(() => {});
    }
    return () => { dead = true; p.current = null; yp?.destroy(); v?.pause(); host.replaceChildren(); };
  }, [yt, src]); // eslint-disable-line react-hooks/exhaustive-deps

  // cập nhật thời gian 4 lần/giây; lặp câu khi hết đoạn
  useEffect(() => {
    const id = setInterval(() => {
      const pl = p.current; if (!pl) return;
      const now = pl.time() || 0, lp = loopRef.current;
      if (lp && now >= lp[1]) pl.seek(lp[0]);
      setT(now); setDur(pl.duration() || 0);
    }, 250);
    return () => clearInterval(id);
  }, []);

  const step = timed ? Math.max(0, starts.findLastIndex(s => s <= t + 0.05)) : -1;
  const slide = step >= 0 ? steps[step].s : -1;
  const sec = sections.findLastIndex(x => x.from <= Math.max(slide, 0));
  const secEnd = sections[sec + 1]?.from ?? slides.length;
  const go = s => { const pl = p.current; if (!pl) return; setLoop(null); pl.seek(s); pl.play(); };
  const stepEnd = i => starts[i + 1] ?? dur;
  const toggleLoop = () => setLoop(lp => (lp || step < 0 ? null : [starts[step], stepEnd(step)]));
  const pickRate = r => { setRate(r); p.current?.rate(r); };

  return (
    <>
      <div ref={box} className="vd-video vd-frame" />
      <div className="vd-ctrls" aria-label="Điều khiển video">
        <Row gap={6} wrap>
          <Button variant="primary" disabled={!ready} onClick={() => (playing ? p.current.pause() : p.current.play())}>{playing ? 'Dừng' : 'Phát'}</Button>
          {timed && <>
            <Button disabled={!ready} onClick={() => go(starts[Math.max(0, t - starts[step] > 1.5 ? step : step - 1)])}>Câu trước</Button>
            <Button disabled={!ready || step >= starts.length - 1} onClick={() => go(starts[step + 1])}>Câu sau</Button>
            <Button className={loop ? 'is-on' : ''} aria-pressed={!!loop} disabled={!ready} onClick={toggleLoop}>Lặp câu</Button>
          </>}
          <span className="vd-rates" role="group" aria-label="Tốc độ">
            {RATES.map(r => <button key={r} type="button" className={`vd-chip${r === rate ? ' is-on' : ''}`} aria-pressed={r === rate} onClick={() => pickRate(r)}>{r}×</button>)}
          </span>
          <span className="vd-time ui-num">{fmt(t)}{dur ? ` / ${fmt(dur)}` : ''}</span>
        </Row>
        {timed && <>
          <div className="vd-secs" role="group" aria-label="Phần của bài">
            {sections.map((x, i) => (
              <button key={x.from} type="button" className={`vd-chip${i === sec ? ' is-on' : ''}`} onClick={() => go(slideAt[x.from])}>{x.name}</button>
            ))}
          </div>
          <div className="vd-slides" role="group" aria-label="Slide trong phần này">
            {slides.slice(sections[sec]?.from ?? 0, secEnd).map((sl, k) => {
              const i = (sections[sec]?.from ?? 0) + k;
              return <button key={i} type="button" className={`vd-slide${i === slide ? ' is-on' : ''}`} aria-current={i === slide ? 'true' : undefined}
                onClick={() => go(slideAt[i])}>{slideLabel(sl)}</button>;
            })}
          </div>
        </>}
      </div>
    </>
  );
}

export function VideosView() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [have, setHave] = useState(null); // null = đang tải danh sách
  const autoplay = useRef(false);

  useEffect(() => {
    let on = true;
    fetch(`${BASE}video/index.json`).then(r => (r.ok ? r.json() : [])).catch(() => [])
      .then(a => { if (on) setHave(new Set(Array.isArray(a) ? a : [])); });
    return () => { on = false; };
  }, []);

  const found = LIST.findIndex(l => l.id === id);
  const cur = found >= 0 ? found : 0;
  const l = LIST[cur];
  const yt = l && YT_IDS[file(l)];
  const ok = !!yt || !!have?.has(file(l));

  const show = useCallback((i, scroll) => {
    autoplay.current = true;
    navigate(`/videos/${LIST[i].id}`, { replace: true });
    if (scroll) window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [navigate]);
  const next = useCallback(() => { if (cur < LIST.length - 1) show(cur + 1); }, [cur, show]);
  useEffect(() => { autoplay.current = false; }, [cur]);

  if (!l) return <p className="ui-muted">Chưa có bài học nào.</p>;
  return (
    <>
      <Breadcrumbs LinkComponent={Link} items={[{ label: 'Lộ trình', to: '/' }, { label: 'Video bài giảng' }]} />
      <section className="vd-player" aria-label="Trình phát">
        {ok
          ? <Player key={l.id} lesson={l} yt={yt} src={`${BASE}video/${file(l)}`} autoplay={autoplay.current} onEnded={next} />
          : !have && <div className="vd-video" aria-hidden="true" />}
        <Row between align="baseline" gap={12}>
          <Stack gap={2}>
            <span className="ui-eyebrow">Cấp {l.lv} · Bài {l.no}</span>
            <h1 style={{ fontSize: 24 }}>{l.title} <Hz className="ui-muted">{l.zh}</Hz></h1>
          </Stack>
          <Row gap={8}>
            <Button disabled={cur === 0} onClick={() => show(cur - 1)}>Bài trước</Button>
            <Button variant="primary" disabled={cur === LIST.length - 1} onClick={() => show(cur + 1)}>Bài sau</Button>
            <Button as={Link} to={`/lesson/${l.id}`}>Học bài này</Button>
          </Row>
        </Row>
        {have && !ok && <p className="vd-empty">Video bài này chưa được dựng. Chạy <code>tools/make_video.py</code> để tạo.</p>}
      </section>
      {LVS.map(lv => (
        <section key={lv} className="vd-lv">
          <h2 style={{ fontSize: 18 }}>Cấp {lv} {LEVELS[lv]?.book && <span className="ui-eyebrow" style={{ marginLeft: 6 }}>{LEVELS[lv].book}</span>}</h2>
          <div className="vd-list">
            {LIST.map((x, i) => {
              if (x.lv !== lv) return null;
              const has = !!YT_IDS[file(x)] || !!have?.has(file(x));
              return (
                <button key={x.id} type="button" className={`vd-item${i === cur ? ' is-on' : ''}${has ? '' : ' is-missing'}`}
                  aria-current={i === cur ? 'true' : undefined} onClick={() => show(i, true)}>
                  <span className="vd-no ui-num">{x.no}</span>
                  <span className="vd-t"><b>{x.title}</b><span className="ui-hz">{x.zh}</span>{!has && have && <small>Chưa có video</small>}</span>
                </button>
              );
            })}
          </div>
        </section>
      ))}
    </>
  );
}
