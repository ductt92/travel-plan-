// Dữ liệu chương trình: cấp độ HSK 3.0, bài học (src/data/lessons.json) và phần Nhập môn.
import RAW from '../data/lessons.json';
import PINYIN_RAW from '../data/pinyin.json';

export const LEVELS = [
  {n:0, hz:'零', name:'Cấp 0 · Nhập môn', sub:'Pinyin, 4 thanh điệu, nét cơ bản'},
  {n:1, hz:'一', name:'Cấp 1', sub:'Chào hỏi, gia đình, thời gian, mua sắm, ăn uống', words:300, gram:40, book:'新HSK教程 1'},
  {n:2, hz:'二', name:'Cấp 2', sub:'Đi lại, du lịch, sở thích, so sánh, thời tiết', words:500, gram:45, book:'新HSK教程 2'},
  {n:3, hz:'三', name:'Cấp 3', sub:'Nhà ở, mua sắm, sức khỏe, đi lại, học tập, công việc', syl:608, chars:900, words:2245, gram:81, newWords:973, plan:40, std:'等级标准 2021'},
  {n:4, hz:'四', name:'Cấp 4', sub:'Quan hệ xã hội, văn hóa, cảm xúc', syl:724, chars:1200, words:3245, gram:76},
  {n:5, hz:'五', name:'Cấp 5', sub:'Kinh tế, môi trường, truyền thông', syl:822, chars:1500, words:4316, gram:71},
  {n:6, hz:'六', name:'Cấp 6', sub:'Khoa học, chính sách, bình luận', syl:908, chars:1800, words:5456, gram:67},
  {n:7, hz:'七–九', name:'Cấp 7–9', sub:'Học thuật, văn học, biên phiên dịch', syl:1110, chars:3000, words:11092, gram:148}
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
export const LESSONS = RAW.map(l => ({
  ...l,
  tag: l.grammar.length ? l.grammar[0].title : '',
  words: l.words.map(a => ({ ...W(a), id: `${l.id}:${a[0]}`, lesson: l.id, lv: l.lv }))
}));
export const WORDS = LESSONS.flatMap(l => l.words);
export const WMAP = Object.fromEntries(WORDS.map(w => [w.id, w]));
export const PINYIN = PINYIN_RAW;
export const byHz = hz => WORDS.find(w => w.hz === hz);
export const lessonById = id => LESSONS.find(l => l.id === id);
export const lessonsOf = n => LESSONS.filter(l => l.lv === n);
// Các cấp có bài trong lessons.json (dùng cho bộ lọc, bài kiểm tra cuối cấp)
export const CONTENT_LEVELS = [...new Set(RAW.map(l => l.lv))].sort((a, b) => a - b);
export const hasContent = n => n === 0 || lessonsOf(n).length > 0;
export const NPARTS = 5; // Bài giảng, Từ mới, Ngữ pháp, Hội thoại, Luyện tập
