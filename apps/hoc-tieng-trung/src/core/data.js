// Dữ liệu chương trình: cấp độ HSK 3.0, bài học và phần Nhập môn.
// Bài Cấp 1–3 (src/data/lessons.json) có sẵn trong gói. Bài Cấp 4 trở lên (src/data/lessons-N.json hoặc lessons-N-pK.json) tải khi cần bằng loadLevel(n);
// trước khi tải, INDEX vẫn có tóm tắt mọi bài (module ảo trong vite.config.js) cho lộ trình, trang cấp, bài tiếp theo.
import RAW from '../data/lessons.json';
import IDX from 'virtual:lesson-index';
import PINYIN_RAW from '../data/pinyin.json';

export const LEVELS = [
  {n:0, hz:'零', name:'Cấp 0 · Nhập môn', sub:'Pinyin, 4 thanh điệu, nét cơ bản'},
  {n:1, hz:'一', name:'Cấp 1', sub:'Chào hỏi, gia đình, thời gian, mua sắm, ăn uống', words:300, gram:40, book:'新HSK教程 1'},
  {n:2, hz:'二', name:'Cấp 2', sub:'Đi lại, du lịch, sở thích, so sánh, thời tiết', words:500, gram:45, book:'新HSK教程 2'},
  {n:3, hz:'三', name:'Cấp 3', sub:'Nhà ở, mua sắm, sức khỏe, đi lại, học tập, công việc', syl:608, chars:900, words:2245, gram:81, newWords:973, plan:40, std:'等级标准 2021'},
  {n:4, hz:'四', name:'Cấp 4', sub:'Quan hệ xã hội, văn hóa, cảm xúc', syl:724, chars:1200, words:3245, gram:76, newWords:991, plan:40, std:'等级标准 2021'},
  {n:5, hz:'五', name:'Cấp 5', sub:'Kinh tế, môi trường, truyền thông', syl:822, chars:1500, words:4316, gram:71, newWords:1067, plan:40, std:'等级标准 2021'},
  {n:6, hz:'六', name:'Cấp 6', sub:'Khoa học, chính sách, bình luận', syl:908, chars:1800, words:5456, gram:67, newWords:1136, plan:40, std:'等级标准 2021'},
  {n:7, hz:'七–九', name:'Cấp 7–9', sub:'Học thuật, văn học, biên phiên dịch', syl:1110, chars:3000, words:11092, gram:148, newWords:5620, plan:150, std:'等级标准 2021'}
];
export const STAGES = [
  {zh:'初等', vi:'Sơ cấp', sub:'Giao tiếp hằng ngày', levels:[0,1,2,3]},
  {zh:'中等', vi:'Trung cấp', sub:'Thảo luận xã hội, văn hóa, công việc', levels:[4,5,6]},
  {zh:'高等', vi:'Cao cấp', sub:'Học thuật, văn học, biên phiên dịch', levels:[7]}
];
export const TONES = [
  {t:1, name:'Thanh 1', how:'Cao, đều, kéo dài', pts:'4,6 68,6', ex:'妈', py:'mā'},
  {t:2, name:'Thanh 2', how:'Đi lên, giống dấu sắc', pts:'4,24 68,6', ex:'麻', py:'má'},
  {t:3, name:'Thanh 3', how:'Xuống thấp rồi lên', pts:'4,30 30,42 68,14', ex:'马', py:'mǎ'},
  {t:4, name:'Thanh 4', how:'Rơi mạnh từ cao xuống', pts:'4,6 68,42', ex:'骂', py:'mà'},
  {t:5, name:'Thanh nhẹ', how:'Ngắn, nhẹ, không dấu', pts:'', ex:'吗', py:'ma'}
];
export const TONE_GAME = [['妈','mā'],['麻','má'],['马','mǎ'],['骂','mà'],['八','bā'],['拔','bá'],['把','bǎ'],['爸','bà'],['汤','tāng'],['糖','táng'],['躺','tǎng'],['烫','tàng'],['衣','yī'],['姨','yí'],['椅','yǐ'],['意','yì'],['书','shū'],['熟','shú'],['鼠','shǔ'],['树','shù']];
export const INITIALS = [
  {g:'Âm môi', note:'b gần “p” tiếng Việt, không bật hơi; p bật hơi mạnh.', k:[['b','八'],['p','爬'],['m','妈'],['f','发']]},
  {g:'Đầu lưỡi giữa', note:'d gần “t”, t bật hơi như “th”.', k:[['d','大'],['t','他'],['n','你'],['l','拉']]},
  {g:'Gốc lưỡi', note:'g gần “c”, k bật hơi như “kh” nhẹ, h xát từ cuống họng.', k:[['g','哥'],['k','课'],['h','喝']]},
  {g:'Mặt lưỡi', note:'j gần “ch”, q là “ch” bật hơi, x gần “x” mềm. Chỉ đi với i, ü.', k:[['j','鸡'],['q','七'],['x','西']]},
  {g:'Uốn lưỡi', note:'Cong đầu lưỡi lên: zh gần “tr”, ch là “tr” bật hơi, sh là “s” uốn lưỡi.', k:[['zh','知'],['ch','吃'],['sh','是'],['r','日']]},
  {g:'Đầu lưỡi trước', note:'Lưỡi thẳng: z như “ch” nhẹ, c bật hơi “ts”, s gần “x”.', k:[['z','字'],['c','次'],['s','四']]}
];
export const FINALS = 'a o e i u ü ai ei ao ou an en ang eng ong er ia ie iao iu ian in iang ing iong ua uo uai ui uan un uang üe üan ün'.split(' ');
export const STROKES = [['一','横','héng','Ngang','Kéo từ trái sang phải'],['丨','竖','shù','Sổ','Kéo từ trên xuống'],['丿','撇','piě','Phẩy','Cong xuống bên trái'],['丶','点','diǎn','Chấm','Chấm ngắn xuống phải'],['㇏','捺','nà','Mác','Kéo xuống bên phải, đuôi loe'],['㇀','提','tí','Hất','Hất lên bên phải'],['𠃍','折','zhé','Gập','Đổi hướng giữa nét'],['亅','钩','gōu','Móc','Móc ở cuối nét']];
export const prevOf = n => LEVELS[n - 1] && LEVELS[n - 1].words ? LEVELS[n - 1] : { syl: 0, chars: 0, words: 0 };

