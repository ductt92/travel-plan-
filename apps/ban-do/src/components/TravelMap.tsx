import { useCallback, useEffect, useMemo, useState } from 'react';
import { Button } from 'react-liquis-glass';
import { HomeIcon } from 'react-liquis-glass/icons';
import { GlassToggle } from '@trang/ui/glass';
import FindDialog from './FindDialog';
import LoginDialog from './LoginDialog';
import LogDialog, { type FeedRow } from './LogDialog';
import NotesDialog from './NotesDialog';
import ProvinceDialog from './ProvinceDialog';
import VietnamMap from './VietnamMap';
import WhenButton from './WhenButton';
import WhenDialog from './WhenDialog';
import { BookIcon, HeartIcon, LockIcon, SearchIcon } from './icons';
import { byCode, provinces } from '@/lib/map-data';
import { inPeriod, scopeLabel, scopeShort } from '@/lib/period';
import { useEntries } from '@/lib/use-entries';
import { useMedia } from '@/lib/use-media';
import { useNotes } from '@/lib/use-notes';
import type { Entries, Level, Period } from '@/lib/types';

const TOTAL = provinces.length;
const BLANK = { status: 'none' as const, trips: [] };

export default function TravelMap({
  width, height, initial, token, userName, onSignIn, onSignOut,
}: {
  width: number; height: number; initial: Entries;
  /** Token của tài khoản đang đăng nhập; rỗng là chưa đăng nhập, chỉ xem được. */
  token: string;
  /** Tên người đang đăng nhập (Đức, Ngọc…) */
  userName: string;
  onSignIn: (username: string, password: string) => Promise<string | null>;
  onSignOut: () => void;
}) {
  const canEdit = Boolean(token);
  const {
    entries, entryOf, setStatus, addTrip, updateTrip, removeTrip, saving, error, clearError,
  } = useEntries(initial, token, onSignOut);

  const [period, setPeriod] = useState<Period>({ year: null, month: null });
  const [selected, setSelected] = useState<string | null>(null);
  const [hovered, setHovered] = useState<string | null>(null);
  /** Tỉnh được khoanh từ popup Tìm tỉnh. */
  const [spotlight, setSpotlight] = useState<string[]>([]);
  const [findOpen, setFindOpen] = useState(false);
  const [whenOpen, setWhenOpen] = useState(false);
  const [logOpen, setLogOpen] = useState(false);
  const [loginOpen, setLoginOpen] = useState(false);
  const [notesOpen, setNotesOpen] = useState(false);
  /** Bấm "Note tình yêu" lúc chưa đăng nhập: đăng nhập xong thì mở luôn hộp lời nhắn. */
  const [notesAfterLogin, setNotesAfterLogin] = useState(false);
  const love = useNotes(token, userName, onSignOut, notesOpen);

  const openNotes = () => {
    setHovered(null);
    if (canEdit) setNotesOpen(true);
    else { setNotesAfterLogin(true); setLoginOpen(true); }
  };

  useEffect(() => {
    if (canEdit && notesAfterLogin) { setNotesAfterLogin(false); setNotesOpen(true); }
  }, [canEdit, notesAfterLogin]);
  // đóng popup đăng nhập mà vẫn chưa vào được thì thôi, không mở hộp lời nhắn nữa
  useEffect(() => {
    if (!loginOpen && !canEdit) setNotesAfterLogin(false);
  }, [loginOpen, canEdit]);

  // màn rộng mở bảng bên phải, màn hẹp mở popup giữa màn
  const wide = useMedia('(min-width:861px)');
  const panel = Boolean(selected) && wide;

  const countOf = useCallback(
    (code: string) => (entries[code]?.trips ?? []).filter(t => inPeriod(t, period)).length,
    [entries, period],
  );

  const levelOf = useCallback((code: string): Level => {
    const n = countOf(code);
    if (n) return Math.min(3, n) as 1 | 2 | 3;
    if (period.year) return 'dim';   // đang lọc: tỉnh ngoài khoảng đó mờ đi
    const s = entries[code]?.status;
    return s === 'wish' ? 'wish' : s === 'visited' ? 1 : 0;
  }, [countOf, entries, period.year]);

  const clearPeriod = useCallback(() => setPeriod({ year: null, month: null }), []);

  const pick = useCallback((code: string) => {
    setSelected(code);
    setHovered(null);
  }, []);

  // trang dồn sang trái nhường chỗ cho bảng bên phải
  useEffect(() => {
    document.body.classList.toggle('panel-open', panel);
    return () => document.body.classList.remove('panel-open');
  }, [panel]);

  // bảng bên phải không phải modal nên phải tự nghe Esc, và nhường popup đang chồng lên
  useEffect(() => {
    if (!panel || findOpen || whenOpen || logOpen || loginOpen || notesOpen) return;
    const onKey = (ev: KeyboardEvent) => {
      if (ev.key === 'Escape') setSelected(null);
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, [panel, findOpen, whenOpen, logOpen, loginOpen, notesOpen]);

  const scope = scopeLabel(period);

  const rows = useMemo<FeedRow[]>(() => {
    const out: FeedRow[] = [];
    for (const [code, e] of Object.entries(entries))
      for (const trip of e.trips) if (inPeriod(trip, period)) out.push({ code, trip });
    return out.sort((a, b) => (b.trip.from || '').localeCompare(a.trip.from || ''));
  }, [entries, period]);

  const codes = Object.keys(entries);
  const visited = codes.filter(c => countOf(c) || (!period.year && entries[c].status === 'visited')).length;
  const wish = codes.filter(c => entries[c].status === 'wish' && !entries[c].trips.length).length;

  const describe = (code: string) => {
    const e = entries[code] ?? BLANK;
    const n = countOf(code);
    if (n) return period.year ? `${n} chuyến trong ${scope}` : `${n} chuyến, lần gần nhất ${lastWhen(code)}`;
    if (period.year) return e.trips.length ? `không đi trong ${scope}` : 'chưa đi lần nào';
    return e.status === 'wish' ? 'đang muốn đi' : 'chưa đi lần nào';
  };

  const lastWhen = (code: string) => {
    const t = [...(entries[code]?.trips ?? [])].sort((a, b) => (b.from || '').localeCompare(a.from || ''))[0];
    return t?.from ? `${t.from.slice(5, 7)}/${t.from.slice(0, 4)}` : '—';
  };

  const province = selected ? byCode[selected] : null;
  const entry = selected ? entryOf(selected) : BLANK;

  return (
    <>
      <div className="wrap">
        {/* thanh trên cùng: về trang chủ bên trái, trạng thái đăng nhập bên phải, cùng một mép với phần dưới */}
        <div className="topbar">
          <Button href="/" variant="glass" className="home-link tool-key" icon={<HomeIcon />}>Trang chủ</Button>
          <NoteBar canEdit={canEdit} userName={userName} />
        </div>

        <div className="layout">
          <header className="intro" data-enter>
            <p className="motto">
              <span><span className="ic">📸</span> Những chuyến đi</span>
              <span><span className="ic">💗</span> Những kỷ niệm</span>
              <span><span className="ic">♾️</span> Chúng mình</span>
            </p>
            <h1>
              <span className="n he">Đức</span>
              <em>&amp;</em>
              <span className="n she">Ngọc</span>
              <span className="ic heart" aria-hidden="true">♡</span>
            </h1>
            <p className="tagline">Câu chuyện của chúng mình, kể bằng {TOTAL} tỉnh thành <span className="ic">🌷</span></p>

            <div className="stats">
              <div className="stat v">
                <span className="n">{visited}<small>/{TOTAL}</small></span>
                <span className="k">Tỉnh {period.year ? (period.month ? 'trong tháng' : 'trong năm') : 'đã đi'}</span>
                <div className="bar"><i style={{ width: `${Math.round(visited / TOTAL * 100)}%` }} /></div>
              </div>
              <div className="stat">
                <span className="n">{rows.length}</span>
                <span className="k">Chuyến đi</span>
              </div>
              {period.year ? (
                <div className="stat">
                  <span className={`n${period.month ? ' sm' : ''}`}>{scopeShort(period)}</span>
                  <span className="k">Đang xem</span>
                </div>
              ) : (
                <div className="stat w">
                  <span className="n">{wish}</span>
                  <span className="k">Muốn đi</span>
                </div>
              )}
            </div>

            <div className="toolbar">
              <WhenButton period={period} onOpen={() => { setHovered(null); setWhenOpen(true); }} onClear={clearPeriod} />
              <div className="tools">
                <Button className="tool tool-key" icon={<SearchIcon />} onClick={() => { setHovered(null); setFindOpen(true); }}>
                  Tìm tỉnh
                </Button>
                <Button className="tool tool-key" icon={<BookIcon />} onClick={() => { setHovered(null); setLogOpen(true); }}>
                  Nhật ký <span className="count">{rows.length}</span>
                </Button>
                <Button className="tool tool-key tool-love" icon={<HeartIcon />} onClick={openNotes}
                  title={love.unread ? `${love.unread} lời nhắn mới` : 'Để lại một lời nhắn'}>
                  Note tình yêu
                  {love.unread > 0 && <span className="count love-badge">{love.unread}</span>}
                </Button>
                {canEdit ? (
                  <Button variant="tinted" color="primary" className="tool tool-key tool-auth" icon={<LockIcon open />} onClick={onSignOut}
                    title={`Đang đăng nhập: ${userName}. Bấm để thoát`}>
                    {userName} · Thoát
                  </Button>
                ) : (
                  <Button variant="tinted" color="primary" className="tool tool-key tool-auth" icon={<LockIcon />} onClick={() => { setHovered(null); setLoginOpen(true); }}>
                    Đăng nhập
                  </Button>
                )}
              </div>
            </div>

            <div className="intro-foot">
              <ul className="legend">
                <li><span className="sw sw-0" />Chưa đi</li>
                <li><span className="sw sw-1" />1 chuyến</li>
                <li><span className="sw sw-3" />3 chuyến trở lên</li>
                <li><span className="sw sw-w" />Muốn đi</li>
              </ul>
              <GlassToggle size="sm" className="tool glass-key" />
            </div>
          </header>

          <section className="map-card" aria-label="Bản đồ 34 tỉnh thành" data-enter>
            {spotlight.length > 0 && (
              <div className="spot-bar">
                <span>
                  Đang chọn {spotlight.map((c, i) => (
                    <span key={c}>{i > 0 && ', '}<b>{byCode[c].name}</b></span>
                  ))}
                </span>
                <button onClick={() => setSpotlight([])}>Bỏ chọn</button>
              </div>
            )}

            <VietnamMap
              width={width}
              height={height}
              levelOf={levelOf}
              countOf={countOf}
              hovered={hovered}
              selected={selected}
              spotlight={spotlight}
              onHover={setHovered}
              onPick={pick}
            />

            <p className="hint" aria-live="polite">
              {hovered
                ? <><b>{byCode[hovered].name}</b> · {describe(hovered)}</>
                : 'Bấm vào một tỉnh để xem và ghi chuyến đi'}
            </p>
          </section>
        </div>
      </div>

      {error ? (
        <div className="toast" role="alert">
          <span>{error}</span>
          <button type="button" aria-label="Đóng" onClick={clearError}>✕</button>
        </div>
      ) : saving ? (
        <div className="toast muted" role="status">Đang lưu…</div>
      ) : null}

      <LoginDialog
        open={loginOpen}
        onClose={() => setLoginOpen(false)}
        onSubmit={onSignIn}
      />

      <NotesDialog
        open={notesOpen && canEdit && !loginOpen}
        userName={userName}
        notes={love.notes}
        error={love.error}
        seen={love.seen}
        onClose={() => { love.markSeen(); setNotesOpen(false); }}
        onAdd={love.add}
        onRemove={id => void love.remove(id)}
        onRetry={love.reload}
      />

      <ProvinceDialog
        province={province}
        entry={entry}
        level={selected ? levelOf(selected) : 0}
        period={period}
        modal={!wide}
        canEdit={canEdit}
        onClose={() => setSelected(null)}
        onStatus={s => selected && setStatus(selected, s)}
        onAdd={data => selected && addTrip(selected, data)}
        onUpdate={(id, data) => selected && updateTrip(selected, id, data)}
        onRemove={id => selected && removeTrip(selected, id)}
        onClearPeriod={clearPeriod}
      />

      <FindDialog
        open={findOpen}
        entries={entries}
        spotlight={spotlight}
        levelOf={levelOf}
        countOf={countOf}
        onClose={() => setFindOpen(false)}
        onApply={codes => {
          setSpotlight(codes);
          setFindOpen(false);
          // chọn đúng một tỉnh thì mở luôn chuyến đi của tỉnh đó
          if (codes.length === 1) pick(codes[0]);
        }}
      />

      <WhenDialog
        open={whenOpen}
        period={period}
        entries={entries}
        onClose={() => setWhenOpen(false)}
        onPick={(year, month) => setPeriod({ year, month })}
      />

      {/* Nhật ký tạm khuất khi popup thời gian mở từ trong nó: hai Modal của thư viện
          chồng nhau thì cả hai cùng bẫy phím Tab và cùng nghe Esc */}
      <LogDialog
        open={logOpen && !whenOpen}
        rows={rows}
        period={period}
        onClose={() => setLogOpen(false)}
        onPick={pick}
        onOpenWhen={() => setWhenOpen(true)}
        onClearPeriod={clearPeriod}
      />
    </>
  );
}

/** Chưa đăng nhập thì không nói gì: nút "Đăng nhập" trên thanh công cụ đã đủ. */
function NoteBar({ canEdit, userName }: { canEdit: boolean; userName: string }) {
  if (!canEdit) return null;
  return (
    <p className="note-bar on">
      <span aria-hidden="true">💾</span>
      <span><b>{userName} đang đăng nhập.</b> Chuyến nào thêm hay sửa đều ghi tên {userName}.</span>
    </p>
  );
}
