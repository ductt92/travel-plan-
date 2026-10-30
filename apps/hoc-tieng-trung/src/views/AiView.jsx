// Hỏi AI: đã bật đồng bộ thì hỏi qua API của mình (Node hoặc Go, khóa giấu trên server);
// chưa bật thì gọi thẳng Gemini bằng khóa API của người dùng (lưu trong S.ai)
import { useEffect, useRef, useState, useSyncExternalStore } from 'react';
import { useLocation } from 'react-router-dom';
import { Button, Card, Chip, Field, PageHeader, Row, Stack, useToast } from '@trang/ui';
import { PasswordInput } from '@trang/ui/password';
import { apiFetch, SyncButton, useSyncStatus } from '@trang/sync';
import { useStore, getState, update, activity, DEF } from '../core/store.js';
import './AiView.css';

const AI_SYS = 'Bạn là giáo viên tiếng Trung cho người Việt, bám theo chuẩn HSK 3.0. Trả lời ngắn gọn, chính xác bằng tiếng Việt. Mỗi khi đưa chữ Hán, kèm pinyin có dấu thanh và nghĩa tiếng Việt; nếu phù hợp thì thêm âm Hán Việt. Không dùng Markdown phức tạp.';
const QUICK = ['Phân biệt 把 và 被', 'Phân biệt 有点儿 và 一点儿', 'Tạo hội thoại gọi món ở nhà hàng', 'Giải thích bộ thủ của chữ 好'];

/* Lịch sử chat giữ trong bộ nhớ (còn khi chuyển trang, mất khi tải lại) */
let chat = { msgs: [{ role: 'model', text: 'Chào bạn! 你好 nǐ hǎo! Mình có thể giải thích ngữ pháp, phân biệt từ gần nghĩa, dịch câu hoặc tạo hội thoại luyện tập. Bạn muốn hỏi gì?' }], busy: false };
const subs = new Set();
const setChat = patch => { chat = { ...chat, ...patch }; subs.forEach(f => f()); };
const useChat = () => useSyncExternalStore(f => { subs.add(f); return () => subs.delete(f); }, () => chat);

// Đồng bộ đang bật (đã có mã) thì hỏi qua server
const useServer = () => !!localStorage.getItem('trang-sync-secret');

