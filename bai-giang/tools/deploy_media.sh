#!/bin/bash
# Đưa video, slide, âm thanh của các bài trong site/ lên Cloudflare Pages (https://ngoc-hsk6.pages.dev),
# để repo da-di-qua (Vercel) chỉ giữ trang và dữ liệu nhẹ — 3,7 GB video làm mỗi lần deploy Vercel mất 10–20 phút.
# Trang đọc file qua MEDIA trong web/template.html. Ghi kèm $REPO/hsk6/media.json (số file, dung lượng từng bài)
# cho scripts/seed-catalog.mjs (trang quản lý). Gói miễn phí của Pages: ≤ 20.000 file mỗi lần, mỗi file ≤ 25 MB.
# Cần đăng nhập một lần: npx wrangler@4 login. Chạy: tools/deploy_media.sh
# Mỗi lần deploy, Pages thay cả bộ file nên phải có đủ mọi file. Video đã lên Pages có thể xoá khỏi site/ cho nhẹ máy:
# file nào máy không còn thì script tải lại từ ngoc-hsk6.pages.dev (theo web/published.json) vào thư mục tạm,
# deploy xong thì xoá thư mục tạm. Lúc đó cần trống ổ cỡ dung lượng video bị thiếu (tối đa ~3,5 GB).
set -e
cd "$(dirname "$0")/.."
REPO=${REPO:-~/Desktop/Project/da-di-qua}
PROJECT=ngoc-hsk6
STAGE=build/hsk6-media
rm -rf "$STAGE"; mkdir -p "$STAGE"
trap 'rm -rf "$STAGE"' EXIT
for d in site/bai?? site/ds??; do
  [ -d "$d" ] || continue
  # link cứng chứ không chép: thư mục tạm không tốn thêm chỗ
  rsync -a --link-dest="$PWD/$d/" --include='vid/***' --include='audio/***' --include='slides/' --include='slides/*.jpg' --exclude='*' "$d/" "$STAGE/$(basename "$d")/"
done
# file trang cần (theo published.json) mà máy không còn: tải lại từ Pages
python3 - "$STAGE" <<'EOF'
import json, os, sys, urllib.request
stage = sys.argv[1]
need = []
for lid, l in json.load(open("web/published.json", encoding="utf-8")).items():
    files = [c["file"] for c in l.get("chapters", []) if c.get("file")] + list(l.get("slides", []))
    files += [x[k] for x in l.get("vocab", []) + l.get("passage", []) for k in ("audio", "exaudio") if x.get(k)]
    need += [f"{lid}/{f}" for f in files if not os.path.exists(os.path.join(stage, lid, f))]
for i, f in enumerate(need, 1):
    out = os.path.join(stage, f)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # Cloudflare chặn User-Agent mặc định của Python (403), nên tự đặt tên
    req = urllib.request.Request("https://ngoc-hsk6.pages.dev/" + f, headers={"User-Agent": "hsk6-deploy/1.0"})
    with urllib.request.urlopen(req) as r, open(out, "wb") as w:
        w.write(r.read())
    if i % 50 == 0 or i == len(need):
        print(f"  tải lại từ Pages: {i}/{len(need)}")
EOF
printf '/*\n  Access-Control-Allow-Origin: *\n  Cache-Control: public, max-age=31536000, immutable\n' > "$STAGE/_headers"
# web/media: _worker.js trả 206 cho Range (Safari cần mới phát video), _routes.json chỉ cho video/âm thanh đi qua nó
cp web/media/_worker.js web/media/_routes.json "$STAGE/"
echo '<!doctype html><meta charset="utf-8"><title>Video bài giảng HSK 6</title><p>Kho video, slide và âm thanh của trang <a href="https://travel-plan-lovat-seven.vercel.app/hsk6/">Ngọc học tiếng Trung</a>.</p>' > "$STAGE/index.html"
big=$(find "$STAGE" -type f -size +25M)
[ -z "$big" ] || { echo "File quá 25 MB, Pages không nhận: $big"; exit 1; }
# wrangler 4 cần Node ≥ 20; tải lên hay đứt giữa chừng (EPIPE) nên thử lại, lần sau chỉ gửi file còn thiếu
NODE20=$(ls -d ~/.nvm/versions/node/v2[0-9]*/bin 2>/dev/null | tail -1)
[ -n "$NODE20" ] && export PATH="$NODE20:$PATH"
for i in 1 2 3 4 5 6; do
  npx -y wrangler@4 pages deploy "$STAGE" --project-name "$PROJECT" --branch main --commit-dirty=true && break
  [ $i -eq 6 ] && { echo "Tải lên Cloudflare Pages lỗi 6 lần"; exit 1; }
  sleep 20
done
python3 - "$STAGE" "$REPO/hsk6/media.json" <<'EOF'
import json, os, sys
stage, out = sys.argv[1], sys.argv[2]
lessons = {}
for d in sorted(os.listdir(stage)):
    if not os.path.isdir(os.path.join(stage, d)):
        continue
    m = {}
    for kind, sub, ext in (("video", "vid", ".mp4"), ("slides", "slides", ".jpg"), ("audio", "audio", ".mp3")):
        p = os.path.join(stage, d, sub)
        fs = [f for f in os.listdir(p) if f.endswith(ext)] if os.path.isdir(p) else []
        if fs:
            m[kind] = [len(fs), sum(os.path.getsize(os.path.join(p, f)) for f in fs)]
    lessons[d] = m
json.dump({"base": "https://ngoc-hsk6.pages.dev/", "lessons": lessons}, open(out, "w"), ensure_ascii=False, indent=0)
print(f"Đã ghi {out}: {len(lessons)} bài")
EOF
