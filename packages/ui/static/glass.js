// Bật/tắt giao diện kính cho trang tĩnh (HSK 6, lớp học, sổ tay) — bản không cần bundler
// của packages/ui/src/glass-mode.js: cùng khóa localStorage['glass'], cùng <html data-glass="off">.
//
// Đặt trong <head> (không defer) để trang mở ra đã đúng chế độ, không nháy:
//   <link rel="stylesheet" href="/glass/react-liquis-glass.css">
//   <link rel="stylesheet" href="/glass/glass.css">
//   <script src="/glass/glass.js"></script>
// Nút bật/tắt: bất kỳ phần tử nào có [data-glass-toggle] (thường là <button>).
// Phần tử con [data-glass-label] (nếu có) được ghi chữ "Liquis glass: on" / "Liquis glass: off".
(function () {
  var KEY = 'glass';
  var root = document.documentElement;

  function read() {
    try { return localStorage.getItem(KEY) !== 'off'; } catch (e) { return true; }
  }
  function apply(on) {
    if (on) root.removeAttribute('data-glass');
    else root.setAttribute('data-glass', 'off');
    var btns = document.querySelectorAll('[data-glass-toggle]');
    for (var i = 0; i < btns.length; i++) {
      var b = btns[i];
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.title = on ? 'Tắt Liquis glass' : 'Bật Liquis glass';
      var l = b.querySelector('[data-glass-label]');
      if (l) l.textContent = on ? 'Liquis glass: on' : 'Liquis glass: off';
    }
  }
  function set(on) {
    try { localStorage.setItem(KEY, on ? 'on' : 'off'); } catch (e) { /* chỉ đổi trang này */ }
    apply(on);
    document.dispatchEvent(new CustomEvent('glasschange', { detail: { on: on } }));
  }

  apply(read());
  document.addEventListener('DOMContentLoaded', function () { apply(read()); });
  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('[data-glass-toggle]')) set(!read());
  });
  addEventListener('storage', function (e) { if (e.key === KEY) apply(read()); });

  window.glassMode = { get: read, set: set, toggle: function () { set(!read()); } };
})();