// Từ: [chữ Hán, pinyin theo âm tiết, Hán Việt, nghĩa, ví dụ (tách bằng |), pinyin ví dụ, nghĩa ví dụ]
const W = a => ({ hz: a[0], py: a[1], hv: a[2], vi: a[3], ex: a[4], exPy: a[5], exVi: a[6] });
const prep = l => ({
  ...l,
  tag: l.grammar.length ? l.grammar[0].title : '',
  words: l.words.map(a => ({ ...W(a), id: `${l.id}:${a[0]}`, lesson: l.id, lv: l.lv }))
});
const byNo = (a, b) => a.lv - b.lv || a.no - b.no;
/** Bài đã có đủ nội dung (Cấp 1–3 và các cấp đã tải), xếp theo cấp, số bài */
export const LESSONS = [];
export const WORDS = [];
export const WMAP = {};
function addLessons(list) {
  for (const l of list.map(prep)) { LESSONS.push(l); for (const w of l.words) { WORDS.push(w); WMAP[w.id] = w; } }
  LESSONS.sort(byNo); WORDS.sort((a, b) => a.lv - b.lv);
}
addLessons(RAW);
/** Tóm tắt mọi bài, kể cả bài chưa tải: id, lv, no, title, zh, tag, nw (số từ), ng (số điểm ngữ pháp) */
export const INDEX = [...RAW.map(l => ({ id: l.id, lv: l.lv, no: l.no, title: l.title, zh: l.zh, tag: l.grammar[0]?.title || '', nw: l.words.length, ng: l.grammar.length })), ...IDX].sort(byNo);
export const PINYIN = PINYIN_RAW;
export const byHz = hz => WORDS.find(w => w.hz === hz);
export const lessonById = id => LESSONS.find(l => l.id === id);
export const lessonsOf = n => INDEX.filter(l => l.lv === n);
export const nextOf = id => INDEX[INDEX.findIndex(l => l.id === id) + 1];
/** Cấp của một bài hay một thẻ từ: "4-12" hoặc "4-12:词" -> 4 */
export const lvOf = id => parseInt(id, 10);
// Các cấp có bài (dùng cho bộ lọc, bài kiểm tra cuối cấp)
export const CONTENT_LEVELS = [...new Set(INDEX.map(l => l.lv))].sort((a, b) => a - b);
export const hasContent = n => n === 0 || lessonsOf(n).length > 0;

/* Tải nội dung các cấp để riêng. Một cấp là lessons-N.json, hoặc chia nhiều phần lessons-N-p1.json, lessons-N-p2.json…
   (Cấp 7–9 có 150 bài nên chia phần cho mỗi file vừa phải); các phần của một cấp tải song song. */
const LAZY = import.meta.glob('../data/lessons-*.json', { import: 'default' });
const filesOf = n => Object.keys(LAZY).filter(f => new RegExp(`/lessons-${n}(-p\\d+)?\\.json$`).test(f));
const loaded = new Set(RAW.map(l => l.lv)), pending = {}, loadSubs = new Set();
export const isLoaded = n => loaded.has(n) || !filesOf(n).length;
/** Báo khi một cấp vừa tải xong (store.js dùng để vẽ lại giao diện) */
export const onLevelLoad = f => { loadSubs.add(f); return () => loadSubs.delete(f); };
export function loadLevel(n) {
  if (isLoaded(n)) return Promise.resolve();
  return pending[n] || (pending[n] = Promise.all(filesOf(n).map(f => LAZY[f]())).then(parts => {
    addLessons(parts.flat()); loaded.add(n); loadSubs.forEach(f => f());
  }, e => { delete pending[n]; throw e; }));
}
export const loadLevels = ns => Promise.all(ns.map(loadLevel));
export const NPARTS = 5; // Bài giảng, Từ mới, Ngữ pháp, Hội thoại, Luyện tập
