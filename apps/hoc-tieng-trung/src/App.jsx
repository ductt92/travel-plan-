import { useEffect } from 'react';
import { HashRouter, Routes, Route, Link, useLocation } from 'react-router-dom';
import { AppShell, Brand, ProgressBar, Icon, ToastProvider } from '@trang/ui';
import { useStore, dueCards, todayN, streak, GOAL } from './core/store.js';
import { stopQueue } from './core/speech.js';
import { HomeView } from './views/HomeView.jsx';
import { LevelView } from './views/LevelView.jsx';
import { IntroView } from './views/IntroView.jsx';
import { PinyinView } from './views/PinyinView.jsx';
import { LessonView } from './views/LessonView.jsx';
import { ReviewView } from './views/ReviewView.jsx';
import { PracticeView } from './views/PracticeView.jsx';
import { WriteView } from './views/WriteView.jsx';
import { DictView } from './views/DictView.jsx';
import { AiView } from './views/AiView.jsx';
import { VideosView } from './views/VideosView.jsx';
import { RenderView, StepsView, AllTextsView } from './views/ToolViews.jsx';

const NAV = [
  { to: '/', label: 'Lộ trình', short: 'Lộ trình', icon: 'path', match: p => p === '/' || /^\/(level|lesson|l0)/.test(p) },
  { to: '/review', label: 'Ôn tập', short: 'Ôn tập', icon: 'cards' },
  { to: '/practice', label: 'Luyện tập', short: 'Luyện', icon: 'quiz' },
  { to: '/write', label: 'Tập viết', short: 'Viết', icon: 'brush' },
  { to: '/dict', label: 'Tra từ', short: 'Tra từ', icon: 'search' },
  { to: '/pinyin', label: 'Bảng pinyin', icon: 'grid', desktopOnly: true },
  { to: '/videos', label: 'Video bài giảng', icon: 'video', desktopOnly: true },
  { to: '/ai', label: 'Hỏi AI', short: 'Hỏi AI', icon: 'ai' }
];

function Goal() {
  useStore();
  const n = todayN();
  return (
    <div className="side-goal">
      <a className="side-home" href="../"><Icon name="home" size={18} />Trang chủ</a>
      <div className="side-goal__box">
        <span className="ui-eyebrow">Mục tiêu hôm nay</span>
        <b className="ui-num">{Math.min(n, GOAL)} / {GOAL} lượt</b>
        <ProgressBar value={n / GOAL} label="Mục tiêu hôm nay" />
        <span className="ui-muted" style={{ fontSize: 13, display: 'flex', alignItems: 'center', gap: 6 }}>
          <Icon name="flame" size={15} style={{ color: 'var(--seal)' }} />{streak()} ngày liên tiếp
        </span>
      </div>
    </div>
  );
}

function Shell({ children }) {
  useStore();
  const { pathname } = useLocation();
  // rời trang thì dừng giọng đọc và cuộn lên đầu
  useEffect(() => { stopQueue(); window.scrollTo(0, 0); }, [pathname]);
  const due = dueCards().length;
  const nav = NAV.map(n => ({ ...n, active: n.match ? n.match(pathname) : pathname.startsWith(n.to), badge: n.to === '/review' ? due : 0 }));
  return (
    <AppShell LinkComponent={Link} nav={nav}
      brand={<Brand LinkComponent={Link} href="/" mark="汉路" title="Hán Lộ" sub="Tiếng Trung theo HSK 3.0" />}
      footer={<Goal />}>
      {children}
    </AppShell>
  );
}

export function App() {
  return (
    <HashRouter>
      <ToastProvider>
        <Routes>
          {/* Các route cho công cụ dựng video / tạo giọng: không có khung app */}
          <Route path="/render/:id/:i" element={<RenderView />} />
          <Route path="/steps/:id" element={<StepsView />} />
          <Route path="/alltexts" element={<AllTextsView />} />
          <Route path="*" element={
            <Shell>
              <Routes>
                <Route path="/" element={<HomeView />} />
                <Route path="/level/:n" element={<LevelView />} />
                <Route path="/l0" element={<IntroView />} />
                <Route path="/pinyin" element={<PinyinView />} />
                <Route path="/lesson/:id" element={<LessonView />} />
                <Route path="/review" element={<ReviewView />} />
                <Route path="/practice" element={<PracticeView />} />
                <Route path="/practice/:scope" element={<PracticeView />} />
                <Route path="/practice/:scope/:id" element={<PracticeView />} />
                <Route path="/write" element={<WriteView />} />
                <Route path="/write/:ch" element={<WriteView />} />
                <Route path="/dict" element={<DictView />} />
                <Route path="/dict/:sel" element={<DictView />} />
                <Route path="/videos" element={<VideosView />} />
                <Route path="/videos/:id" element={<VideosView />} />
                <Route path="/ai" element={<AiView />} />
                <Route path="*" element={<p>Không tìm thấy trang. <Link to="/">Về lộ trình</Link></p>} />
              </Routes>
            </Shell>
          } />
        </Routes>
      </ToastProvider>
    </HashRouter>
  );
}
