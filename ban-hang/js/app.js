/* Trang cửa hàng: một trang duy nhất, tự định tuyến theo đường dẫn */
(() => {
  'use strict';

  // ---------- Tiện ích ----------
  // Trang chạy ở /ban-hang/ của site, API ở /api/node/ban-hang
  const B = '/ban-hang';
  const API = '/api/node/ban-hang';
  // Link nhập trong trang quản trị ghi kiểu "/cua-hang": tự gắn thêm /ban-hang phía trước
  const L = (u) => (/^\/(?!\/)/.test(u || '') && u !== B && !u.startsWith(`${B}/`) && !u.startsWith(`${B}?`) ? B + u : u);
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const main = $('#main');
  const esc = (v) => String(v == null ? '' : v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const money = (n) => `${Number(n || 0).toLocaleString('vi-VN')} ₫`;
  const date = (s) => (s ? new Date(s.replace(' ', 'T')).toLocaleString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }) : '');
  const ICON = {
    truck: '<svg viewBox="0 0 24 24"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>',
    swap: '<svg viewBox="0 0 24 24"><path d="M7 4 3 8l4 4M3 8h14M17 20l4-4-4-4M21 16H7"/></svg>',
    cash: '<svg viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/></svg>',
    shield: '<svg viewBox="0 0 24 24"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>',
    check: '<svg viewBox="0 0 24 24"><path d="m5 12 5 5 9-10"/></svg>',
    filter: '<svg viewBox="0 0 24 24"><path d="M4 6h16M7 12h10M10 18h4"/></svg>',
    trash: '<svg viewBox="0 0 24 24"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>',
  };

  async function api(method, url, body) {
    const res = await fetch(`${API}${url}`, {
      method, credentials: 'same-origin',
      headers: body ? { 'Content-Type': 'application/json' } : {},
      body: body ? JSON.stringify(body) : undefined,
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) { const e = new Error(data.error || 'Có lỗi xảy ra'); e.fields = data.fields || {}; e.status = res.status; throw e; }
    return data;
  }

  let toastTimer;
  function toast(html) {
    const t = $('#toast');
    t.innerHTML = html;
    t.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove('show'), 3500);
  }

  // Hiện lỗi theo từng ô nhập (ô có name trùng với key trong fields)
  function showErrors(form, err) {
    $$('.err', form).forEach((e) => (e.textContent = ''));
    $$('.bad', form).forEach((e) => e.classList.remove('bad'));
    const box = $('.form-alert', form);
    let placed = false;
    for (const [k, msg] of Object.entries(err.fields || {})) {
      const input = form.elements[k];
      const slot = $(`.err[data-for="${k}"]`, form);
      if (input && input.classList) input.classList.add('bad');
      if (slot) { slot.textContent = msg; placed = true; }
    }
    if (box) { box.hidden = placed; box.className = 'alert form-alert'; box.textContent = err.message; }
    else if (!placed) toast(esc(err.message));
    const firstBad = $('.bad', form); if (firstBad) firstBad.focus();
  }
  const fieldHTML = (name, label, attrs = '', value = '') =>
    `<div class="field"><label for="f-${name}">${label}</label><input class="input" id="f-${name}" name="${name}" value="${esc(value)}" ${attrs}><div class="err" data-for="${name}"></div></div>`;

  // ---------- Dữ liệu chung ----------
  let SITE = { settings: {}, menu: [], categories: [], banners: [], pages: [], statuses: {} };
  let ME = null;
  const S = (k) => SITE.settings[k] || '';

  // ---------- Giỏ hàng (lưu trên trình duyệt) ----------
  const Cart = {
    get() { try { return JSON.parse(localStorage.getItem('fg_cart') || '[]'); } catch { return []; } },
    set(items) { try { localStorage.setItem('fg_cart', JSON.stringify(items)); } catch { /* bỏ qua */ } Cart.badge(); },
    add(id, size, color, qty) {
      const items = Cart.get();
      const f = items.find((i) => i.id === id && i.size === size && i.color === color);
      if (f) f.qty = Math.min(99, f.qty + qty); else items.push({ id, size, color, qty });
      Cart.set(items);
    },
    count() { return Cart.get().reduce((s, i) => s + i.qty, 0); },
    badge() { const n = Cart.count(); const b = $('#cartCount'); b.textContent = n; b.hidden = !n; },
    payload() { return Cart.get().map((i) => ({ product_id: i.id, qty: i.qty, size: i.size, color: i.color })); },
  };

  // ---------- Giao diện chung ----------
  function hexToRgb(h) { const n = parseInt(h.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; }
  function applyTheme() {
    const c = /^#[0-9a-f]{6}$/i.test(S('primary_color')) ? S('primary_color') : '#E8552B';
    const [r, g, b] = hexToRgb(c);
    const lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
    document.documentElement.style.setProperty('--primary', c);
    document.documentElement.style.setProperty('--on-primary', lum > 0.6 ? '#111' : '#fff');
    const brand = $('#brand');
    brand.innerHTML = S('logo') ? `<img src="${esc(S('logo'))}" alt="${esc(S('store_name'))}">` : esc(S('store_name') || 'Cửa hàng');
    if (S('favicon')) $('#favicon').href = S('favicon');
    const ann = $('#announce');
    ann.textContent = S('announcement'); ann.hidden = !S('announcement');
    const navHTML = SITE.menu.map((m) => `<a href="${esc(L(m.url))}" data-link>${esc(m.label)}</a>`).join('');
    $('#nav').innerHTML = navHTML;
    $('#navM').innerHTML = navHTML + SITE.pages.filter((p) => p.show_in_footer).map((p) => `<a href="${B}/trang/${esc(p.slug)}" data-link>${esc(p.title)}</a>`).join('');
    renderFooter();
  }

  function renderFooter() {
    const contact = [
      S('hotline') && `<li>Hotline: <a href="tel:${esc(S('hotline').replace(/\s/g, ''))}">${esc(S('hotline'))}</a></li>`,
      S('email') && `<li><a href="mailto:${esc(S('email'))}">${esc(S('email'))}</a></li>`,
      S('address') && `<li>${esc(S('address'))}</li>`,
      S('working_hours') && `<li>${esc(S('working_hours'))}</li>`,
    ].filter(Boolean).join('');
    const socials = [['facebook', 'FB'], ['instagram', 'IG'], ['tiktok', 'TT'], ['zalo', 'Zalo']]
      .filter(([k]) => S(k)).map(([k, l]) => `<a href="${esc(S(k))}" target="_blank" rel="noopener" aria-label="${k}">${l}</a>`).join('');
    $('#footer').innerHTML = `<div class="wrap">
      <div class="footer-grid">
        <div><h4>${esc(S('store_name'))}</h4><p>${esc(S('footer_about'))}</p>${socials ? `<div class="social">${socials}</div>` : ''}</div>
        <div><h4>Mua sắm</h4><ul>${SITE.categories.map((c) => `<li><a href="${B}/cua-hang?danh-muc=${esc(c.slug)}" data-link>${esc(c.name)}</a></li>`).join('')}</ul></div>
        <div><h4>Hỗ trợ</h4><ul>${SITE.pages.filter((p) => p.show_in_footer).map((p) => `<li><a href="${B}/trang/${esc(p.slug)}" data-link>${esc(p.title)}</a></li>`).join('')}
          <li><a href="${B}/tra-cuu-don" data-link>Tra cứu đơn hàng</a></li></ul></div>
        <div><h4>Liên hệ</h4><ul>${contact}</ul></div>
      </div>
      <div class="big" aria-hidden="true">${esc(S('store_name'))}</div>
      <div class="bottom"><span>© ${new Date().getFullYear()} ${esc(S('store_name'))}</span><span>Ảnh minh hoạ: Unsplash</span></div>
    </div>`;
  }

  function setTitle(t) { document.title = t ? `${t} – ${S('store_name')}` : (S('seo_title') || S('store_name')); }
  function setMeta(desc) { const m = $('meta[name="description"]'); if (m) m.content = desc || S('seo_description'); }

  // ---------- Thẻ sản phẩm ----------
  function priceHTML(p) {
    const sale = p.final_price < p.price;
    return `<div class="price"><b class="now ${sale ? 'sale' : ''}">${money(p.final_price)}</b>${sale ? `<s>${money(p.price)}</s>` : ''}</div>`;
  }
  function cardHTML(p) {
    const sale = p.final_price < p.price;
    const pct = sale ? Math.round((1 - p.final_price / p.price) * 100) : 0;
    const tag = p.stock <= 0 ? '<span class="tag out">Hết hàng</span>' : sale ? `<span class="tag">−${pct}%</span>` : '';
    return `<a class="card" href="${B}/san-pham/${esc(p.slug)}" data-link>
      <div class="ph">${tag}<img src="${esc(p.images[0] || '')}" alt="${esc(p.name)}" loading="lazy">${p.images[1] ? `<img class="alt" src="${esc(p.images[1])}" alt="" loading="lazy">` : ''}</div>
      <div class="info"><div class="ccat">${esc(p.category_name || '')}</div><div class="cname">${esc(p.name)}</div>${priceHTML(p)}</div></a>`;
  }
  const skeletonGrid = (n) => `<div class="grid">${Array.from({ length: n }, () => '<div><div class="skeleton" style="aspect-ratio:4/5"></div><div class="skeleton" style="height:14px;margin-top:12px;width:70%"></div></div>').join('')}</div>`;

  // ---------- Trang chủ ----------
  async function pageHome() {
    setTitle(''); setMeta();
    const banners = SITE.banners;
    main.innerHTML = `
      <section class="hero">
        ${S('hero_image') ? `<img src="${esc(S('hero_image'))}" alt="" fetchpriority="high">` : ''}
        <div class="wrap">
          <h1 class="enter">${esc(S('hero_title'))}</h1>
          <p class="enter enter-2">${esc(S('hero_subtitle'))}</p>
          <div class="actions enter enter-3">
            ${S('hero_button_text') ? `<a class="btn btn-primary" href="${esc(L(S('hero_button_link') || '/cua-hang'))}" data-link>${esc(S('hero_button_text'))}</a>` : ''}
            <a class="btn btn-ghost" href="${B}/cua-hang?giam-gia=1" data-link>Xem hàng giảm giá</a>
          </div>
        </div>
      </section>
      <div class="perks">
        <div class="perk">${ICON.truck}<div><b>Miễn phí giao hàng</b>${Number(S('free_ship_threshold')) ? `Đơn từ ${money(S('free_ship_threshold'))}` : 'Giao toàn quốc'}</div></div>
        <div class="perk">${ICON.swap}<div><b>Đổi size 7 ngày</b>Còn tem mác là đổi được</div></div>
        <div class="perk">${ICON.cash}<div><b>Kiểm tra rồi trả tiền</b>Thanh toán khi nhận hàng</div></div>
        <div class="perk">${ICON.shield}<div><b>Giá rõ ràng</b>Không phụ thu khi nhận</div></div>
      </div>
      <section class="section"><div class="wrap">
        <div class="section-head"><h2>Mua theo nhóm đồ</h2><a class="link" href="${B}/cua-hang" data-link>Xem tất cả sản phẩm</a></div>
        <div class="cats">${SITE.categories.map((c) => `<a class="cat" href="${B}/cua-hang?danh-muc=${esc(c.slug)}" data-link>${c.image ? `<img src="${esc(c.image)}" alt="" loading="lazy">` : ''}<span>${esc(c.name)}<small>${c.count} sản phẩm</small></span></a>`).join('')}</div>
      </div></section>
      <section class="section section-alt"><div class="wrap">
        <div class="section-head"><h2>${esc(S('home_featured_title') || 'Nổi bật')}</h2><a class="link" href="${B}/cua-hang?sap-xep=best" data-link>Xem hàng bán chạy</a></div>
        <div id="featured">${skeletonGrid(4)}</div>
      </div></section>
      ${banners.length ? `<section class="section"><div class="wrap"><h2 class="sr">Bộ sưu tập</h2><div class="banners">${banners.slice(0, 4).map((b) => `
        <a class="banner" href="${esc(L(b.link || '/cua-hang'))}" data-link><img src="${esc(b.image)}" alt="" loading="lazy"><div>
          ${b.title ? `<h3 style="font-size:40px">${esc(b.title)}</h3>` : ''}${b.subtitle ? `<p>${esc(b.subtitle)}</p>` : ''}
          ${b.button_text ? `<span class="btn btn-light">${esc(b.button_text)}</span>` : ''}</div></a>`).join('')}</div></div></section>` : ''}
      <section class="section" id="saleSec"><div class="wrap">
        <div class="section-head"><h2>${esc(S('home_sale_title') || 'Đang giảm giá')}</h2><a class="link" href="${B}/cua-hang?giam-gia=1" data-link>Xem mọi món giảm giá</a></div>
        <div id="sale">${skeletonGrid(4)}</div>
      </div></section>
      <section class="section section-alt"><div class="wrap">
        <div class="section-head"><h2>${esc(S('home_new_title') || 'Hàng mới')}</h2><a class="link" href="${B}/cua-hang?sap-xep=newest" data-link>Xem hàng mới</a></div>
        <div id="newest">${skeletonGrid(4)}</div>
      </div></section>`;
    const [f, s, n] = await Promise.all([
      api('GET', '/products?featured=1&limit=8&sort=best'), api('GET', '/products?sale=1&limit=4'), api('GET', '/products?sort=newest&limit=4'),
    ]);
    const fill = (id, list) => { const n = list.items.length >= 4 ? Math.floor(list.items.length / 4) * 4 : list.items.length; $(`#${id}`).innerHTML = n ? `<div class="grid">${list.items.slice(0, n).map(cardHTML).join('')}</div>` : ''; };
    fill('featured', f); fill('sale', s); fill('newest', n);
    if (!s.items.length) $('#saleSec').remove();
  }

  // ---------- Cửa hàng / danh mục / tìm kiếm ----------
  async function pageShop() {
    const qs = new URLSearchParams(location.search);
    const cat = qs.get('danh-muc') || '';
    const q = qs.get('q') || '';
    const sale = qs.get('giam-gia') || '';
    const sort = qs.get('sap-xep') || '';
    const size = qs.get('size') || '';
    const min = qs.get('tu') || ''; const max = qs.get('den') || '';
    const page = Number(qs.get('trang') || 1);
    const category = SITE.categories.find((c) => c.slug === cat);
    const title = q ? `Kết quả cho “${q}”` : category ? category.name : sale ? 'Đang giảm giá' : 'Tất cả sản phẩm';
    setTitle(title); setMeta(category ? category.description : '');
    const link = (patch) => { const p = new URLSearchParams(location.search); for (const [k, v] of Object.entries(patch)) v ? p.set(k, v) : p.delete(k); p.delete('trang'); if ('trang' in patch && patch.trang) p.set('trang', patch.trang); const s = p.toString(); return `${B}/cua-hang${s ? `?${s}` : ''}`; };
    const prices = [['', '', 'Mọi mức giá'], ['', '200000', 'Dưới 200.000 ₫'], ['200000', '400000', '200.000 – 400.000 ₫'], ['400000', '', 'Trên 400.000 ₫']];
    const sizes = ['S', 'M', 'L', 'XL', '39', '40', '41', '42', '43'];
    main.innerHTML = `<div class="wrap">
      <div class="page-head"><div class="crumbs"><a href="${B}/" data-link>Trang chủ</a> / ${category ? `<a href="${B}/cua-hang" data-link>Cửa hàng</a> / ` : ''}${esc(title)}</div>
        <h1 style="font-size:clamp(36px,5vw,64px)">${esc(title)}</h1>${category && category.description ? `<p class="muted" style="margin-top:8px">${esc(category.description)}</p>` : ''}</div>
      <div class="shop">
        <aside class="filters" id="filters">
          <div class="group"><h3>Danh mục</h3>
            <a class="f ${!cat ? 'on' : ''}" href="${link({ 'danh-muc': '' })}" data-link><span>Tất cả</span></a>
            ${SITE.categories.map((c) => `<a class="f ${c.slug === cat ? 'on' : ''}" href="${link({ 'danh-muc': c.slug })}" data-link><span>${esc(c.name)}</span><span class="muted">${c.count}</span></a>`).join('')}
          </div>
          <div class="group"><h3>Mức giá</h3>${prices.map(([a, b, l]) => `<a class="f ${min === a && max === b ? 'on' : ''}" href="${link({ tu: a, den: b })}" data-link>${l}</a>`).join('')}</div>
          <div class="group"><h3>Size</h3><div class="chips">${sizes.map((s) => `<a class="chip ${s === size ? 'on' : ''}" href="${link({ size: s === size ? '' : s })}" data-link>${s}</a>`).join('')}</div></div>
          <div class="group"><h3>Ưu đãi</h3><a class="f ${sale ? 'on' : ''}" href="${link({ 'giam-gia': sale ? '' : '1' })}" data-link>Chỉ hàng giảm giá</a></div>
        </aside>
        <div>
          <div class="toolbar">
            <button class="btn btn-ghost filter-toggle" id="filterToggle">${ICON.filter} Bộ lọc</button>
            <span class="muted" id="count"></span>
            <label class="sr" for="sort">Sắp xếp</label>
            <select class="select" id="sort">
              <option value="">Nổi bật</option><option value="newest">Mới nhất</option><option value="best">Bán chạy</option>
              <option value="price_asc">Giá thấp đến cao</option><option value="price_desc">Giá cao đến thấp</option>
            </select>
          </div>
          <div id="list">${skeletonGrid(8)}</div>
        </div>
      </div></div>`;
    $('#sort').value = sort;
    $('#sort').onchange = (e) => go(link({ 'sap-xep': e.target.value }));
    $('#filterToggle').onclick = () => $('#filters').classList.toggle('open');
    const params = new URLSearchParams({ page, limit: 12 });
    if (cat) params.set('category', cat); if (q) params.set('q', q); if (sale) params.set('sale', 1);
    if (sort) params.set('sort', sort); if (size) params.set('size', size); if (min) params.set('min', min); if (max) params.set('max', max);
    const data = await api('GET', `/products?${params}`);
    $('#count').textContent = `${data.total} sản phẩm`;
    $('#list').innerHTML = data.items.length
      ? `<div class="grid">${data.items.map(cardHTML).join('')}</div>${data.pages > 1 ? `<nav class="pager" aria-label="Phân trang">${Array.from({ length: data.pages }, (_, i) => `<a class="chip ${i + 1 === page ? 'on' : ''}" href="${link({ trang: i + 1 > 1 ? String(i + 1) : '' })}" data-link>${i + 1}</a>`).join('')}</nav>` : ''}`
      : `<div class="empty"><p>Không có sản phẩm khớp bộ lọc.</p><a class="btn btn-ghost" href="${B}/cua-hang" data-link>Xoá bộ lọc</a></div>`;
  }

  // ---------- Chi tiết sản phẩm ----------
  async function pageProduct(slug) {
    main.innerHTML = `<div class="wrap" style="padding:40px var(--gutter)"><div class="skeleton" style="height:520px"></div></div>`;
    let data;
    try { data = await api('GET', `/products/${encodeURIComponent(slug)}`); } catch { return pageNotFound(); }
    const p = data.product;
    setTitle(p.name); setMeta(p.short_desc);
    const state = { size: p.sizes.length === 1 ? p.sizes[0] : '', color: p.colors.length === 1 ? p.colors[0] : '', qty: 1, img: 0 };
    const stockLine = p.stock <= 0 ? '<div class="stock out">Tạm hết hàng</div>' : p.stock <= Number(S('low_stock_threshold') || 5) ? `<div class="stock low">Chỉ còn ${p.stock} sản phẩm</div>` : '<div class="stock">Còn hàng</div>';
    const stars = (n) => '★'.repeat(Math.round(n)) + '☆'.repeat(5 - Math.round(n));
    main.innerHTML = `<div class="wrap">
      <div class="crumbs" style="padding-top:20px"><a href="${B}/" data-link>Trang chủ</a> / <a href="${B}/cua-hang?danh-muc=${esc(p.category_slug || '')}" data-link>${esc(p.category_name || 'Cửa hàng')}</a> / ${esc(p.name)}</div>
      <div class="pd">
        <div class="gallery">
          <div class="thumbs">${p.images.map((src, i) => `<button class="${i ? '' : 'on'}" data-i="${i}" aria-label="Ảnh ${i + 1}"><img src="${esc(src)}" alt=""></button>`).join('')}</div>
          <div class="main-img"><img id="mainImg" src="${esc(p.images[0] || '')}" alt="${esc(p.name)}"></div>
        </div>
        <div>
          <div class="ccat muted" style="text-transform:uppercase;letter-spacing:.06em;font-size:12px">${esc(p.category_name || '')} · Mã ${esc(p.sku)}</div>
          <h1>${esc(p.name)}</h1>
          ${p.rating ? `<div style="margin-bottom:8px"><span class="stars">${stars(p.rating)}</span> <a class="link" href="#reviews">${p.reviews.length} đánh giá</a></div>` : ''}
          ${priceHTML(p)}
          <p class="muted">${esc(p.short_desc)}</p>
          ${p.colors.length ? `<div class="opt"><div class="opt-label"><span>Màu: <span id="colorLabel" class="muted">${esc(state.color || 'chọn màu')}</span></span></div><div class="chips" id="colors">${p.colors.map((c) => `<button class="chip ${c === state.color ? 'on' : ''}" data-v="${esc(c)}">${esc(c)}</button>`).join('')}</div><div class="err" id="colorErr"></div></div>` : ''}
          ${p.sizes.length ? `<div class="opt"><div class="opt-label"><span>Size: <span id="sizeLabel" class="muted">${esc(state.size || 'chọn size')}</span></span><a class="link" href="${B}/trang/huong-dan-chon-size" data-link style="font-weight:400;font-size:14px">Bảng size</a></div><div class="chips" id="sizes">${p.sizes.map((s) => `<button class="chip ${s === state.size ? 'on' : ''}" data-v="${esc(s)}">${esc(s)}</button>`).join('')}</div><div class="err" id="sizeErr"></div></div>` : ''}
          <div class="opt"><div class="opt-label">Số lượng</div>
            <div class="qty"><button id="minus" aria-label="Giảm">−</button><input id="qty" value="1" inputmode="numeric" aria-label="Số lượng"><button id="plus" aria-label="Tăng">+</button></div>
            ${stockLine}</div>
          <div class="buy">
            <button class="btn btn-ghost" id="addBtn" ${p.stock <= 0 ? 'disabled' : ''}>Thêm vào giỏ</button>
            <button class="btn btn-primary" id="buyBtn" ${p.stock <= 0 ? 'disabled' : ''}>Mua ngay</button>
          </div>
          <div class="notes">
            <div>${ICON.truck}<span>${Number(S('free_ship_threshold')) ? `Miễn phí giao hàng cho đơn từ ${money(S('free_ship_threshold'))}` : 'Giao hàng toàn quốc'}</span></div>
            <div>${ICON.swap}<span>Đổi size trong 7 ngày, xem <a class="link" href="${B}/trang/chinh-sach-doi-tra" data-link>chính sách đổi trả</a></span></div>
            <div>${ICON.cash}<span>Được kiểm tra hàng trước khi thanh toán</span></div>
          </div>
          <div class="rich" style="margin-top:24px">${p.description || ''}</div>
        </div>
      </div>
      <section class="section" id="reviews" style="border-top:1px solid var(--line)">
        <div class="pd" style="padding:0">
          <div><h2>Đánh giá${p.rating ? ` · ${p.rating}/5` : ''}</h2>
            <div style="margin-top:16px">${p.reviews.length ? p.reviews.map((r) => `<div class="review"><div><span class="stars">${stars(r.rating)}</span> <b>${esc(r.name)}</b> <span class="muted" style="font-size:13px">${date(r.created_at)}</span></div><p style="margin:6px 0 0">${esc(r.content)}</p></div>`).join('') : '<p class="muted">Chưa có đánh giá cho sản phẩm này.</p>'}</div>
          </div>
          <form id="reviewForm" novalidate>
            <h3 style="margin-bottom:12px">Viết đánh giá</h3>
            <div class="alert form-alert" hidden></div>
            <div class="field"><span style="font-size:13px;font-weight:500">Số sao</span><div class="star-pick" id="starPick">${[1, 2, 3, 4, 5].map((n) => `<button type="button" data-n="${n}" aria-label="${n} sao">★</button>`).join('')}</div><input type="hidden" name="rating"><div class="err" data-for="rating"></div></div>
            ${fieldHTML('name', 'Tên của bạn', 'autocomplete="name"', ME ? ME.name : '')}
            <div class="field"><label for="f-content">Nhận xét</label><textarea class="input" id="f-content" name="content" placeholder="Vải mặc có nóng không, form có vừa không…"></textarea><div class="err" data-for="content"></div></div>
            <button class="btn">Gửi đánh giá</button>
          </form>
        </div>
      </section>
      ${data.related.length ? `<section class="section" style="padding-top:0"><div class="section-head"><h2>Có thể bạn thích</h2></div><div class="grid">${data.related.map(cardHTML).join('')}</div></section>` : ''}
    </div>`;

    $$('.thumbs button').forEach((b) => (b.onclick = () => {
      $$('.thumbs button').forEach((x) => x.classList.remove('on')); b.classList.add('on');
      $('#mainImg').src = p.images[b.dataset.i];
    }));
    const pickChip = (wrap, key, label, errId) => wrap && $$('button', wrap).forEach((b) => (b.onclick = () => {
      state[key] = b.dataset.v; $$('button', wrap).forEach((x) => x.classList.toggle('on', x === b));
      $(label).textContent = b.dataset.v; $(errId).textContent = '';
    }));
    pickChip($('#sizes'), 'size', '#sizeLabel', '#sizeErr');
    pickChip($('#colors'), 'color', '#colorLabel', '#colorErr');
    const qty = $('#qty');
    const setQty = (v) => { state.qty = Math.max(1, Math.min(p.stock || 1, Number(v) || 1)); qty.value = state.qty; };
    $('#minus').onclick = () => setQty(state.qty - 1);
    $('#plus').onclick = () => setQty(state.qty + 1);
    qty.onchange = () => setQty(qty.value);
    const tryAdd = () => {
      let ok = true;
      if (p.colors.length && !state.color) { $('#colorErr').textContent = 'Chọn màu'; ok = false; }
      if (p.sizes.length && !state.size) { $('#sizeErr').textContent = 'Chọn size'; ok = false; }
      if (!ok) return false;
      const inCart = Cart.get().filter((i) => i.id === p.id).reduce((s, i) => s + i.qty, 0);
      if (inCart + state.qty > p.stock) { toast(`Chỉ còn ${p.stock} sản phẩm, giỏ của bạn đã có ${inCart}`); return false; }
      Cart.add(p.id, state.size, state.color, state.qty);
      return true;
    };
    $('#addBtn').onclick = () => { if (tryAdd()) toast(`Đã thêm vào giỏ <a href="${B}/gio-hang" data-link>Xem giỏ hàng</a>`); };
    $('#buyBtn').onclick = () => { if (tryAdd()) go('/thanh-toan'); };

    const rf = $('#reviewForm');
    $$('#starPick button').forEach((b) => (b.onclick = () => {
      rf.elements.rating.value = b.dataset.n;
      $$('#starPick button').forEach((x) => x.classList.toggle('on', Number(x.dataset.n) <= Number(b.dataset.n)));
      $('.err[data-for="rating"]', rf).textContent = '';
    }));
    rf.onsubmit = async (e) => {
      e.preventDefault();
      const body = Object.fromEntries(new FormData(rf));
      try {
        const r = await api('POST', `/products/${p.id}/reviews`, body);
        rf.innerHTML = `<div class="alert ok">${esc(r.message)}</div>`;
      } catch (err) { showErrors(rf, err); }
    };
  }

  // ---------- Giỏ hàng ----------
  let couponCode = '';
  try { couponCode = sessionStorage.getItem('fg_coupon') || ''; } catch { /* bỏ qua */ }
  const saveCoupon = (c) => { couponCode = c; try { c ? sessionStorage.setItem('fg_coupon', c) : sessionStorage.removeItem('fg_coupon'); } catch { /* bỏ qua */ } };

  async function loadCartProducts() {
    const items = Cart.get();
    if (!items.length) return { items, map: {} };
    const data = await api('GET', `/products?ids=${[...new Set(items.map((i) => i.id))].join(',')}&limit=100`);
    const map = Object.fromEntries(data.items.map((p) => [p.id, p]));
    const kept = items.filter((i) => map[i.id]);
    if (kept.length !== items.length) Cart.set(kept);
    return { items: kept, map };
  }

  async function quoteCart() {
    try { return await api('POST', '/cart/quote', { items: Cart.payload(), coupon: couponCode }); }
    catch (err) {
      if (couponCode && err.fields && err.fields.coupon) { const msg = err.fields.coupon; saveCoupon(''); const q = await api('POST', '/cart/quote', { items: Cart.payload() }); q.couponError = msg; return q; }
      throw err;
    }
  }

  function summaryHTML(q, withCoupon) {
    return `<div class="r"><span>Tạm tính</span><span>${money(q.subtotal)}</span></div>
      ${q.discount ? `<div class="r"><span>Giảm giá (${esc(q.coupon.code)})</span><span>−${money(q.discount)}</span></div>` : ''}
      <div class="r"><span>Phí giao hàng</span><span>${q.shipping ? money(q.shipping) : 'Miễn phí'}</span></div>
      ${withCoupon ? `<div class="coupon" id="couponBox"><label class="sr" for="f-coupon">Mã giảm giá</label><input class="input" id="f-coupon" placeholder="Mã giảm giá" value="${esc(couponCode)}"><button class="btn btn-ghost" type="button" id="applyCoupon">Áp dụng</button></div>
        <div class="err" id="couponErr">${esc(q.couponError || '')}</div>${q.coupon ? `<div style="font-size:13px;color:var(--success)">${esc(q.coupon.description || 'Đã áp dụng mã')} · <button class="link" id="rmCoupon" type="button">Bỏ mã</button></div>` : ''}` : ''}
      <div class="r total"><span>Tổng cộng</span><span>${money(q.total)}</span></div>
      ${q.shipping && Number(S('free_ship_threshold')) ? `<p class="muted" style="font-size:13px;margin:8px 0 0">Mua thêm ${money(Number(S('free_ship_threshold')) - (q.subtotal - q.discount))} để được miễn phí giao hàng.</p>` : ''}`;
  }

  function bindCoupon(rerender) {
    const input = $('#f-coupon'); if (!input) return;
    input.onkeydown = (e) => { if (e.key === 'Enter') { e.preventDefault(); $('#applyCoupon').click(); } };
    $('#applyCoupon').onclick = async () => {
      const code = input.value.trim();
      if (!code) { $('#couponErr').textContent = 'Nhập mã giảm giá'; return; }
      try { await api('POST', '/cart/quote', { items: Cart.payload(), coupon: code }); saveCoupon(code); rerender(); toast('Đã áp dụng mã giảm giá'); }
      catch (err) { $('#couponErr').textContent = (err.fields && err.fields.coupon) || err.message; }
    };
    const rm = $('#rmCoupon'); if (rm) rm.onclick = () => { saveCoupon(''); rerender(); };
  }

  async function pageCart() {
    setTitle('Giỏ hàng');
    main.innerHTML = `<div class="wrap"><div class="page-head"><h1 style="font-size:clamp(36px,5vw,64px)">Giỏ hàng</h1></div><div id="cartBody"><div class="skeleton" style="height:240px"></div></div></div>`;
    const { items, map } = await loadCartProducts();
    if (!items.length) {
      $('#cartBody').innerHTML = `<div class="empty" style="margin-bottom:80px"><p>Giỏ hàng của bạn đang trống.</p><a class="btn btn-primary" href="${B}/cua-hang" data-link>Mua đồ tập</a></div>`;
      return;
    }
    let q; let quoteErr = '';
    try { q = await quoteCart(); } catch (err) { quoteErr = err.message; }
    $('#cartBody').innerHTML = `<div class="cart">
      <div>${quoteErr ? `<div class="alert">${esc(quoteErr)}</div>` : ''}${items.map((it, idx) => { const p = map[it.id]; return `
        <div class="line">
          <a href="${B}/san-pham/${esc(p.slug)}" data-link><img src="${esc(p.images[0] || '')}" alt="${esc(p.name)}"></a>
          <div><a href="${B}/san-pham/${esc(p.slug)}" data-link style="text-decoration:none;font-weight:500">${esc(p.name)}</a>
            <div class="meta">${[it.color, it.size && `Size ${it.size}`].filter(Boolean).map(esc).join(' · ')}</div>
            ${priceHTML(p)}${p.stock < it.qty ? `<div class="err">Chỉ còn ${p.stock} sản phẩm</div>` : ''}</div>
          <div class="line-end" style="display:flex;gap:8px;align-items:center">
            <div class="qty"><button data-act="dec" data-idx="${idx}" aria-label="Giảm">−</button><input value="${it.qty}" data-idx="${idx}" aria-label="Số lượng" inputmode="numeric"><button data-act="inc" data-idx="${idx}" aria-label="Tăng">+</button></div>
            <button class="icon-btn" data-act="rm" data-idx="${idx}" aria-label="Xoá ${esc(p.name)}">${ICON.trash}</button>
          </div>
        </div>`; }).join('')}
        <p style="margin-top:20px"><a class="link" href="${B}/cua-hang" data-link>Tiếp tục mua sắm</a></p>
      </div>
      <aside class="summary"><h3 style="margin-bottom:12px">Đơn hàng</h3>${q ? summaryHTML(q, true) : ''}
        <a class="btn btn-primary btn-block" style="margin-top:16px" href="${B}/thanh-toan" data-link ${quoteErr ? 'aria-disabled="true"' : ''}>Tiến hành đặt hàng</a></aside>
    </div>`;
    const update = (idx, qty) => { const all = Cart.get(); if (qty <= 0) all.splice(idx, 1); else all[idx].qty = Math.min(99, qty); Cart.set(all); pageCart(); };
    $$('[data-act]', main).forEach((b) => (b.onclick = () => {
      const idx = Number(b.dataset.idx); const it = Cart.get()[idx];
      if (b.dataset.act === 'rm') update(idx, 0); else update(idx, it.qty + (b.dataset.act === 'inc' ? 1 : -1));
    }));
    $$('.qty input', main).forEach((i) => (i.onchange = () => update(Number(i.dataset.idx), Number(i.value) || 1)));
    bindCoupon(pageCart);
  }

  // ---------- Thanh toán ----------
  async function pageCheckout() {
    setTitle('Đặt hàng');
    if (!Cart.count()) return go('/gio-hang', true);
    main.innerHTML = `<div class="wrap"><div class="page-head"><div class="crumbs"><a href="${B}/gio-hang" data-link>Giỏ hàng</a> / Đặt hàng</div><h1 style="font-size:clamp(36px,5vw,64px)">Đặt hàng</h1></div><div id="co"><div class="skeleton" style="height:300px"></div></div></div>`;
    await loadCartProducts();
    let q;
    try { q = await quoteCart(); } catch (err) { $('#co').innerHTML = `<div class="alert">${esc(err.message)}</div><a class="btn" href="${B}/gio-hang" data-link>Quay lại giỏ hàng</a>`; return; }
    const codOn = S('cod_enabled') !== '0'; const bankOn = S('bank_enabled') !== '0';
    $('#co').innerHTML = `<form class="cart" id="coForm" novalidate>
      <div>
        <div class="alert form-alert" hidden></div>
        ${ME ? '' : `<p class="muted">Đã có tài khoản? <a class="link" href="${B}/dang-nhap?tiep=/thanh-toan" data-link>Đăng nhập</a> để lưu lịch sử đơn.</p>`}
        <h3 style="margin:8px 0 16px">Thông tin nhận hàng</h3>
        <div class="row2">${fieldHTML('name', 'Họ tên người nhận', 'autocomplete="name" required', ME ? ME.name : '')}${fieldHTML('phone', 'Số điện thoại', 'type="tel" autocomplete="tel" required', ME ? ME.phone : '')}</div>
        ${fieldHTML('email', 'Email (để nhận thông tin đơn)', 'type="email" autocomplete="email"', ME ? ME.email : '')}
        <div class="field"><label for="f-address">Địa chỉ giao hàng</label><textarea class="input" id="f-address" name="address" autocomplete="street-address" placeholder="Số nhà, đường, phường/xã, quận/huyện, tỉnh/thành">${esc(ME ? ME.address : '')}</textarea><div class="err" data-for="address"></div></div>
        <div class="field"><label for="f-note">Ghi chú (không bắt buộc)</label><textarea class="input" id="f-note" name="note" placeholder="Giao giờ hành chính, gọi trước khi giao…"></textarea></div>
        <h3 style="margin:24px 0 16px">Thanh toán</h3>
        ${codOn ? `<label class="pay-opt"><input type="radio" name="payment_method" value="cod" checked><div><b>Thanh toán khi nhận hàng (COD)</b><div class="muted" style="font-size:14px">Kiểm tra hàng rồi trả tiền cho người giao.</div></div></label>` : ''}
        ${bankOn ? `<label class="pay-opt"><input type="radio" name="payment_method" value="bank" ${codOn ? '' : 'checked'}><div><b>Chuyển khoản ngân hàng</b><div class="muted" style="font-size:14px">Thông tin tài khoản hiện sau khi đặt hàng.</div></div></label>` : ''}
        <div class="err" data-for="payment_method"></div>
      </div>
      <aside class="summary"><h3 style="margin-bottom:12px">Đơn hàng (${Cart.count()} sản phẩm)</h3>
        ${q.lines.map((l) => `<div class="mini"><img src="${esc(l.image)}" alt=""><div style="flex:1"><div>${esc(l.name)} × ${l.qty}</div><div class="muted" style="font-size:13px">${[l.color, l.size && `Size ${l.size}`].filter(Boolean).map(esc).join(' · ')}</div></div><b style="font-weight:500">${money(l.price * l.qty)}</b></div>`).join('')}
        <div style="border-top:1px solid #d9d7d1;margin-top:8px;padding-top:8px" id="sumBox">${summaryHTML(q, true)}</div>
        <button class="btn btn-primary btn-block" style="margin-top:16px" id="placeBtn">Đặt hàng · ${money(q.total)}</button>
        <p class="muted" style="font-size:12px;margin:10px 0 0">Bấm “Đặt hàng” là bạn đồng ý với <a class="link" href="${B}/trang/chinh-sach-doi-tra" data-link>chính sách đổi trả</a>.</p>
      </aside></form>`;
    bindCoupon(pageCheckout);
    const form = $('#coForm');
    form.onsubmit = async (e) => {
      e.preventDefault();
      const fd = new FormData(form);
      const body = { name: fd.get('name'), phone: fd.get('phone'), email: fd.get('email'), address: fd.get('address'), note: fd.get('note'), payment_method: fd.get('payment_method'), items: Cart.payload(), coupon: couponCode };
      const btn = $('#placeBtn'); btn.disabled = true; btn.textContent = 'Đang gửi đơn…';
      try {
        const r = await api('POST', '/orders', body);
        Cart.set([]); saveCoupon('');
        try { sessionStorage.setItem('fg_last_phone', body.phone); } catch { /* bỏ qua */ }
        go(`/dat-hang-thanh-cong/${r.code}`);
      } catch (err) {
        btn.disabled = false; btn.textContent = `Đặt hàng · ${money(q.total)}`;
        showErrors(form, err);
      }
    };
  }

  async function pageDone(code) {
    setTitle('Đặt hàng thành công');
    let phone = ''; try { phone = sessionStorage.getItem('fg_last_phone') || ''; } catch { /* bỏ qua */ }
    let o = null;
    if (phone) { try { o = await api('GET', `/orders/track?code=${encodeURIComponent(code)}&phone=${encodeURIComponent(phone)}`); } catch { o = null; } }
    const bank = o && o.payment_method === 'bank';
    main.innerHTML = `<div class="wrap"><div class="done-box">
      <div class="check">${ICON.check}</div>
      <h1 style="font-size:clamp(36px,5vw,56px)">Đã nhận đơn ${esc(code)}</h1>
      <p class="muted" style="margin-top:12px">Cửa hàng sẽ gọi xác nhận trong giờ làm việc. Lưu mã đơn để tra cứu khi cần.</p>
      ${o ? `<div class="summary" style="text-align:left;margin:24px 0">${o.items.map((l) => `<div class="mini"><img src="${esc(l.image)}" alt=""><div style="flex:1">${esc(l.name)} × ${l.qty}<div class="muted" style="font-size:13px">${[l.color, l.size && `Size ${l.size}`].filter(Boolean).map(esc).join(' · ')}</div></div><span>${money(l.price * l.qty)}</span></div>`).join('')}
        <div class="r total"><span>Tổng cộng</span><span>${money(o.total)}</span></div></div>` : ''}
      ${bank ? `<div class="bankbox" style="text-align:left"><b>Chuyển khoản để hoàn tất đơn</b><br>
        Ngân hàng: ${esc(S('bank_name'))}<br>Số tài khoản: <b>${esc(S('bank_account') || '(cửa hàng chưa cập nhật)')}</b><br>Chủ tài khoản: ${esc(S('bank_owner'))}<br>
        Số tiền: <b>${money(o.total)}</b><br>Nội dung: <b>${esc(code)}</b></div>` : ''}
      <div style="display:flex;gap:12px;justify-content:center;margin-top:28px;flex-wrap:wrap">
        <a class="btn btn-ghost" href="${B}/tra-cuu-don?ma=${esc(code)}" data-link>Tra cứu đơn</a>
        <a class="btn btn-primary" href="${B}/cua-hang" data-link>Tiếp tục mua sắm</a></div>
    </div></div>`;
  }

  // ---------- Tra cứu đơn ----------
  function orderView(o) {
    return `<div class="order-card">
      <div class="top"><b>Đơn ${esc(o.code)}</b><span class="st ${o.status}">${esc(o.status_label)}</span></div>
      <div class="muted" style="font-size:14px">Đặt lúc ${date(o.created_at)} · ${o.payment_method === 'bank' ? 'Chuyển khoản' : 'COD'} · ${o.payment_status === 'paid' ? 'Đã thanh toán' : 'Chưa thanh toán'}</div>
      ${o.items.map((l) => `<div class="mini"><img src="${esc(l.image)}" alt=""><div style="flex:1">${esc(l.name)} × ${l.qty}<div class="muted" style="font-size:13px">${[l.color, l.size && `Size ${l.size}`].filter(Boolean).map(esc).join(' · ')}</div></div><span>${money(l.price * l.qty)}</span></div>`).join('')}
      <div style="display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:10px;margin-top:6px"><span>Tổng cộng</span><b>${money(o.total)}</b></div>
      ${o.history ? `<ul class="timeline">${o.history.map((h) => `<li><b>${esc(SITE.statuses[h.status] || h.status)}</b> <span class="muted">${date(h.created_at)}</span>${h.note ? `<div class="muted">${esc(h.note)}</div>` : ''}</li>`).join('')}</ul>` : ''}
    </div>`;
  }

  function pageTrack() {
    setTitle('Tra cứu đơn hàng');
    const qs = new URLSearchParams(location.search);
    main.innerHTML = `<div class="wrap"><div class="auth" style="max-width:640px">
      <h1 style="font-size:clamp(36px,5vw,56px);margin-bottom:8px">Tra cứu đơn hàng</h1>
      <p class="muted">Nhập mã đơn và số điện thoại đã dùng khi đặt.</p>
      <form id="trackForm" novalidate><div class="alert form-alert" hidden></div>
        <div class="row2">${fieldHTML('code', 'Mã đơn hàng', 'placeholder="DH100123"', qs.get('ma') || '')}${fieldHTML('phone', 'Số điện thoại', 'type="tel"')}</div>
        <button class="btn">Tra cứu</button></form>
      <div id="trackResult" style="margin-top:28px"></div></div></div>`;
    const f = $('#trackForm');
    f.onsubmit = async (e) => {
      e.preventDefault();
      const code = f.elements.code.value.trim(); const phone = f.elements.phone.value.trim();
      if (!code || !phone) return showErrors(f, { message: 'Nhập đủ mã đơn và số điện thoại', fields: { ...(code ? {} : { code: 'Nhập mã đơn' }), ...(phone ? {} : { phone: 'Nhập số điện thoại' }) } });
      try { const o = await api('GET', `/orders/track?code=${encodeURIComponent(code)}&phone=${encodeURIComponent(phone)}`); showErrors(f, { fields: {} }); $('.form-alert', f).hidden = true; $('#trackResult').innerHTML = orderView(o); }
      catch (err) { $('#trackResult').innerHTML = ''; showErrors(f, err); }
    };
  }

  // ---------- Tài khoản ----------
  function pageAuth(mode) {
    if (ME) return go('/tai-khoan', true);
    const next = new URLSearchParams(location.search).get('tiep') || '/tai-khoan';
    const reg = mode === 'register';
    setTitle(reg ? 'Đăng ký' : 'Đăng nhập');
    main.innerHTML = `<div class="wrap"><div class="auth">
      <div class="tabs"><button class="${reg ? '' : 'on'}" data-go="/dang-nhap">Đăng nhập</button><button class="${reg ? 'on' : ''}" data-go="/dang-ky">Tạo tài khoản</button></div>
      <form id="authForm" novalidate><div class="alert form-alert" hidden></div>
        ${reg ? fieldHTML('name', 'Họ tên', 'autocomplete="name"') : ''}
        ${fieldHTML('email', 'Email', 'type="email" autocomplete="email"')}
        ${reg ? fieldHTML('phone', 'Số điện thoại (không bắt buộc)', 'type="tel" autocomplete="tel"') : ''}
        ${fieldHTML('password', 'Mật khẩu', `type="password" autocomplete="${reg ? 'new-password' : 'current-password'}"`)}
        <button class="btn btn-primary btn-block">${reg ? 'Tạo tài khoản' : 'Đăng nhập'}</button>
      </form>
      <p class="muted" style="margin-top:16px;font-size:14px">Không cần tài khoản vẫn đặt hàng được. Tài khoản giúp bạn xem lại đơn và điền sẵn địa chỉ.</p>
    </div></div>`;
    $$('[data-go]').forEach((b) => (b.onclick = () => go(b.dataset.go + location.search)));
    const f = $('#authForm');
    f.onsubmit = async (e) => {
      e.preventDefault();
      try { await api('POST', reg ? '/auth/register' : '/auth/login', Object.fromEntries(new FormData(f))); await loadMe(); go(next.startsWith('/') ? next : '/tai-khoan'); toast(reg ? 'Đã tạo tài khoản' : 'Đã đăng nhập'); }
      catch (err) { showErrors(f, err); }
    };
  }

  async function pageAccount() {
    if (!ME) return go('/dang-nhap', true);
    setTitle('Tài khoản');
    const tab = new URLSearchParams(location.search).get('tab') || 'orders';
    main.innerHTML = `<div class="wrap" style="padding-bottom:80px"><div class="page-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap">
      <div><h1 style="font-size:clamp(36px,5vw,56px)">Xin chào, ${esc(ME.name)}</h1><p class="muted" style="margin:6px 0 0">${esc(ME.email)}</p></div>
      <button class="btn btn-ghost" id="logout">Đăng xuất</button></div>
      <div class="tabs">${[['orders', 'Đơn hàng'], ['profile', 'Thông tin'], ['password', 'Đổi mật khẩu']].map(([k, l]) => `<button class="${k === tab ? 'on' : ''}" data-tab="${k}">${l}</button>`).join('')}</div>
      <div id="tabBody" style="max-width:760px"></div></div>`;
    $('#logout').onclick = async () => { await api('POST', '/auth/logout'); ME = null; go('/'); toast('Đã đăng xuất'); };
    $$('[data-tab]').forEach((b) => (b.onclick = () => go(`/tai-khoan?tab=${b.dataset.tab}`, true)));
    const body = $('#tabBody');
    if (tab === 'orders') {
      const orders = await api('GET', '/account/orders');
      body.innerHTML = orders.length ? orders.map((o) => orderView(o) + (o.status === 'pending' ? `<button class="btn btn-ghost" data-cancel="${esc(o.code)}" style="margin:-4px 0 18px">Huỷ đơn ${esc(o.code)}</button>` : '')).join('')
        : `<div class="empty"><p>Bạn chưa có đơn hàng nào.</p><a class="btn btn-primary" href="${B}/cua-hang" data-link>Mua đồ tập</a></div>`;
      $$('[data-cancel]').forEach((b) => (b.onclick = async () => {
        if (!confirm(`Huỷ đơn ${b.dataset.cancel}?`)) return;
        try { await api('POST', `/account/orders/${b.dataset.cancel}/cancel`); toast('Đã huỷ đơn'); pageAccount(); } catch (err) { toast(esc(err.message)); }
      }));
    } else if (tab === 'profile') {
      body.innerHTML = `<form id="pf" novalidate><div class="alert form-alert" hidden></div>
        <div class="row2">${fieldHTML('name', 'Họ tên', 'autocomplete="name"', ME.name)}${fieldHTML('phone', 'Số điện thoại', 'type="tel"', ME.phone)}</div>
        <div class="field"><label for="f-address">Địa chỉ giao hàng mặc định</label><textarea class="input" id="f-address" name="address">${esc(ME.address)}</textarea><div class="err" data-for="address"></div></div>
        <button class="btn">Lưu thông tin</button></form>`;
      const f = $('#pf');
      f.onsubmit = async (e) => { e.preventDefault(); try { await api('PUT', '/account', Object.fromEntries(new FormData(f))); await loadMe(); toast('Đã lưu thông tin'); showErrors(f, { fields: {} }); $('.form-alert', f).hidden = true; } catch (err) { showErrors(f, err); } };
    } else {
      body.innerHTML = `<form id="pw" novalidate style="max-width:420px"><div class="alert form-alert" hidden></div>
        ${fieldHTML('current', 'Mật khẩu hiện tại', 'type="password" autocomplete="current-password"')}
        ${fieldHTML('password', 'Mật khẩu mới', 'type="password" autocomplete="new-password"')}
        <button class="btn">Đổi mật khẩu</button></form>`;
      const f = $('#pw');
      f.onsubmit = async (e) => { e.preventDefault(); try { await api('PUT', '/account/password', Object.fromEntries(new FormData(f))); f.reset(); toast('Đã đổi mật khẩu'); $('.form-alert', f).hidden = true; } catch (err) { showErrors(f, err); } };
    }
  }

  // ---------- Trang nội dung ----------
  async function pageStatic(slug) {
    let pg;
    try { pg = await api('GET', `/pages/${encodeURIComponent(slug)}`); } catch { return pageNotFound(); }
    setTitle(pg.title);
    main.innerHTML = `<div class="wrap"><div class="page-head"><div class="crumbs"><a href="${B}/" data-link>Trang chủ</a> / ${esc(pg.title)}</div><h1 style="font-size:clamp(36px,5vw,64px)">${esc(pg.title)}</h1></div>
      <article class="rich" style="max-width:760px;padding-bottom:96px">${pg.content}</article></div>`;
  }

  function pageNotFound() {
    setTitle('Không tìm thấy trang');
    main.innerHTML = `<div class="wrap"><div class="done-box"><h1>Không tìm thấy trang</h1><p class="muted" style="margin:12px 0 24px">Đường dẫn có thể đã đổi hoặc sản phẩm đã ngừng bán.</p><a class="btn btn-primary" href="${B}/cua-hang" data-link>Xem sản phẩm</a></div></div>`;
  }

  // ---------- Định tuyến ----------
  const routes = [
    [/^\/$/, pageHome],
    [/^\/cua-hang\/?$/, pageShop],
    [/^\/san-pham\/([^/]+)\/?$/, pageProduct],
    [/^\/gio-hang\/?$/, pageCart],
    [/^\/thanh-toan\/?$/, pageCheckout],
    [/^\/dat-hang-thanh-cong\/([^/]+)\/?$/, pageDone],
    [/^\/tra-cuu-don\/?$/, pageTrack],
    [/^\/dang-nhap\/?$/, () => pageAuth('login')],
    [/^\/dang-ky\/?$/, () => pageAuth('register')],
    [/^\/tai-khoan\/?$/, pageAccount],
    [/^\/trang\/([^/]+)\/?$/, pageStatic],
  ];

  async function render() {
    const full = decodeURI(location.pathname);
    const path = full === B ? '/' : full.startsWith(`${B}/`) ? full.slice(B.length) || '/' : full;
    $('#drawer').hidden = true; $('#menuBtn').setAttribute('aria-expanded', 'false');
    $$('#nav a').forEach((a) => a.classList.toggle('active', a.getAttribute('href') === location.pathname + location.search));
    for (const [re, fn] of routes) {
      const m = path.match(re);
      if (m) {
        try { await fn(...m.slice(1).map(decodeURIComponent)); }
        catch (err) { console.error(err); main.innerHTML = `<div class="wrap"><div class="done-box"><h1>Có lỗi khi tải trang</h1><p class="muted">${esc(err.message)}</p><button class="btn" onclick="location.reload()">Tải lại trang</button></div></div>`; }
        return;
      }
    }
    pageNotFound();
  }

  function go(url, replace) {
    url = L(url);
    if (replace) history.replaceState(null, '', url); else history.pushState(null, '', url);
    const samePage = url.includes('#');
    render().then(() => { if (!samePage) window.scrollTo(0, 0); });
  }

  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[data-link]');
    if (!a || e.ctrlKey || e.metaKey || e.shiftKey || a.target === '_blank') return;
    const url = new URL(a.href, location.origin);
    if (url.origin !== location.origin) return;
    e.preventDefault();
    go(url.pathname + url.search);
  });
  window.addEventListener('popstate', render);

  const onSearch = (e) => { e.preventDefault(); const q = new FormData(e.target).get('q').trim(); go(q ? `/cua-hang?q=${encodeURIComponent(q)}` : '/cua-hang'); };
  $('#searchForm').onsubmit = onSearch;
  $('#searchFormM').onsubmit = onSearch;
  $('#menuBtn').onclick = () => { $('#drawer').hidden = false; $('#menuBtn').setAttribute('aria-expanded', 'true'); $('#drawerClose').focus(); };
  $('#drawerClose').onclick = () => { $('#drawer').hidden = true; $('#menuBtn').setAttribute('aria-expanded', 'false'); };
  $('#drawer').onclick = (e) => { if (e.target.id === 'drawer') $('#drawerClose').click(); };
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !$('#drawer').hidden) $('#drawerClose').click(); });

  async function loadMe() { ME = (await api('GET', '/auth/me')).customer; }

  (async function init() {
    Cart.badge();
    try { [SITE] = await Promise.all([api('GET', '/site'), loadMe()]); } catch (err) { main.innerHTML = `<div class="wrap"><div class="done-box"><h1>Không kết nối được máy chủ</h1><p class="muted">${esc(err.message)}</p></div></div>`; return; }
    applyTheme();
    render();
  })();
})();
