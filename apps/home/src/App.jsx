import { useEffect, useState } from 'react';
import { Icon } from '@trang/ui';
import { Tag } from 'react-liquis-glass';
import { GlassToggle } from '@trang/ui/glass';
import { MapArt, ZhArt, Hsk6Art, AdminArt } from './Art.jsx';

// số liệu tính lúc build trong vite.config.js
const { zh, hsk6, courses } = __STATS__; // eslint-disable-line no-undef
const n = x => Math.round(x).toLocaleString('vi-VN');

// Các lối vào của site. Thêm app mới: thêm một phần tử vào đây và một tranh trong Art.jsx.
const CHOICES = [
  {
    id: 'map', href: 'ban-do/', tag: 'Ngọc ♥ Đức', title: 'Bản đồ du lịch', cta: 'Mở bản đồ',
    text: 'Những nơi hai người đã đến cùng nhau: trái tim trên bản đồ, đường bay, và từng quán ăn, điểm chơi đã ghé trong mỗi chuyến.',
    chips: ['Tam Đảo', 'Đà Lạt'], Art: MapArt   // số tỉnh, chuyến, địa điểm đọc từ API bản đồ (useMapChips)
  },
  {
    id: 'zh', href: 'hoc-tieng-trung/', tag: 'Hán Lộ · HSK 3.0', title: 'App học tiếng Trung', cta: 'Mở app học',
    text: `${zh.lessons} bài HSK cấp 1–${zh.levels} với bài giảng video, bảng pinyin, thẻ ôn tập và luyện viết chữ Hán.`,
    chips: [`${n(zh.lessons)} bài`, `${n(zh.words)} từ`, `${n(zh.videos)} video`], Art: ZhArt
  },
  {
    id: 'hsk6', href: 'hsk6/', tag: 'Ngọc · HSK 6', title: 'Ngọc học tiếng Trung', cta: 'Vào học',
    text: `Bài giảng video theo Giáo trình chuẩn HSK 6${hsk6.ds ? ' và 顶石中文' : ''}, slide chạy theo lời giảng, từ vựng có đọc mẫu, bài khóa và luyện tập.`,
    chips: [`${n(hsk6.lessons)} bài`, `${n(hsk6.words)} từ`, `${n(hsk6.hours)} giờ video`], Art: Hsk6Art
  },
  {
    id: 'admin', href: 'quan-ly/', tag: 'Học liệu', title: 'Quản lý học liệu', cta: 'Mở trang quản lý',
    text: 'Giáo trình, bài học và tài liệu đi kèm của Hán Lộ, HSK 6 và 顶石中文: dung lượng repo, Neon, R2 và link video YouTube.',
    chips: [`${courses} giáo trình`, `${n(zh.lessons + hsk6.lessons)} bài`, `${n(zh.youtube)} video YouTube`], Art: AdminArt
  }
];

/** Bản đồ lưu trong database nên đếm lúc mở trang; lỗi mạng (hay chạy dev không có API) thì giữ chip mặc định */
function useMapChips() {
  const [chips, setChips] = useState(null);
  useEffect(() => {
    let on = true;
    fetch('/api/node/ban-do').then(r => (r.ok ? r.json() : null)).then(d => {
      const all = Object.values(d?.entries || {});
      if (!on || !all.length) return;
      const trips = all.flatMap(e => e.trips || []);
      setChips([`${all.filter(e => e.status === 'visited').length}/34 tỉnh đã đi`, `${trips.length} chuyến đi`,
        `${trips.reduce((s, t) => s + (t.places?.length || 0), 0)} địa điểm`]);
    }).catch(() => {});
    return () => { on = false; };
  }, []);
  return chips;
}

// Ngọc về Việt Nam (ngày dự kiến, đổi ở đây khi chốt vé)
const NGOC_VE = new Date(2027, 0, 10);

/** "Còn N ngày nữa Ngọc về", đếm theo ngày lịch ở giờ máy; qua ngày đó thì thôi hiện */
function NgocCountdown({ now }) {
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const days = Math.round((NGOC_VE - today) / 86400000);
  if (days < 0) return null;
  const when = NGOC_VE.toLocaleDateString('vi-VN', { day: 'numeric', month: 'numeric', year: 'numeric' });
  return (
    <p className="home__cd" role="status">
      <span aria-hidden="true">💗</span>
      {days === 0
        ? <span><b>Hôm nay Ngọc về</b></span>
        : <span>Còn <b className="home__cd-n">{days.toLocaleString('vi-VN')}</b> ngày nữa Ngọc về</span>}
      <span className="home__cd-when">khoảng {when}</span>
    </p>
  );
}

function greeting(h) { return h < 11 ? 'Chào buổi sáng' : h < 18 ? 'Chào buổi chiều' : 'Chào buổi tối'; }

function ChoiceCard({ c, chips = c.chips }) {
  const { Art } = c;
  return (
    <a className={`choice choice--${c.id}`} href={c.href}>
      <Art />
      <div className="choice__body">
        <Tag variant="glass" className="choice__tag">{c.tag}</Tag>
        <b>{c.title}</b>
        <p>{c.text}</p>
        <div className="choice__chips">{chips.map(t => <span key={t}>{t}</span>)}</div>
        <span className="choice__go">{c.cta} <Icon name="arrow" size={18} strokeWidth="2.2" /></span>
      </div>
    </a>
  );
}

export function App() {
  const d = new Date();
  const mapChips = useMapChips();
  return (
    <>
      <main className="home">
        <header className="home__hello">
          <div className="home__top">
            <span className="ui-eyebrow">{d.toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'numeric', year: 'numeric' })}</span>
            <GlassToggle />
          </div>
          <h1>{greeting(d.getHours())}, hôm nay mở <em>trang nào</em>?</h1>
          <NgocCountdown now={d} />
        </header>
        <div className="home__choices">{CHOICES.map(c => <ChoiceCard key={c.id} c={c} chips={c.id === 'map' ? mapChips ?? c.chips : c.chips} />)}</div>
      </main>
      <footer className="home__foot">Sổ tay chuyến Tam Đảo – Đà Lạt vẫn mở được từ trong bản đồ, hoặc ở <a href="travel/">travel/</a>.</footer>
    </>
  );
}
