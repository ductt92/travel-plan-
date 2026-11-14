// Dữ liệu ban đầu của web bán hàng. Tự chạy lần đầu có người mở trang (bảng shop_staff còn trống).
//
// Tài khoản quản trị tạo sẵn: admin@fitgear.local, mật khẩu lấy từ SHOP_ADMIN_PASSWORD,
// không có thì dùng APP_SECRET. Đổi mật khẩu ngay sau lần đăng nhập đầu.
// Đơn hàng và khách demo chỉ tạo khi gọi seed({ demo: true }) (script scripts/seed-ban-hang.mjs --demo, dùng ở máy).
import { tx, setSettings } from './db.js';
import { hashPassword, slugify } from './util.js';

const IMG = (n) => `/ban-hang/anh/${n}.jpg`;

const SETTINGS = {
  store_name: 'FITGEAR',
  logo: '',
  favicon: '',
  tagline: 'Đồ tập gym, yoga và chạy bộ',
  announcement: 'Miễn phí giao hàng cho đơn từ 499.000 ₫ · Đổi size trong 7 ngày',
  primary_color: '#E8552B',
  hero_title: 'Đồ tập cho buổi tập thật',
  hero_subtitle: 'Áo, quần, giày và dụng cụ cho gym, yoga, chạy bộ. Giao toàn quốc, đổi size trong 7 ngày.',
  hero_image: IMG('hero'),
  hero_button_text: 'Mua đồ tập',
  hero_button_link: '/cua-hang',
  home_featured_title: 'Bán chạy tuần này',
  home_sale_title: 'Đang giảm giá',
  home_new_title: 'Hàng mới về',
  footer_about: 'FITGEAR bán đồ tập gym, yoga và chạy bộ: chất vải thoáng, form dễ mặc, giá rõ ràng.',
  hotline: '',
  email: 'hello@fitgear.example',
  address: 'Quận 1, TP. Hồ Chí Minh',
  working_hours: '8:00 – 21:00, thứ Hai đến Chủ nhật',
  facebook: '',
  instagram: '',
  tiktok: '',
  zalo: '',
  shipping_fee: '30000',
  free_ship_threshold: '499000',
  cod_enabled: '1',
  bank_enabled: '1',
  bank_name: 'Vietcombank',
  bank_account: '',
  bank_owner: '',
  bank_note: 'Nội dung chuyển khoản: mã đơn hàng (ví dụ DH100123)',
  low_stock_threshold: '5',
  seo_title: 'FITGEAR – Đồ tập gym, yoga, chạy bộ',
  seo_description: 'Áo, quần, giày và dụng cụ tập gym, yoga, chạy bộ. Giao toàn quốc, đổi size trong 7 ngày.',
  menu: JSON.stringify([
    { label: 'Tất cả', url: '/cua-hang' },
    { label: 'Nam', url: '/cua-hang?danh-muc=ao-nam' },
    { label: 'Nữ', url: '/cua-hang?danh-muc=do-nu' },
    { label: 'Giày', url: '/cua-hang?danh-muc=giay' },
    { label: 'Dụng cụ', url: '/cua-hang?danh-muc=dung-cu-tap' },
    { label: 'Giảm giá', url: '/cua-hang?giam-gia=1' },
  ]),
};

const CATEGORIES = [
  ['Áo nam', 'Áo thun, tank top thấm hút mồ hôi', IMG('tee-white-2')],
  ['Quần nam', 'Quần short, quần jogger', IMG('shorts-1')],
  ['Đồ nữ', 'Áo bra, legging, bộ đồ yoga', IMG('legging-2')],
  ['Áo khoác', 'Hoodie, áo nỉ, áo khoác gió', IMG('hoodie')],
  ['Giày', 'Giày chạy bộ, giày tập', IMG('shoes-1')],
  ['Dụng cụ tập', 'Thảm, tạ, dây nhảy', IMG('dumbbell-rope')],
  ['Phụ kiện', 'Bình nước, balo, túi tập', IMG('bottle')],
];

