import path from 'node:path';
import type { NextConfig } from 'next';

/** Tên miền của trang chính, nơi /ban-do/ được chuyển tiếp sang app này. */
const SITE = 'travel-plan-lovat-seven.vercel.app';

const config: NextConfig = {
  reactStrictMode: true,

  // app này sống ở /ban-do/ chứ không phải gốc tên miền, nên mọi đường dẫn
  // (kể cả /_next/...) phải mang sẵn tiền tố, không thì qua proxy là gãy
  basePath: '/ban-do',

  // trong monorepo có nhiều package-lock.json, chỉ rõ gốc của riêng app này
  outputFileTracingRoot: path.join(__dirname),

  experimental: {
    // server action gửi về đúng đường dẫn cũ, Next đối chiếu Origin với Host —
    // đi qua proxy thì hai cái khác nhau, phải khai tên miền trang chính ra đây
    serverActions: { allowedOrigins: [SITE] },
  },
};

export default config;
