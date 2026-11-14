/* Trang quản trị cửa hàng */
(() => {
  'use strict';

  // ================= Tiện ích =================
  const B = '/ban-hang';
  const API = '/api/node/ban-hang';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const app = $('#app');
  const esc = (v) => String(v == null ? '' : v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const money = (n) => `${Number(n || 0).toLocaleString('vi-VN')} ₫`;
  const short = (n) => (n >= 1e6 ? `${(n / 1e6).toLocaleString('vi-VN', { maximumFractionDigits: 1 })} tr` : n >= 1e3 ? `${Math.round(n / 1e3)}k` : String(n));
  const dt = (s) => (s ? new Date(s.replace(' ', 'T')).toLocaleString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }) : '');
  const d = (s) => (s ? new Date(s.replace(' ', 'T')).toLocaleDateString('vi-VN') : '');
  const STATUS = { pending: 'Chờ xác nhận', confirmed: 'Đã xác nhận', shipping: 'Đang giao', completed: 'Hoàn thành', cancelled: 'Đã huỷ' };
  const I = (p) => `<svg class="i" viewBox="0 0 24 24" aria-hidden="true">${p}</svg>`;
  const IC = {
    dash: I('<path d="M4 13h6V4H4zM14 20h6v-9h-6zM4 20h6v-4H4zM14 8h6V4h-6z"/>'),
    order: I('<path d="M6 3h12l1 18H5zM9 7a3 3 0 0 0 6 0"/>'),
    box: I('<path d="M3 7l9-4 9 4-9 4zM3 7v10l9 4 9-4V7M12 11v10"/>'),
    tag: I('<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>'),
    users: I('<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-6 7-6s7 2.5 7 6M16 4.5a3.5 3.5 0 0 1 0 7M22 20c0-3-2-5.2-5-5.8"/>'),
    star: I('<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>'),
    ticket: I('<path d="M3 8a2 2 0 0 0 0 4v4h18v-4a2 2 0 0 1 0-4V4H3zM14 4v16"/>'),
    paint: I('<path d="M4 4h16v6H4zM12 10v4M10 14h4v7h-4z"/>'),
    file: I('<path d="M6 3h8l4 4v14H6zM14 3v4h4M9 13h6M9 17h6"/>'),
    gear: I('<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>'),
    shield: I('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/>'),
    cat: I('<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/>'),
    plus: I('<path d="M12 5v14M5 12h14"/>'),
    edit: I('<path d="M4 20h4L19 9l-4-4L4 16z"/>'),
    trash: I('<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/>'),
    ext: I('<path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6"/>'),
    menu: I('<path d="M3 6h18M3 12h18M3 18h18"/>'),
    x: I('<path d="M6 6l12 12M18 6 6 18"/>'),
    up: I('<path d="M12 19V5M5 12l7-7 7 7"/>'),
    dl: I('<path d="M12 4v12M6 10l6 6 6-6M4 20h16"/>'),
    print: I('<path d="M6 9V3h12v6M6 18H4v-7h16v7h-2M7 14h10v7H7z"/>'),
    img: I('<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 17-5-5-9 8"/>'),
  };

  async function api(method, url, body) {
    const res = await fetch(`${API}/admin${url}`, {
      method, credentials: 'same-origin',
      headers: body ? { 'Content-Type': 'application/json' } : {},
      body: body ? JSON.stringify(body) : undefined,
    });
    const data = await res.json().catch(() => ({}));
    if (res.status === 401 && !url.startsWith('/login')) { ME = null; renderLogin(); throw Object.assign(new Error(data.error || 'Phiên đăng nhập đã hết hạn'), { silent: true }); }
    if (!res.ok) throw Object.assign(new Error(data.error || 'Có lỗi xảy ra'), { fields: data.fields || {} });
    return data;
  }

  // Thu nhỏ ảnh ngay trên trình duyệt (cạnh dài tối đa 1600px, JPEG) rồi gửi từng ảnh,
  // vì function trên Vercel chỉ nhận tối đa 4,5MB mỗi lần gửi. GIF giữ nguyên để không mất chuyển động.
  async function shrink(file) {
    if (!/^image\/(jpeg|png|webp|gif|avif)$/.test(file.type)) throw new Error('Chỉ nhận file ảnh jpg, png, webp, gif');
    const toB64 = (blob) => new Promise((ok, bad) => { const r = new FileReader(); r.onload = () => ok(String(r.result).split(',')[1]); r.onerror = bad; r.readAsDataURL(blob); });
    if (file.type === 'image/gif') return { type: file.type, data: await toB64(file) };
    const bmp = await createImageBitmap(file);
    const k = Math.min(1, 1600 / Math.max(bmp.width, bmp.height));
    const c = document.createElement('canvas');
    c.width = Math.round(bmp.width * k); c.height = Math.round(bmp.height * k);
    const g = c.getContext('2d');
    g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height);
    g.drawImage(bmp, 0, 0, c.width, c.height);
    const blob = await new Promise((ok) => c.toBlob(ok, 'image/jpeg', 0.84));
    return { type: 'image/jpeg', data: await toB64(blob) };
  }

  async function upload(files) {
    const urls = [];
    for (const f of [...files]) {
      const one = await shrink(f);
      const res = await fetch(`${API}/admin/upload`, { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ files: [one] }) });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || 'Tải ảnh thất bại');
      urls.push(...data.urls);
    }
    return urls;
  }

  let toastT;
  function toast(msg, bad) {
    const t = $('#toast'); t.textContent = msg; t.className = `toast show${bad ? ' bad' : ''}`;
    clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('show'), 3000);
  }
  const fail = (err) => { if (!err.silent) toast(err.message, true); };

  function showErrors(root, err) {
    $$('.err', root).forEach((e) => (e.textContent = ''));
    $$('.bad', root).forEach((e) => e.classList.remove('bad'));
    const box = $('.form-alert', root);
    if (!err) { if (box) box.hidden = true; return; }
    let placed = false;
    for (const [k, m] of Object.entries(err.fields || {})) {
      const slot = $(`.err[data-for="${k}"]`, root);
      const inp = $(`[name="${k}"]`, root);
      if (inp) inp.classList.add('bad');
      if (slot) { slot.textContent = m; placed = true; }
    }
    if (box) { box.hidden = false; box.textContent = err.message; }
    else if (!placed) toast(err.message, true);
    const b = $('.bad', root); if (b) b.focus();
  }

  // ================= Bộ dựng form =================
  // spec: { name, label, type, col, help, options:[[value,label]], placeholder }
  function fieldsHTML(spec, v = {}) {
    return `<div class="form-grid">${spec.map((f) => {
      if (f.type === 'heading') return `<h2 style="grid-column:span 12;margin-top:8px">${esc(f.label)}</h2>`;
      const val = v[f.name] == null ? (f.default == null ? '' : f.default) : v[f.name];
      const id = `fld-${f.name}`;
      const col = f.col ? ` c${f.col}` : '';
      const help = f.help ? `<div class="help">${f.help}</div>` : '';
      const err = `<div class="err" data-for="${f.name}"></div>`;
      const ph = f.placeholder ? ` placeholder="${esc(f.placeholder)}"` : '';
      let input;
      switch (f.type) {
        case 'textarea': input = `<textarea class="input" id="${id}" name="${f.name}"${ph} rows="${f.rows || 3}">${esc(val)}</textarea>`; break;
        case 'select': input = `<select class="input" id="${id}" name="${f.name}">${f.options.map(([o, l]) => `<option value="${esc(o)}" ${String(o) === String(val) ? 'selected' : ''}>${esc(l)}</option>`).join('')}</select>`; break;
        case 'switch': return `<div class="field${col}"><label class="check"><span class="switch"><input type="checkbox" name="${f.name}" ${val && val !== '0' ? 'checked' : ''}><span></span></span>${esc(f.label)}</label>${help}${err}</div>`;
        case 'color': input = `<div class="color-row"><input type="color" value="${esc(val || '#000000')}" data-pair="${id}" aria-label="Chọn màu"><input class="input" id="${id}" name="${f.name}" value="${esc(val)}" style="width:120px"></div>`; break;
        case 'image': input = `<div class="single-img" data-img="${f.name}"><input type="hidden" name="${f.name}" value="${esc(val)}"><img src="${esc(val)}" alt="" ${val ? '' : 'hidden'}><div style="display:flex;gap:6px;flex-wrap:wrap"><label class="btn btn-sm">${IC.img} ${val ? 'Đổi ảnh' : 'Tải ảnh'}<input type="file" accept="image/*" hidden></label><button type="button" class="btn btn-sm btn-danger" data-clear ${val ? '' : 'hidden'}>Xoá ảnh</button></div></div>`; break;
        case 'images': input = `<div class="imgs" data-imgs="${f.name}" data-val="${esc(JSON.stringify(val || []))}"></div>`; break;
        case 'rich': input = `<div class="rte" data-rte="${f.name}"><div class="tb">
            <button type="button" data-cmd="bold" title="Đậm"><b>B</b></button><button type="button" data-cmd="italic" title="Nghiêng"><i>I</i></button>
            <button type="button" data-cmd="formatBlock" data-arg="h3" title="Tiêu đề">H</button><button type="button" data-cmd="formatBlock" data-arg="p" title="Đoạn văn">¶</button>
            <button type="button" data-cmd="insertUnorderedList" title="Danh sách">•</button><button type="button" data-cmd="insertOrderedList" title="Danh sách số">1.</button>
            <button type="button" data-cmd="createLink" title="Chèn link">🔗</button><button type="button" data-cmd="insertImage" title="Chèn ảnh">${IC.img}</button>
            <button type="button" data-cmd="removeFormat" title="Xoá định dạng">✕</button><button type="button" data-src title="Sửa HTML" style="margin-left:auto;font-weight:500;font-size:12px">HTML</button>
          </div><div class="ed" contenteditable="true" id="${id}"></div><textarea hidden aria-label="Mã HTML"></textarea><input type="file" accept="image/*" hidden></div>`; break;
        default: input = `<input class="input" id="${id}" name="${f.name}" type="${f.type || 'text'}" value="${esc(val)}"${ph}${f.type === 'number' ? ' min="0" step="1"' : ''}>`;
      }
      return `<div class="field${col}"><label for="${id}" class="lbl">${esc(f.label)}</label>${input}${help}${err}</div>`;
    }).join('')}</div>`;
  }

  function mountFields(root, spec, v = {}) {
    $$('input[type=color][data-pair]', root).forEach((c) => {
      const t = $(`#${c.dataset.pair}`, root);
      c.oninput = () => (t.value = c.value);
      t.oninput = () => { if (/^#[0-9a-f]{6}$/i.test(t.value)) c.value = t.value; };
    });
    $$('[data-img]', root).forEach((box) => {
      const hidden = $('input[type=hidden]', box); const img = $('img', box); const file = $('input[type=file]', box); const clr = $('[data-clear]', box);
      file.onchange = async () => {
        if (!file.files.length) return;
        try { const [u] = await upload(file.files); hidden.value = u; img.src = u; img.hidden = false; clr.hidden = false; } catch (e) { toast(e.message, true); }
        file.value = '';
      };
      clr.onclick = () => { hidden.value = ''; img.hidden = true; clr.hidden = true; };
    });
    $$('[data-imgs]', root).forEach((box) => {
      box._value = JSON.parse(box.dataset.val || '[]');
      const draw = () => {
        box.innerHTML = box._value.map((u, i) => `<div class="it">${i === 0 ? '<span class="first">Ảnh chính</span>' : ''}<img src="${esc(u)}" alt="">
          <div class="bar"><button type="button" data-mv="-1" data-i="${i}" aria-label="Lên trước">←</button><button type="button" data-rm="${i}" aria-label="Xoá ảnh">✕</button><button type="button" data-mv="1" data-i="${i}" aria-label="Ra sau">→</button></div></div>`).join('')
          + `<label class="upload">${IC.plus}<span>Thêm ảnh<br>(chọn nhiều)</span><input type="file" accept="image/*" multiple hidden></label>`;
        $('input[type=file]', box).onchange = async (e) => {
          try { box._value.push(...await upload(e.target.files)); draw(); } catch (er) { toast(er.message, true); }
        };
        $$('[data-rm]', box).forEach((b) => (b.onclick = () => { box._value.splice(+b.dataset.rm, 1); draw(); }));
        $$('[data-mv]', box).forEach((b) => (b.onclick = () => {
          const i = +b.dataset.i; const j = i + +b.dataset.mv; if (j < 0 || j >= box._value.length) return;
          [box._value[i], box._value[j]] = [box._value[j], box._value[i]]; draw();
        }));
      };
      draw();
    });
    $$('[data-rte]', root).forEach((box) => {
      const ed = $('.ed', box); const ta = $('textarea', box); const file = $('input[type=file]', box);
      ed.innerHTML = v[box.dataset.rte] || '';
      $$('[data-cmd]', box).forEach((b) => (b.onclick = () => {
        ed.focus();
        if (b.dataset.cmd === 'createLink') { const u = prompt('Địa chỉ liên kết (https://… hoặc /trang/...)'); if (u) document.execCommand('createLink', false, u); return; }
        if (b.dataset.cmd === 'insertImage') { file.click(); return; }
        document.execCommand(b.dataset.cmd, false, b.dataset.arg ? `<${b.dataset.arg}>` : null);
      }));
      file.onchange = async () => { try { const [u] = await upload(file.files); ed.focus(); document.execCommand('insertImage', false, u); } catch (e) { toast(e.message, true); } file.value = ''; };
      $('[data-src]', box).onclick = (e) => {
        const toSrc = ta.hidden;
        if (toSrc) { ta.value = ed.innerHTML; } else { ed.innerHTML = ta.value; }
        ta.hidden = !toSrc; ed.hidden = toSrc; e.currentTarget.classList.toggle('on', toSrc);
      };
    });
    void spec;
  }

  function readFields(root, spec) {
    const out = {};
    for (const f of spec) {
      if (f.type === 'heading') continue;
      if (f.type === 'images') { out[f.name] = $(`[data-imgs="${f.name}"]`, root)._value; continue; }
      if (f.type === 'rich') { const b = $(`[data-rte="${f.name}"]`, root); const ta = $('textarea', b); out[f.name] = ta.hidden ? $('.ed', b).innerHTML : ta.value; continue; }
      const el = $(`[name="${f.name}"]`, root);
      if (!el) continue;
      out[f.name] = f.type === 'switch' ? el.checked : el.value.trim();
    }
    return out;
  }

  // ================= Hộp thoại =================
  function modal({ title, body, wide, saveText = 'Lưu', onSave, onOpen, foot }) {
    const bg = document.createElement('div');
    bg.className = 'modal-bg';
    bg.innerHTML = `<div class="modal ${wide ? 'wide' : ''}" role="dialog" aria-modal="true" aria-label="${esc(title)}">
      <div class="mh"><h2 style="margin:0">${esc(title)}</h2><button class="btn btn-icon" data-close aria-label="Đóng">${IC.x}</button></div>
      <form class="mb" novalidate><div class="alert form-alert" hidden></div>${body}</form>
      <div class="mf">${foot || ''}<span style="flex:1"></span><button class="btn" data-close type="button">Huỷ</button>${onSave ? `<button class="btn btn-primary" data-save>${esc(saveText)}</button>` : ''}</div></div>`;
    document.body.appendChild(bg);
    const prevFocus = document.activeElement;
    const close = () => { bg.remove(); document.removeEventListener('keydown', onKey); if (prevFocus) prevFocus.focus(); };
    const onKey = (e) => { if (e.key === 'Escape') close(); };
    document.addEventListener('keydown', onKey);
    $$('[data-close]', bg).forEach((b) => (b.onclick = close));
    bg.addEventListener('mousedown', (e) => { if (e.target === bg) close(); });
    const form = $('form', bg);
    const save = async () => {
      const btn = $('[data-save]', bg); btn.disabled = true;
      try { await onSave(form, close); } catch (err) { if (!err.silent) showErrors(form, err); } finally { btn.disabled = false; }
    };
    if (onSave) { $('[data-save]', bg).onclick = save; form.onsubmit = (e) => { e.preventDefault(); save(); }; }
    if (onOpen) onOpen(form, close, bg);
    const first = $('input:not([type=hidden]):not([type=file]), select, textarea', form); if (first) first.focus();
    return { el: bg, form, close };
  }
  const confirmBox = (msg, okText = 'Xoá') => new Promise((resolve) => {
    modal({ title: 'Xác nhận', body: `<p style="margin:0">${msg}</p>`, saveText: okText, onSave: (_f, close) => { close(); resolve(true); } });
  });

  const pager = (data, onPage) => {
    if (!data.pages || data.pages <= 1) return '';
    const btns = [];
    for (let i = 1; i <= data.pages; i++) if (i === 1 || i === data.pages || Math.abs(i - data.page) <= 2) btns.push(i); else if (btns[btns.length - 1] !== '…') btns.push('…');
    setTimeout(() => $$('[data-page]').forEach((b) => (b.onclick = () => onPage(+b.dataset.page))));
    return `<div class="pager"><span class="muted" style="margin-right:auto">${data.total} mục</span>${btns.map((p) => (p === '…' ? '<span>…</span>' : `<button class="btn btn-sm ${p === data.page ? 'btn-primary' : ''}" data-page="${p}">${p}</button>`)).join('')}</div>`;
  };
  const qsOf = (o) => new URLSearchParams(Object.entries(o).filter(([, v]) => v !== '' && v != null)).toString();
  const debounce = (fn, ms = 300) => { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; };

  // ================= Khung trang =================
  let ME = null;
  let PENDING = 0;
  const NAV = [
    ['', null, [['dashboard', 'Tổng quan', IC.dash], ['orders', 'Đơn hàng', IC.order], ['products', 'Sản phẩm', IC.box], ['categories', 'Danh mục', IC.cat], ['customers', 'Khách hàng', IC.users], ['reviews', 'Đánh giá', IC.star], ['coupons', 'Mã giảm giá', IC.ticket]]],
    ['Giao diện', 'admin', [['appearance', 'Trang chủ và banner', IC.paint], ['menu', 'Menu', IC.menu], ['pages', 'Trang nội dung', IC.file]]],
    ['Hệ thống', 'admin', [['settings', 'Cài đặt cửa hàng', IC.gear], ['staff', 'Nhân viên', IC.shield]]],
  ];

  function shell() {
    app.innerHTML = `<div class="layout">
      <aside class="side" id="side">
        <div class="logo">${IC.box}<div>Quản trị<small id="storeName"></small></div></div>
        <nav aria-label="Quản trị">${NAV.filter(([, role]) => !role || ME.role === role).map(([g, , items]) => `${g ? `<div class="grp">${g}</div>` : ''}${items.map(([k, l, ic]) => `<a href="#/${k}" data-nav="${k}">${ic}<span>${l}</span>${k === 'orders' ? '<span class="cnt" id="pendingCnt" hidden></span>' : ''}</a>`).join('')}`).join('')}</nav>
      </aside>
      <div>
        <header class="top">
          <button class="btn btn-icon menu-btn" id="menuBtn" aria-label="Mở menu">${IC.menu}</button>
          <span class="sp"></span>
          <a class="btn btn-sm" href="${B}/" target="_blank" rel="noopener">${IC.ext} Xem cửa hàng</a>
          <button class="btn btn-sm" id="pwBtn">${esc(ME.name)} · ${ME.role === 'admin' ? 'Quản trị viên' : 'Nhân viên'}</button>
          <button class="btn btn-sm" id="logoutBtn">Đăng xuất</button>
        </header>
        <main class="content" id="view"></main>
      </div></div>`;
    $('#menuBtn').onclick = () => $('#side').classList.toggle('open');
    $('#logoutBtn').onclick = async () => { await api('POST', '/logout'); ME = null; location.hash = ''; renderLogin(); };
    $('#pwBtn').onclick = changePassword;
    fetch(`${API}/site`).then((r) => r.json()).then((s) => { $('#storeName').textContent = s.settings.store_name || ''; }).catch(() => {});
  }

  function setPending(n) { PENDING = n; const c = $('#pendingCnt'); if (c) { c.textContent = n; c.hidden = !n; } }

  function changePassword() {
    const spec = [{ name: 'current', label: 'Mật khẩu hiện tại', type: 'password' }, { name: 'password', label: 'Mật khẩu mới (tối thiểu 6 ký tự)', type: 'password' }];
    modal({ title: 'Đổi mật khẩu', body: fieldsHTML(spec), saveText: 'Đổi mật khẩu', onSave: async (f, close) => { await api('PUT', '/me/password', readFields(f, spec)); close(); toast('Đã đổi mật khẩu'); } });
  }

  function renderLogin() {
    app.innerHTML = `<div class="login"><form class="card" id="loginForm" novalidate>
      <h1>Đăng nhập quản trị</h1><p class="muted" style="margin:0 0 18px">Dành cho chủ cửa hàng và nhân viên.</p>
      <div class="alert form-alert" hidden></div>
      <div class="field"><label for="le">Email</label><input class="input" id="le" name="email" type="email" autocomplete="username"></div>
      <div class="field"><label for="lp">Mật khẩu</label><input class="input" id="lp" name="password" type="password" autocomplete="current-password"></div>
      <button class="btn btn-primary" style="width:100%;height:42px">Đăng nhập</button>
      <p style="margin:16px 0 0;text-align:center"><a href="${B}/">Về trang cửa hàng</a></p></form></div>`;
    const f = $('#loginForm');
    $('#le').focus();
    f.onsubmit = async (e) => {
      e.preventDefault();
      try { await api('POST', '/login', { email: f.email.value, password: f.password.value }); await boot(); }
      catch (err) { showErrors(f, err); }
    };
  }

  // ================= Tổng quan =================
  async function viewDashboard(v) {
    const x = await api('GET', '/dashboard');
    setPending(x.pending);
    const pct = x.revenue_prev_month ? Math.round(((x.revenue_month - x.revenue_prev_month) / x.revenue_prev_month) * 100) : null;
    const max = Math.max(1, ...x.chart.map((c) => c.revenue));
    const sc = Object.fromEntries(x.status_counts.map((s) => [s.status, s.n]));
    v.innerHTML = `<div class="page-title"><h1>Tổng quan</h1><span class="muted">${new Date().toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })}</span></div>
      <div class="kpis">
        <div class="kpi"><div class="l">Doanh thu tháng này</div><div class="v">${money(x.revenue_month)}</div><div class="d ${pct == null ? 'muted' : pct >= 0 ? 'up' : 'down'}">${pct == null ? 'Chưa có số liệu tháng trước' : `${pct >= 0 ? '▲' : '▼'} ${Math.abs(pct)}% so với tháng trước`}</div></div>
        <div class="kpi"><div class="l">Đơn hàng tháng này</div><div class="v">${x.orders_month}</div><div class="d muted">${x.orders_today} đơn hôm nay</div></div>
        <div class="kpi"><div class="l">Đơn chờ xác nhận</div><div class="v" style="color:${x.pending ? 'var(--amber)' : 'inherit'}">${x.pending}</div><div class="d"><a href="#/orders?status=pending">Xử lý ngay</a></div></div>
        <div class="kpi"><div class="l">Khách hàng</div><div class="v">${x.customers}</div><div class="d muted">${x.customers_month} khách mới tháng này</div></div>
      </div>
      <div class="cols">
        <div class="card"><h2>Doanh thu 14 ngày</h2>
          <div class="chart">${x.chart.map((c) => `<div class="b"><div class="bar" style="height:${Math.round((c.revenue / max) * 160)}px"><span class="tip">${money(c.revenue)} · ${c.orders} đơn</span></div><span>${c.date.slice(8)}/${c.date.slice(5, 7)}</span></div>`).join('')}</div>
        </div>
        <div class="card"><h2>Trạng thái đơn hàng</h2>
          ${Object.entries(STATUS).map(([k, l]) => `<a class="list-row" href="#/orders?status=${k}" style="text-decoration:none;color:inherit"><span class="st ${k}">${l}</span><span class="grow"></span><b>${sc[k] || 0}</b></a>`).join('')}
          ${x.reviews_pending ? `<div class="alert info" style="margin:14px 0 0">${x.reviews_pending} đánh giá đang chờ duyệt. <a href="#/reviews">Xem</a></div>` : ''}
        </div>
      </div>
      <div class="cols" style="margin-top:16px">
        <div class="card"><h2>Đơn hàng mới</h2>
          <table class="tbl"><thead><tr><th>Mã</th><th>Khách</th><th>Ngày</th><th class="num">Tổng</th><th>Trạng thái</th></tr></thead>
          <tbody>${x.recent_orders.map((o) => `<tr class="click" data-href="#/orders/${o.id}"><td><b>${esc(o.code)}</b></td><td>${esc(o.name)}</td><td>${dt(o.created_at)}</td><td class="num">${money(o.total)}</td><td><span class="st ${o.status}">${STATUS[o.status]}</span></td></tr>`).join('') || '<tr><td colspan="5" class="empty">Chưa có đơn hàng</td></tr>'}</tbody></table>
        </div>
        <div>
          <div class="card"><h2>Bán chạy 14 ngày</h2>${x.top_products.map((p, i) => `<div class="list-row"><b style="width:18px">${i + 1}</b><span class="grow">${esc(p.name)}</span><span class="muted">${p.qty} sp</span></div>`).join('') || '<p class="muted">Chưa có dữ liệu</p>'}</div>
          <div class="card"><h2>Sắp hết hàng (≤ ${x.low_stock_threshold})</h2>${x.low_stock.map((p) => `<a class="list-row" href="#/products/${p.id}" style="text-decoration:none;color:inherit">${p.image ? `<img src="${esc(p.image)}" alt="">` : ''}<span class="grow">${esc(p.name)}</span><span class="st ${p.stock ? 'pending' : 'cancelled'}">Còn ${p.stock}</span></a>`).join('') || '<p class="muted">Kho đang đủ hàng</p>'}</div>
        </div>
      </div>`;
    $$('tr[data-href]', v).forEach((tr) => (tr.onclick = () => (location.hash = tr.dataset.href)));
  }

  // ================= Đơn hàng =================
  async function viewOrders(v, params) {
    const st = { status: params.get('status') || '', q: params.get('q') || '', from: '', to: '', payment: '', page: 1 };
    v.innerHTML = `<div class="page-title"><h1>Đơn hàng</h1><a class="btn" id="exportBtn" href="#">${IC.dl} Xuất Excel (CSV)</a></div>
      <div class="tabs" id="stTabs"></div>
      <div class="filters">
        <input class="input" id="q" placeholder="Tìm mã đơn, tên, SĐT, email" value="${esc(st.q)}" style="min-width:260px" aria-label="Tìm đơn">
        <select class="input" id="pay" aria-label="Thanh toán"><option value="">Mọi trạng thái thanh toán</option><option value="paid">Đã thanh toán</option><option value="unpaid">Chưa thanh toán</option></select>
        <label class="muted">Từ <input class="input" type="date" id="from"></label><label class="muted">đến <input class="input" type="date" id="to"></label>
      </div><div id="tbl"></div>`;
    const load = async () => {
      const data = await api('GET', `/orders?${qsOf({ ...st, limit: 20 })}`);
      setPending(data.counts.pending || 0);
      const total = Object.values(data.counts).reduce((a, b) => a + b, 0);
      $('#stTabs').innerHTML = [['', 'Tất cả', total], ...Object.entries(STATUS).map(([k, l]) => [k, l, data.counts[k] || 0])]
        .map(([k, l, n]) => `<button class="${st.status === k ? 'on' : ''}" data-st="${k}">${l}<span class="n">${n}</span></button>`).join('');
      $$('[data-st]', v).forEach((b) => (b.onclick = () => { st.status = b.dataset.st; st.page = 1; load(); }));
      $('#exportBtn').href = `${API}/admin/orders/export.csv?${qsOf({ status: st.status, q: st.q, from: st.from, to: st.to, payment: st.payment })}`;
      $('#tbl').innerHTML = `<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Mã đơn</th><th>Ngày đặt</th><th>Khách hàng</th><th>SL</th><th class="num">Tổng tiền</th><th>Thanh toán</th><th>Trạng thái</th></tr></thead><tbody>
        ${data.items.map((o) => `<tr class="click" data-id="${o.id}"><td><b>${esc(o.code)}</b></td><td>${dt(o.created_at)}</td><td>${esc(o.name)}<div class="muted" style="font-size:12px">${esc(o.phone)}</div></td><td>${o.item_count || 0}</td>
          <td class="num"><b>${money(o.total)}</b></td><td><span class="st ${o.payment_status}">${o.payment_status === 'paid' ? 'Đã TT' : 'Chưa TT'}</span> <span class="muted" style="font-size:12px">${o.payment_method === 'bank' ? 'CK' : 'COD'}</span></td><td><span class="st ${o.status}">${STATUS[o.status]}</span></td></tr>`).join('') || '<tr><td colspan="7" class="empty">Không có đơn hàng phù hợp</td></tr>'}
        </tbody></table></div>${pager(data, (p) => { st.page = p; load(); })}`;
      $$('tr[data-id]', v).forEach((tr) => (tr.onclick = () => (location.hash = `#/orders/${tr.dataset.id}`)));
    };
    $('#q').oninput = debounce((e) => { st.q = e.target.value.trim(); st.page = 1; load(); });
    $('#pay').onchange = (e) => { st.payment = e.target.value; st.page = 1; load(); };
    $('#from').onchange = (e) => { st.from = e.target.value; st.page = 1; load(); };
    $('#to').onchange = (e) => { st.to = e.target.value; st.page = 1; load(); };
    await load();
  }

  async function viewOrder(v, id) {
    const o = await api('GET', `/orders/${id}`);
    const next = { pending: 'confirmed', confirmed: 'shipping', shipping: 'completed' }[o.status];
    v.innerHTML = `<div class="page-title"><div><a href="#/orders">← Đơn hàng</a><h1 style="margin-top:6px">Đơn ${esc(o.code)} <span class="st ${o.status}" style="vertical-align:middle">${STATUS[o.status]}</span></h1><span class="muted">Đặt lúc ${dt(o.created_at)}</span></div>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn" id="printBtn">${IC.print} In hoá đơn</button>
        ${next ? `<button class="btn btn-primary" id="nextBtn">Chuyển sang “${STATUS[next]}”</button>` : ''}
      </div></div>
      <div class="cols">
        <div>
          <div class="card"><h2>Sản phẩm</h2>
            <table class="tbl"><tbody>${o.items.map((l) => `<tr><td style="width:60px"><img class="thumb" src="${esc(l.image)}" alt=""></td><td>${l.product_id ? `<a href="#/products/${l.product_id}">${esc(l.name)}</a>` : esc(l.name)}<div class="muted" style="font-size:12px">${[l.color, l.size && `Size ${l.size}`].filter(Boolean).map(esc).join(' · ')}</div></td><td class="num">${money(l.price)} × ${l.qty}</td><td class="num"><b>${money(l.price * l.qty)}</b></td></tr>`).join('')}</tbody></table>
            <div style="max-width:320px;margin:14px 0 0 auto">
              <div class="list-row"><span class="grow">Tạm tính</span>${money(o.subtotal)}</div>
              ${o.discount ? `<div class="list-row"><span class="grow">Giảm giá ${o.coupon_code ? `(${esc(o.coupon_code)})` : ''}</span>−${money(o.discount)}</div>` : ''}
              <div class="list-row"><span class="grow">Phí giao hàng</span>${o.shipping ? money(o.shipping) : 'Miễn phí'}</div>
              <div class="list-row" style="font-size:16px"><b class="grow">Tổng cộng</b><b>${money(o.total)}</b></div>
            </div>
          </div>
          <div class="card"><h2>Cập nhật đơn</h2><form id="upd" novalidate><div class="alert form-alert" hidden></div>
            <div class="form-grid">
              <div class="field c6"><label for="u-st">Trạng thái đơn</label><select class="input" id="u-st" name="status">${Object.entries(STATUS).map(([k, l]) => `<option value="${k}" ${k === o.status ? 'selected' : ''}>${l}</option>`).join('')}</select><div class="help">Chuyển sang “Đã huỷ” sẽ trả hàng về kho.</div></div>
              <div class="field c6"><label for="u-pay">Thanh toán</label><select class="input" id="u-pay" name="payment_status"><option value="unpaid">Chưa thanh toán</option><option value="paid" ${o.payment_status === 'paid' ? 'selected' : ''}>Đã thanh toán</option></select><div class="help">${o.payment_method === 'bank' ? 'Khách chọn chuyển khoản' : 'Khách chọn COD'}</div></div>
              <div class="field"><label for="u-sn">Ghi chú cho lần đổi trạng thái (khách xem được)</label><input class="input" id="u-sn" name="status_note" placeholder="Ví dụ: Đã giao cho GHN, mã vận đơn …"></div>
              <div class="field"><label for="u-an">Ghi chú nội bộ (khách không thấy)</label><textarea class="input" id="u-an" name="admin_note">${esc(o.admin_note)}</textarea></div>
            </div><button class="btn btn-primary">Lưu thay đổi</button>${ME.role === 'admin' ? ' <button type="button" class="btn btn-danger" id="delOrder">Xoá đơn</button>' : ''}</form></div>
        </div>
        <div>
          <div class="card"><h2>Người nhận</h2>
            <dl class="dl"><dt>Họ tên</dt><dd>${esc(o.name)}</dd><dt>Điện thoại</dt><dd><a href="tel:${esc(o.phone)}">${esc(o.phone)}</a></dd><dt>Email</dt><dd>${esc(o.email) || '—'}</dd><dt>Địa chỉ</dt><dd>${esc(o.address)}</dd>${o.note ? `<dt>Khách ghi chú</dt><dd>${esc(o.note)}</dd>` : ''}
            <dt>Tài khoản</dt><dd>${o.customer ? `<a href="#/customers?open=${o.customer.id}">${esc(o.customer.name)}</a>` : 'Khách vãng lai'}</dd></dl>
            <button class="btn btn-sm" id="editAddr" style="margin-top:12px">${IC.edit} Sửa thông tin nhận hàng</button>
          </div>
          <div class="card"><h2>Lịch sử</h2><ul class="timeline">${o.history.map((h) => `<li><b>${STATUS[h.status]}</b> <span class="muted">${dt(h.created_at)}</span><div class="muted" style="font-size:12px">${esc(h.by_name)}${h.note ? ` · ${esc(h.note)}` : ''}</div></li>`).join('')}</ul></div>
        </div>
      </div>`;
    const f = $('#upd');
    f.onsubmit = async (e) => {
      e.preventDefault();
      try { await api('PUT', `/orders/${o.id}`, { status: f.status.value, payment_status: f.payment_status.value, status_note: f.status_note.value, admin_note: f.admin_note.value }); toast('Đã lưu đơn hàng'); route(); }
      catch (err) { showErrors(f, err); }
    };
    if (next) $('#nextBtn').onclick = async () => { try { await api('PUT', `/orders/${o.id}`, { status: next }); toast(`Đã chuyển sang “${STATUS[next]}”`); route(); } catch (e) { fail(e); } };
    $('#printBtn').onclick = () => printInvoice(o);
    if ($('#delOrder')) $('#delOrder').onclick = async () => { if (await confirmBox(`Xoá vĩnh viễn đơn ${esc(o.code)}? Hàng chưa giao sẽ được trả về kho. Không thể hoàn tác.`)) { await api('DELETE', `/orders/${o.id}`).catch(fail); toast('Đã xoá đơn'); location.hash = '#/orders'; } };
    $('#editAddr').onclick = () => {
      const spec = [{ name: 'name', label: 'Họ tên', col: 6 }, { name: 'phone', label: 'Điện thoại', col: 6 }, { name: 'email', label: 'Email' }, { name: 'address', label: 'Địa chỉ', type: 'textarea' }];
      modal({ title: 'Sửa thông tin nhận hàng', body: fieldsHTML(spec, o), onSave: async (mf, close) => { await api('PUT', `/orders/${o.id}`, readFields(mf, spec)); close(); toast('Đã lưu'); route(); } });
    };
  }

  async function printInvoice(o) {
    const s = await fetch(`${API}/site`).then((r) => r.json());
    const w = window.open('', '_blank');
    if (!w) return toast('Trình duyệt chặn cửa sổ in, hãy cho phép popup', true);
    w.document.write(`<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Hoá đơn ${esc(o.code)}</title><style>
      body{font:13px/1.5 system-ui,sans-serif;margin:32px;color:#111}h1{font-size:22px;margin:0}table{width:100%;border-collapse:collapse;margin:16px 0}
      th,td{border-bottom:1px solid #ddd;padding:8px;text-align:left}td.n,th.n{text-align:right}.top{display:flex;justify-content:space-between;gap:24px}.tot td{border:0;padding:4px 8px}</style></head><body>
      <div class="top"><div><h1>${esc(s.settings.store_name)}</h1>${esc(s.settings.address || '')}<br>${esc(s.settings.hotline || '')} ${esc(s.settings.email || '')}</div>
      <div style="text-align:right"><h1>HOÁ ĐƠN</h1>Mã đơn: <b>${esc(o.code)}</b><br>Ngày: ${dt(o.created_at)}</div></div>
      <p><b>Người nhận:</b> ${esc(o.name)} · ${esc(o.phone)}<br><b>Địa chỉ:</b> ${esc(o.address)}${o.note ? `<br><b>Ghi chú:</b> ${esc(o.note)}` : ''}</p>
      <table><thead><tr><th>Sản phẩm</th><th>Phân loại</th><th class="n">Đơn giá</th><th class="n">SL</th><th class="n">Thành tiền</th></tr></thead><tbody>
      ${o.items.map((l) => `<tr><td>${esc(l.name)}</td><td>${[l.color, l.size].filter(Boolean).map(esc).join(' / ')}</td><td class="n">${money(l.price)}</td><td class="n">${l.qty}</td><td class="n">${money(l.price * l.qty)}</td></tr>`).join('')}</tbody></table>
      <table class="tot" style="width:320px;margin-left:auto"><tr><td>Tạm tính</td><td class="n">${money(o.subtotal)}</td></tr>${o.discount ? `<tr><td>Giảm giá</td><td class="n">−${money(o.discount)}</td></tr>` : ''}
      <tr><td>Phí giao hàng</td><td class="n">${money(o.shipping)}</td></tr><tr><td><b>Tổng cộng</b></td><td class="n"><b>${money(o.total)}</b></td></tr>
      <tr><td>Thanh toán</td><td class="n">${o.payment_method === 'bank' ? 'Chuyển khoản' : 'COD'} · ${o.payment_status === 'paid' ? 'Đã thanh toán' : 'Chưa thanh toán'}</td></tr></table>
      <p style="margin-top:32px;text-align:center">Cảm ơn bạn đã mua hàng!</p><script>window.onload=()=>window.print()<\/script></body></html>`);
    w.document.close();
  }

  // ================= Sản phẩm =================
  let CATS = [];
  const loadCats = async () => (CATS = await api('GET', '/categories'));

  async function viewProducts(v, params) {
    await loadCats();
    const st = { q: '', category: params.get('category') || '', status: params.get('status') || '', page: 1 };
    v.innerHTML = `<div class="page-title"><h1>Sản phẩm</h1><a class="btn btn-primary" href="#/products/new">${IC.plus} Thêm sản phẩm</a></div>
      <div class="filters">
        <input class="input" id="q" placeholder="Tìm tên hoặc mã sản phẩm" style="min-width:260px" aria-label="Tìm sản phẩm">
        <select class="input" id="cat" aria-label="Danh mục"><option value="">Mọi danh mục</option>${CATS.map((c) => `<option value="${c.id}" ${String(c.id) === st.category ? 'selected' : ''}>${esc(c.name)}</option>`).join('')}</select>
        <select class="input" id="stt" aria-label="Trạng thái"><option value="">Mọi trạng thái</option><option value="active">Đang bán</option><option value="hidden">Đang ẩn</option><option value="low">Sắp hết hàng</option><option value="sale">Đang giảm giá</option></select>
      </div><div id="tbl"></div>`;
    $('#stt').value = st.status;
    const load = async () => {
      const data = await api('GET', `/products?${qsOf({ ...st, limit: 20 })}`);
      $('#tbl').innerHTML = `<div class="tbl-wrap"><table class="tbl"><thead><tr><th></th><th>Sản phẩm</th><th>Danh mục</th><th class="num">Giá bán</th><th>Tồn kho</th><th>Đã bán</th><th>Nổi bật</th><th>Hiển thị</th><th></th></tr></thead><tbody>
        ${data.items.map((p) => `<tr>
          <td style="width:60px"><img class="thumb" src="${esc(p.images[0] || '')}" alt=""></td>
          <td><a href="#/products/${p.id}"><b>${esc(p.name)}</b></a><div class="muted" style="font-size:12px">${esc(p.sku)}</div></td>
          <td>${esc(p.category_name || '—')}</td>
          <td class="num">${p.final_price < p.price ? `<b style="color:var(--red)">${money(p.final_price)}</b><br><s class="muted">${money(p.price)}</s>` : money(p.price)}</td>
          <td><input class="input" type="number" min="0" value="${p.stock}" data-stock="${p.id}" style="width:84px;height:32px" aria-label="Tồn kho ${esc(p.name)}"></td>
          <td>${p.sold}</td>
          <td><label class="switch"><input type="checkbox" data-feat="${p.id}" ${p.featured ? 'checked' : ''} aria-label="Nổi bật"><span></span></label></td>
          <td><label class="switch"><input type="checkbox" data-act="${p.id}" ${p.active ? 'checked' : ''} aria-label="Hiển thị"><span></span></label></td>
          <td class="act"><a class="btn btn-sm btn-icon" href="${B}/san-pham/${esc(p.slug)}" target="_blank" rel="noopener" aria-label="Xem trên web">${IC.ext}</a> <a class="btn btn-sm btn-icon" href="#/products/${p.id}" aria-label="Sửa">${IC.edit}</a> <button class="btn btn-sm btn-icon btn-danger" data-del="${p.id}" data-name="${esc(p.name)}" aria-label="Xoá">${IC.trash}</button></td>
        </tr>`).join('') || '<tr><td colspan="9" class="empty">Không có sản phẩm</td></tr>'}</tbody></table></div>${pager(data, (pg) => { st.page = pg; load(); })}`;
      const patch = async (id, body, msg) => { try { await api('PATCH', `/products/${id}`, body); toast(msg); } catch (e) { fail(e); } };
      $$('[data-stock]', v).forEach((i) => (i.onchange = () => patch(i.dataset.stock, { stock: i.value }, 'Đã cập nhật tồn kho')));
      $$('[data-feat]', v).forEach((i) => (i.onchange = () => patch(i.dataset.feat, { featured: i.checked }, i.checked ? 'Đã đặt nổi bật' : 'Đã bỏ nổi bật')));
      $$('[data-act]', v).forEach((i) => (i.onchange = () => patch(i.dataset.act, { active: i.checked }, i.checked ? 'Đã hiện sản phẩm' : 'Đã ẩn sản phẩm')));
      $$('[data-del]', v).forEach((b) => (b.onclick = async () => {
        if (!(await confirmBox(`Xoá sản phẩm “${b.dataset.name}”? Đơn hàng cũ vẫn giữ tên sản phẩm. Muốn tạm ngừng bán thì nên tắt “Hiển thị”.`))) return;
        try { await api('DELETE', `/products/${b.dataset.del}`); toast('Đã xoá sản phẩm'); load(); } catch (e) { fail(e); }
      }));
    };
    $('#q').oninput = debounce((e) => { st.q = e.target.value.trim(); st.page = 1; load(); });
    $('#cat').onchange = (e) => { st.category = e.target.value; st.page = 1; load(); };
    $('#stt').onchange = (e) => { st.status = e.target.value; st.page = 1; load(); };
    await load();
  }

  async function viewProduct(v, id) {
    await loadCats();
    const isNew = id === 'new';
    const p = isNew ? { active: true, images: [], sizes: [], colors: [] } : await api('GET', `/products/${id}`);
    const spec = [
      { name: 'name', label: 'Tên sản phẩm', col: 8 }, { name: 'sku', label: 'Mã sản phẩm (SKU)', col: 4 },
      { name: 'category_id', label: 'Danh mục', type: 'select', col: 4, options: [['', '— Chưa phân loại —'], ...CATS.map((c) => [c.id, c.name])] },
      { name: 'price', label: 'Giá bán (₫)', type: 'number', col: 3 }, { name: 'sale_price', label: 'Giá khuyến mãi (₫)', type: 'number', col: 3, help: 'Để trống nếu không giảm' },
      { name: 'stock', label: 'Tồn kho', type: 'number', col: 2 },
      { name: 'sizes', label: 'Size', col: 6, placeholder: 'S, M, L, XL', help: 'Cách nhau bằng dấu phẩy. Để trống nếu không có size' },
      { name: 'colors', label: 'Màu sắc', col: 6, placeholder: 'Đen, Trắng', help: 'Cách nhau bằng dấu phẩy' },
      { name: 'images', label: 'Ảnh sản phẩm', type: 'images', help: 'Ảnh đầu tiên là ảnh chính. Nên dùng ảnh dọc tỉ lệ 4:5.' },
      { name: 'short_desc', label: 'Mô tả ngắn', type: 'textarea', rows: 2, help: 'Hiện dưới giá và trên Google' },
      { name: 'description', label: 'Mô tả chi tiết', type: 'rich' },
      { name: 'slug', label: 'Đường dẫn (slug)', col: 6, help: 'Tự tạo từ tên nếu để trống' },
      { name: 'featured', label: 'Sản phẩm nổi bật (hiện ở trang chủ)', type: 'switch', col: 3 },
      { name: 'active', label: 'Đang bán (hiện trên web)', type: 'switch', col: 3 },
    ];
    const vals = { ...p, sizes: (p.sizes || []).join(', '), colors: (p.colors || []).join(', '), sale_price: p.sale_price || '' };
    v.innerHTML = `<div class="page-title"><div><a href="#/products">← Sản phẩm</a><h1 style="margin-top:6px">${isNew ? 'Thêm sản phẩm' : esc(p.name)}</h1></div>
      ${isNew ? '' : `<a class="btn" href="${B}/san-pham/${esc(p.slug)}" target="_blank" rel="noopener">${IC.ext} Xem trên web</a>`}</div>
      <form class="card" id="pf" novalidate><div class="alert form-alert" hidden></div>${fieldsHTML(spec, vals)}
      <div style="display:flex;gap:8px"><button class="btn btn-primary">${isNew ? 'Tạo sản phẩm' : 'Lưu thay đổi'}</button><a class="btn" href="#/products">Huỷ</a></div></form>`;
    const f = $('#pf');
    mountFields(f, spec, vals);
    f.onsubmit = async (e) => {
      e.preventDefault();
      const body = readFields(f, spec);
      try {
        if (isNew) { const r = await api('POST', '/products', body); toast('Đã tạo sản phẩm'); location.hash = `#/products/${r.id}`; }
        else { await api('PUT', `/products/${id}`, body); toast('Đã lưu sản phẩm'); route(); }
      } catch (err) { showErrors(f, err); }
    };
  }

  // ================= Danh mục =================
  async function viewCategories(v) {
    const cats = await loadCats();
    v.innerHTML = `<div class="page-title"><h1>Danh mục</h1><button class="btn btn-primary" id="add">${IC.plus} Thêm danh mục</button></div>
      <div class="tbl-wrap"><table class="tbl"><thead><tr><th></th><th>Tên</th><th>Đường dẫn</th><th>Số sản phẩm</th><th>Thứ tự</th><th>Hiển thị</th><th></th></tr></thead><tbody>
      ${cats.map((c) => `<tr><td style="width:60px">${c.image ? `<img class="thumb" src="${esc(c.image)}" alt="">` : ''}</td><td><b>${esc(c.name)}</b><div class="muted" style="font-size:12px">${esc(c.description)}</div></td>
        <td class="muted">/cua-hang?danh-muc=${esc(c.slug)}</td><td><a href="#/products?category=${c.id}">${c.count}</a></td><td>${c.sort}</td><td><span class="st ${c.active ? 'on' : 'off'}">${c.active ? 'Hiện' : 'Ẩn'}</span></td>
        <td class="act"><button class="btn btn-sm btn-icon" data-edit="${c.id}" aria-label="Sửa">${IC.edit}</button> <button class="btn btn-sm btn-icon btn-danger" data-del="${c.id}" aria-label="Xoá">${IC.trash}</button></td></tr>`).join('') || '<tr><td colspan="7" class="empty">Chưa có danh mục</td></tr>'}
      </tbody></table></div>`;
    const spec = [{ name: 'name', label: 'Tên danh mục', col: 8 }, { name: 'sort', label: 'Thứ tự', type: 'number', col: 4, help: 'Số nhỏ hiện trước' },
      { name: 'description', label: 'Mô tả ngắn', type: 'textarea', rows: 2 }, { name: 'image', label: 'Ảnh danh mục (trang chủ)', type: 'image' },
      { name: 'slug', label: 'Đường dẫn (slug)', help: 'Tự tạo từ tên nếu để trống. Đổi slug thì nhớ sửa link trong Menu.' }, { name: 'active', label: 'Hiển thị trên web', type: 'switch', default: true }];
    const open = (c) => modal({
      title: c ? 'Sửa danh mục' : 'Thêm danh mục', body: fieldsHTML(spec, c || {}), onOpen: (f) => mountFields(f, spec, c || {}),
      onSave: async (f, close) => { const b = readFields(f, spec); if (c) await api('PUT', `/categories/${c.id}`, b); else await api('POST', '/categories', b); close(); toast('Đã lưu danh mục'); route(); },
    });
    $('#add').onclick = () => open(null);
    $$('[data-edit]', v).forEach((b) => (b.onclick = () => open(cats.find((c) => c.id === +b.dataset.edit))));
    $$('[data-del]', v).forEach((b) => (b.onclick = async () => {
      const c = cats.find((x) => x.id === +b.dataset.del);
      if (await confirmBox(`Xoá danh mục “${esc(c.name)}”? ${c.count} sản phẩm trong danh mục sẽ chuyển thành “chưa phân loại”.`)) { await api('DELETE', `/categories/${c.id}`).catch(fail); toast('Đã xoá danh mục'); route(); }
    }));
  }

  // ================= Khách hàng =================
  async function viewCustomers(v, params) {
    const st = { q: '', status: '', page: 1 };
    v.innerHTML = `<div class="page-title"><h1>Khách hàng</h1></div>
      <div class="filters"><input class="input" id="q" placeholder="Tìm tên, email, SĐT" style="min-width:260px" aria-label="Tìm khách"><select class="input" id="stt" aria-label="Lọc"><option value="">Tất cả</option><option value="locked">Đã khoá</option></select></div><div id="tbl"></div>`;
    const load = async () => {
      const data = await api('GET', `/customers?${qsOf({ ...st, limit: 20 })}`);
      $('#tbl').innerHTML = `<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Khách hàng</th><th>Điện thoại</th><th>Ngày đăng ký</th><th>Số đơn</th><th class="num">Đã chi</th><th>Trạng thái</th></tr></thead><tbody>
        ${data.items.map((c) => `<tr class="click" data-id="${c.id}"><td><b>${esc(c.name)}</b><div class="muted" style="font-size:12px">${esc(c.email)}</div></td><td>${esc(c.phone) || '—'}</td><td>${d(c.created_at)}</td><td>${c.orders}</td><td class="num">${money(c.spent)}</td><td><span class="st ${c.locked ? 'off' : 'on'}">${c.locked ? 'Đã khoá' : 'Hoạt động'}</span></td></tr>`).join('') || '<tr><td colspan="6" class="empty">Chưa có khách hàng</td></tr>'}
        </tbody></table></div>${pager(data, (p) => { st.page = p; load(); })}`;
      $$('tr[data-id]', v).forEach((tr) => (tr.onclick = () => openCustomer(+tr.dataset.id, load)));
    };
    $('#q').oninput = debounce((e) => { st.q = e.target.value.trim(); st.page = 1; load(); });
    $('#stt').onchange = (e) => { st.status = e.target.value; st.page = 1; load(); };
    await load();
    if (params.get('open')) openCustomer(+params.get('open'), load);
  }

  async function openCustomer(id, reload) {
    const c = await api('GET', `/customers/${id}`);
    const spec = [{ name: 'name', label: 'Họ tên', col: 6 }, { name: 'phone', label: 'Điện thoại', col: 6 }, { name: 'address', label: 'Địa chỉ', type: 'textarea', rows: 2 },
      { name: 'new_password', label: 'Đặt lại mật khẩu', type: 'password', help: 'Để trống nếu không đổi' }];
    modal({
      title: c.name, wide: true,
      body: `<div class="cols-half"><div><p class="muted" style="margin-top:0">${esc(c.email)} · Đăng ký ${d(c.created_at)}</p>${fieldsHTML(spec, c)}</div>
        <div><h2>Đơn hàng (${c.orders.length})</h2>${c.orders.map((o) => `<a class="list-row" href="#/orders/${o.id}" style="text-decoration:none;color:inherit"><b>${esc(o.code)}</b><span class="grow muted">${d(o.created_at)}</span><span>${money(o.total)}</span><span class="st ${o.status}">${STATUS[o.status]}</span></a>`).join('') || '<p class="muted">Chưa có đơn</p>'}</div></div>`,
      foot: `<button type="button" class="btn ${c.locked ? '' : 'btn-danger'}" id="lockBtn">${c.locked ? 'Mở khoá tài khoản' : 'Khoá tài khoản'}</button>${ME.role === 'admin' ? '<button type="button" class="btn btn-danger" id="delCus">Xoá</button>' : ''}`,
      onOpen: (f, close, bg) => {
        $$('a[href^="#/orders"]', bg).forEach((a) => a.addEventListener('click', close));
        $('#lockBtn', bg).onclick = async () => { await api('PUT', `/customers/${id}`, { locked: !c.locked }).catch(fail); toast(c.locked ? 'Đã mở khoá' : 'Đã khoá tài khoản'); close(); reload(); };
        const del = $('#delCus', bg);
        if (del) del.onclick = async () => { close(); if (await confirmBox(`Xoá tài khoản “${esc(c.name)}”? Đơn hàng cũ vẫn được giữ lại.`)) { await api('DELETE', `/customers/${id}`).catch(fail); toast('Đã xoá khách hàng'); reload(); } };
      },
      onSave: async (f, close) => { await api('PUT', `/customers/${id}`, readFields(f, spec)); close(); toast('Đã lưu khách hàng'); reload(); },
    });
  }

  // ================= Đánh giá =================
  async function viewReviews(v) {
    let status = 'pending';
    v.innerHTML = `<div class="page-title"><h1>Đánh giá sản phẩm</h1></div><div class="tabs" id="rt"></div><div id="list"></div>`;
    const load = async () => {
      $('#rt').innerHTML = [['pending', 'Chờ duyệt'], ['approved', 'Đã duyệt'], ['', 'Tất cả']].map(([k, l]) => `<button class="${k === status ? 'on' : ''}" data-s="${k}">${l}</button>`).join('');
      $$('[data-s]', v).forEach((b) => (b.onclick = () => { status = b.dataset.s; load(); }));
      const rows = await api('GET', `/reviews?status=${status}`);
      $('#list').innerHTML = `<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Sản phẩm</th><th>Người viết</th><th>Sao</th><th>Nội dung</th><th>Ngày</th><th>Trạng thái</th><th></th></tr></thead><tbody>
        ${rows.map((r) => `<tr><td>${r.product_slug ? `<a href="${B}/san-pham/${esc(r.product_slug)}" target="_blank" rel="noopener">${esc(r.product_name)}</a>` : '—'}</td><td>${esc(r.name)}</td><td style="color:#d29a00;white-space:nowrap">${'★'.repeat(r.rating)}</td>
          <td style="max-width:380px">${esc(r.content)}</td><td>${d(r.created_at)}</td><td><span class="st ${r.approved ? 'on' : 'pending'}">${r.approved ? 'Đang hiện' : 'Chờ duyệt'}</span></td>
          <td class="act"><button class="btn btn-sm" data-ap="${r.id}" data-v="${r.approved ? 0 : 1}">${r.approved ? 'Ẩn' : 'Duyệt'}</button> <button class="btn btn-sm btn-icon btn-danger" data-del="${r.id}" aria-label="Xoá">${IC.trash}</button></td></tr>`).join('') || '<tr><td colspan="7" class="empty">Không có đánh giá</td></tr>'}
        </tbody></table></div>`;
      $$('[data-ap]', v).forEach((b) => (b.onclick = async () => { await api('PUT', `/reviews/${b.dataset.ap}`, { approved: b.dataset.v === '1' }).catch(fail); toast(b.dataset.v === '1' ? 'Đã duyệt, đánh giá đã hiện trên web' : 'Đã ẩn đánh giá'); load(); }));
      $$('[data-del]', v).forEach((b) => (b.onclick = async () => { if (await confirmBox('Xoá đánh giá này?')) { await api('DELETE', `/reviews/${b.dataset.del}`).catch(fail); load(); } }));
    };
    await load();
  }

  // ================= Mã giảm giá =================
  async function viewCoupons(v) {
    const rows = await api('GET', '/coupons');
    const n0 = new Date(); const today = `${n0.getFullYear()}-${String(n0.getMonth() + 1).padStart(2, '0')}-${String(n0.getDate()).padStart(2, '0')}`;
    const state = (c) => (!c.active ? ['off', 'Tắt'] : c.expires_at && c.expires_at < today ? ['off', 'Hết hạn'] : c.max_uses && c.used >= c.max_uses ? ['off', 'Hết lượt'] : ['on', 'Đang chạy']);
    v.innerHTML = `<div class="page-title"><h1>Mã giảm giá</h1><button class="btn btn-primary" id="add">${IC.plus} Tạo mã</button></div>
      <div class="tbl-wrap"><table class="tbl"><thead><tr><th>Mã</th><th>Mức giảm</th><th>Đơn tối thiểu</th><th>Đã dùng</th><th>Thời hạn</th><th>Trạng thái</th><th></th></tr></thead><tbody>
      ${rows.map((c) => { const [k, l] = state(c); return `<tr><td><b style="font-family:ui-monospace,monospace">${esc(c.code)}</b><div class="muted" style="font-size:12px">${esc(c.description)}</div></td>
        <td>${c.type === 'percent' ? `${c.value}%${c.max_discount ? ` (tối đa ${money(c.max_discount)})` : ''}` : money(c.value)}</td><td>${c.min_order ? money(c.min_order) : '—'}</td>
        <td>${c.used}${c.max_uses ? ` / ${c.max_uses}` : ''}</td><td>${c.starts_at || c.expires_at ? `${c.starts_at ? d(c.starts_at) : '…'} → ${c.expires_at ? d(c.expires_at) : '…'}` : 'Không giới hạn'}</td>
        <td><span class="st ${k}">${l}</span></td><td class="act"><button class="btn btn-sm btn-icon" data-edit="${c.id}" aria-label="Sửa">${IC.edit}</button> <button class="btn btn-sm btn-icon btn-danger" data-del="${c.id}" aria-label="Xoá">${IC.trash}</button></td></tr>`; }).join('') || '<tr><td colspan="7" class="empty">Chưa có mã giảm giá</td></tr>'}
      </tbody></table></div>`;
    const spec = [
      { name: 'code', label: 'Mã (khách nhập)', col: 6, placeholder: 'SALE10' }, { name: 'type', label: 'Loại giảm', type: 'select', col: 6, options: [['percent', 'Theo phần trăm (%)'], ['fixed', 'Số tiền cố định (₫)']] },
      { name: 'value', label: 'Mức giảm', type: 'number', col: 4, help: 'Số % hoặc số tiền' }, { name: 'max_discount', label: 'Giảm tối đa (₫)', type: 'number', col: 4, help: 'Chỉ cho loại %, 0 = không giới hạn' },
      { name: 'min_order', label: 'Đơn tối thiểu (₫)', type: 'number', col: 4 },
      { name: 'max_uses', label: 'Số lượt tối đa', type: 'number', col: 4, help: '0 = không giới hạn' }, { name: 'starts_at', label: 'Bắt đầu', type: 'date', col: 4 }, { name: 'expires_at', label: 'Hết hạn', type: 'date', col: 4 },
      { name: 'description', label: 'Mô tả (khách thấy khi áp mã)' }, { name: 'active', label: 'Đang bật', type: 'switch', default: true },
    ];
    const open = (c) => modal({ title: c ? 'Sửa mã giảm giá' : 'Tạo mã giảm giá', body: fieldsHTML(spec, c || {}),
      onSave: async (f, close) => { const b = readFields(f, spec); if (c) await api('PUT', `/coupons/${c.id}`, b); else await api('POST', '/coupons', b); close(); toast('Đã lưu mã giảm giá'); route(); } });
    $('#add').onclick = () => open(null);
    $$('[data-edit]', v).forEach((b) => (b.onclick = () => open(rows.find((c) => c.id === +b.dataset.edit))));
    $$('[data-del]', v).forEach((b) => (b.onclick = async () => { if (await confirmBox('Xoá mã giảm giá này?')) { await api('DELETE', `/coupons/${b.dataset.del}`).catch(fail); toast('Đã xoá mã'); route(); } }));
  }

  // ================= Giao diện: trang chủ + banner =================
  async function viewAppearance(v) {
    const [s, banners] = await Promise.all([api('GET', '/settings'), api('GET', '/banners')]);
    const spec = [
      { type: 'heading', label: 'Thương hiệu' },
      { name: 'store_name', label: 'Tên cửa hàng', col: 6 }, { name: 'primary_color', label: 'Màu chủ đạo (nút bấm, giá giảm)', type: 'color', col: 6 },
      { name: 'logo', label: 'Logo (thay cho chữ tên cửa hàng)', type: 'image', col: 6, help: 'Ảnh ngang, nền trong suốt, cao khoảng 80px' },
      { name: 'favicon', label: 'Biểu tượng tab trình duyệt', type: 'image', col: 6, help: 'Ảnh vuông 64×64' },
      { name: 'announcement', label: 'Dòng thông báo trên cùng', help: 'Để trống để ẩn' },
      { type: 'heading', label: 'Ảnh bìa trang chủ' },
      { name: 'hero_title', label: 'Tiêu đề lớn', col: 6 }, { name: 'hero_button_text', label: 'Chữ trên nút', col: 3 }, { name: 'hero_button_link', label: 'Nút dẫn tới', col: 3, placeholder: '/cua-hang' },
      { name: 'hero_subtitle', label: 'Dòng mô tả', type: 'textarea', rows: 2 },
      { name: 'hero_image', label: 'Ảnh bìa', type: 'image', help: 'Ảnh ngang lớn, tối thiểu 1600px chiều rộng' },
      { type: 'heading', label: 'Tiêu đề các khu vực trang chủ' },
      { name: 'home_featured_title', label: 'Khu sản phẩm nổi bật', col: 4 }, { name: 'home_sale_title', label: 'Khu giảm giá', col: 4 }, { name: 'home_new_title', label: 'Khu hàng mới', col: 4 },
      { type: 'heading', label: 'Chân trang' },
      { name: 'footer_about', label: 'Giới thiệu ngắn ở chân trang', type: 'textarea', rows: 2 },
    ];
    v.innerHTML = `<div class="page-title"><h1>Trang chủ và banner</h1><a class="btn" href="${B}/" target="_blank" rel="noopener">${IC.ext} Xem trang chủ</a></div>
      <form class="card" id="af" novalidate><div class="alert form-alert" hidden></div>${fieldsHTML(spec, s)}<button class="btn btn-primary">Lưu giao diện</button></form>
      <div class="card"><div class="page-title" style="margin-bottom:12px"><h2 style="margin:0">Banner bộ sưu tập (dưới khu nổi bật)</h2><button class="btn" id="addB">${IC.plus} Thêm banner</button></div>
        <div class="tbl-wrap"><table class="tbl"><thead><tr><th></th><th>Tiêu đề</th><th>Dẫn tới</th><th>Thứ tự</th><th>Hiển thị</th><th></th></tr></thead><tbody>
        ${banners.map((b) => `<tr><td style="width:120px"><img src="${esc(b.image)}" alt="" style="width:110px;height:62px;object-fit:cover;border-radius:4px"></td><td><b>${esc(b.title)}</b><div class="muted" style="font-size:12px">${esc(b.subtitle)}</div></td><td class="muted">${esc(b.link)}</td><td>${b.sort}</td>
          <td><span class="st ${b.active ? 'on' : 'off'}">${b.active ? 'Hiện' : 'Ẩn'}</span></td><td class="act"><button class="btn btn-sm btn-icon" data-edit="${b.id}" aria-label="Sửa">${IC.edit}</button> <button class="btn btn-sm btn-icon btn-danger" data-del="${b.id}" aria-label="Xoá">${IC.trash}</button></td></tr>`).join('') || '<tr><td colspan="6" class="empty">Chưa có banner</td></tr>'}
        </tbody></table></div></div>`;
    const f = $('#af');
    mountFields(f, spec, s);
    f.onsubmit = async (e) => { e.preventDefault(); try { await api('PUT', '/settings', readFields(f, spec)); showErrors(f, null); toast('Đã lưu giao diện, tải lại trang cửa hàng để xem'); } catch (err) { showErrors(f, err); } };
    const bspec = [{ name: 'image', label: 'Ảnh banner', type: 'image' }, { name: 'title', label: 'Tiêu đề', col: 6 }, { name: 'button_text', label: 'Chữ trên nút', col: 6 },
      { name: 'subtitle', label: 'Dòng mô tả' }, { name: 'link', label: 'Dẫn tới', col: 8, placeholder: '/cua-hang?danh-muc=do-nu' }, { name: 'sort', label: 'Thứ tự', type: 'number', col: 4 },
      { name: 'active', label: 'Hiển thị', type: 'switch', default: true }];
    const open = (b) => modal({ title: b ? 'Sửa banner' : 'Thêm banner', body: fieldsHTML(bspec, b || {}), onOpen: (mf) => mountFields(mf, bspec, b || {}),
      onSave: async (mf, close) => { const body = readFields(mf, bspec); if (b) await api('PUT', `/banners/${b.id}`, body); else await api('POST', '/banners', body); close(); toast('Đã lưu banner'); route(); } });
    $('#addB').onclick = () => open(null);
    $$('[data-edit]', v).forEach((b) => (b.onclick = () => open(banners.find((x) => x.id === +b.dataset.edit))));
    $$('[data-del]', v).forEach((b) => (b.onclick = async () => { if (await confirmBox('Xoá banner này?')) { await api('DELETE', `/banners/${b.dataset.del}`).catch(fail); route(); } }));
  }

  // ================= Menu =================
  async function viewMenu(v) {
    const [s, cats, pages] = await Promise.all([api('GET', '/settings'), api('GET', '/categories'), api('GET', '/pages')]);
    let items = []; try { items = JSON.parse(s.menu || '[]'); } catch { items = []; }
    const suggestions = [['Tất cả sản phẩm', '/cua-hang'], ['Hàng giảm giá', '/cua-hang?giam-gia=1'], ['Hàng mới', '/cua-hang?sap-xep=newest'], ...cats.map((c) => [c.name, `/cua-hang?danh-muc=${c.slug}`]), ...pages.map((p) => [p.title, `/trang/${p.slug}`]), ['Tra cứu đơn hàng', '/tra-cuu-don']];
    v.innerHTML = `<div class="page-title"><h1>Menu trên cùng</h1></div>
      <div class="cols"><div class="card"><h2>Các mục menu</h2><div class="menu-rows" id="rows"></div>
        <div style="display:flex;gap:8px;margin-top:12px"><button class="btn" id="addRow">${IC.plus} Thêm mục</button><button class="btn btn-primary" id="saveMenu">Lưu menu</button></div></div>
        <div class="card"><h2>Thêm nhanh</h2><p class="muted" style="margin-top:0">Bấm để thêm vào menu.</p>${suggestions.map(([l, u], i) => `<button class="btn btn-sm" style="margin:0 6px 6px 0" data-sg="${i}">${IC.plus} ${esc(l)}</button>`).join('')}</div></div>`;
    const draw = () => {
      $('#rows').innerHTML = items.map((m, i) => `<div class="mr"><input class="input" value="${esc(m.label)}" data-i="${i}" data-k="label" aria-label="Tên mục ${i + 1}" placeholder="Tên hiển thị"><input class="input" value="${esc(m.url)}" data-i="${i}" data-k="url" aria-label="Liên kết mục ${i + 1}" placeholder="/cua-hang">
        <div style="display:flex;gap:4px"><button class="btn btn-icon" data-up="${i}" aria-label="Lên trên">${IC.up}</button><button class="btn btn-icon btn-danger" data-rm="${i}" aria-label="Xoá">${IC.trash}</button></div></div>`).join('') || '<p class="muted">Menu đang trống.</p>';
      $$('[data-k]', v).forEach((inp) => (inp.oninput = () => (items[+inp.dataset.i][inp.dataset.k] = inp.value)));
      $$('[data-rm]', v).forEach((b) => (b.onclick = () => { items.splice(+b.dataset.rm, 1); draw(); }));
      $$('[data-up]', v).forEach((b) => (b.onclick = () => { const i = +b.dataset.up; if (i > 0) { [items[i - 1], items[i]] = [items[i], items[i - 1]]; draw(); } }));
    };
    draw();
    $('#addRow').onclick = () => { items.push({ label: '', url: '' }); draw(); $$('[data-k="label"]', v).pop().focus(); };
    $$('[data-sg]', v).forEach((b) => (b.onclick = () => { const [l, u] = suggestions[+b.dataset.sg]; items.push({ label: l, url: u }); draw(); }));
    $('#saveMenu').onclick = async () => {
      const clean = items.filter((m) => m.label.trim() && m.url.trim()).map((m) => ({ label: m.label.trim(), url: m.url.trim() }));
      try { await api('PUT', '/settings', { menu: clean }); items = clean; draw(); toast('Đã lưu menu'); } catch (e) { fail(e); }
    };
  }

  // ================= Trang nội dung =================
  async function viewPages(v) {
    const pages = await api('GET', '/pages');
    v.innerHTML = `<div class="page-title"><h1>Trang nội dung</h1><a class="btn btn-primary" href="#/pages/new">${IC.plus} Thêm trang</a></div>
      <div class="tbl-wrap"><table class="tbl"><thead><tr><th>Tiêu đề</th><th>Đường dẫn</th><th>Chân trang</th><th>Hiển thị</th><th>Cập nhật</th><th></th></tr></thead><tbody>
      ${pages.map((p) => `<tr><td><a href="#/pages/${p.id}"><b>${esc(p.title)}</b></a></td><td class="muted">/trang/${esc(p.slug)}</td><td>${p.show_in_footer ? 'Có' : '—'}</td><td><span class="st ${p.active ? 'on' : 'off'}">${p.active ? 'Hiện' : 'Ẩn'}</span></td><td>${d(p.updated_at)}</td>
        <td class="act"><a class="btn btn-sm btn-icon" href="${B}/trang/${esc(p.slug)}" target="_blank" rel="noopener" aria-label="Xem">${IC.ext}</a> <a class="btn btn-sm btn-icon" href="#/pages/${p.id}" aria-label="Sửa">${IC.edit}</a> <button class="btn btn-sm btn-icon btn-danger" data-del="${p.id}" aria-label="Xoá">${IC.trash}</button></td></tr>`).join('') || '<tr><td colspan="6" class="empty">Chưa có trang</td></tr>'}
      </tbody></table></div>`;
    $$('[data-del]', v).forEach((b) => (b.onclick = async () => { if (await confirmBox('Xoá trang này? Liên kết tới trang sẽ không còn hoạt động.')) { await api('DELETE', `/pages/${b.dataset.del}`).catch(fail); route(); } }));
  }

  async function viewPage(v, id) {
    const isNew = id === 'new';
    const p = isNew ? { active: true, show_in_footer: true } : await api('GET', `/pages/${id}`);
    const spec = [{ name: 'title', label: 'Tiêu đề', col: 8 }, { name: 'slug', label: 'Đường dẫn (slug)', col: 4, help: 'Tự tạo nếu để trống' }, { name: 'content', label: 'Nội dung', type: 'rich' },
      { name: 'show_in_footer', label: 'Hiện link ở chân trang', type: 'switch', col: 4 }, { name: 'active', label: 'Hiển thị', type: 'switch', col: 4 }];
    v.innerHTML = `<div class="page-title"><div><a href="#/pages">← Trang nội dung</a><h1 style="margin-top:6px">${isNew ? 'Thêm trang' : esc(p.title)}</h1></div></div>
      <form class="card" id="pgf" novalidate><div class="alert form-alert" hidden></div>${fieldsHTML(spec, p)}<button class="btn btn-primary">${isNew ? 'Tạo trang' : 'Lưu trang'}</button></form>`;
    const f = $('#pgf');
    mountFields(f, spec, p);
    f.onsubmit = async (e) => {
      e.preventDefault();
      try { if (isNew) { const r = await api('POST', '/pages', readFields(f, spec)); location.hash = `#/pages/${r.id}`; } else { await api('PUT', `/pages/${id}`, readFields(f, spec)); route(); } toast('Đã lưu trang'); }
      catch (err) { showErrors(f, err); }
    };
  }

  // ================= Cài đặt =================
  async function viewSettings(v) {
    const s = await api('GET', '/settings');
    const spec = [
      { type: 'heading', label: 'Thông tin cửa hàng' },
      { name: 'store_name', label: 'Tên cửa hàng', col: 6 }, { name: 'tagline', label: 'Khẩu hiệu ngắn', col: 6 },
      { name: 'hotline', label: 'Hotline', col: 4 }, { name: 'email', label: 'Email liên hệ', col: 4 }, { name: 'working_hours', label: 'Giờ làm việc', col: 4 },
      { name: 'address', label: 'Địa chỉ cửa hàng' },
      { type: 'heading', label: 'Mạng xã hội (dán đường link, để trống để ẩn)' },
      { name: 'facebook', label: 'Facebook', col: 6 }, { name: 'instagram', label: 'Instagram', col: 6 }, { name: 'tiktok', label: 'TikTok', col: 6 }, { name: 'zalo', label: 'Zalo', col: 6 },
      { type: 'heading', label: 'Giao hàng' },
      { name: 'shipping_fee', label: 'Phí giao hàng (₫)', type: 'number', col: 4 }, { name: 'free_ship_threshold', label: 'Miễn phí ship cho đơn từ (₫)', type: 'number', col: 4, help: '0 = không miễn phí' },
      { name: 'low_stock_threshold', label: 'Cảnh báo sắp hết hàng khi còn', type: 'number', col: 4 },
      { type: 'heading', label: 'Thanh toán' },
      { name: 'cod_enabled', label: 'Nhận thanh toán khi nhận hàng (COD)', type: 'switch', col: 6 }, { name: 'bank_enabled', label: 'Nhận chuyển khoản ngân hàng', type: 'switch', col: 6 },
      { name: 'bank_name', label: 'Ngân hàng', col: 4 }, { name: 'bank_account', label: 'Số tài khoản', col: 4 }, { name: 'bank_owner', label: 'Chủ tài khoản', col: 4 },
      { name: 'bank_note', label: 'Hướng dẫn chuyển khoản' },
      { type: 'heading', label: 'Tìm kiếm Google (SEO)' },
      { name: 'seo_title', label: 'Tiêu đề trang chủ' }, { name: 'seo_description', label: 'Mô tả trang chủ', type: 'textarea', rows: 2 },
    ];
    v.innerHTML = `<div class="page-title"><h1>Cài đặt cửa hàng</h1></div><form class="card" id="sf" novalidate><div class="alert form-alert" hidden></div>${fieldsHTML(spec, s)}<button class="btn btn-primary">Lưu cài đặt</button></form>`;
    const f = $('#sf');
    mountFields(f, spec, s);
    f.onsubmit = async (e) => {
      e.preventDefault();
      const b = readFields(f, spec); b.cod_enabled = b.cod_enabled ? '1' : '0'; b.bank_enabled = b.bank_enabled ? '1' : '0';
      if (b.cod_enabled === '0' && b.bank_enabled === '0') return showErrors(f, { message: 'Cần bật ít nhất một cách thanh toán', fields: { cod_enabled: 'Bật COD hoặc chuyển khoản' } });
      try { await api('PUT', '/settings', b); showErrors(f, null); toast('Đã lưu cài đặt'); } catch (err) { showErrors(f, err); }
    };
  }

  // ================= Nhân viên =================
  async function viewStaff(v) {
    const rows = await api('GET', '/staff');
    v.innerHTML = `<div class="page-title"><h1>Nhân viên</h1><button class="btn btn-primary" id="add">${IC.plus} Thêm nhân viên</button></div>
      <div class="alert info"><b>Quản trị viên</b>: toàn quyền. <b>Nhân viên</b>: quản lý đơn hàng, sản phẩm, danh mục, khách hàng, đánh giá, mã giảm giá; không vào được Giao diện, Cài đặt, Nhân viên.</div>
      <div class="tbl-wrap"><table class="tbl"><thead><tr><th>Họ tên</th><th>Email</th><th>Vai trò</th><th>Đăng nhập gần nhất</th><th>Trạng thái</th><th></th></tr></thead><tbody>
      ${rows.map((u) => `<tr><td><b>${esc(u.name)}</b>${u.id === ME.id ? ' <span class="muted">(bạn)</span>' : ''}</td><td>${esc(u.email)}</td><td>${u.role === 'admin' ? 'Quản trị viên' : 'Nhân viên'}</td><td>${u.last_login ? dt(u.last_login) : '—'}</td>
        <td><span class="st ${u.active ? 'on' : 'off'}">${u.active ? 'Hoạt động' : 'Đã khoá'}</span></td><td class="act"><button class="btn btn-sm btn-icon" data-edit="${u.id}" aria-label="Sửa">${IC.edit}</button>${u.id === ME.id ? '' : ` <button class="btn btn-sm btn-icon btn-danger" data-del="${u.id}" aria-label="Xoá">${IC.trash}</button>`}</td></tr>`).join('')}
      </tbody></table></div>`;
    const spec = (isNew) => [{ name: 'name', label: 'Họ tên', col: 6 }, { name: 'email', label: 'Email đăng nhập', type: 'email', col: 6 },
      { name: 'role', label: 'Vai trò', type: 'select', col: 6, options: [['staff', 'Nhân viên'], ['admin', 'Quản trị viên']] },
      { name: 'password', label: isNew ? 'Mật khẩu' : 'Mật khẩu mới', type: 'password', col: 6, help: isNew ? 'Tối thiểu 6 ký tự' : 'Để trống nếu không đổi' },
      { name: 'active', label: 'Cho phép đăng nhập', type: 'switch', default: true }];
    const open = (u) => { const sp = spec(!u); modal({ title: u ? 'Sửa nhân viên' : 'Thêm nhân viên', body: fieldsHTML(sp, u || {}),
      onSave: async (f, close) => { const b = readFields(f, sp); if (u) await api('PUT', `/staff/${u.id}`, b); else await api('POST', '/staff', b); close(); toast('Đã lưu nhân viên'); route(); } }); };
    $('#add').onclick = () => open(null);
    $$('[data-edit]', v).forEach((b) => (b.onclick = () => open(rows.find((u) => u.id === +b.dataset.edit))));
    $$('[data-del]', v).forEach((b) => (b.onclick = async () => { if (await confirmBox('Xoá tài khoản nhân viên này?')) { await api('DELETE', `/staff/${b.dataset.del}`).catch(fail); route(); } }));
  }

  // ================= Định tuyến =================
  const ROUTES = [
    [/^dashboard$/, viewDashboard], [/^orders$/, viewOrders], [/^orders\/(\d+)$/, viewOrder],
    [/^products$/, viewProducts], [/^products\/(new|\d+)$/, viewProduct], [/^categories$/, viewCategories],
    [/^customers$/, viewCustomers], [/^reviews$/, viewReviews], [/^coupons$/, viewCoupons],
    [/^appearance$/, viewAppearance, 'admin'], [/^menu$/, viewMenu, 'admin'], [/^pages$/, viewPages, 'admin'], [/^pages\/(new|\d+)$/, viewPage, 'admin'],
    [/^settings$/, viewSettings, 'admin'], [/^staff$/, viewStaff, 'admin'],
  ];

  async function route() {
    if (!ME) return;
    const raw = location.hash.replace(/^#\/?/, '') || 'dashboard';
    const [path, query] = raw.split('?');
    const params = new URLSearchParams(query || '');
    const v = $('#view');
    $('#side').classList.remove('open');
    $$('[data-nav]').forEach((a) => a.classList.toggle('on', path === a.dataset.nav || path.startsWith(`${a.dataset.nav}/`)));
    for (const [re, fn, role] of ROUTES) {
      const m = path.match(re);
      if (!m) continue;
      if (role && ME.role !== role) { v.innerHTML = '<div class="card empty">Bạn không có quyền vào mục này.</div>'; return; }
      v.innerHTML = '<div class="muted" style="padding:40px 0">Đang tải…</div>';
      try { await (m[1] ? fn(v, m[1], params) : fn(v, params)); document.title = `${$('h1', v) ? $('h1', v).textContent : 'Quản trị'} – Quản trị`; }
      catch (err) { if (!err.silent) v.innerHTML = `<div class="card"><div class="alert">${esc(err.message)}</div><a href="#/dashboard">Về tổng quan</a></div>`; }
      window.scrollTo(0, 0);
      return;
    }
    v.innerHTML = '<div class="card empty">Không tìm thấy mục này. <a href="#/dashboard">Về tổng quan</a></div>';
  }
  window.addEventListener('hashchange', route);

  async function boot() {
    try { ME = await api('GET', '/me'); } catch { return; }
    shell();
    route();
    api('GET', '/orders?status=pending&limit=1').then((x) => setPending(x.total)).catch(() => {});
  }

  boot();
  void PENDING;
})();
