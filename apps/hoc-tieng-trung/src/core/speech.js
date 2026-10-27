// Phát âm: ưu tiên file giọng Google Dịch tạo sẵn trong public/audio (tra theo khóa băm của "ngôn ngữ|câu"),
// thiếu file thì dùng giọng đọc của trình duyệt (Web Speech API).
const BASE = import.meta.env.BASE_URL;
let AUDIO = new Set();
export const audioReady = fetch(`${BASE}audio/index.json`).then(r => (r.ok ? r.json() : [])).then(keys => { AUDIO = new Set(keys); return AUDIO.size; }).catch(() => 0);
export const hasAudioPack = () => AUDIO.size > 0;

export let zhVoice = null, viVoice = null;
const voiceSubs = new Set();
export const onVoices = f => { voiceSubs.add(f); return () => voiceSubs.delete(f); };
function pickVoice() {
  if (!('speechSynthesis' in window)) return;
  const vs = speechSynthesis.getVoices();
  zhVoice = vs.find(v => /zh[-_]CN/i.test(v.lang)) || vs.find(v => /^zh/i.test(v.lang)) || null;
  viVoice = vs.find(v => /^vi/i.test(v.lang)) || null;
  voiceSubs.forEach(f => f());
}
if (typeof window !== 'undefined' && 'speechSynthesis' in window) { pickVoice(); speechSynthesis.onvoiceschanged = pickVoice; }

/** Khóa file âm thanh: FNV-1a + djb2 trên UTF-8 của "lang|text" (khớp tools/gen_audio.py) */
export function audioKey(lang, text) {
  let h1 = 0x811c9dc5, h2 = 5381;
  for (const x of new TextEncoder().encode(lang + '|' + text)) { h1 = Math.imul(h1 ^ x, 0x01000193) >>> 0; h2 = (Math.imul(h2, 33) + x) >>> 0; }
  return h1.toString(16).padStart(8, '0') + h2.toString(16).padStart(8, '0');
}

let curAudio = null;
export function stopVoice() {
  if (curAudio) { curAudio.onended = curAudio.onerror = null; curAudio.pause(); curAudio = null; }
  if ('speechSynthesis' in window) speechSynthesis.cancel();
}
function tts(lang, text, rate, done) {
  const voice = lang === 'zh' ? zhVoice : viVoice;
  if (!('speechSynthesis' in window) || (lang === 'vi' && !voice)) { setTimeout(done, Math.max(1400, text.length * 70) / rate); return; }
  const u = new SpeechSynthesisUtterance(text);
  u.lang = lang === 'zh' ? 'zh-CN' : 'vi-VN'; if (voice) u.voice = voice;
  u.rate = (lang === 'zh' ? 0.8 : 1.05) * rate; u.onend = done; u.onerror = done; window._utt = u;
  speechSynthesis.speak(u);
}
/** Phát một câu; done() được gọi khi đọc xong hoặc khi không phát được */
export function playClip(lang, text, rate = 1, done = () => {}) {
  const key = audioKey(lang, text);
  let fired = false;
  const fin = () => { if (fired) return; fired = true; clearTimeout(guard); done(); };
  const guard = setTimeout(fin, 6000 + text.length * 300 / rate);
  if (AUDIO.has(key)) {
    const a = new Audio(`${BASE}audio/${key}.mp3`); curAudio = a;
    a.playbackRate = rate * (lang === 'zh' ? 0.9 : 1.05);
    a.onended = fin; a.onerror = () => tts(lang, text, rate, fin);
    a.play().catch(() => tts(lang, text, rate, fin));
  } else tts(lang, text, rate, fin);
}
/** Đọc một câu tiếng Trung (dừng câu đang đọc) */
export function say(text, rate = 1) { stopVoice(); playClip('zh', text, rate); }
let qTok = 0;
/** Đọc lần lượt nhiều câu tiếng Trung */
export function sayQueue(list) {
  stopVoice(); const tok = ++qTok;
  const next = i => { if (i < list.length && tok === qTok) playClip('zh', list[i], 1, () => setTimeout(() => next(i + 1), 450)); };
  next(0);
}
export function stopQueue() { qTok++; stopVoice(); }
