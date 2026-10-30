import { useEffect } from 'react';
import { Button, Card, Empty, Popconfirm, Tabs, Tag } from 'react-liquis-glass';
import { BookIcon, EditIcon, PlusIcon, TrashIcon } from 'react-liquis-glass/icons';
import { fmtBytes, lessonsBytes } from '@/lib/format';
import type { Course, Lesson } from '@/lib/types';
import LessonTable from './LessonTable';

interface Props {
  courses: Course[];
  activeId: number | null;
  onSelect: (id: number) => void;
  onAddCourse: () => void;
  onEditCourse: (c: Course) => void;
  onDeleteCourse: (c: Course) => Promise<void>;
  onAddLesson: (c: Course) => void;
  onEditLesson: (c: Course, l: Lesson) => void;
  onDeleteLesson: (l: Lesson) => Promise<void>;
  onToggleLesson: (l: Lesson, visible: boolean) => Promise<void>;
  onFiles: (l: Lesson) => void;
  onYoutube: (l: Lesson) => void;
}

export default function CourseSection(p: Props) {
  const { courses } = p;
  const totalLessons = courses.reduce((s, c) => s + c.lessons.length, 0);
  const totalFiles = courses.reduce((s, c) => s + c.lessons.reduce((t, l) => t + l.assets.length, 0), 0);
  const totalBytes = courses.reduce((s, c) => s + lessonsBytes(c.lessons), 0);
  // thanh tab cuộn ngang khi nhiều giáo trình: kéo tab đang chọn vào tầm nhìn (chỉ cuộn ngang)
  useEffect(() => {
    const tab = document.querySelector<HTMLElement>('.course-tabs .lg-tab.lg-active');
    const list = tab?.parentElement;
    if (!tab || !list) return;
    const left = tab.offsetLeft - 8, right = tab.offsetLeft + tab.offsetWidth + 8;
    if (left < list.scrollLeft) list.scrollLeft = left;
    else if (right > list.scrollLeft + list.clientWidth) list.scrollLeft = right - list.clientWidth;
  }, [p.activeId, courses.length]);
  const add = <Button variant="filled" color="primary" icon={<PlusIcon />} onClick={p.onAddCourse}>Thêm giáo trình</Button>;

  return (
    <section className="section" aria-labelledby="courses-title">
      <div className="section__bar">
        <div>
          <h2 id="courses-title" className="section__title">Giáo trình</h2>
          <p className="section__sub">
            {courses.length} giáo trình · {totalLessons} bài · {totalFiles} tài liệu · {fmtBytes(totalBytes)}
          </p>
        </div>
        {add}
      </div>

      {courses.length === 0 ? (
        <Card><Empty description="Chưa có giáo trình nào. Thêm HSK 1 trước nhé.">{add}</Empty></Card>
      ) : (
        <Tabs
          variant="pill" className="course-tabs"
          activeKey={String(p.activeId ?? courses[0].id)}
          onChange={k => p.onSelect(Number(k))}
          items={courses.map(c => ({
            key: String(c.id),
            label: (
              <span className="course-tab">
                <span>{c.title}</span>
                <span className="course-tab__meta">{c.lessons.length} bài · {fmtBytes(lessonsBytes(c.lessons))}</span>
              </span>
            ),
            children: <CourseView course={c} {...p} />,
          }))}
        />
      )}
    </section>
  );
}

function CourseView({ course: c, ...p }: Props & { course: Course }) {
  const files = c.lessons.reduce((t, l) => t + l.assets.length, 0);
  return (
    <Card className="course-card">
      <div className="course-head">
        <span className="course-head__icon" aria-hidden="true"><BookIcon /></span>
        <div className="course-head__text">
          <h3>{c.title}</h3>
          <span className="course-head__meta">
            <Tag size="sm" variant="outline">{c.slug}</Tag>
            <span>{c.lessons.length} bài</span>
            <span>{files} tài liệu</span>
            <span>{fmtBytes(lessonsBytes(c.lessons))}</span>
          </span>
        </div>
        <div className="course-head__actions">
          <Button size="sm" variant="glass" icon={<EditIcon />} onClick={() => p.onEditCourse(c)}>Sửa</Button>
          <Popconfirm
            title={`Xoá giáo trình ${c.title}?`}
            description={c.lessons.length
              ? `Xoá luôn ${c.lessons.length} bài và ${files} mục tài liệu bên trong; file trên R2 bị xoá theo. Không hoàn tác được.`
              : 'Giáo trình chưa có bài nào.'}
            okText="Xoá" okDanger placement="bottomRight" onConfirm={() => p.onDeleteCourse(c)}
          >
            <Button size="sm" variant="glass" color="danger" icon={<TrashIcon />}>Xoá</Button>
          </Popconfirm>
          <Button size="sm" variant="filled" color="primary" icon={<PlusIcon />} onClick={() => p.onAddLesson(c)}>Thêm bài</Button>
        </div>
      </div>
      <LessonTable
        lessons={c.lessons}
        onToggle={p.onToggleLesson}
        onEdit={l => p.onEditLesson(c, l)}
        onDelete={p.onDeleteLesson}
        onFiles={p.onFiles}
        onYoutube={p.onYoutube}
        onAdd={() => p.onAddLesson(c)}
      />
    </Card>
  );
}