const APPAREL = ['S', 'M', 'L', 'XL'];
// [tên, danh mục, giá, giá KM, ảnh[], size[], màu[], tồn, nổi bật, mô tả ngắn]
const PRODUCTS = [
  ['Áo thun tập Dry-Fit trắng', 'Áo nam', 199000, 169000, ['tee-white-1', 'tee-white-2'], APPAREL, ['Trắng'], 48, 1, 'Vải polyester mắt lưới, khô nhanh, không bám dính khi ra mồ hôi.'],
  ['Áo thun tập Basic đen', 'Áo nam', 199000, null, ['tee-black-2'], APPAREL, ['Đen'], 60, 1, 'Form regular, cổ tròn bo gọn, mặc tập hay mặc đi đều được.'],
  ['Áo thun Oversize xanh rêu', 'Áo nam', 249000, null, ['tee-green'], APPAREL, ['Xanh rêu', 'Xám'], 35, 0, 'Cotton 2 chiều dày vừa, vai rộng, mặc rộng thoải mái.'],
  ['Áo tank top nam', 'Áo nam', 179000, 149000, ['tank-1', 'tank-2'], APPAREL, ['Đen', 'Xám'], 4, 0, 'Khoét nách sâu, thoáng vai khi tập ngực và tay.'],
  ['Quần short chạy bộ 2 lớp', 'Quần nam', 229000, null, ['shorts-1', 'shorts-2'], APPAREL, ['Xanh navy', 'Đen'], 40, 1, 'Lớp trong bó, lớp ngoài dù nhẹ, túi khoá kéo đựng điện thoại.'],
  ['Áo bra thể thao nữ', 'Đồ nữ', 259000, 219000, ['bra-1', 'bra-2'], ['S', 'M', 'L'], ['Trắng', 'Đen'], 30, 1, 'Nâng đỡ vừa, có mút tháo rời, lưng chéo không vướng khi tập.'],
  ['Quần legging cạp cao', 'Đồ nữ', 329000, null, ['legging-1', 'legging-2'], ['S', 'M', 'L'], ['Đen', 'Hồng đất'], 3, 1, 'Cạp cao ôm bụng, vải 4 chiều không lộ khi squat.'],
  ['Bộ đồ tập yoga', 'Đồ nữ', 459000, 399000, ['yoga-set-1', 'yoga-set-2'], ['S', 'M', 'L'], ['Đen', 'Be'], 18, 0, 'Gồm áo croptop và quần legging, vải mềm, co giãn khi gập người.'],
  ['Áo hoodie nỉ xám', 'Áo khoác', 399000, null, ['hoodie'], APPAREL, ['Xám'], 25, 0, 'Nỉ bông dày, mũ hai lớp, mặc khởi động hoặc đi lại sau buổi tập.'],
  ['Áo khoác bomber', 'Áo khoác', 549000, 489000, ['bomber'], APPAREL, ['Nâu cam'], 12, 0, 'Vải dù cản gió nhẹ, bo tay và gấu, khoá kéo kim loại.'],
  ['Áo nỉ trắng cổ tròn', 'Áo khoác', 349000, null, ['sweatshirt'], APPAREL, ['Trắng'], 20, 0, 'Nỉ da cá, form suông, mặc sau buổi tập buổi sáng.'],
  ['Giày chạy bộ đế êm', 'Giày', 890000, 790000, ['shoes-1', 'shoes-2'], ['39', '40', '41', '42', '43'], ['Cam', 'Đen'], 22, 1, 'Đế EVA êm, mũi giày thoáng, dùng cho chạy đường và chạy máy.'],
  ['Thảm tập yoga 6mm', 'Dụng cụ tập', 289000, null, ['mat-1', 'mat-2'], [], ['Xanh rêu', 'Tím than', 'Hồng'], 50, 1, 'TPE dày 6mm, hai mặt chống trượt, kèm dây buộc.'],
  ['Cặp tạ tay 2kg', 'Dụng cụ tập', 199000, null, ['dumbbell-pink'], [], ['Hồng', 'Xanh'], 2, 0, 'Bọc nhựa mềm, không lăn, hợp tập tay tại nhà.'],
  ['Bộ tạ tay và dây nhảy', 'Dụng cụ tập', 349000, 299000, ['dumbbell-rope'], [], [], 15, 0, 'Một cặp tạ 3kg và dây nhảy cáp thép chỉnh được độ dài.'],
  ['Bình nước giữ nhiệt 750ml', 'Phụ kiện', 189000, null, ['bottle'], [], ['Xanh rêu', 'Đen'], 70, 0, 'Inox 2 lớp, giữ lạnh 12 tiếng, nắp không rò nước.'],
  ['Balo tập gym chống nước', 'Phụ kiện', 459000, null, ['backpack'], [], ['Xanh navy'], 10, 0, 'Ngăn giày riêng, ngăn laptop 15 inch, vải phủ chống nước.'],
];