async function ask(text) {
  const { key, model } = getState().ai;
  setChat({ msgs: [...chat.msgs, { role: 'user', text }], busy: true });
  activity();
  try {
    // 12 lượt gần nhất, bỏ tin lỗi, bắt đầu bằng lượt của người dùng
    const contents = chat.msgs.filter(m => !m.err).slice(-12).map(m => ({ role: m.role, parts: [{ text: m.text }] }));
    while (contents.length && contents[0].role !== 'user') contents.shift();
    let out;
    if (useServer()) {
      const res = await apiFetch('ai', { method: 'POST', body: { model, system: AI_SYS, contents } });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || `Máy chủ trả lỗi ${res.status}`);
      out = data.text;
    } else {
      const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent`, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
        body: JSON.stringify({ systemInstruction: { parts: [{ text: AI_SYS }] }, contents })
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error?.message || `Máy chủ trả lỗi ${res.status}`);
      out = data.candidates?.[0]?.content?.parts?.map(p => p.text).join('');
    }
    out = out || 'Không nhận được câu trả lời.';
    setChat({ msgs: [...chat.msgs, { role: 'model', text: out.replace(/\*\*(.+?)\*\*/g, '$1') }], busy: false });
  } catch (e) {
    setChat({ msgs: [...chat.msgs, { role: 'model', err: true, text: `Không gọi được AI: ${e.message}. Kiểm tra mã đồng bộ hoặc khóa API, tên mô hình và kết nối mạng.` }], busy: false });
  }
}

export function AiView() {
  const S = useStore();
  const { msgs, busy } = useChat();
  const loc = useLocation();
  const toast = useToast();
  const sync = useSyncStatus();
  const server = sync.state !== 'off';
  const hasKey = server || !!S.ai.key;
  const [input, setInput] = useState(loc.state?.q || '');
  const [open, setOpen] = useState(!hasKey);
  const [keyIn, setKeyIn] = useState(S.ai.key);
  const [modelIn, setModelIn] = useState(S.ai.model);
  const box = useRef(null), keyRef = useRef(null);

  useEffect(() => { if (loc.state?.q) setInput(loc.state.q); }, [loc.key]); // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => { const c = box.current; if (c) c.scrollTop = c.scrollHeight; }, [msgs, busy]);

  const send = text => {
    text = text.trim(); if (!text || chat.busy) return;
    if (!server && !getState().ai.key) {
      toast('Hãy nhập khóa API trong phần Cài đặt');
      setOpen(true); setTimeout(() => keyRef.current?.focus(), 0);
      return;
    }
    setInput('');
    ask(text);
  };
  const save = e => {
    e.preventDefault();
    const key = keyIn.trim(), model = modelIn.trim() || DEF.ai.model;
    update(s => { s.ai.key = key; s.ai.model = model; });
    setKeyIn(key); setModelIn(model); setOpen(!key);
    toast('Đã lưu cài đặt');
  };
  const clear = () => { update(s => { s.ai.key = ''; }); setKeyIn(''); setOpen(true); };

  return (
    <>
      <PageHeader eyebrow="Hỏi AI" title="Trợ lý học tiếng Trung" sub={server ? `Giải thích ngữ pháp, dịch câu, tạo hội thoại. Đang hỏi qua API ${sync.backend === 'go' ? 'Go' : 'Node.js'} của mình, không cần khóa riêng.` : 'Giải thích ngữ pháp, dịch câu, tạo hội thoại. Bật đồng bộ để hỏi qua server, hoặc dùng khóa Gemini của riêng bạn.'}
        extra={<SyncButton />} />
      <Card as="section" className="ui-stack" style={{ gap: 14 }}>
        <div className="chat" ref={box} aria-live="polite">
          {msgs.map((m, i) => <div key={i} className={`msg ${m.role === 'user' ? 'me' : m.err ? 'err' : 'ai'}`}>{m.text}</div>)}
          {busy && <div className="msg ai ui-muted">Đang trả lời…</div>}
        </div>
        <form className="ui-row" style={{ gap: 8, flexWrap: 'nowrap' }} onSubmit={e => { e.preventDefault(); send(input); }}>
          <label htmlFor="ai-in" className="ui-sr">Câu hỏi</label>
          <input id="ai-in" className="ui-input" autoComplete="off" value={input} onChange={e => setInput(e.target.value)}
            placeholder={hasKey ? 'Hỏi ngữ pháp, dịch câu hoặc đặt câu…' : 'Nhập khóa API bên dưới để bắt đầu'} />
          <Button variant="primary" type="submit" icon="send" disabled={busy}>Gửi</Button>
        </form>
        <Row gap={8}>
          <span className="ui-muted" style={{ fontSize: 13 }}>Gợi ý:</span>
          {QUICK.map(t => <Chip key={t} onClick={() => send(t)}>{t}</Chip>)}
        </Row>
      </Card>
      <details className="ui-card ui-card--pad set" open={open} onToggle={e => setOpen(e.currentTarget.open)}>
        <summary>Cài đặt khóa API</summary>
        <form className="ui-stack" style={{ gap: 12, paddingTop: 8 }} onSubmit={save}>
          <p className="ui-muted" style={{ fontSize: 14 }}>Tạo khóa miễn phí tại <a href="https://aistudio.google.com/apikey" target="_blank" rel="noopener noreferrer">aistudio.google.com/apikey</a> rồi dán vào đây. Khóa chỉ lưu trong trình duyệt này và chỉ gửi tới máy chủ của Google.</p>
          <Field id="ai-key" label="Khóa API Gemini">
            <PasswordInput id="ai-key" ref={keyRef} className="ui-input" autoComplete="off" value={keyIn} onChange={e => setKeyIn(e.target.value)} />
          </Field>
          <Field id="ai-model" label="Mô hình">
            <input id="ai-model" className="ui-input" autoComplete="off" value={modelIn} onChange={e => setModelIn(e.target.value)} />
          </Field>
          <Row>
            <Button variant="primary" type="submit">Lưu</Button>
            {hasKey && <Button onClick={clear}>Xóa khóa</Button>}
          </Row>
        </form>
      </details>
    </>
  );
}
