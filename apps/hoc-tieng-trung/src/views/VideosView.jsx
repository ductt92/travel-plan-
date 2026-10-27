// Video bài giảng: trình phát lớn ở trên, danh sách bài chia theo cấp bên dưới.
// Danh sách file có sẵn đọc từ public/video/index.json (mảng tên file mp4).
import { useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Breadcrumbs, Button, Row, Stack } from '@trang/ui';
import { LESSONS, LEVELS } from '../core/data.js';
import { Hz } from '../components/Hanzi.jsx';
import './VideosView.css';

const BASE = import.meta.env.BASE_URL;
const LIST = LESSONS.slice().sort((a, b) => a.lv - b.lv || a.no - b.no);
const LVS = [...new Set(LIST.map(l => l.lv))];
const file = l => `bai-giang-cap${l.lv}-bai${String(l.no).padStart(2, '0')}.mp4`;

export function VideosView() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [have, setHave] = useState(null); // null = đang tải danh sách
  const video = useRef(null);
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
  const ok = !!have?.has(file(l));

  // đổi bài: phát luôn nếu người dùng vừa chọn
  useEffect(() => {
    const v = video.current;
    if (v && ok && autoplay.current) v.play().catch(() => {});
    autoplay.current = false;
  }, [cur, ok]);

  const show = (i, scroll) => {
    autoplay.current = true;
    navigate(`/videos/${LIST[i].id}`, { replace: true });
    if (scroll) window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (!l) return <p className="ui-muted">Chưa có bài học nào.</p>;
  return (
    <>
      <Breadcrumbs LinkComponent={Link} items={[{ label: 'Lộ trình', to: '/' }, { label: 'Video bài giảng' }]} />
      <section className="vd-player" aria-label="Trình phát">
        {ok
          ? <video ref={video} className="vd-video" src={`${BASE}video/${file(l)}`} controls preload="metadata" playsInline
              onEnded={() => { if (cur < LIST.length - 1) show(cur + 1); }} />
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
              const has = !!have?.has(file(x));
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
