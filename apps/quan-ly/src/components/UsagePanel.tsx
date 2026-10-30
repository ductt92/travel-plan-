import type { ReactNode } from 'react';
import { Card, Progress, Statistic, Tag } from 'react-liquis-glass';
import { CloudIcon, DatabaseIcon, FolderIcon, VideoIcon } from 'react-liquis-glass/icons';
import { fmtBytes, pct } from '@/lib/format';
import type { Catalog } from '@/lib/types';

// repo không có giới hạn cứng, nhưng quá ~1 GB là clone/deploy bắt đầu chậm
const REPO_SOFT_LIMIT = 1024 ** 3;
const WARN = 80;

interface MeterProps {
  icon: ReactNode;
  title: string;
  used: number;
  limit: number;
  limitLabel: string;
  children?: ReactNode;
}

function Meter({ icon, title, used, limit, limitLabel, children }: MeterProps) {
  const raw = limit > 0 ? (used / limit) * 100 : 0;
  const over = raw >= 100;
  const warn = raw >= WARN;
  return (
    <Card className={`usage${warn ? ' usage--warn' : ''}`} size="sm">
      <div className="usage__head">
        <span className="usage__icon" aria-hidden="true">{icon}</span>
        <h3>{title}</h3>
        {warn && <Tag color={over ? 'danger' : 'warning'} size="sm">{over ? 'Vượt mức' : 'Sắp đầy'}</Tag>}
      </div>
      <Statistic value={fmtBytes(used)} suffix={<span className="usage__limit">/ {limitLabel}</span>} />
      <Progress
        percent={pct(used, limit)}
        status={over ? 'exception' : 'normal'}
        strokeColor={over ? undefined : warn ? 'var(--lg-warning)' : undefined}
        format={() => `${raw.toLocaleString('vi-VN', { maximumFractionDigits: raw < 10 ? 1 : 0 })}%`}
      />
      {children && <div className="usage__note">{children}</div>}
    </Card>
  );
}

export default function UsagePanel({ data }: { data: Catalog }) {
  const { usage, r2 } = data;
  return (
    <section className="section" aria-labelledby="usage-title">
      <h2 id="usage-title" className="section__title">Dung lượng</h2>
      <div className="usage-grid">
        <Meter
          icon={<DatabaseIcon />} title="Database (Neon)"
          used={usage.dbBytes} limit={usage.dbLimitBytes} limitLabel={fmtBytes(usage.dbLimitBytes)}
        >
          Gói miễn phí. Chỉ lưu danh mục và tiến độ học, không lưu file.
        </Meter>

        {r2.configured ? (
          <Meter
            icon={<CloudIcon />} title="Cloudflare R2"
            used={usage.r2Bytes} limit={usage.r2LimitBytes} limitLabel={fmtBytes(usage.r2LimitBytes)}
          >
            Nơi để video, slide, audio mới. Miễn phí {fmtBytes(usage.r2LimitBytes)}, không tính tiền tải xuống.
          </Meter>
        ) : (
          <Card className="usage usage--off" size="sm">
            <div className="usage__head">
              <span className="usage__icon" aria-hidden="true"><CloudIcon /></span>
              <h3>Cloudflare R2</h3>
              <Tag color="default" size="sm">Chưa cấu hình</Tag>
            </div>
            <Statistic value="—" suffix={<span className="usage__limit">/ {fmtBytes(usage.r2LimitBytes)} miễn phí</span>} />
            <div className="usage__note">
              Tạo bucket trên Cloudflare R2, bật truy cập công khai (r2.dev hoặc tên miền riêng), tạo API token
              quyền Object Read &amp; Write, rồi đặt các biến môi trường R2 cho server API và triển khai lại.
              Khi đó mới tải file lên được.
            </div>
          </Card>
        )}

        <Meter
          icon={<FolderIcon />} title="File trong repo"
          used={usage.repoBytes} limit={REPO_SOFT_LIMIT} limitLabel="~1 GB nên có"
        >
          Repo git nên giữ dưới ~1 GB. Các file này nên chuyển dần sang R2 (hoặc video lên YouTube) rồi xoá khỏi repo.
        </Meter>

        <Card className="usage usage--yt" size="sm">
          <div className="usage__head">
            <span className="usage__icon" aria-hidden="true"><VideoIcon /></span>
            <h3>YouTube</h3>
          </div>
          <Statistic value={(usage.youtubeCount ?? 0).toLocaleString('vi-VN')} suffix={<span className="usage__limit">video trên YouTube</span>} />
          <div className="usage__note">Video gắn bằng link YouTube không tốn dung lượng database, R2 hay repo.</div>
        </Card>
      </div>
    </section>
  );
}
