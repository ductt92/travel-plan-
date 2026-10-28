import raw from '@/data/provinces.json';
import type { MapData, Region } from './types';

export const REGION: Record<Region, string> = {
  bac: 'Miền Bắc',
  trung: 'Miền Trung',
  nam: 'Miền Nam',
};

/** Quá số chip địa điểm này thì gấp bớt lại, bấm "+n nữa" mới mở hết. */
export const CLIP = 8;

export const mapData = raw as MapData;
export const provinces = mapData.provinces;
export const byCode = Object.fromEntries(provinces.map(p => [p.code, p]));