const LONG_DESC = (short) => `<p>${short}</p>
<h3>Chất liệu và form</h3>
<ul><li>Đường may chắc, không cấn khi vận động</li><li>Giặt máy ở chế độ nhẹ, không dùng chất tẩy</li><li>Phơi nơi thoáng, tránh nắng gắt</li></ul>
<h3>Đổi trả</h3>
<p>Đổi size hoặc đổi mẫu trong 7 ngày nếu sản phẩm còn nguyên tem mác.</p>`;

const PAGES = [
  ['Giới thiệu', 'gioi-thieu', `<p>FITGEAR bán đồ tập cho người tập gym, yoga và chạy bộ. Mỗi mẫu được chọn vì mặc thoải mái khi vận động, giặt nhiều lần vẫn giữ form.</p><p>Chúng tôi giao hàng toàn quốc, cho kiểm tra hàng trước khi nhận và đổi size trong 7 ngày.</p>`],
  ['Chính sách đổi trả', 'chinh-sach-doi-tra', `<h3>Điều kiện đổi</h3><ul><li>Trong 7 ngày kể từ khi nhận hàng</li><li>Sản phẩm còn tem mác, chưa giặt, chưa qua sử dụng</li><li>Đồ lót thể thao (áo bra) chỉ đổi khi lỗi từ nhà sản xuất</li></ul><h3>Cách đổi</h3><p>Liên hệ cửa hàng kèm mã đơn hàng. Phí ship đổi size do cửa hàng chịu ở lần đổi đầu tiên.</p>`],
  ['Chính sách vận chuyển', 'chinh-sach-van-chuyen', `<ul><li>Nội thành TP.HCM: 1–2 ngày</li><li>Tỉnh thành khác: 2–5 ngày</li><li>Phí ship đồng giá 30.000 ₫, miễn phí cho đơn từ 499.000 ₫</li></ul><p>Bạn được kiểm tra hàng trước khi thanh toán với đơn COD.</p>`],
  ['Hướng dẫn chọn size', 'huong-dan-chon-size', `<table><thead><tr><th>Size</th><th>Chiều cao (cm)</th><th>Cân nặng (kg)</th></tr></thead><tbody><tr><td>S</td><td>150–160</td><td>45–53</td></tr><tr><td>M</td><td>160–168</td><td>53–62</td></tr><tr><td>L</td><td>168–175</td><td>62–72</td></tr><tr><td>XL</td><td>175–182</td><td>72–82</td></tr></tbody></table><p>Nếu bạn ở giữa hai size, chọn size lớn hơn để mặc thoải mái khi tập.</p>`],
  ['Liên hệ', 'lien-he', `<p>Nhắn tin cho cửa hàng qua email hoặc mạng xã hội ở cuối trang, chúng tôi trả lời trong giờ làm việc.</p>`],
];

const BANNERS = [
  ['Đồ tập nữ', 'Bra, legging và bộ yoga mặc thoải mái khi gập người', IMG('banner-yoga'), 'Xem đồ nữ', '/cua-hang?danh-muc=do-nu'],
  ['Tập tại nhà', 'Thảm, tạ tay và dây nhảy cho góc tập nhỏ', IMG('banner-weights'), 'Xem dụng cụ', '/cua-hang?danh-muc=dung-cu-tap'],
];

const COUPONS = [
  ['CHAOBAN', 'Giảm 10% cho đơn đầu tiên, tối đa 50.000 ₫', 'percent', 10, 50000, 0, 0],
  ['GIAM50K', 'Giảm 50.000 ₫ cho đơn từ 600.000 ₫', 'fixed', 50000, 0, 600000, 100],
];

