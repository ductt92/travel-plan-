// Màn hình Lộ trình: lời chào, học tiếp, ôn tập đến hạn, lộ trình 3 giai đoạn và tiến độ.
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, Icon, Pill, ProgressBar, Row, Stack, StatTile, useToast } from '@trang/ui';
import { LEVELS, STAGES, LESSONS, WMAP, NPARTS, prevOf, hasContent } from '../core/data.js';
import { fmtN } from '../core/pinyin.js';
import { SyncButton } from '@trang/sync';
import { useStore, nextLesson, dueCards, lessonDoneCount, lessonDone, levelStats, levelStatus, streak, resetAll } from '../core/store.js';
import './HomeView.css';

/** Thẻ "học tiếp": Nhập môn, bài tiếp theo, hoặc đã học hết */
function NextCard({ nl }) {
  if (!nl) return (
    <Card className="home-next">
      <span className="home-next__big">好</span>
      <Stack gap={12} style={{ flex: '1 1 240px' }}>
        <span className="ui-eyebrow">Hoàn thành nội dung hiện có</span>
        <h2 style={{ fontSize: 22 }}>Bạn đã học hết các bài đã soạn</h2>
        <p className="ui-muted">Làm bài kiểm tra cuối cấp hoặc ôn tập để giữ trí nhớ.</p>
      </Stack>
      <Button variant="primary" as={Link} to="/practice">Luyện tập</Button>
    </Card>
  );
  if (nl.kind === 'l0') return (
    <Card className="home-next">
      <span className="home-next__big">声</span>
      <Stack gap={12} style={{ flex: '1 1 260px', minWidth: 0 }}>
        <span className="ui-eyebrow">Bắt đầu · Cấp 0</span>
        <h2 style={{ fontSize: 24 }}>Pinyin và 4 thanh điệu</h2>
        <p className="ui-muted">Nền móng cho mọi cấp sau: nghe phân biệt thanh, thanh mẫu, vận mẫu, nét cơ bản.</p>
      </Stack>
      <Button variant="primary" as={Link} to="/l0">Bắt đầu học</Button>
    </Card>
  );
  const l = nl.l, d = lessonDoneCount(l.id);
  return (
    <Card className="home-next">
      <span className="home-next__big" aria-hidden="true">{[...l.zh][0]}</span>
      <Stack gap={8} style={{ flex: '1 1 260px', minWidth: 0 }}>
        <span className="ui-eyebrow">{d ? 'Học tiếp' : 'Bài tiếp theo'} · Cấp {l.lv} · Bài {l.no}</span>
        <h2 style={{ fontSize: 24 }}>{l.title} <span className="ui-hz ui-muted" style={{ fontSize: 20 }}>{l.zh}</span></h2>
        <p className="ui-muted">Bài giảng · {l.words.length} từ mới · {l.grammar.length} điểm ngữ pháp · 2 hội thoại</p>
        <Row gap={10}>
          <ProgressBar value={d / NPARTS} label="Tiến độ bài" />
          <span className="ui-muted ui-num" style={{ fontSize: 13 }}>{d}/{NPARTS} phần</span>
        </Row>
      </Stack>
      <Button variant="primary" as={Link} to={`/lesson/${l.id}`}>{d ? 'Học tiếp' : 'Bắt đầu'}</Button>
    </Card>
  );
}

/** Thẻ một cấp trong lộ trình */
function LevelCard({ n }) {
  const L = LEVELS[n], st = levelStatus(n), p = prevOf(n);
  const pill = {
    done: <Pill tone="jade">Hoàn thành</Pill>,
    active: <Pill tone="solid">Đang học</Pill>,
    test: <Pill tone="seal">Chờ kiểm tra</Pill>,
    open: <Pill tone="grey">Mở</Pill>,
    soon: <span className="ui-muted"><Icon name="lock" size={18} label="Đang soạn" /></span>
  }[st];
  const nums = n === 0 ? L.sub
    : L.book ? `+${fmtN(L.words - p.words)} từ · ${L.gram} điểm ngữ pháp · ${L.book}`
    : L.std ? `+${fmtN(L.newWords)} từ · ${L.gram} điểm ngữ pháp · chuẩn 2021`
    : `Khoảng ${fmtN(L.words)} từ · ${fmtN(L.chars)} chữ (chuẩn 2021)`;
  let foot = null;
  if (st === 'soon') foot = <span className="ui-muted" style={{ fontSize: 12, marginTop: 'auto' }}>Nội dung đang soạn</span>;
  else if (n > 0 && hasContent(n)) {
    const s = levelStats(n);
    foot = (
      <Row gap={10} style={{ marginTop: 'auto' }}>
        <ProgressBar value={s.total ? s.done / s.total : 0} label={`Tiến độ ${L.name}`} />
        <span className="ui-muted ui-num" style={{ fontSize: 12 }}>{s.done}/{s.total} bài</span>
      </Row>
    );
  }
  return (
    <Link className={`home-lvl${st === 'active' ? ' is-active' : ''}${st === 'soon' ? ' is-soon' : ''}`} to={n === 0 ? '/l0' : `/level/${n}`}>
      <Row between align="flex-start"><span className="home-lvl__n">{L.hz}</span>{pill}</Row>
      <b style={{ fontSize: 16 }}>{L.name}</b>
      <span className="ui-muted ui-num" style={{ fontSize: 13, lineHeight: 1.5 }}>{nums}</span>
      {foot}
    </Link>
  );
}

