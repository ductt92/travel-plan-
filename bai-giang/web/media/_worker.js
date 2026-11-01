// Pages chỉ trả cả file (200) mà bỏ qua Range; Safari (iPhone, WeChat) cần 206 mới phát video, tua cũng cần.
// _routes.json chỉ cho video/âm thanh chạy qua đây, slide ảnh vẫn là file tĩnh của Pages.
const CORS = { 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'public, max-age=31536000, immutable', 'Accept-Ranges': 'bytes' };

/** bỏ `skip` byte đầu, lấy đúng `take` byte, không đọc hết file vào bộ nhớ */
function slice(body, skip, take) {
  return body.pipeThrough(new TransformStream({
    transform(chunk, ctl) {
      if (take <= 0) return;
      let c = chunk;
      if (skip >= c.length) { skip -= c.length; return; }
      if (skip) { c = c.subarray(skip); skip = 0; }
      if (c.length > take) c = c.subarray(0, take);
      take -= c.length;
      ctl.enqueue(c);
    },
  }));
}

export default {
  async fetch(req, env) {
    const res = await env.ASSETS.fetch(new Request(req.url, { method: req.method === 'HEAD' ? 'HEAD' : 'GET' }));
    const headers = new Headers(res.headers);
    for (const [k, v] of Object.entries(CORS)) headers.set(k, v);
    const m = /^bytes=(\d*)-(\d*)$/.exec((req.headers.get('Range') || '').trim());
    if (res.status !== 200 || !m || (!m[1] && !m[2])) return new Response(res.body, { status: res.status, headers });
    // asset server của Pages trả dạng stream, thường không kèm Content-Length: khi đó đọc cả file (≤ 25 MB) để biết cỡ
    let size = Number(res.headers.get('content-length')), buf = null;
    if (!size && req.method !== 'HEAD') { buf = new Uint8Array(await res.arrayBuffer()); size = buf.length; }
    if (!size) return new Response(null, { status: 200, headers });
    let start = m[1] ? Number(m[1]) : Math.max(0, size - Number(m[2]));
    let end = m[1] && m[2] ? Math.min(Number(m[2]), size - 1) : size - 1;
    if (start >= size || start > end) {
      if (!buf) res.body?.cancel();
      headers.set('Content-Range', `bytes */${size}`);
      headers.delete('Content-Length');
      return new Response(null, { status: 416, headers });
    }
    headers.set('Content-Range', `bytes ${start}-${end}/${size}`);
    headers.set('Content-Length', String(end - start + 1));
    const body = req.method === 'HEAD' ? null : buf ? buf.subarray(start, end + 1) : slice(res.body, start, end - start + 1);
    return new Response(body, { status: 206, headers });
  },
};
