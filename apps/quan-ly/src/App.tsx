import { useCallback, useEffect, useMemo, useState } from 'react';
import { Alert, Button, Card, Empty, Spin, message } from 'react-liquis-glass';
import { HomeIcon, LogInIcon, LogOutIcon, RefreshIcon } from 'react-liquis-glass/icons';
import { GlassToggle } from '@trang/ui/glass';
import * as api from '@/lib/api';
import type { Catalog, Course, CourseDraft, Lesson, LessonDraft } from '@/lib/types';
import AssetsDrawer from './components/AssetsDrawer';
import CourseDialog from './components/CourseDialog';
import CourseSection from './components/CourseSection';
import LessonDialog from './components/LessonDialog';
import LoginDialog from './components/LoginDialog';
import UsagePanel from './components/UsagePanel';
import YoutubeDialog from './components/YoutubeDialog';

type CourseEdit = { course: Course | null } | null;
type LessonEdit = { course: Course; lesson: Lesson | null } | null;

/**
 * Danh mục cần mật khẩu ngay từ lúc đọc. Có mật khẩu nhớ sẵn thì nạp luôn; server
 * báo 401 (đổi mật khẩu) thì mở lại hộp đăng nhập kèm câu "Sai mật khẩu".
 * Sửa gì xong cũng nạp lại cả danh mục: nhỏ, và dung lượng luôn khớp với server.
 */
