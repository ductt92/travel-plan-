// Các route không có khung app, dùng cho script dựng video và tạo giọng đọc
import { useEffect, useMemo } from 'react';
import { useParams } from 'react-router-dom';
import { LESSONS, TONES, TONE_GAME, INITIALS, PINYIN, lessonById } from '../core/data.js';
import { plainHz } from '../core/pinyin.js';
import { buildLecture, stepParts } from '../core/lecture.js';
import { audioKey } from '../core/speech.js';
import { LecturePlayer } from '../components/LecturePlayer.jsx';

/** /render/:id/:i — một khung hình của bài giảng ở bước i, toàn khung nhìn */
export function RenderView() {
  const { id, i } = useParams();
  const l = lessonById(id);
  useEffect(() => {
    const b = document.body.style, h = document.documentElement.style;
    const old = [b.background, b.overflow, h.overflow];
    b.background = '#000'; b.overflow = 'hidden'; h.overflow = 'hidden';
    return () => { [b.background, b.overflow, h.overflow] = old; };
  }, []);
  if (!l) return null;
  return <LecturePlayer key={l.id} lesson={l} renderMode startStep={+i || 0} />;
}

/** /slide/:id/:s — trọn trang s của bài giảng (đủ nội dung, không phụ đề), lớp học trực tiếp nhúng làm slide */
export function SlideView() {
  const { id, s } = useParams();
  const l = lessonById(id);
  useEffect(() => {
    const b = document.body.style, h = document.documentElement.style;
    const old = [b.background, b.overflow, h.overflow];
    b.background = '#000'; b.overflow = 'hidden'; h.overflow = 'hidden';
    return () => { [b.background, b.overflow, h.overflow] = old; };
  }, []);
  if (!l) return null;
  return <LecturePlayer key={l.id} lesson={l} renderMode slide={+s || 0} />;
}

/** /steps/:id — danh sách bước đọc của bài giảng dạng JSON */
export function StepsView() {
  const { id } = useParams();
  const l = lessonById(id);
  const json = useMemo(() => (l ? JSON.stringify(buildLecture(l).steps.map(st => ({ s: st.s, lang: st.lang, text: st.text, parts: stepParts(st) }))) : '[]'), [l]);
  return <pre id="steps">{json}</pre>;
}

/** /alltexts — mọi câu cần giọng đọc (không trùng) kèm khóa file âm thanh */
export function AllTextsView() {
  const json = useMemo(() => {
    const seen = new Map();
    const add = (lang, text) => { text = (text || '').trim(); if (text) seen.set(lang + '|' + text, { lang, text, key: audioKey(lang, text) }); };
    LESSONS.forEach(l => buildLecture(l).steps.forEach(st => stepParts(st).forEach(p => add(p.lang, p.text))));
    LESSONS.forEach(l => {
      l.words.forEach(w => { add('zh', w.hz); add('zh', plainHz(w.ex)); });
      l.grammar.forEach(g => g.ex.forEach(e => add('zh', e[0])));
      l.dialogs.forEach(d => d.lines.forEach(x => add('zh', x[1])));
    });
    TONES.forEach(t => add('zh', t.ex));
    TONE_GAME.forEach(t => add('zh', t[0]));
    INITIALS.forEach(g => g.k.forEach(k => add('zh', k[1])));
    ['你好', '不是', '一个', '一天'].forEach(t => add('zh', t));
    Object.values(PINYIN || {}).forEach(v => add('zh', v[0]));
    return JSON.stringify([...seen.values()]);
  }, []);
  return <pre id="steps">{json}</pre>;
}