const DEMO_CUSTOMERS = [
  ['Nguyễn Thu Lan', 'khach@fitgear.local', '0912345678', 'Phường Bến Nghé, Quận 1, TP.HCM'],
  ['Trần Minh Quân', 'quan.tran@mail.example', '0987654321', 'Phường Dịch Vọng, Cầu Giấy, Hà Nội'],
  ['Lê Thị Hoa', 'hoa.le@mail.example', '0905123456', 'Phường Hải Châu 1, Hải Châu, Đà Nẵng'],
  ['Phạm Anh Tú', 'tu.pham@mail.example', '0934567890', 'Phường 7, Quận 3, TP.HCM'],
  ['Võ Ngọc Mai', 'mai.vo@mail.example', '0978123123', 'Phường Tân Định, Quận 1, TP.HCM'],
  ['Đặng Quốc Huy', 'huy.dang@mail.example', '0911222333', 'Phường Láng Hạ, Đống Đa, Hà Nội'],
];


export async function seedIfEmpty() {
  await tx(async (t) => {
    // khoá theo số cố định: nhiều function khởi động cùng lúc thì chỉ một cái tạo dữ liệu
    await t.q('SELECT pg_advisory_xact_lock(727274001)');
    if ((await t.one('SELECT COUNT(*)::int n FROM shop_staff')).n) return;
    await seedBase(t, false);
  });
}

export async function seed({ demo = false, reset = false } = {}) {
  await tx(async (t) => {
    await t.q('SELECT pg_advisory_xact_lock(727274001)');
    if (reset) {
      await t.q(`TRUNCATE shop_order_history, shop_order_items, shop_orders, shop_reviews, shop_products, shop_categories,
        shop_customers, shop_staff, shop_sessions, shop_coupons, shop_banners, shop_pages, shop_settings RESTART IDENTITY CASCADE`);
      await t.q('ALTER SEQUENCE shop_order_code_seq RESTART WITH 100001');
    }
    await seedBase(t, demo);
  });
}

async function seedBase(t, demo) {
  const adminPass = process.env.SHOP_ADMIN_PASSWORD || process.env.APP_SECRET;
  if (!adminPass) throw new Error('cần SHOP_ADMIN_PASSWORD hoặc APP_SECRET để tạo tài khoản quản trị');
  await setSettings(SETTINGS, t);
  await t.q("INSERT INTO shop_staff(name, email, password_hash, role) VALUES('Chủ cửa hàng', 'admin@fitgear.local', ?, 'admin')", [hashPassword(adminPass)]);
  if (demo) await t.q("INSERT INTO shop_staff(name, email, password_hash, role) VALUES('Nhân viên bán hàng', 'nhanvien@fitgear.local', ?, 'staff')", [hashPassword('Nhanvien@123')]);

  const catId = {};
  for (const [i, [name, desc, img]] of CATEGORIES.entries()) {
    catId[name] = (await t.one('INSERT INTO shop_categories(name, slug, description, image, sort) VALUES(?,?,?,?,?) RETURNING id', [name, slugify(name), desc, img, i + 1])).id;
  }
  for (const [i, [name, cat, price, sale, imgs, sizes, colors, stock, featured, short]] of PRODUCTS.entries()) {
    await t.q(`INSERT INTO shop_products(name, slug, sku, category_id, short_desc, description, price, sale_price, images, sizes, colors, stock, featured)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)`, [name, slugify(name), `FG${String(i + 1).padStart(3, '0')}`, catId[cat], short, LONG_DESC(short), price, sale,
      JSON.stringify(imgs.map(IMG)), JSON.stringify(sizes), JSON.stringify(colors), stock, featured]);
  }
  for (const [title, slug, content] of PAGES) await t.q('INSERT INTO shop_pages(title, slug, content) VALUES(?,?,?)', [title, slug, content]);
  for (const [i, [title, sub, img, btn, link]] of BANNERS.entries()) {
    await t.q('INSERT INTO shop_banners(title, subtitle, image, button_text, link, sort) VALUES(?,?,?,?,?,?)', [title, sub, img, btn, link, i + 1]);
  }
  for (const [code, d, type, v, maxd, min, uses] of COUPONS) {
    await t.q('INSERT INTO shop_coupons(code, description, type, value, max_discount, min_order, max_uses) VALUES(?,?,?,?,?,?,?)', [code, d, type, v, maxd, min, uses]);
  }
  if (demo) await seedDemoOrders(t);
}