export default function App() {
  const [pass, setPassState] = useState(api.savedPass);
  const [login, setLogin] = useState<{ error: string | null } | null>(pass ? null : { error: null });
  const [data, setData] = useState<Catalog | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [activeId, setActiveId] = useState<number | null>(null);
  const [courseEdit, setCourseEdit] = useState<CourseEdit>(null);
  const [lessonEdit, setLessonEdit] = useState<LessonEdit>(null);
  const [filesId, setFilesId] = useState<number | null>(null);
  const [ytId, setYtId] = useState<number | null>(null);

  const reload = useCallback(async () => {
    try {
      const d = await api.loadCatalog();
      d.courses.sort((a, b) => a.sort - b.sort || a.id - b.id);
      setData(d);
      setLoadError(null);
    } catch (err) {
      const e = err as api.ApiError;
      if (e.status !== 401) setLoadError(e.message);
    }
  }, []);

  useEffect(() => {
    api.handleUnauthorized(() => {
      api.rememberPass('');
      api.setPass('');
      setPassState('');
      setLogin({ error: 'Sai mật khẩu.' });
    });
  }, []);

  useEffect(() => { if (pass) void reload(); }, [pass, reload]);

  const signIn = useCallback(async (raw: string) => {
    const typed = raw.trim();
    const err = await api.checkPass(typed);
    if (err) return err;
    api.rememberPass(typed);
    api.setPass(typed);
    setPassState(typed);
    return null;
  }, []);

  const signOut = () => {
    api.rememberPass('');
    api.setPass('');
    setPassState('');
    setData(null);
    setLogin({ error: null });
  };

  // chạy một thao tác: báo thành công/thất bại bằng toast rồi nạp lại; ném tiếp lỗi để hộp thoại giữ nguyên
  const run = useCallback(async (job: () => Promise<unknown>, ok: string) => {
    try {
      await job();
      message.success(ok);
    } catch (err) {
      const e = err as api.ApiError;
      if (e.status !== 401 && e.status !== 400) message.error(e.message);
      throw err;
    } finally {
      await reload();
    }
  }, [reload]);

  const courses = data?.courses ?? [];
  const allLessons = useMemo(() => courses.flatMap(c => c.lessons), [courses]);
  const findLesson = (id: number | null) => (id == null ? null : allLessons.find(l => l.id === id) ?? null);

  // giáo trình đang chọn bị xoá thì quay về cái đầu
  const active = courses.find(c => c.id === activeId) ?? courses[0] ?? null;

  const saveCourse = (d: CourseDraft) => {
    const c = courseEdit?.course;
    return c
      ? run(() => api.updateCourse(c.id, { title: d.title, sort: d.sort }), 'Đã lưu giáo trình.')
      : run(async () => setActiveId((await api.createCourse(d)).id), `Đã thêm ${d.title}.`);
  };

  const saveLesson = (d: LessonDraft) => {
    if (!lessonEdit) return Promise.resolve();
    const { course, lesson } = lessonEdit;
    return lesson
      ? run(() => api.updateLesson(lesson.id, d), `Đã lưu bài ${d.num}.`)
      : run(() => api.createLesson(course.id, { ...d, sort: d.num }), `Đã thêm bài ${d.num}.`);
  };

  const toggle = (l: Lesson, visible: boolean) => {
    // đổi ngay trên màn hình cho mượt, hỏng thì nạp lại sẽ trả về như cũ
    setData(d => d && {
      ...d,
      courses: d.courses.map(c => ({ ...c, lessons: c.lessons.map(x => (x.id === l.id ? { ...x, visible } : x)) })),
    });
    return run(() => api.updateLesson(l.id, { visible }), visible ? `Đã hiện bài ${l.num}.` : `Đã ẩn bài ${l.num}.`).catch(() => {});
  };

  const ytLesson = findLesson(ytId);

  return (
    <div className="wrap">
      <header className="top">
        <div className="top__title">
          <span className="top__seal" aria-hidden="true">学</span>
          <div>
            <h1>Quản lý học liệu</h1>
            <p className="top__sub">Giáo trình, bài học, tài liệu đính kèm và dung lượng còn lại</p>
          </div>
        </div>
        <nav className="top__tools" aria-label="Công cụ">
          <Button variant="glass" size="sm" href="/" icon={<HomeIcon />}>Trang chủ</Button>
          <GlassToggle compact />
          {pass
            ? <Button variant="glass" size="sm" icon={<LogOutIcon />} onClick={signOut}>Thoát</Button>
            : <Button variant="filled" color="primary" size="sm" icon={<LogInIcon />} onClick={() => setLogin({ error: null })}>Đăng nhập</Button>}
        </nav>
      </header>

      <main>
        {!pass ? (
          <Card className="gate">
            <Empty description="Đăng nhập để xem và sửa danh mục học liệu.">
              <Button variant="filled" color="primary" icon={<LogInIcon />} onClick={() => setLogin({ error: null })}>Đăng nhập</Button>
            </Empty>
          </Card>
        ) : !data ? (
          loadError ? (
            <Alert
              type="error" showIcon title="Không đọc được danh mục" description={loadError}
              action={<Button size="sm" icon={<RefreshIcon />} onClick={() => void reload()}>Thử lại</Button>}
            />
          ) : (
            <div className="loading"><Spin size="lg" tip="Đang tải danh mục…" /></div>
          )
        ) : (
          <>
            {loadError && (
              <Alert
                type="warning" showIcon closable title="Chưa nạp lại được" description={loadError}
                onClose={() => setLoadError(null)} className="reload-alert"
              />
            )}
            <UsagePanel data={data} />
            <CourseSection
              courses={courses}
              activeId={active?.id ?? null}
              onSelect={setActiveId}
              onAddCourse={() => setCourseEdit({ course: null })}
              onEditCourse={c => setCourseEdit({ course: c })}
              onDeleteCourse={c => run(() => api.deleteCourse(c.id), `Đã xoá ${c.title}.`).catch(() => {})}
              onAddLesson={c => setLessonEdit({ course: c, lesson: null })}
              onEditLesson={(c, l) => setLessonEdit({ course: c, lesson: l })}
              onDeleteLesson={l => run(() => api.deleteLesson(l.id), `Đã xoá bài ${l.num}.`).catch(() => {})}
              onToggleLesson={toggle}
              onFiles={l => setFilesId(l.id)}
              onYoutube={l => setYtId(l.id)}
            />
          </>
        )}
      </main>

      <LoginDialog open={!!login} initialError={login?.error} onClose={() => setLogin(null)} onSubmit={signIn} />
      <CourseDialog
        open={!!courseEdit} course={courseEdit?.course}
        defaultSort={courses.reduce((m, c) => Math.max(m, c.sort), 0) + 10}
        takenSlugs={courses.map(c => c.slug)}
        onClose={() => setCourseEdit(null)} onSubmit={saveCourse}
      />
      <LessonDialog
        open={!!lessonEdit} lesson={lessonEdit?.lesson} courseTitle={lessonEdit?.course.title ?? ''}
        defaultNum={(lessonEdit?.course.lessons ?? []).reduce((m, l) => Math.max(m, l.num), 0) + 1}
        takenNums={(courses.find(c => c.id === lessonEdit?.course.id)?.lessons ?? []).map(l => l.num)}
        onClose={() => setLessonEdit(null)} onSubmit={saveLesson}
      />
      <AssetsDrawer
        lesson={findLesson(filesId)} r2Configured={!!data?.r2.configured}
        onClose={() => setFilesId(null)} onChanged={reload} onAddYoutube={l => setYtId(l.id)}
      />
      <YoutubeDialog
        lesson={ytLesson}
        onClose={() => setYtId(null)}
        onSubmit={(name, url) => run(() => api.addYoutube(ytLesson!.id, name, url), 'Đã thêm video YouTube.')}
      />
    </div>
  );
}