export function HomeView() {
  const S = useStore();
  const toast = useToast();
  const [ask, setAsk] = useState(false);
  const nl = nextLesson(), due = dueCards().length;
  const dateStr = new Date().toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'numeric' });
  const learned = Object.keys(S.cards);
  // Khóa thẻ là "bài:chữ" nên lấy chữ Hán qua WMAP
  const charSet = new Set(learned.flatMap(k => (WMAP[k] ? [...WMAP[k].hz] : [])));
  const acc = S.stats.ans ? Math.round(S.stats.ok / S.stats.ans * 100) + '%' : '–';
  const total = learned.length;

  const doReset = () => { resetAll(); setAsk(false); toast('Đã xóa tiến độ'); };

  return (
    <>
      <header className="ui-row" style={{ justifyContent: 'space-between', alignItems: 'flex-end', flexWrap: 'wrap', gap: 16 }}>
        <Stack gap={4}>
          <span className="ui-muted" style={{ fontSize: 13, textTransform: 'capitalize' }}>{dateStr}</span>
          <h1 style={{ fontSize: 30 }}>{nl && nl.kind === 'lesson' ? `Chào bạn, hôm nay học tiếp Cấp ${nl.l.lv} nhé` : 'Chào bạn, bắt đầu con đường Hán ngữ'}</h1>
        </Stack>
        <Row gap={8}>
          <Pill tone="grey" style={{ fontSize: 14, padding: '6px 12px' }}>
            <Icon name="flame" size={18} style={{ color: 'var(--seal)' }} />{streak()} ngày liên tiếp
          </Pill>
          <SyncButton />
        </Row>
      </header>

      <section className="ui-row" style={{ alignItems: 'stretch', gap: 20, flexWrap: 'wrap' }} aria-label="Hôm nay">
        <NextCard nl={nl} />
        <Card tone="dark" className="ui-stack" style={{ flex: '1 1 280px', minWidth: 0, gap: 12 }}>
          <span className="ui-eyebrow">Ôn tập đến hạn</span>
          <b style={{ fontSize: 40, lineHeight: 1 }} className="ui-num">{due} <span style={{ fontSize: 16, fontWeight: 500 }} className="ui-muted">thẻ</span></b>
          <span className="ui-muted" style={{ fontSize: 14 }}>
            {total ? (due ? `Khoảng ${Math.max(1, Math.round(due * 0.2))} phút. Ôn trước khi học bài mới để nhớ lâu hơn.` : 'Bạn đã ôn hết thẻ hôm nay.') : 'Học từ mới trong bài để tạo thẻ ôn tập.'}
          </span>
          <Button variant="light" as={Link} to="/review" style={{ alignSelf: 'flex-start' }}>{due ? 'Ôn ngay' : 'Mở ôn tập'}</Button>
        </Card>
      </section>

      <Stack as="section" gap={24} aria-labelledby="h-lt">
        <Row between style={{ alignItems: 'baseline' }}>
          <h2 id="h-lt" style={{ fontSize: 22 }}>Lộ trình HSK 3.0</h2>
          <span className="ui-muted" style={{ fontSize: 14 }}>3 giai đoạn · 9 cấp · 11.092 từ · 3.000 chữ Hán</span>
        </Row>
        {STAGES.map(s => (
          <Stack key={s.zh} gap={14}>
            <div className="home-stage">
              <span className="ui-hz">{s.zh}</span><b>{s.vi}</b>
              <span className="ui-muted" style={{ fontSize: 13 }}>{s.sub}</span>
            </div>
            <div className="home-grid">{s.levels.map(n => <LevelCard key={n} n={n} />)}</div>
          </Stack>
        ))}
      </Stack>

      <Stack as="section" gap={14} aria-labelledby="h-td">
        <h2 id="h-td" style={{ fontSize: 22 }}>Tiến độ của bạn</h2>
        <div className="home-tiles">
          <StatTile label="Từ đã học" value={total} sub="/ 11.092" />
          <StatTile label="Chữ Hán đã gặp" value={charSet.size} sub="/ 3.000" />
          <StatTile label="Độ chính xác luyện tập" value={acc} />
          <StatTile label="Bài đã hoàn thành" value={LESSONS.filter(l => lessonDone(l.id)).length} sub={`/ ${LESSONS.length} bài đã soạn`} />
        </div>
        <Row gap={10}>
          <span className="ui-muted" style={{ fontSize: 13 }}>Tiến độ lưu trên trình duyệt này.</span>
          <button type="button" className="ui-link" style={{ color: 'var(--seal)' }} onClick={() => setAsk(true)}>Xóa tiến độ</button>
          {ask && (
            <Row gap={8}>
              <span style={{ fontSize: 13 }}>Xóa toàn bộ tiến độ và thẻ ôn tập?</span>
              <Button size="sm" onClick={() => setAsk(false)}>Hủy</Button>
              <Button size="sm" variant="danger" onClick={doReset}>Xóa</Button>
            </Row>
          )}
        </Row>
      </Stack>
    </>
  );
}