// Đơn hàng demo trong 30 ngày gần đây để trang tổng quan có số liệu khi xem thử
async function seedDemoOrders(t) {
  const custIds = [];
  for (const [i, [name, email, phone, address]] of DEMO_CUSTOMERS.entries()) {
    custIds.push((await t.one("INSERT INTO shop_customers(name, email, phone, address, password_hash, created_at) VALUES(?,?,?,?,?, now() - make_interval(days => ?)) RETURNING id",
      [name, email, phone, address, hashPassword(i === 0 ? 'Khach@123' : `Demo@${Math.random()}`), 30 - i * 4])).id);
  }
  const products = await t.all('SELECT * FROM shop_products ORDER BY id');
  let seedN = 7;
  const rand = () => { seedN = (seedN * 9301 + 49297) % 233280; return seedN / 233280; };
  const pick = (arr) => arr[Math.floor(rand() * arr.length)];
  const statuses = ['completed', 'completed', 'completed', 'shipping', 'confirmed', 'pending', 'cancelled'];
  const price = (p) => (p.sale_price && p.sale_price < p.price ? p.sale_price : p.price);
  const dayList = Array.from({ length: 46 }, () => Math.floor(rand() * 29)).sort((x, y) => y - x);
  for (let n = 0; n < 46; n++) {
    const ci = Math.floor(rand() * DEMO_CUSTOMERS.length);
    const [name, email, phone, address] = DEMO_CUSTOMERS[ci];
    const daysAgo = dayList[n];
    const status = daysAgo < 2 ? pick(['pending', 'pending', 'confirmed']) : daysAgo < 5 ? pick(['shipping', 'confirmed', 'completed']) : pick(statuses);
    const lines = [];
    const count = 1 + Math.floor(rand() * 3);
    for (let k = 0; k < count; k++) {
      const p = pick(products);
      const sizes = JSON.parse(p.sizes); const colors = JSON.parse(p.colors);
      lines.push({ p, qty: 1 + Math.floor(rand() * 2), size: sizes.length ? pick(sizes) : '', color: colors.length ? pick(colors) : '' });
    }
    const subtotal = lines.reduce((s, l) => s + price(l.p) * l.qty, 0);
    const shipping = subtotal >= 499000 ? 0 : 30000;
    const method = rand() < 0.65 ? 'cod' : 'bank';
    const paid = status === 'completed' || (method === 'bank' && status !== 'pending' && status !== 'cancelled');
    const { n: num } = await t.one("SELECT nextval('shop_order_code_seq')::int AS n");
    const { id } = await t.one(`INSERT INTO shop_orders(code, customer_id, name, phone, email, address, payment_method, payment_status, status, subtotal, discount, shipping, total, created_at, updated_at)
      VALUES(?,?,?,?,?,?,?,?,?,?,0,?,?, now() - make_interval(days => ?), now() - make_interval(days => ?)) RETURNING id`,
      [`DH${num}`, custIds[ci], name, phone, email, address, method, paid ? 'paid' : 'unpaid', status, subtotal, shipping, subtotal + shipping, daysAgo, daysAgo]);
    for (const l of lines) {
      await t.q('INSERT INTO shop_order_items(order_id, product_id, name, image, price, qty, size, color) VALUES(?,?,?,?,?,?,?,?)',
        [id, l.p.id, l.p.name, JSON.parse(l.p.images)[0] || '', price(l.p), l.qty, l.size, l.color]);
      if (status !== 'cancelled') await t.q('UPDATE shop_products SET sold = sold + ? WHERE id = ?', [l.qty, l.p.id]);
    }
    await t.q("INSERT INTO shop_order_history(order_id, status, note, by_name, created_at) VALUES(?, 'pending', 'Khách đặt hàng', ?, now() - make_interval(days => ?))", [id, name, daysAgo]);
    if (status !== 'pending') await t.q("INSERT INTO shop_order_history(order_id, status, note, by_name, created_at) VALUES(?, ?, '', 'Chủ cửa hàng', now() - make_interval(days => ?))", [id, status, daysAgo]);
  }
}
