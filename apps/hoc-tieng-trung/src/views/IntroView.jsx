// Cấp 0 · Nhập môn: thanh điệu, luyện tai, biến điệu, thanh mẫu, vận mẫu, nét cơ bản.
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Breadcrumbs, Button, Card, Icon, LinkButton, Row, Stack, useToast } from '@trang/ui';
import { TONES, TONE_GAME, INITIALS, FINALS, STROKES } from '../core/data.js';
import { toneOf, bareSyl, markSyl, pickOne } from '../core/pinyin.js';
import { say } from '../core/speech.js';
import { useStore, update, activity } from '../core/store.js';
import './IntroView.css';

/** Hình đường đi của thanh điệu (thanh nhẹ là một chấm) */
function Contour({ t }) {
  return (
    <svg viewBox="0 0 72 48" aria-hidden="true">
      <path d="M2 6H70M2 42H70" stroke="var(--line)" strokeWidth="1" fill="none" />
      {t.pts
        ? <polyline points={t.pts} fill="none" stroke={`var(--t${t.t})`} strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
        : <circle cx="36" cy="26" r="5" fill="var(--t5)" />}
    </svg>
  );
}

/** Trò "Nghe và chọn thanh điệu" */
function ToneGame() {
  const [g, setG] = useState(() => ({ item: pickOne(TONE_GAME), answered: false, picked: 0, right: 0, total: 0 }));
  const [ch, py] = g.item, tt = toneOf(py);
  const pick = t => { setG(s => ({ ...s, answered: true, picked: t, total: s.total + 1, right: s.right + (t === tt ? 1 : 0) })); activity(); };
  const next = () => {
    const item = pickOne(TONE_GAME);
    setG(s => ({ ...s, item, answered: false, picked: 0 }));
    setTimeout(() => say(item[0], 0.75), 150);
  };
  const ok = g.picked === tt;
  return (
    <Card as="section" className="ui-stack" style={{ gap: 18 }} aria-labelledby="h-tg">
      <Row between>
        <Stack gap={4}><span className="ui-eyebrow">Luyện tai</span><h2 id="h-tg" style={{ fontSize: 20 }}>Nghe và chọn thanh điệu</h2></Stack>
        <span className="ui-muted ui-num">Đúng {g.right}/{g.total}</span>
      </Row>
      <button type="button" className="l0-play" aria-label="Nghe âm" onClick={() => say(ch, 0.75)}><Icon name="sound" size={38} /></button>
      <div className="l0-opts">
        {[1, 2, 3, 4].map(t => {
          const cls = g.answered ? (t === tt ? ' is-right' : t === g.picked ? ' is-wrong' : '') : '';
          return (
            <button key={t} type="button" className={`l0-opt${cls}`} disabled={g.answered} onClick={() => pick(t)}>
              <span className={`ui-py t${t}`} style={{ fontSize: 24 }}>{markSyl(bareSyl(py), t)}</span>
              <span style={{ fontSize: 13 }} className="ui-muted">Thanh {t}</span>
            </button>
          );
        })}
      </div>
      {g.answered && (
        <div className={`l0-fb ${ok ? 'is-ok' : 'is-no'}`} role="status">
          <h3>{ok ? 'Chính xác!' : 'Chưa đúng'}</h3>
          <p><span className="ui-hz" style={{ fontSize: 22 }}>{ch}</span> đọc là <span className={`ui-py t${tt}`} style={{ fontWeight: 600 }}>{py}</span>, thanh {tt}.</p>
          <Button variant="primary" onClick={next} style={{ alignSelf: 'flex-start' }}>Âm tiếp theo</Button>
        </div>
      )}
    </Card>
  );
}

/** Nút nghe một ví dụ biến điệu */
function SayEx({ hz, size = 22, children }) {
  return (
    <LinkButton onClick={() => say(hz)} style={{ alignSelf: 'flex-start', fontSize: 15 }}>
      <span className="ui-hz" style={{ fontSize: size, color: 'var(--ink)' }}>{hz}</span> <span className="ui-py">{children}</span>
    </LinkButton>
  );
}

