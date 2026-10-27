"""Tạo kho giọng đọc cho mọi câu app cần đọc.
  - Tiếng Việt: giọng Linh có sẵn trên macOS (nữ miền Bắc), tạo bằng lệnh `say` rồi chuyển sang mp3 bằng ffmpeg.
  - Tiếng Trung: giọng neural Xiaoxiao của Microsoft (gói edge-tts), không cần khóa.
Chạy trên macOS: <python có edge-tts> apps/hoc-tieng-trung/tools/gen_audio.py [--lang vi|zh] [--force]
  --lang   chỉ tạo một ngôn ngữ (mặc định cả hai)
  --force  xóa file cũ của ngôn ngữ đó rồi tạo lại (dùng khi đổi giọng)
Cần site đã build đang chạy (npm run build && npm run preview, cổng 4173) để lấy danh sách câu từ route #/alltexts.
Mỗi câu lưu thành public/audio/<khóa>.mp3, khóa = băm FNV-1a + djb2 của "ngôn ngữ|câu" (giống audioKey trong src/core/speech.js)."""
import asyncio, html, json, os, re, subprocess, sys
import edge_tts

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
AUD = os.path.join(ROOT, 'public', 'audio')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
BASE = os.environ.get('BASE', 'http://localhost:4173/hoc-tieng-trung/')
PROF = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'hanlo-chrome-texts')
ZH_VOICE = 'zh-CN-XiaoxiaoNeural'
VI_VOICE, VI_RATE = 'Linh', '185'
CONCURRENCY = {'zh': 6, 'vi': 6}

def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
LANGS = [arg('--lang')] if arg('--lang') else ['vi', 'zh']

def key(lang, text):
    h1, h2 = 0x811c9dc5, 5381
    for x in (lang + '|' + text).encode('utf-8'):
        h1 = ((h1 ^ x) * 0x01000193) & 0xffffffff
        h2 = (h2 * 33 + x) & 0xffffffff
    return f'{h1:08x}{h2:08x}'

dom = subprocess.run([CHROME, '--headless=new', '--disable-gpu', f'--user-data-dir={PROF}', '--virtual-time-budget=5000',
                      '--dump-dom', BASE + '#/alltexts'], capture_output=True, text=True).stdout
items = json.loads(html.unescape(re.search(r'<pre id="steps">(.*?)</pre>', dom, re.S).group(1)))
for it in items:
    assert key(it['lang'], it['text']) == it['key'], it  # khóa Python phải khớp khóa trong app
items = [it for it in items if it['lang'] in LANGS]
os.makedirs(AUD, exist_ok=True)
if '--force' in sys.argv:
    for it in items:
        p = os.path.join(AUD, it['key'] + '.mp3')
        if os.path.exists(p): os.remove(p)
todo = [it for it in items if not os.path.exists(os.path.join(AUD, it['key'] + '.mp3'))]
print(f'{len(items)} câu ({", ".join(LANGS)}), cần tạo {len(todo)}', flush=True)

async def zh_clip(session, text, path):
    await edge_tts.Communicate(text, ZH_VOICE).save(path)

async def vi_clip(session, text, path):
    # giọng Linh của macOS: say ra aiff rồi ffmpeg chuyển sang mp3
    aiff = path + '.aiff'
    p = await asyncio.create_subprocess_exec('say', '-v', VI_VOICE, '-r', VI_RATE, '-o', aiff, '--', text)
    await p.wait()
    p = await asyncio.create_subprocess_exec('ffmpeg', '-y', '-v', 'error', '-i', aiff, '-ac', '1', '-b:a', '64k', '-f', 'mp3', path)
    await p.wait()
    os.remove(aiff)

async def make(session, it, sem, stat):
    path = os.path.join(AUD, it['key'] + '.mp3')
    async with sem[it['lang']]:
        for attempt in range(6):
            try:
                await (vi_clip if it['lang'] == 'vi' else zh_clip)(session, it['text'], path + '.part')
                if os.path.getsize(path + '.part') == 0: raise RuntimeError('file rỗng')
                os.replace(path + '.part', path)
                stat['done'] += 1
                if stat['done'] % 200 == 0: print(f"  {stat['done']}/{len(todo)}", flush=True)
                return
            except Exception as e:
                await asyncio.sleep(3 * (attempt + 1))
        print('LỖI', it['lang'], it['text'][:40], flush=True)

async def main():
    sem, stat = {k: asyncio.Semaphore(v) for k, v in CONCURRENCY.items()}, {'done': 0}
    await asyncio.gather(*(make(None, it, sem, stat) for it in todo))

asyncio.run(main())
keys = sorted(f[:-4] for f in os.listdir(AUD) if f.endswith('.mp3'))
open(os.path.join(AUD, 'index.json'), 'w').write(json.dumps(keys))
print(f'xong: {len(keys)} file âm thanh', flush=True)
