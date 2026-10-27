// Màn hình bài học: 5 phần (Bài giảng, Từ mới, Ngữ pháp, Hội thoại, Luyện tập)
import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Breadcrumbs, Button, Card, EmptyState, Icon, IconButton, Row, Stack, Tabs, Toggle, useToast } from '@trang/ui';
import { LESSONS, LEVELS, lessonById } from '../core/data.js';
import { useStore, update, markPart, activity, addCards, lessonDone } from '../core/store.js';
import { say, sayQueue, stopQueue, hasAudioPack, audioReady, onVoices, viVoice } from '../core/speech.js';
import { buildLecture, lectureScript } from '../core/lecture.js';
import { Hz, WordCard } from '../components/Hanzi.jsx';
import { LecturePlayer, whoTone } from '../components/LecturePlayer.jsx';
import './LessonView.css';

const TAB_NAMES = ['Bài giảng', 'Từ mới', 'Ngữ pháp', 'Hội thoại', 'Luyện tập'];

/** Ghi chú giọng đọc: có gói âm thanh sẵn thì không cần */
function LecNote() {
  const [, force] = useState(0);
  useEffect(() => {
    const off = onVoices(() => force(n => n + 1));
    audioReady.then(() => force(n => n + 1));
    return off;
  }, []);
  if (hasAudioPack()) return null;
  if (!('speechSynthesis' in window)) return <Card as="p" className="ui-muted" style={{ fontSize: 14 }}>Trình duyệt này không hỗ trợ giọng đọc, bài giảng sẽ chạy bằng phụ đề.</Card>;
  if (!viVoice) return (
    <Card as="p" style={{ fontSize: 14, borderColor: 'var(--warn-ink)' }}>
      <b>Máy chưa có giọng đọc tiếng Việt</b>, nên lời giảng tiếng Việt chỉ hiện bằng phụ đề (phần tiếng Trung vẫn đọc to). Trên macOS: Cài đặt hệ thống → Trợ năng → Nội dung được đọc → Giọng hệ thống → Quản lý giọng → thêm giọng Tiếng Việt (Linh), rồi tải lại trang.
    </Card>
  );
  return null;
}

/** Kịch bản bài giảng dạng chữ: xem, sao chép, tải .txt */
function ScriptBox({ l }) {
  const toast = useToast();
  const ta = useRef(null);
  const txt = useMemo(() => lectureScript(l, buildLecture(l)), [l]);
  const copy = () => {
    const fail = () => { ta.current?.select(); toast('Hãy nhấn Cmd+C để sao chép'); };
    if (!navigator.clipboard?.writeText) return fail();
    navigator.clipboard.writeText(txt).then(() => toast('Đã sao chép kịch bản'), fail);
  };
  const download = () => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([txt], { type: 'text/plain;charset=utf-8' }));
    a.download = `bai-giang-${l.id}.txt`; a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 2000);
  };
  return (
    <Card as="section"><Stack gap={12}>
      <Row between><b>Kịch bản bài giảng</b><Row gap={8}><Button onClick={copy}>Sao chép</Button><Button onClick={download}>Tải file .txt</Button></Row></Row>
      <p className="ui-muted" style={{ fontSize: 13 }}>Dùng kịch bản này để dựng video với công cụ người dẫn ảo AI (HeyGen, Synthesia, CapCut…) nếu bạn muốn có giảng viên ảo.</p>
      <textarea ref={ta} className="ui-input" style={{ minHeight: 280, padding: 12, font: '14px/1.6 var(--f-ui)' }} readOnly value={txt} aria-label="Kịch bản bài giảng" />
    </Stack></Card>
  );
}

