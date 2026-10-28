// Màn hình chi tiết một cấp: mô tả, số liệu, danh sách bài và bài kiểm tra cuối cấp.
import { Link, Navigate, useParams } from 'react-router-dom';
import { Breadcrumbs, Button, Card, EmptyState, Icon, ProgressBar, Row, Stack, StatTile, Tag } from '@trang/ui';
import { LEVELS, STAGES, NPARTS, prevOf, lessonsOf } from '../core/data.js';
import { fmtN } from '../core/pinyin.js';
import { useStore, levelStats, nextLesson, lessonDoneCount } from '../core/store.js';
import './LevelView.css';

export function LevelView() {
  const S = useStore();
  const n = Number(useParams().n);
  const L = LEVELS[n];
  if (!L || n === 0) return <Navigate to="/l0" replace />;
  const p = prevOf(n), stage = STAGES.find(s => s.levels.includes(n));
  const ls = lessonsOf(n), st = levelStats(n), nl = nextLesson();
  const nlHere = nl && nl.l && nl.l.lv === n;

  return (
    <>
      <Breadcrumbs LinkComponent={Link} items={[{ label: 'Lộ trình', to: '/' }, { label: stage.vi }, { label: L.name }]} />
      <header className="ui-row" style={{ gap: 28, flexWrap: 'wrap' }}>
        <span className="ui-hz lv-mark" aria-hidden="true" style={{ fontSize: n === 7 ? 34 : 66 }}>{L.hz}</span>
        <Stack gap={8} style={{ flex: '1 1 320px', minWidth: 0 }}>
          <span className="ui-eyebrow">{stage.vi} {stage.zh} · {L.name}</span>
          <h1 style={{ fontSize: 30 }}>{L.sub}</h1>
          <p className="ui-muted" style={{ maxWidth: '62ch' }}>
            {L.book
              ? `Bám theo khung chủ đề, từ vựng và ngữ pháp của giáo trình ${L.book}. Hoàn thành cấp này bạn nắm được khoảng ${fmtN(L.words)} từ.`
              : L.std
              ? `Bám theo danh sách ${fmtN(L.newWords)} từ và ${L.gram} điểm ngữ pháp của ${L.name} trong chuẩn HSK 3.0 bản 2021, chia thành ${L.plan} bài theo chủ đề đời sống. Theo chuẩn, hết cấp này bạn tích lũy khoảng ${fmtN(L.words)} từ.`
              : `Theo chuẩn HSK 3.0 bản 2021, cấp này tích lũy khoảng ${fmtN(L.words)} từ và ${fmtN(L.chars)} chữ Hán.`}
          </p>
        </Stack>
        {ls.length > 0 && (
          <Stack gap={8} style={{ minWidth: 210 }}>
            <Row between style={{ fontSize: 14 }}><span className="ui-muted">Tiến độ</span><b className="ui-num">{st.done}/{st.total} bài</b></Row>
            <ProgressBar value={st.done / st.total} height={8} label={`Tiến độ ${L.name}`} className="lv-bar" />
            {nlHere && <Button variant="primary" as={Link} to={`/lesson/${nl.l.id}`} style={{ marginTop: 6 }}>Học bài {nl.l.no}</Button>}
          </Stack>
        )}
      </header>

      <div className="lv-tiles">
        {L.book || L.std ? <>
          <StatTile label="Từ vựng mới" value={`+${fmtN(L.book ? L.words - p.words : L.newWords)}`} />
          <StatTile label="Điểm ngữ pháp" value={L.gram} />
          <StatTile label={L.plan > ls.length ? 'Bài đã soạn' : 'Số bài'} value={L.plan > ls.length ? `${ls.length}/${L.plan}` : ls.length} />
          <StatTile label={L.book ? 'Giáo trình tham chiếu' : 'Chuẩn tham chiếu'} value={<span className="ui-hz" style={{ fontSize: 18 }}>{L.book || L.std}</span>} />
        </> : <>
          <StatTile label="Từ vựng tích lũy" value={fmtN(L.words)} />
          <StatTile label="Chữ Hán tích lũy" value={fmtN(L.chars)} />
          <StatTile label="Điểm ngữ pháp" value={L.gram} />
        </>}
      </div>

      {ls.length ? (
        <Stack as="section">
          <h2 style={{ fontSize: 20 }}>Danh sách bài học</h2>
          <Card pad={false} className="lv-lessons">
            {ls.map(l => {
              const d = lessonDoneCount(l.id), done = d === NPARTS, cur = !done && nl && nl.l && nl.l.id === l.id;
              const score = S.lessons[l.id]?.score;
              return (
                <Link key={l.id} className={`lv-row${done ? ' is-done' : ''}${cur ? ' is-cur' : ''}`} to={`/lesson/${l.id}`}>
                  <span className="lv-row__no">{done ? <Icon name="check" size={17} strokeWidth="2.4" /> : l.no}</span>
                  <span className="lv-row__t">
                    <b>Bài {l.no} · {l.title} <span className="ui-hz ui-muted" style={{ fontWeight: 500 }}>{l.zh}</span></b>
                    <span style={{ fontSize: 13 }} className={cur ? '' : 'ui-muted'}>
                      {done ? `Hoàn thành${score != null ? ` · luyện tập ${score}%` : ''}` : d ? `Đang học · ${d}/${NPARTS} phần` : `${l.words.length} từ mới`}
                    </span>
                  </span>
                  {l.tag && <Tag className="lv-row__tag">{l.tag}</Tag>}
                </Link>
              );
            })}
            <Link className="lv-row lv-row--test" to={`/practice/level/${n}`}>
              <span className="lv-row__no">考</span>
              <span className="lv-row__t">
                <b>Kiểm tra cuối {L.name}</b>
                <span style={{ fontSize: 13, color: 'var(--on-dark-2)' }}>20 câu từ các bài đã soạn · đạt 80% để hoàn thành cấp</span>
              </span>
              <span style={{ fontSize: 13, color: 'var(--on-dark-2)' }}>{S.passed[n] ? `Đã đạt ${S.passed[n]}%` : 'Làm bài'}</span>
            </Link>
          </Card>
        </Stack>
      ) : (
        <EmptyState glyph={L.hz} title={`Nội dung ${L.name} đang được soạn`}
          actions={<Button variant="primary" as={Link} to="/">Về lộ trình</Button>}>
          <p className="ui-muted" style={{ maxWidth: '52ch' }}>Khung cấp độ đã có theo chuẩn HSK 3.0. Bài học sẽ được bổ sung dần. Trong lúc chờ, bạn có thể ôn tập các cấp trước.</p>
        </EmptyState>
      )}
    </>
  );
}
