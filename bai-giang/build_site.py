#!/usr/bin/env python3
"""Dựng trang web học tập (thư mục site/) từ các bài giảng đã làm.

Cách dùng:  python3 build_site.py bai21 [bai22 ...]
Cần có sẵn: <bai>_src.py, <bai>.json và out/<bai>.mp4, out/<bai>.srt, out/<bai>_slides.pdf
(bài đã có trong web/published.json mà mất video gốc thì giữ bản đã lên trang; mọi bài trong đó luôn được giữ)
Video được cắt theo chương và nén lại 720p để trang tải nhanh (mỗi file < 15 MB).
Bài đã đưa lên YouTube (có id trong web/youtube.json, hoặc file ở biến môi trường YOUTUBE_JSON)
thì không cắt video: trang phát cả bài từ YouTube, mỗi chương ghi giây bắt đầu ("start"),
và thư mục site/<bai>/vid/ được xoá.
"""
import glob
import json
import os
import re
import runpy
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "site")
TEMPLATE = os.path.join(HERE, "web", "template.html")
YOUTUBE_JSON = os.environ.get("YOUTUBE_JSON") or os.path.join(HERE, "web", "youtube.json")


def youtube_ids():
    """{"bai01": "<id video YouTube>", …}; chưa có file thì mọi bài dùng video trên máy."""
    if not os.path.exists(YOUTUBE_JSON):
        return {}
    return {k: v for k, v in json.load(open(YOUTUBE_JSON, encoding="utf-8")).items() if v}


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def chapters(mp4):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_chapters", "-of", "json", mp4],
                         capture_output=True, text=True).stdout
    return [(float(c["start_time"]), float(c["end_time"]), c["tags"]["title"])
            for c in json.loads(out)["chapters"]]


def srt(path):
    def sec(t):
        h, m, s = t.replace(",", ".").split(":")
        return int(h) * 3600 + int(m) * 60 + float(s)
    cues = []
    for block in open(path, encoding="utf-8").read().strip().split("\n\n"):
        lines = block.split("\n")
        a, b = lines[1].split(" --> ")
        cues.append((sec(a), sec(b), " ".join(lines[2:])))
    return cues