export function LessonView() {
  const { id } = useParams();
  const S = useStore();
  const navigate = useNavigate();
  const toast = useToast();
  const [tab, setTab] = useState(0);
  const [script, setScript] = useState(false);
  useEffect(() => { setTab(0); setScript(false); }, [id]);

  const l = lessonById(id);
  if (!l) return <EmptyState title="Không tìm thấy bài học" actions={<Button variant="primary" as={Link} to="/">Về lộ trình</Button>} />;
  const L = LEVELS[l.lv];
  const p = S.lessons[l.id] || { parts: [], score: null };
  const nxt = LESSONS[LESSONS.indexOf(l) + 1];
  const go = i => { stopQueue(); setTab(i); window.scrollTo(0, 0); };
  const partNext = i => { markPart(l.id, i); activity(); go(i + 1); };

  let body;
  if (tab === 0) body = (
    <>
      <LecturePlayer key={l.id} lesson={l} />
      <LecNote />
      <Card as="section"><Stack gap={10}>
        <span className="ui-eyebrow">Mục tiêu bài học</span>
        <ul className="lv-goals">{l.goal.map((g, i) => <li key={i}>{g}</li>)}</ul>
      </Stack></Card>
      <Row>
        <Button variant="primary" onClick={() => { markPart(l.id, 0); activity(); go(1); }}>{p.parts[0] ? 'Sang từ mới' : 'Đã xem xong · sang từ mới'}</Button>
        <Button as={Link} to={`/videos/${l.id}`}>Xem bản video MP4</Button>
        <Button onClick={() => setScript(v => !v)}>Xem kịch bản bài giảng</Button>
      </Row>
      {script && <ScriptBox l={l} />}
    </>
  );
  else if (tab === 1) body = (
    <>
      <Row between>
        <h2 style={{ fontSize: 18 }}>{l.words.length} từ mới</h2>
        <Row gap={10}><span className="ui-muted" style={{ fontSize: 13 }}>Màu pinyin = thanh điệu</span><Button variant="soft" icon="play" onClick={() => sayQueue(l.words.map(w => w.hz))}>Nghe tất cả</Button></Row>
      </Row>
      <div className="words">{l.words.map(w => <WordCard key={w.id} w={w} />)}</div>
      <Card><Row between>
        <span className="ui-muted" style={{ fontSize: 14 }}>Học xong thì thêm các từ vào bộ thẻ ôn tập ngắt quãng.</span>
        <Button variant="primary" onClick={() => {
          if (!p.parts[1]) { markPart(l.id, 1); const n = addCards(l.words); activity(); toast(n ? `Đã thêm ${n} thẻ vào ôn tập` : 'Các từ đã có trong ôn tập'); }
          go(2);
        }}>{p.parts[1] ? 'Sang ngữ pháp' : 'Đã học xong · thêm vào ôn tập'}</Button>
      </Row></Card>
    </>
  );
  else if (tab === 2) {
    const q = 'Giải thích thêm các điểm ngữ pháp: ' + l.grammar.map(g => g.title).join('; ') + '. Mỗi điểm cho 3 câu ví dụ có pinyin và nghĩa tiếng Việt.';
    body = (
      <>
        {l.grammar.map((g, gi) => (
          <Card key={gi} tone="dark" as="section" style={{ maxWidth: 820 }}><Stack gap={16}>
            <span className="ui-eyebrow">Ngữ pháp {gi + 1}/{l.grammar.length}</span>
            <h2 style={{ fontSize: 24 }}>{g.title}</h2>
            <div className="lv-formula">{g.formula.map((f, i) => <span key={i} className={i === g.key ? 'k' : ''}>{f}</span>)}</div>
            {g.ex.map((e, k) => (
              <div key={k} className="lv-gex">
                <Row gap={10} between wrap={false}><Hz size={20}>{e[0]}</Hz><IconButton icon="sound" variant="ondark" label="Nghe câu" onClick={() => say(e[0])} /></Row>
                {S.showPy && <span className="ui-py ui-muted">{e[1]}</span>}
                {S.showVi && <span className="ui-muted">{e[2]}</span>}
              </div>
            ))}
            <p style={{ fontSize: 15, lineHeight: 1.65, color: 'var(--on-dark-2)' }}>{g.note}</p>
          </Stack></Card>
        ))}
        <Row>
          <Button variant="primary" onClick={() => partNext(2)}>Hiểu rồi · sang hội thoại</Button>
          <Button icon="ai" onClick={() => navigate('/ai', { state: { q } })}>Hỏi AI thêm ví dụ</Button>
        </Row>
      </>
    );
  } else if (tab === 3) body = (
    <>
      {l.dialogs.map((d, di) => (
        <Card key={di} as="section"><Stack gap={20}>
          <Row between>
            <Stack gap={2}><span className="ui-eyebrow">Hội thoại {di + 1}</span><h2 style={{ fontSize: 18 }}>{d.title}</h2></Stack>
            <Button variant="soft" icon="play" onClick={() => sayQueue(d.lines.map(x => x[1]))}>Nghe cả đoạn</Button>
          </Row>
          <Stack gap={18} style={{ maxWidth: 780 }}>
            {d.lines.map((x, k) => (
              <div key={k} className="lv-dl">
                <span className={`lv-who ${whoTone(x[0])}`}>{[...x[0]][0]}</span>
                <Stack gap={2}>
                  <span className="ui-muted" style={{ fontSize: 12 }}>{x[0]}</span>
                  <Hz size={21}>{x[1]}</Hz>
                  {S.showPy && <span className="ui-py lv-dl__py">{x[2]}</span>}
                  {S.showVi && <span>{x[3]}</span>}
                </Stack>
                <IconButton icon="sound" label="Nghe câu này" onClick={() => say(x[1])} />
              </div>
            ))}
          </Stack>
        </Stack></Card>
      ))}
      <Row><Button variant="primary" onClick={() => partNext(3)}>Sang luyện tập</Button></Row>
    </>
  );
  else body = (
    <Card as="section" style={{ maxWidth: 760 }}><Stack gap={14}>
      <h2 style={{ fontSize: 20 }}>Luyện tập {l.words.length} từ của bài</h2>
      <p className="ui-muted">10 câu trộn các dạng: chọn nghĩa, chọn pinyin đúng thanh, nghe rồi chọn chữ, sắp xếp câu. {p.score != null ? `Lần trước: ${p.score}%.` : ''}</p>
      <Row>
        <Button variant="primary" as={Link} to={`/practice/lesson/${l.id}`}>{p.score != null ? 'Luyện lại' : 'Bắt đầu luyện tập'}</Button>
        <Button icon="brush" as={Link} to={`/write/${encodeURIComponent([...l.words[0].hz][0])}`}>Tập viết chữ của bài</Button>
      </Row>
    </Stack></Card>
  );

  return (
    <>
      <Breadcrumbs LinkComponent={Link} items={[{ label: 'Lộ trình', to: '/' }, { label: L.name, to: `/level/${l.lv}` }, { label: `Bài ${l.no}` }]} />
      <Row between align="flex-end">
        <Stack gap={6}>
          <span className="ui-eyebrow">{L.name} · Bài {l.no}</span>
          <h1 style={{ fontSize: 30 }}>{l.title} <Hz className="ui-muted" size={26}>{l.zh}</Hz></h1>
        </Stack>
        <Row gap={18}>
          <Toggle id="tg-py" checked={S.showPy} onChange={v => update(s => { s.showPy = v; })}>Hiện pinyin</Toggle>
          <Toggle id="tg-vi" checked={S.showVi} onChange={v => update(s => { s.showVi = v; })}>Hiện bản dịch</Toggle>
        </Row>
      </Row>
      <Tabs label="Phần của bài" value={tab} onChange={go}
        items={TAB_NAMES.map((t, i) => ({ id: i, label: `${i + 1} · ${t}`, done: !!p.parts[i] }))} />
      {body}
      {lessonDone(l.id) && (
        <Card style={{ borderColor: 'var(--jade)' }}><Row between>
          <b style={{ color: 'var(--jade-ink)' }}>Bạn đã hoàn thành bài này</b>
          {nxt
            ? <Button variant="primary" as={Link} to={`/lesson/${nxt.id}`}>Bài tiếp: {nxt.title}</Button>
            : <Button variant="primary" as={Link} to={`/level/${l.lv}`}>Về {L.name}</Button>}
        </Row></Card>
      )}
    </>
  );
}
