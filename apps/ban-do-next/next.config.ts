import path from 'node:path';
import type { NextConfig } from 'next';

const config: NextConfig = {
  reactStrictMode: true,
  // trong monorepo có nhiều package-lock.json, chỉ rõ gốc của riêng app này
  outputFileTracingRoot: path.join(__dirname),
};

export default config;
