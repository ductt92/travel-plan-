import { Icon } from '@trang/ui';
import { Tag } from 'react-liquis-glass';
import { GlassToggle } from '@trang/ui/glass';
import { MapArt, ZhArt, Hsk6Art, AdminArt } from './Art.jsx';

// Các lối vào của site. Thêm app mới: thêm một phần tử vào đây và một tranh trong Art.jsx.
const CHOICES = [
  {
    id: 'map', href: 'ban-do/', tag: 'Ngọc ♥ Đức', title: 'Bản đồ du lịch', cta: 'Mở bản đồ',
    text: 'Những nơi hai người đã đến cùng nhau: trái tim trên bản đồ, đường bay, và từng quán ăn, điểm chơi đã ghé trong mỗi chuyến.',
    chips: ['Tam Đảo', 'Đà Lạt', '49 địa điểm'], Art: MapArt
  },
  {
    id: 'zh', href: 'hoc-tieng-trung/', tag: 'Hán Lộ · HSK 3.0', title: 'App học tiếng Trung', cta: 'Mở app học',
    text: '30 bài theo 新HSK教程 1–2 với bài giảng video, bảng pinyin, thẻ ôn tập và luyện viết chữ Hán.',
    chips: ['30 bài', '512 từ', '30 video'], Art: ZhArt
  },
  {
    id: 'hsk6', href: 'hsk6/', tag: 'Ngọc · HSK 6', title: 'Ngọc học tiếng Trung', cta: 'Vào học',
    text: 'Bài giảng video theo Giáo trình chuẩn HSK 6, slide chạy theo lời giảng, từ vựng có đọc mẫu, bài khóa và luyện tập.',
    chips: ['Bài 21 · 未来商店', '54 từ', '51 phút video'], Art: Hsk6Art
  },
  {
    id: 'admin', href: 'quan-ly/', tag: 'Học liệu', title: 'Quản lý học liệu', cta: 'Mở trang quản lý',
    text: 'Giáo trình, bài học và tài liệu đi kèm của Hán Lộ, HSK 6 và 顶石中文: dung lượng repo, Neon, R2 và link video YouTube.',
    chips: ['6 giáo trình', '118 bài', '30 video YouTube'], Art: AdminArt
  }
];

function greeting(h) { return h < 11 ? 'Chào buổi sáng' : h < 18 ? 'Chào buổi chiều' : 'Chào buổi tối'; }

function ChoiceCard({ c }) {
  const { Art } = c;
  return (
    <a className={`choice choice--${c.id}`} href={c.href}>
      <Art />
      <div className="choice__body">
        <Tag variant="glass" className="choice__tag">{c.tag}</Tag>
        <b>{c.title}</b>
        <p>{c.text}</p>
        <div className="choice__chips">{c.chips.map(t => <span key={t}>{t}</span>)}</div>
        <span className="choice__go">{c.cta} <Icon name="arrow" size={18} strokeWidth="2.2" /></span>
      </div>
    </a>
  );
}

export function App() {
  const d = new Date();
  return (
    <>
      <main className="home">
        <header className="home__hello">
          <div className="home__top">
            <span className="ui-eyebrow">{d.toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'numeric', year: 'numeric' })}</span>
            <GlassToggle />
          </div>
          <h1>{greeting(d.getHours())}, hôm nay mở <em>trang nào</em>?</h1>
        </header>
        <div className="home__choices">{CHOICES.map(c => <ChoiceCard key={c.id} c={c} />)}</div>
      </main>
      <footer className="home__foot">Sổ tay chuyến Tam Đảo – Đà Lạt vẫn mở được từ trong bản đồ, hoặc ở <a href="travel/">travel/</a>.</footer>
    </>
  );
}
