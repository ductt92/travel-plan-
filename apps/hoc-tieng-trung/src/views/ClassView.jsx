// Lớp học trực tiếp: lối vào trang /lop-hoc/ (video như Google Meet, giáo viên vẽ lên slide, chat).
// Bản thân lớp học là trang tĩnh riêng ở lop-hoc/ trong repo, chạy qua Ably — ở đây chỉ chọn phòng rồi mở sang đó.
import { useState } from 'react';
import { Button, Card, Field, Icon, PageHeader, Stack } from '@trang/ui';
import './ClassView.css';

const FEATURES = [
  ['cam', 'Video và mic', 'Cả lớp thấy và nghe nhau, tối đa 6 người một phòng.'],
  ['brush', 'Vẽ lên slide', 'Giáo viên mở slide bài giảng và vẽ trực tiếp, có thể giao bút cho học sinh.'],
  ['hand', 'Giơ tay, chat', 'Học sinh giơ tay hoặc nhắn hỏi, người vào muộn vẫn thấy lại bảng và tin nhắn.'],
  ['full', 'Phóng to giáo viên', 'Mỗi người tự chọn xem camera giáo viên to, bảng thu nhỏ ở góc.']
];

// Mã phòng chỉ gồm chữ thường không dấu, số và gạch nối (giống trang lớp học)
const cleanRoom = s => s.trim().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd')
  .replace(/[^a-z0-9-]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 32);

export function ClassView() {
  const [room, setRoom] = useState('hsk');
  const code = cleanRoom(room);
  const join = e => {
    e.preventDefault();
    if (code) window.location.href = `/lop-hoc/?room=${encodeURIComponent(code)}`;
  };
  return (
    <>
      <PageHeader eyebrow="Học cùng giáo viên" title="Lớp học trực tiếp"
        sub="Học online với giáo viên ngay trên trình duyệt, máy tính hay điện thoại đều được. Không cần cài đặt gì." />

      <Card as="form" onSubmit={join} style={{ maxWidth: 520 }}>
        <Stack gap={14}>
          <Field id="room" label="Mã phòng (giáo viên gửi cho bạn)">
            <input id="room" className="ui-input" value={room} onChange={e => setRoom(e.target.value)}
              autoComplete="off" autoCapitalize="none" maxLength={40} placeholder="ví dụ: hsk" />
          </Field>
          <Button variant="primary" type="submit" disabled={!code} style={{ alignSelf: 'flex-start' }}>
            <Icon name="cam" size={18} />Vào lớp
          </Button>
          <span className="ui-muted" style={{ fontSize: 13 }}>
            Trình duyệt sẽ hỏi quyền dùng camera và mic. Giáo viên vào bằng mục "Giáo viên" với mật khẩu của trang.
          </span>
        </Stack>
      </Card>

      <div className="class-features">
        {FEATURES.map(([icon, title, text]) => (
          <Card key={title}>
            <Stack gap={6}>
              <Icon name={icon} size={22} style={{ color: 'var(--jade)' }} />
              <b>{title}</b>
              <span className="ui-muted" style={{ fontSize: 14 }}>{text}</span>
            </Stack>
          </Card>
        ))}
      </div>
    </>
  );
}
