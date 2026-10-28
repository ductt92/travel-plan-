/** Ba miền, đúng khoá dùng trong provinces.json. */
export type Region = 'bac' | 'trung' | 'nam';

/** Một tỉnh trên bản đồ. `d` là đường viền SVG, `lx`/`ly` là chỗ đặt nhãn. */
export interface Province {
  code: string;
  name: string;
  region: Region;
  isCity: boolean;
  /** Tên các tỉnh cũ đã nhập vào tỉnh này từ 1/7/2025. */
  merged: string[];
  d: string;
  lx: number;
  ly: number;
  area: number;
  /** Khung bao [x, y, rộng, cao], tính sẵn lúc dựng dữ liệu để khỏi phải đo bằng getBBox. */
  bb: [number, number, number, number];
}

export interface MapData {
  W: number;
  H: number;
  provinces: Province[];
}

export type Status = 'none' | 'visited' | 'wish';

export interface Trip {
  id: number;
  /** 'YYYY-MM-DD', rỗng nếu chưa rõ ngày. */
  from: string;
  to: string;
  /** Đi cùng ai. */
  with: string;
  /** 0–5 sao, 0 là chưa chấm. */
  rate: number;
  places: string[];
  note: string;
}

export interface ProvinceEntry {
  status: Status;
  trips: Trip[];
}

/** Toàn bộ nhật ký, khoá là mã tỉnh. */
export type Entries = Record<string, ProvinceEntry>;

/** Khoảng thời gian đang lọc. year null là không lọc; month chỉ có nghĩa khi có year. */
export interface Period {
  year: number | null;
  month: number | null;
}

/** 0 chưa đi · 1–3 theo số chuyến · 'wish' muốn đi · 'dim' ngoài khoảng đang lọc. */
export type Level = 0 | 1 | 2 | 3 | 'wish' | 'dim';

/** Dữ liệu một chuyến lúc gửi từ form, chưa có id. */
export type TripDraft = Omit<Trip, 'id'>;

/** Kết quả một server action: hoặc xong kèm dữ liệu, hoặc hỏng kèm câu để hiện ra. */
export type ActionResult<T = null> = { ok: true; value: T } | { ok: false; error: string };
