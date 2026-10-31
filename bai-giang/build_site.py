#!/usr/bin/env python3
"""Dựng trang web học tập (thẳng vào hsk6/ của repo) từ các bài giảng đã làm.

Cách dùng:  python3 build_site.py bai21 [bai22 ...]   (không ghi tên bài: dựng mọi bài đang có out/<bai>.mp4)
Cần có sẵn: <bai>_src.py, <bai>.json và out/<bai>.mp4, out/<bai>.srt, out/<bai>_slides.pdf
Video được cắt theo chương và nén lại 720p để trang tải nhanh (mỗi file < 15 MB).
Bài không dựng lại lần này giữ nguyên dữ liệu đang có trong hsk6/index.html (out/ của bài cũ có thể không còn).
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
SITE = os.environ.get("HSK6_SITE") or os.path.join(HERE, "..", "hsk6")
TEMPLATE = os.path.join(HERE, "web", "template.html")


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
    """Đọc câu tiếng Trung bằng giọng Tingting, lưu m4a nhỏ."""
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
    run(["ffmpeg", "-y", "-i", aiff, "-ac", "1", "-c:a", "aac", "-b:a", "40k", out])
    os.remove(aiff)


def slide_titles(lesson, zh):
    """Tên bài và tiêu đề từng slide (slides/titles.json), để giáo viên chọn bài/slide ở lớp học trực tiếp."""
    one = lambda t: " ".join(str(t or "").split())  # tiêu đề dài có thể xuống dòng trên slide
    return {"title": one(lesson["slides"][0].get("vi")), "zh": zh,
            "slides": [{"title": one(s.get("title") or s.get("vi")), "section": one(s.get("section"))}
                       for s in lesson["slides"]]}


def build_lesson(name):
    src = runpy.run_path(os.path.join(HERE, f"{name}_src.py"), run_name="__src__")
    lesson = json.load(open(os.path.join(HERE, f"{name}.json"), encoding="utf-8"))
    repl = lesson.get("tts_replace", {})
    d = os.path.join(SITE, name)
    for sub in ("vid", "slides", "audio"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    mp4 = os.path.join(HERE, "out", f"{name}.mp4")

    # 1. Video theo chương + lời giảng (transcript) theo chương
    cues = srt(os.path.join(HERE, "out", f"{name}.srt"))
    # mỗi câu giảng (một dòng phụ đề) thuộc về một slide, để trang hiện đúng slide theo video
    cue_slide = [k for k, s in enumerate(lesson["slides"]) for _ in s["say"]]
    assert len(cue_slide) == len(cues), "số dòng phụ đề không khớp số câu giảng"
    cues = [(a, b, t, cue_slide[k]) for k, (a, b, t) in enumerate(cues)]
    chaps = []
    for i, (a, b, title) in enumerate(chapters(mp4)):
        f = f"vid/c{i + 1:02d}.mp4"
        out = os.path.join(d, f)
        if not os.path.exists(out):
            print(f"  nén chương {i + 1}: {title}")
            run(["ffmpeg", "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", mp4, "-map", "0:v:0", "-map", "0:a:0",
                 "-vf", "scale=1280:720", "-c:v", "libx264", "-tune", "stillimage", "-crf", "28",
                 "-preset", "medium", "-r", "10", "-c:a", "aac", "-b:a", "48k", "-ac", "1",
                 "-movflags", "+faststart", out])
        lines = [[round(s - a, 2), t, k] for s, e, t, k in cues if a - 0.5 <= s < b - 0.1]
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
    for i, (zh, py, hv, loai, vi, ex, exvi, _expl) in enumerate(src["V"]):
        w, e = f"audio/w{i + 1:02d}.m4a", f"audio/e{i + 1:02d}.m4a"
        zh_audio(zh, os.path.join(d, w), repl, 120)
        zh_audio(ex, os.path.join(d, e), repl, 140)
        vocab.append({"zh": zh, "py": py, "hv": hv, "type": loai, "vi": vi, "ex": ex, "exvi": exvi,
                      "audio": w, "exaudio": e})
    passage = []
    for i, (zh, vi, notes) in enumerate(src["P"]):
        a = f"audio/p{i + 1:02d}.m4a"
        zh_audio(zh, os.path.join(d, a), repl, 140)
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
    m = re.search(r"Bài (\d+)", title)
    first = lesson["slides"][0]
    # tên bài đầy đủ lấy từ TAG; slide tiêu đề có thể tách tên dài thành hai dòng (vd. Bài 40),
    # khi đó dòng đầu của "sub" là pinyin đầy đủ
    zh = title.split("·")[-1].strip() or first.get("zh", "")
    py = first.get("py", "")
    if zh != first.get("zh") and first.get("sub"):
        py = first["sub"].split("\n")[0]
    with open(os.path.join(d, "slides", "titles.json"), "w", encoding="utf-8") as f:
        json.dump(slide_titles(lesson, zh), f, ensure_ascii=False)
    return {"id": name, "num": int(m.group(1)) if m else 0, "zh": zh,
            "py": py, "vi": first.get("vi", ""), "tag": title,
            "chapters": chaps, "slides": slides, "vocab": vocab, "passage": passage,
            "exercises": exercises}


def main():
    names = sys.argv[1:] or sorted(os.path.basename(p)[:-4] for p in glob.glob(os.path.join(HERE, "out", "*.mp4")))
    built = {}
    for n in names:
        print(f"Bài {n}")
        built[n] = build_lesson(n)
    # giữ các bài đã có trên trang mà lần này không dựng lại
    lessons, index = [], os.path.join(SITE, "index.html")
    if os.path.exists(index):
        m = re.search(r"^const LESSONS = (.*);$", open(index, encoding="utf-8").read(), re.M)
        if m and not m.group(1).startswith("/*"):
            lessons = json.loads(m.group(1).replace("<\\/", "</"))
    lessons = sorted([built.pop(l["id"], l) for l in lessons] + list(built.values()), key=lambda l: l["id"])
    data =json.dumps(lessons, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    # danh sách tất cả bài trong các giáo trình (bài chưa có video hiện là "Sắp có")
    catalog = json.load(open(os.path.join(HERE, "web", "catalog.json"), encoding="utf-8"))
    cat = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    # file Excel thuật ngữ (tạo bằng thuat_ngu.py), nhúng nguyên dạng sheet cho mục "Thuật ngữ"
    terms_path = os.path.join(HERE, "web", "terms.json")
    terms = (open(terms_path, encoding="utf-8").read().strip().replace("</", "<\\/")
             if os.path.exists(terms_path) else "null")
    html = (open(TEMPLATE, encoding="utf-8").read()
            .replace("/*LESSONS*/[]", data).replace('/*CATALOG*/{"books":[]}', cat)
            .replace("/*TERMS*/null", terms))
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
    # file mẫu cho trang ghi chú (nút "Thêm ghi chú mẫu")
    if os.path.isdir(os.path.join(HERE, "web", "samples")):
        shutil.copytree(os.path.join(HERE, "web", "samples"), os.path.join(SITE, "samples"), dirs_exist_ok=True)
    total = sum(os.path.getsize(p) for p in glob.glob(os.path.join(SITE, "**", "*"), recursive=True)
                if os.path.isfile(p))
    print(f"Xong: {SITE}/index.html  ({total / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
