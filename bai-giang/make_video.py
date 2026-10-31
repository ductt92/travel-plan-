#!/usr/bin/env python3
"""Dựng video bài giảng từ file kịch bản JSON.

Cách dùng:  python3 make_video.py bai21.json
Kết quả:    out/<tên>.mp4 (kèm phụ đề và mục lục chương) + out/<tên>.srt

Mỗi slide có danh sách "say" (lời giảng). Mỗi câu là một khung hình riêng
có phụ đề; chữ Hán trong câu được đọc bằng giọng Trung (Tingting), phần còn
lại bằng giọng Việt (Linh).
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import wave
from concurrent.futures import ThreadPoolExecutor

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
SR = 22050

# ---------- màu & phông ----------
BG = (251, 248, 243)
PURPLE = (91, 42, 110)
PURPLE_L = (243, 237, 246)
ORANGE = (222, 112, 40)
INK = (40, 36, 48)
GRAY = (105, 100, 115)
CAP_BG = (30, 27, 46)
WHITE = (255, 255, 255)
GREEN = (40, 140, 80)

F_CJK = "/System/Library/Fonts/Hiragino Sans GB.ttc"
F_LAT = "/System/Library/Fonts/Supplemental/Arial.ttf"
F_LAT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
_fc = {}


def font(kind, size, bold=False):
    key = (kind, size, bold)
    if key not in _fc:
        if kind == "cjk":
            _fc[key] = ImageFont.truetype(F_CJK, size, index=1 if bold else 0)
        else:
            _fc[key] = ImageFont.truetype(F_LAT_B if bold else F_LAT, size)
    return _fc[key]


CJK_RE = re.compile(r"[一-鿿㐀-䶿　-〿＀-￯]+")
CJK_CH = re.compile(r"[一-鿿㐀-䶿　-〿＀-￯“”‘’…—]")
NO_LINE_START = set("，。、；：！？）」』”’…—,.;:!?)")


# ---------- chữ hỗn hợp Hán + Latin ----------
def tokens(text):
    """Tách thành đơn vị ngắt dòng: mỗi chữ Hán một đơn vị, chữ Latin theo từ."""
    out, buf = [], ""
    for ch in text:
        if CJK_CH.match(ch):
            if buf:
                out.append(buf)
                buf = ""
            if out and ch in NO_LINE_START:
                out[-1] += ch
            else:
                out.append(ch)
        elif ch == " ":
            buf += ch
            out.append(buf)
            buf = ""
        else:
            buf += ch
    if buf:
        out.append(buf)
    return out


def text_len(s, size, bold=False):
    total = 0
    for i, part in enumerate(re.split(r"([一-鿿㐀-䶿　-〿＀-￯“”‘’…—]+)", s)):
        if not part:
            continue
        kind = "cjk" if i % 2 else "lat"
        total += font(kind, size, bold).getlength(part)
    return total


def wrap(text, size, maxw, bold=False):
    lines = []
    for para in text.split("\n"):
        line = ""
        for tk in tokens(para):
            if line and text_len(line + tk.rstrip(), size, bold) > maxw:
                lines.append(line.rstrip())
                line = tk.lstrip()
            else:
                line += tk
        lines.append(line.rstrip())
    return lines


def draw_line(d, x, y, s, size, color, bold=False):
    asc = font("lat", size, bold).getmetrics()[0]
    for i, part in enumerate(re.split(r"([一-鿿㐀-䶿　-〿＀-￯“”‘’…—]+)", s)):
        if not part:
            continue
        f = font("cjk" if i % 2 else "lat", size, bold)
        fa = f.getmetrics()[0]
        d.text((x, y + asc - fa), part, font=f, fill=color)
        x += f.getlength(part)
    return x


def draw_block(d, x, y, text, size, color, maxw, bold=False, lh=1.45, center=False):
    for ln in wrap(text, size, maxw, bold):
        lx = x + (maxw - text_len(ln, size, bold)) / 2 if center else x
        draw_line(d, lx, y, ln, size, color, bold)
        y += int(size * lh)
    return y


def block_h(text, size, maxw, bold=False, lh=1.45):
    return len(wrap(text, size, maxw, bold)) * int(size * lh)


# ---------- các kiểu slide ----------
def base(lesson, slide):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 110], fill=PURPLE)
    draw_line(d, 50, 32, lesson["tag"], 40, WHITE, True)
    sec = slide.get("section", "")
    if sec:
        draw_line(d, W - 50 - text_len(sec, 34), 38, sec, 34, (230, 215, 240))
    d.rectangle([0, 110, W, 116], fill=ORANGE)
    return im, d


def r_title(lesson, s, focus):
    im = Image.new("RGB", (W, H), PURPLE)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 700, W, 712], fill=ORANGE)
    draw_block(d, 0, 120, s.get("top", ""), 44, (230, 215, 240), W, center=True)
    draw_block(d, 0, 230, s["zh"], 170, WHITE, W, bold=True, center=True)
    draw_block(d, 0, 450, s.get("py", ""), 56, (255, 200, 150), W, center=True)
    draw_block(d, 0, 560, s.get("vi", ""), 64, WHITE, W, bold=True, center=True)
    draw_block(d, 0, 760, s.get("sub", ""), 40, (230, 215, 240), W, center=True)
    return im


def r_bullets(lesson, s, focus):
    im, d = base(lesson, s)
    y = 150
    if s.get("title"):
        y = draw_block(d, 80, y, s["title"], 56, PURPLE, W - 160, bold=True) + 20
    size = s.get("size", 42)
    items = s["items"]
    if focus == -1:  # bản slide PDF: hiện hết, không tô sáng
        focus = None
    elif s.get("reveal") and focus is not None:
        items = items[: focus + 1]
    elif s.get("reveal"):
        items = items[:1]
    for i, it in enumerate(items):
        hl = focus == i
        sub = it.startswith("## ")
        txt = it[3:] if sub else it
        if sub:
            y += 6
            y = draw_block(d, 80, y, txt, size + 2, ORANGE, W - 160, bold=True) + 6
            continue
        h = block_h(txt, size, W - 260)
        if hl:
            d.rounded_rectangle([80, y - 10, W - 80, y + h], 16, fill=(255, 238, 220))
        d.ellipse([110, y + size * 0.45 - 8, 126, y + size * 0.45 + 8], fill=ORANGE if hl else PURPLE)
        y = draw_block(d, 150, y, txt, size, INK, W - 260, bold=hl) + 14
    return im


def r_vocab(lesson, s, focus):
    im, d = base(lesson, s)
    draw_block(d, 80, 140, s.get("title", "Từ mới"), 44, PURPLE, W - 160, bold=True)
    words = s["words"]
    top, bottom, gap = 215, 880, 16
    ch = (bottom - top - gap * (len(words) - 1)) // max(len(words), 3)
    for i, w in enumerate(words):
        y0 = top + i * (ch + gap)
        hl = focus == i
        d.rounded_rectangle([80, y0, W - 80, y0 + ch], 20,
                            fill=WHITE if hl else PURPLE_L,
                            outline=ORANGE if hl else (220, 210, 228), width=6 if hl else 2)
        zsize = 92 if len(w["zh"]) <= 3 else 78
        draw_block(d, 100, y0 + 28, w["zh"], zsize, PURPLE, 440, bold=True, center=True)
        draw_block(d, 100, y0 + 40 + int(zsize * 1.15), w["py"], 40, ORANGE, 440, center=True)
        x = 580
        d.line([x - 20, y0 + 20, x - 20, y0 + ch - 20], fill=(210, 200, 220), width=2)
        y = y0 + 22
        draw_line(d, x, y, f"Hán Việt: {w['hv']}", 34, PURPLE, True)
        if w.get("loai"):
            draw_line(d, W - 130 - text_len(w["loai"], 30), y + 4, w["loai"], 30, GRAY)
        y = draw_block(d, x, y + 50, w["vi"], 36, INK, W - 100 - x, bold=True, lh=1.3)
        if w.get("ex"):
            y = draw_block(d, x, y + 4, "Ví dụ: " + w["ex"], 34, INK, W - 100 - x, lh=1.3)
        if w.get("exvi"):
            draw_block(d, x, y, w["exvi"], 30, GRAY, W - 100 - x, lh=1.3)
    return im


def r_passage(lesson, s, focus):
    im, d = base(lesson, s)
    draw_block(d, 80, 140, s.get("title", "Bài khóa"), 44, PURPLE, W - 160, bold=True)
    zsize = s.get("zsize", 48)
    y = 225
    zh_h = block_h(s["zh"], zsize, W - 260, lh=1.65)
    d.rounded_rectangle([80, y - 20, W - 80, y + zh_h + 10], 20, fill=WHITE, outline=(220, 210, 228), width=2)
    y = draw_block(d, 130, y, s["zh"], zsize, INK, W - 260, lh=1.65) + 40
    if focus is None or focus >= 1 or s.get("show_vi"):
        d.rectangle([80, y, 88, y + block_h(s["vi"], 32, W - 260, lh=1.4)], fill=ORANGE)
        draw_block(d, 120, y, s["vi"], 32, GRAY, W - 240, lh=1.4)
    return im


def r_compare(lesson, s, focus):
    im, d = base(lesson, s)
    y = draw_block(d, 80, 140, s["title"], 52, PURPLE, W - 160, bold=True) + 10
    if s.get("common"):
        y = draw_block(d, 80, y, s["common"], 36, INK, W - 160) + 16
    cw = (W - 160 - 40) // 2
    for ci, col in enumerate(s["cols"]):
        x0 = 80 + ci * (cw + 40)
        hl = focus == ci
        d.rounded_rectangle([x0, y, x0 + cw, 870], 20, fill=WHITE if hl else PURPLE_L,
                            outline=ORANGE if hl else (220, 210, 228), width=6 if hl else 2)
        draw_block(d, x0, y + 20, col["head"], 64, ORANGE, cw, bold=True, center=True)
        yy = y + 120
        for ln in col["lines"]:
            color = GREEN if ln.startswith("Đúng") else (200, 60, 60) if ln.startswith("Sai") else INK
            yy = draw_block(d, x0 + 30, yy, ln, 34, color, cw - 60, lh=1.35) + 12
    return im


RENDER = {"title": r_title, "bullets": r_bullets, "vocab": r_vocab,
          "passage": r_passage, "compare": r_compare}


def add_caption(im, text):
    if not text:
        return im
    im = im.copy()
    d = ImageDraw.Draw(im)
    size = 40
    lines = wrap(text, size, W - 200)
    while len(lines) > 3 and size > 28:
        size -= 3
        lines = wrap(text, size, W - 200)
    lines = lines[:4]
    lh = int(size * 1.35)
    top = H - 30 - lh * len(lines) - 20
    d.rectangle([0, top, W, H], fill=CAP_BG)
    y = top + 18
    for ln in lines:
        draw_line(d, (W - text_len(ln, size)) / 2, y, ln, size, WHITE)
        y += lh
    return im


# ---------- âm thanh ----------
def tts(text, voice, rate, cache):
    key = hashlib.md5(f"{voice}|{rate}|{text}".encode()).hexdigest()
    path = os.path.join(cache, key + ".wav")
    if not os.path.exists(path):
        # "say" thỉnh thoảng treo vô hạn: đặt giờ chờ rồi thử lại; ghi ra file tạm để
        # một lần đọc bị ngắt không để lại file dở trong bộ nhớ đệm. Mỗi luồng một file tạm
        # riêng: cùng một câu có thể được đọc song song ở hai luồng
        tmp = f"{path}.{threading.get_ident()}.part.wav"
        for attempt in range(4):
            try:
                subprocess.run(["say", "-v", voice, "-r", str(rate), "--file-format=WAVE",
                                f"--data-format=LEI16@{SR}", "-o", tmp, text], check=True, timeout=90)
                break
            except subprocess.TimeoutExpired:
                if attempt == 3:
                    raise
        os.replace(tmp, path)
    return path


def pieces(text, repl):
    """Chia câu thành các đoạn (ngôn ngữ, chữ) để đổi giọng đọc."""
    out, pos = [], 0
    for m in CJK_RE.finditer(text):
        if m.start() > pos:
            out.append(("vi", text[pos:m.start()]))
        zh = m.group()
        for a, b in repl.items():
            zh = zh.replace(a, b)
        out.append(("zh", zh))
        pos = m.end()
    if pos < len(text):
        out.append(("vi", text[pos:]))
    return [(l, t.strip(" “”\"'()（）")) for l, t in out if re.search(r"\w", t)]


def read_wav(path):
    with wave.open(path) as w:
        return w.readframes(w.getnframes())


def silence(sec):
    return b"\x00\x00" * int(SR * sec)


def main():
    src = sys.argv[1]
    lesson = json.load(open(src, encoding="utf-8"))
    name = os.path.splitext(os.path.basename(src))[0]
    here = os.path.dirname(os.path.abspath(src))
    work = os.path.join(here, "build", name)
    cache = os.path.join(here, "build", "tts_cache")
    outdir = os.path.join(here, "out")
    for p in (work, cache, outdir):
        os.makedirs(p, exist_ok=True)
    repl = lesson.get("tts_replace", {})
    vi_voice, zh_voice = lesson.get("vi_voice", "Linh"), lesson.get("zh_voice", "Tingting")

    # 1) gom các câu
    segs = []
    for si, s in enumerate(lesson["slides"]):
        for item in s["say"]:
            if isinstance(item, str):
                item = {"t": item}
            segs.append({"slide": si, "text": item["t"], "focus": item.get("f"),
                         "cap": item.get("cap", item["t"]),
                         "zr": item.get("zr", s.get("zr", lesson.get("zh_rate", 145))),
                         "vr": lesson.get("vi_rate", 175)})

    # 2) tổng hợp giọng nói (song song)
    jobs = []
    for sg in segs:
        sg["parts"] = pieces(sg["text"], repl)
        for lang, t in sg["parts"]:
            jobs.append((t, zh_voice if lang == "zh" else vi_voice, sg["zr"] if lang == "zh" else sg["vr"]))
    print(f"{len(segs)} câu, {len(jobs)} đoạn giọng đọc…", flush=True)
    with ThreadPoolExecutor(8) as ex:
        paths = list(ex.map(lambda j: tts(j[0], j[1], j[2], cache), jobs))

    # 3) ghép âm thanh, tính thời lượng từng câu
    audio, k, t = bytearray(), 0, 0.0
    prev_slide = None
    for sg in segs:
        lead = 0.8 if sg["slide"] != prev_slide else 0.0
        prev_slide = sg["slide"]
        chunk = bytearray(silence(lead))
        for i, _ in enumerate(sg["parts"]):
            chunk += read_wav(paths[k])
            chunk += silence(0.25)
            k += 1
        chunk += silence(0.45)
        sg["start"], sg["dur"] = t, len(chunk) / 2 / SR
        t += sg["dur"]
        audio += chunk
    audio += silence(1.5)
    segs[-1]["dur"] += 1.5
    wav_path = os.path.join(work, "audio.wav")
    with wave.open(wav_path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(bytes(audio))

    # 4) vẽ khung hình
    print("Vẽ slide…", flush=True)
    bases = {}
    for i, sg in enumerate(segs):
        s = lesson["slides"][sg["slide"]]
        key = (sg["slide"], sg["focus"])
        if key not in bases:
            bases[key] = RENDER[s["type"]](lesson, s, sg["focus"])
        sg["img"] = os.path.join(work, f"f{i:04d}.png")
        add_caption(bases[key], sg["cap"]).save(sg["img"], optimize=False, compress_level=1)

    # bộ slide PDF đi kèm (mỗi slide một trang, hiện đầy đủ đáp án)
    pages = [RENDER[s["type"]](lesson, s, -1 if s["type"] == "bullets" else None)
             for s in lesson["slides"]]
    pdf = os.path.join(outdir, name + "_slides.pdf")
    pages[0].save(pdf, save_all=True, append_images=pages[1:], resolution=150)
    print(f"Slide: {pdf}", flush=True)

    # 5) danh sách ghép + phụ đề + chương
    with open(os.path.join(work, "list.ffconcat"), "w") as f:
        f.write("ffconcat version 1.0\n")
        for sg in segs:
            f.write(f"file '{sg['img']}'\nduration {sg['dur']:.3f}\n")
        f.write(f"file '{segs[-1]['img']}'\n")

    def ts(x, sep=","):
        h, m = int(x // 3600), int(x % 3600 // 60)
        return f"{h:02d}:{m:02d}:{int(x % 60):02d}{sep}{int(x * 1000 % 1000):03d}"

    srt = os.path.join(outdir, name + ".srt")
    with open(srt, "w", encoding="utf-8") as f:
        for i, sg in enumerate(segs, 1):
            f.write(f"{i}\n{ts(sg['start'])} --> {ts(sg['start'] + sg['dur'] - 0.2)}\n{sg['text']}\n\n")

    meta = os.path.join(work, "chapters.txt")
    chapters = []
    for sg in segs:
        ch = lesson["slides"][sg["slide"]].get("chapter")
        if ch and (not chapters or chapters[-1][1] != ch) and sg["slide"] not in [c[2] for c in chapters]:
            chapters.append((sg["start"], ch, sg["slide"]))
    with open(meta, "w", encoding="utf-8") as f:
        f.write(";FFMETADATA1\ntitle=" + lesson["title"] + "\n")
        for i, (st, ch, _) in enumerate(chapters):
            end = chapters[i + 1][0] if i + 1 < len(chapters) else t + 1.5
            f.write(f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(st * 1000)}\nEND={int(end * 1000)}\ntitle={ch}\n")

    # 6) xuất video
    out = os.path.join(outdir, name + ".mp4")
    print("Xuất video…", flush=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", os.path.join(work, "list.ffconcat"), "-i", wav_path, "-i", srt, "-i", meta,
                    "-map", "0:v", "-map", "1:a", "-map", "2:s", "-map_metadata", "3", "-map_chapters", "3",
                    "-vf", "fps=25,format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                    "-tune", "stillimage", "-crf", "22", "-c:a", "aac", "-b:a", "128k",
                    "-c:s", "mov_text", "-metadata:s:s:0", "language=vie",
                    "-movflags", "+faststart", out], check=True)
    print(f"Xong: {out}  ({t / 60:.1f} phút)")
    for st, ch, _ in chapters:
        print(f"  {ts(st, '.')[:8]}  {ch}")


if __name__ == "__main__":
    main()