def zh_audio(text, out, repl, rate):
    """Đọc câu tiếng Trung bằng giọng Tingting, lưu mp3 nhỏ."""
    if os.path.exists(out):
        return
    for k, v in repl.items():
        text = text.replace(k, v)
    aiff = out + ".aiff"
    # "say" thỉnh thoảng treo vô hạn: đặt giờ chờ rồi thử lại
    for attempt in range(4):
        try:
            subprocess.run(["say", "-v", "Tingting", "-r", str(rate), "-o", aiff, text],
                           check=True, timeout=60, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            break
        except subprocess.TimeoutExpired:
            if attempt == 3:
                raise
    run(["ffmpeg", "-y", "-i", aiff, "-ac", "1", "-c:a", "libmp3lame", "-b:a", "48k", out])
    os.remove(aiff)


def slide_titles(lesson, zh):
    """Tên bài và tiêu đề từng slide (slides/titles.json), để giáo viên chọn bài/slide ở lớp học trực tiếp."""
    one = lambda t: " ".join(str(t or "").split())  # tiêu đề dài có thể xuống dòng trên slide
    return {"title": one(lesson["slides"][0].get("vi")), "zh": zh,
            "slides": [{"title": one(s.get("title") or s.get("vi")), "section": one(s.get("section"))}
                       for s in lesson["slides"]]}


def build_lesson(name, yt=None):
    src = runpy.run_path(os.path.join(HERE, f"{name}_src.py"), run_name="__src__")
    lesson = json.load(open(os.path.join(HERE, f"{name}.json"), encoding="utf-8"))
    repl = lesson.get("tts_replace", {})
    d = os.path.join(SITE, name)
    for sub in ("slides", "audio") if yt else ("vid", "slides", "audio"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    if yt and os.path.isdir(os.path.join(d, "vid")):
        print("  đã có trên YouTube: xoá video trên máy")
        shutil.rmtree(os.path.join(d, "vid"))
    mp4 = os.path.join(HERE, "out", f"{name}.mp4")

    # 1. Video theo chương + lời giảng (transcript) theo chương
    cues = srt(os.path.join(HERE, "out", f"{name}.srt"))
    # mỗi câu giảng (một dòng phụ đề) thuộc về một slide, để trang hiện đúng slide theo video
    cue_slide = [k for k, s in enumerate(lesson["slides"]) for _ in s["say"]]
    assert len(cue_slide) == len(cues), "số dòng phụ đề không khớp số câu giảng"
    cues = [(a, b, t, cue_slide[k]) for k, (a, b, t) in enumerate(cues)]
    chaps = []
    for i, (a, b, title) in enumerate(chapters(mp4)):
        lines = [[round(s - a, 2), t, k] for s, e, t, k in cues if a - 0.5 <= s < b - 0.1]
        if yt:
            # video YouTube là cả bài: chương = đoạn bắt đầu ở giây "start"
            chaps.append({"title": title, "start": round(a, 3), "dur": round(b - a, 1), "lines": lines})
            continue
        f = f"vid/c{i + 1:02d}.mp4"
        out = os.path.join(d, f)
        if not os.path.exists(out):
            print(f"  nén chương {i + 1}: {title}")
            run(["ffmpeg", "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", mp4, "-map", "0:v:0", "-map", "0:a:0",
                 "-vf", "scale=1280:720", "-c:v", "libx264", "-tune", "stillimage", "-crf", "28",
                 "-preset", "medium", "-r", "10", "-c:a", "aac", "-b:a", "48k", "-ac", "1",
                 "-movflags", "+faststart", out])
        chaps.append({"title": title, "file": f, "dur": round(b - a, 1), "lines": lines})

    # 2. Slide dạng ảnh
    if not glob.glob(os.path.join(d, "slides", "*.jpg")):
        print("  xuất slide")
        run(["pdftoppm", "-jpeg", "-jpegopt", "quality=82", "-scale-to-x", "1280", "-scale-to-y", "-1",
             os.path.join(HERE, "out", f"{name}_slides.pdf"), os.path.join(d, "slides", "s")])
    slides = sorted(os.path.relpath(p, d) for p in glob.glob(os.path.join(d, "slides", "*.jpg")))

    # 3. Từ vựng, bài khóa + âm thanh đọc mẫu
    print("  tạo âm thanh từ vựng / bài khóa")
    vocab = []
    for i, v in enumerate(src["V"]):
        # phần tử thứ 9 (nếu có) là chữ đồng âm để đọc từ một chữ dễ bị đọc sai âm (vd. 乘 → 承)
        zh, py, hv, loai, vi, ex, exvi, _expl = v[:8]
        w, e = f"audio/w{i + 1:02d}.mp3", f"audio/e{i + 1:02d}.mp3"
        zh_audio(v[8] if len(v) > 8 else zh, os.path.join(d, w), repl, 120)
        zh_audio(ex, os.path.join(d, e), repl, 140)
        vocab.append({"zh": zh, "py": py, "hv": hv, "type": loai, "vi": vi, "ex": ex, "exvi": exvi,
                      "audio": w, "exaudio": e})
    passage = []
    for i, p in enumerate(src["P"]):
        # phần tử thứ 4 (nếu có) là bản để đọc: số viết bằng chữ Hán, bỏ ngoặc kép
        zh, vi, notes = p[:3]
        spoken = p[3] if len(p) > 3 else zh
        a = f"audio/p{i + 1:02d}.mp3"
        zh_audio(spoken, os.path.join(d, a), repl, 140)
        passage.append({"zh": zh, "vi": vi, "notes": notes, "audio": a})

    # 4. Bài tập có đáp án (các slide "reveal": câu hỏi rồi tới dòng "Đáp án")
    exercises = []
    for s in lesson["slides"]:
        if not s.get("reveal"):
            continue
        items, qs = s["items"], []
        for j, it in enumerate(items):
            if not it.startswith("Đáp án") and j + 1 < len(items) and items[j + 1].startswith("Đáp án"):
                qs.append({"q": it, "a": re.sub(r"^Đáp án( gợi ý)?:\s*", "", items[j + 1])})
        exercises.append({"title": s["title"], "items": qs})

    title = src.get("TAG", lesson["tag"])
    # 顶石中文 đánh số kiểu "Bài 1.1": giữ nguyên dạng chuỗi, HSK 6 vẫn là số nguyên
    m = re.search(r"Bài (\d+(?:\.\d+)?)", title)
    first = lesson["slides"][0]
    # tên bài đầy đủ lấy từ TAG; slide tiêu đề có thể tách tên dài thành hai dòng (vd. Bài 40),
    # khi đó dòng đầu của "sub" là pinyin đầy đủ
    zh = title.split("·")[-1].strip() or first.get("zh", "")
    py = first.get("py", "")
    if zh != first.get("zh") and first.get("sub"):
        py = first["sub"].split("\n")[0]
    with open(os.path.join(d, "slides", "titles.json"), "w", encoding="utf-8") as f:
        json.dump(slide_titles(lesson, zh), f, ensure_ascii=False)
    info = {"id": name, "num": (int(m.group(1)) if m.group(1).isdigit() else m.group(1)) if m else 0, "zh": zh,
            "py": py, "vi": first.get("vi", ""), "tag": title,
            "chapters": chaps, "slides": slides, "vocab": vocab, "passage": passage,
            "exercises": exercises}
    if yt:
        info["yt"] = yt
    return info


# dữ liệu mọi bài đã lên trang (web/published.json): bài nào không còn video gốc out/<bai>.mp4
# (vd. mất thư mục HSK ngày 31/10) vẫn giữ nguyên trên trang, và lần dựng sau không làm rơi bài nào
PUBLISHED = os.path.join(HERE, "web", "published.json")


def main():
    names = sys.argv[1:] or sorted(os.path.basename(p)[:-4] for p in glob.glob(os.path.join(HERE, "out", "*.mp4")))
    published = json.load(open(PUBLISHED, encoding="utf-8")) if os.path.exists(PUBLISHED) else {}
    names += [n for n in published if n not in names]
    built, yt = {}, youtube_ids()
    for n in names:
        if not os.path.exists(os.path.join(HERE, "out", n + ".mp4")) and n in published:
            print(f"Bài {n}  (giữ bản đã lên trang)")
            built[n] = published[n]
            continue
        print(f"Bài {n}" + (f"  (YouTube {yt[n]})" if n in yt else ""))
        built[n] = build_lesson(n, yt.get(n))
    json.dump({**published, **built}, open(PUBLISHED, "w", encoding="utf-8"), ensure_ascii=False)
    # danh sách tất cả bài trong các giáo trình (bài chưa có video hiện là "Sắp có")
    catalog = json.load(open(os.path.join(HERE, "web", "catalog.json"), encoding="utf-8"))
    order = [l["id"] for bk in catalog["books"] for u in bk["units"] for l in u["lessons"]]
    lessons = sorted(built.values(), key=lambda l: order.index(l["id"]) if l["id"] in order else len(order))
    data = json.dumps(lessons, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    cat = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (open(TEMPLATE, encoding="utf-8").read()
            .replace("/*LESSONS*/[]", data).replace('/*CATALOG*/{"books":[]}', cat))
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(html)
    # ảnh dùng trên trang (ảnh của Ngọc…) nằm cạnh template
    os.makedirs(os.path.join(SITE, "img"), exist_ok=True)
    for p in glob.glob(os.path.join(HERE, "web", "*.webp")) + glob.glob(os.path.join(HERE, "web", "*.png")):
        shutil.copy(p, os.path.join(SITE, "img"))
    # trang "Ngữ pháp qua tình huống" (web/ngu-phap.html viết dạng artifact, không có <head>: bọc thêm ở đây)
    os.makedirs(os.path.join(SITE, "ngu-phap"), exist_ok=True)
    with open(os.path.join(SITE, "ngu-phap", "index.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                '<style>body { margin: 0; }</style>\n'
                # Liquis glass dùng chung cả site, giống đầu web/template.html
                '<link rel="stylesheet" href="/glass/react-liquis-glass.css">\n'
                '<link rel="stylesheet" href="/glass/glass.css">\n'
                '<script src="/glass/glass.js"></script>\n'
                '<script>if (window.glassMode) document.documentElement.classList.add("glass-ok");</script>\n'
                + open(os.path.join(HERE, "web", "ngu-phap.html"), encoding="utf-8").read() + "\n</html>\n")
    # nội dung trang ngữ pháp: trang đọc từ /api/node/grammar (Neon), lỗi thì dùng bản đi kèm này
    # (nạp vào Neon: node scripts/seed-grammar.mjs trong repo da-di-qua)
    shutil.copy(os.path.join(HERE, "web", "ngu-phap.json"), os.path.join(SITE, "ngu-phap", "data.json"))
    # file mẫu cho trang ghi chú (nút "Thêm ghi chú mẫu")
    if os.path.isdir(os.path.join(HERE, "web", "samples")):
        shutil.copytree(os.path.join(HERE, "web", "samples"), os.path.join(SITE, "samples"), dirs_exist_ok=True)
    total = sum(os.path.getsize(p) for p in glob.glob(os.path.join(SITE, "**", "*"), recursive=True)
                if os.path.isfile(p))
    print(f"Xong: {SITE}/index.html  ({total / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