export function IntroView() {
  const S = useStore();
  const toast = useToast();
  const nav = useNavigate();
  const finish = () => { update(s => { s.l0 = true; }); activity(); toast('Đã hoàn thành Nhập môn'); nav('/level/1'); };

  return (
    <>
      <Breadcrumbs LinkComponent={Link} items={[{ label: 'Lộ trình', to: '/' }, { label: 'Sơ cấp' }, { label: 'Cấp 0 · Nhập môn' }]} />
      <Stack as="header" gap={8}>
        <span className="ui-eyebrow">Cấp 0 · Nhập môn 入门</span>
        <h1 style={{ fontSize: 30 }}>Pinyin, thanh điệu và nét chữ</h1>
        <Button variant="soft" icon="grid" as={Link} to="/pinyin" style={{ alignSelf: 'flex-start' }}>Mở bảng pinyin đầy đủ</Button>
        <p className="ui-muted" style={{ maxWidth: '64ch' }}>Tiếng Trung có 4 thanh điệu và một thanh nhẹ. Cùng âm “ma” mà khác thanh là khác nghĩa hoàn toàn. Bấm vào từng thẻ để nghe.</p>
      </Stack>

      <Stack as="section" aria-labelledby="h-tone">
        <h2 id="h-tone" style={{ fontSize: 20 }}>Bốn thanh điệu và thanh nhẹ</h2>
        <div className="l0-tones">
          {TONES.map(t => (
            <button key={t.t} type="button" className="l0-tone" onClick={() => say(t.ex)}>
              <Contour t={t} />
              <b className={`t${t.t}`}>{t.name}</b>
              <span className="ui-muted" style={{ fontSize: 13 }}>{t.how}</span>
              <span><span className="ui-hz" style={{ fontSize: 26 }}>{t.ex}</span> <span className={`ui-py t${t.t}`} style={{ fontSize: 17 }}>{t.py}</span></span>
            </button>
          ))}
        </div>
      </Stack>

      <ToneGame />

      <Stack as="section" aria-labelledby="h-bd">
        <h2 id="h-bd" style={{ fontSize: 20 }}>Ba quy tắc biến điệu</h2>
        <div className="l0-rules">
          <Card className="ui-stack" style={{ gap: 8 }}>
            <b>Hai thanh 3 liền nhau</b>
            <p className="ui-muted" style={{ fontSize: 14 }}>Thanh 3 đầu đọc thành thanh 2.</p>
            <SayEx hz="你好">nǐ hǎo → <span className="t2">ní</span> hǎo</SayEx>
          </Card>
          <Card className="ui-stack" style={{ gap: 8 }}>
            <b>不 trước thanh 4</b>
            <p className="ui-muted" style={{ fontSize: 14 }}>不 bù đọc thành bú.</p>
            <SayEx hz="不是">bù shì → <span className="t2">bú</span> shì</SayEx>
          </Card>
          <Card className="ui-stack" style={{ gap: 8 }}>
            <b>Biến điệu của 一</b>
            <p className="ui-muted" style={{ fontSize: 14 }}>Trước thanh 4 đọc yí, trước thanh 1/2/3 đọc yì, đếm số giữ yī.</p>
            <Row gap={6}>
              <SayEx hz="一个" size={20}><span className="t2">yí</span> ge</SayEx>
              <SayEx hz="一天" size={20}><span className="t4">yì</span> tiān</SayEx>
            </Row>
          </Card>
        </div>
      </Stack>

      <Stack as="section" aria-labelledby="h-tm">
        <h2 id="h-tm" style={{ fontSize: 20 }}>21 thanh mẫu (phụ âm đầu)</h2>
        <div className="l0-inits">
          {INITIALS.map(g => (
            <div key={g.g} className="l0-ini">
              <b>{g.g}</b>
              <div className="l0-keys">
                {g.k.map(([p, h]) => (
                  <button key={p} type="button" aria-label={`Nghe ${p}`} onClick={() => say(h)}><b>{p}</b><span>{h}</span></button>
                ))}
              </div>
              <p className="ui-muted" style={{ fontSize: 13 }}>{g.note}</p>
            </div>
          ))}
        </div>
      </Stack>

      <Card as="section" className="ui-stack" style={{ gap: 12 }} aria-labelledby="h-vm">
        <h2 id="h-vm" style={{ fontSize: 20 }}>Vận mẫu (phần vần)</h2>
        <div className="l0-finals">{FINALS.map(f => <span key={f}>{f}</span>)}</div>
        <p className="ui-muted" style={{ fontSize: 13 }}>Dấu thanh đặt trên a hoặc e nếu có; với “ou” đặt trên o; còn lại đặt trên nguyên âm cuối: guì, liù.</p>
      </Card>

      <Stack as="section" aria-labelledby="h-net">
        <h2 id="h-net" style={{ fontSize: 20 }}>8 nét cơ bản</h2>
        <div className="l0-strokes">
          {STROKES.map(s => (
            <div key={s[1]} className="l0-stroke">
              <span className="ui-hz">{s[0]}</span>
              <b>{s[3]} <span className="ui-hz ui-muted" style={{ fontSize: 14 }}>{s[1]} {s[2]}</span></b>
              <span className="ui-muted" style={{ fontSize: 13 }}>{s[4]}</span>
            </div>
          ))}
        </div>
        <p className="ui-muted" style={{ fontSize: 14 }}>Quy tắc viết: trên trước dưới sau, trái trước phải sau, ngang trước sổ sau, ngoài trước trong sau, đóng khung sau cùng. Xem từng chữ ở mục <Link to="/write">Tập viết</Link>.</p>
      </Stack>

      <Card className="ui-row" style={{ justifyContent: 'space-between', flexWrap: 'wrap', gap: 16 }}>
        <Stack gap={4}>
          <b>{S.l0 ? 'Bạn đã hoàn thành Nhập môn' : 'Đã nắm được thanh điệu và pinyin?'}</b>
          <span className="ui-muted" style={{ fontSize: 14 }}>{S.l0 ? 'Có thể quay lại luyện tai bất cứ lúc nào.' : 'Đánh dấu hoàn thành để chuyển sang Cấp 1.'}</span>
        </Stack>
        {S.l0
          ? <Button variant="primary" as={Link} to="/level/1">Sang Cấp 1</Button>
          : <Button variant="primary" onClick={finish}>Hoàn thành Nhập môn</Button>}
      </Card>
    </>
  );
}
