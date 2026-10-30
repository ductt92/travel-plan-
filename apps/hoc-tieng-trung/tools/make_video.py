"""Dựng video MP4 cho bài giảng.
Chạy: python3 apps/hoc-tieng-trung/tools/make_video.py <thư mục tạm> apps/hoc-tieng-trung/public/video <id bài> [...]   (vd 1-1 1-2 …, "cap3" cho cả một cấp, hoặc "all")
Cần: site đã build đang chạy (npm run build && npm run preview, cổng 4173), ffmpeg, Google Chrome, kho giọng public/audio/ (tools/gen_audio.py).
Giọng: file Google Dịch trong audio/; câu nào thiếu thì dùng giọng macOS (Linh / Tingting).
Khung hình: Chrome headless chụp route #/render/<id>/<bước> ở 1920×1080."""
import html, json, os, re, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP, OUTDIR, IDS = sys.argv[1], sys.argv[2], [a for a in sys.argv[3:] if not a.startswith('--')]
TIMING_ONLY = '--timing' in sys.argv     # chỉ tính mốc thời gian từng bước (không chụp khung, không dựng video)
TIMING = os.path.join(ROOT, 'src', 'data', 'video-timing.json')
BASE = os.environ.get('BASE', 'http://localhost:4173/hoc-tieng-trung/')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
TEMPO = {'vi': 1.08, 'zh': 0.88}          # tốc độ đọc: tiếng Việt nhanh hơn chút, tiếng Trung chậm lại cho dễ nghe
GAP = {'vi': 0.3, 'zh': 0.6}
SLIDE_GAP = 0.7
MAC = {'vi': ('Linh', '185'), 'zh': ('Tingting', '135')}
N = int(os.environ.get('VIDEO_JOBS', 6))   # số Chrome chụp khung song song

def key(lang, text):
    h1, h2 = 0x811c9dc5, 5381
    for x in (lang + '|' + text).encode('utf-8'):
        h1 = ((h1 ^ x) * 0x01000193) & 0xffffffff
        h2 = (h2 * 33 + x) & 0xffffffff
    return f'{h1:08x}{h2:08x}'

def run(*a):
    subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def duration(path):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout)

def dump(route):
    dom = subprocess.run([CHROME, '--headless=new', '--disable-gpu', f'--user-data-dir={TMP}/prof-x', '--virtual-time-budget=5000',
                          '--dump-dom', f'{BASE}#/{route}'], capture_output=True, text=True).stdout
    return json.loads(html.unescape(re.search(r'<pre id="steps">(.*?)</pre>', dom, re.S).group(1)))

def save_timing(lid, durs):
    """Giây bắt đầu của từng bước trong video, để trang Video bài giảng nhảy tới câu / slide"""
    data = json.load(open(TIMING)) if os.path.exists(TIMING) else {}
    t, starts = 0.0, []
    for d in durs: starts.append(round(t, 2)); t += d
    data[lid] = starts
    open(TIMING, 'w').write(json.dumps(dict(sorted(data.items(), key=lambda kv: tuple(map(int, kv[0].split('-'))))), separators=(',', ':')))

def silence(sec, path):
    run('ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', f'{sec:.2f}', '-c:a', 'pcm_s16le', path)

def build(lid):
    work = f'{TMP}/{lid}'; shutil.rmtree(work, ignore_errors=True)
    os.makedirs(f'{work}/frames'); os.makedirs(f'{work}/audio')
    steps = dump(f'steps/{lid}')
    missing = 0

    def step_audio(i):
        nonlocal missing
        st, pieces = steps[i], []
        for k, p in enumerate(st['parts']):
            src = os.path.join(ROOT, 'public', 'audio', key(p['lang'], p['text']) + '.mp3')
            if not os.path.exists(src):
                missing += 1; src = f'{work}/audio/{i}_{k}.aiff'
                v, r = MAC[p['lang']]; run('say', '-v', v, '-r', r, '-o', src, p['text'])
            wav = f'{work}/audio/{i}_{k}.wav'
            # cắt khoảng lặng đầu/cuối của file gốc rồi chỉnh tốc độ
            run('ffmpeg', '-y', '-i', src, '-af', f'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,atempo={TEMPO[p["lang"]]}',
                '-ar', '44100', '-ac', '1', '-c:a', 'pcm_s16le', wav)
            last = k == len(st['parts']) - 1
            gap = GAP[p['lang']] + (SLIDE_GAP if last and i + 1 < len(steps) and steps[i + 1]['s'] != st['s'] else 0)
            sil = f'{work}/audio/{i}_{k}_gap.wav'; silence(gap, sil)
            pieces += [wav, sil]
        if not pieces:
            sil = f'{work}/audio/{i}_empty.wav'; silence(1.0, sil); pieces = [sil]
        lst = f'{work}/audio/{i}.txt'
        open(lst, 'w').write(''.join(f"file '{x}'\n" for x in pieces))
        out = f'{work}/audio/step_{i:03d}.wav'
        run('ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out)
        return duration(out)

    def frame(i):                           # Chrome headless đôi khi treo lúc thoát khi máy tải nặng: ảnh đã ghi ra thì coi là xong
        png = f'{work}/frames/f_{i:03d}.png'
        for t in range(4):
            prof = f'{TMP}/prof-{i % N}' if t == 0 else f'{TMP}/prof-retry-{i}-{t}'
            if os.path.exists(png): os.remove(png)
            try:
                subprocess.run((CHROME, '--headless=new', '--disable-gpu', f'--user-data-dir={prof}', '--hide-scrollbars', '--window-size=1920,1080',
                                '--virtual-time-budget=5000', f'--screenshot={png}', f'{BASE}#/render/{lid}/{i}'),
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
            except subprocess.TimeoutExpired:
                pass
            if os.path.exists(png) and os.path.getsize(png) > 0: return
            time.sleep(3)
        raise RuntimeError(f'không chụp được khung {i} của {lid}')

    with ThreadPoolExecutor(N) as ex:
        durs = list(ex.map(step_audio, range(len(steps))))
    save_timing(lid, durs)
    if TIMING_ONLY:
        shutil.rmtree(work, ignore_errors=True)
        return None, sum(durs), len(steps), missing
    for b in range(0, len(steps), N):       # mỗi luồng một hồ sơ Chrome riêng (i % N) để không bị khóa hồ sơ
        with ThreadPoolExecutor(N) as ex:
            list(ex.map(frame, range(b, min(b + N, len(steps)))))
    with open(f'{work}/frames.txt', 'w') as f:
        for i, d in enumerate(durs):
            f.write(f"file '{work}/frames/f_{i:03d}.png'\nduration {d:.3f}\n")
        f.write(f"file '{work}/frames/f_{len(durs) - 1:03d}.png'\n")
    with open(f'{work}/audio.txt', 'w') as f:
        f.write(''.join(f"file '{work}/audio/step_{i:03d}.wav'\n" for i in range(len(durs))))
    run('ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', f'{work}/audio.txt', '-c', 'copy', f'{work}/full.wav')
    lv, no = lid.split('-')
    out = os.path.join(OUTDIR, f'bai-giang-cap{lv}-bai{int(no):02d}.mp4')
    run('ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', f'{work}/frames.txt', '-i', f'{work}/full.wav',
        '-vf', 'fps=15,scale=1280:720:flags=lanczos,format=yuv420p', '-c:v', 'libx264', '-preset', 'slow', '-tune', 'stillimage', '-crf', '24', '-c:a', 'aac', '-b:a', '96k',
        '-movflags', '+faststart', '-shortest', out)
    shutil.rmtree(work, ignore_errors=True)
    files = sorted(f for f in os.listdir(OUTDIR) if f.endswith('.mp4'))   # danh sách cho trang videos.html
    open(os.path.join(OUTDIR, 'index.json'), 'w').write(json.dumps(files))
    return out, duration(out), len(steps), missing

os.makedirs(OUTDIR, exist_ok=True)
if IDS == ['all'] or (len(IDS) == 1 and IDS[0].startswith('cap')):   # "all" hoặc cả một cấp, vd "cap3"
    LS = json.load(open(os.path.join(ROOT, 'src', 'data', 'lessons.json')))
    IDS = [l['id'] for l in LS if IDS[0] == 'all' or l['lv'] == int(IDS[0][3:])]
t0 = time.time()
for lid in IDS:
    lv, no = lid.split('-')
    if '--skip' in sys.argv and not TIMING_ONLY and os.path.exists(os.path.join(OUTDIR, f'bai-giang-cap{lv}-bai{int(no):02d}.mp4')):
        continue
    out, d, n, miss = build(lid)
    print(f'{lid}: {d / 60:.1f} phút, {n} bước{f", {miss} câu dùng giọng macOS" if miss else ""} → {os.path.basename(out) if out else "mốc thời gian"}  [{(time.time() - t0) / 60:.0f} phút]', flush=True)
print('XONG')
