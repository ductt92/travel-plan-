"""Kiểm tra bài Cấp 3 so với kế hoạch src/data/hsk30/cap3-ke-hoach.txt (từ, ngữ pháp theo chuẩn HSK 3.0 bản 2021).
Chạy: python3 apps/hoc-tieng-trung/tools/check_cap3.py [bài-nháp.json ...]
Không có tham số thì kiểm tra các bài lv 3 trong src/data/lessons.json và báo đã phủ bao nhiêu từ, điểm ngữ pháp."""
import json, re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = {}
for line in open(os.path.join(ROOT, 'src', 'data', 'hsk30', 'cap3-ke-hoach.txt')):
    if line.startswith('#') or not line.strip(): continue
    no, t, g, w = line.strip().split('|'); PLAN[int(no)] = (t, g.split(','), w.split())
CJK = re.compile(r'[㐀-鿿]')
def norm(hz):  # dạng mục từ trong plan -> chữ Hán dùng trong bài
    return {'…极了': '极了', '初（初一）': '初一', '化（现代化）': '现代化', '性（积极性）': '积极性', '员（服务员）': '服务员', '者（志愿者）': '志愿者'}.get(hz, hz)
bad = 0
def err(f, m):
    global bad; bad += 1; print(f'{f}: {m}')
if sys.argv[1:]:
    LESSONS = [(f, json.load(open(f))) for f in sys.argv[1:]]
else:
    LESSONS = [(l['id'], l) for l in json.load(open(os.path.join(ROOT, 'src', 'data', 'lessons.json'))) if l['lv'] == 3]
for f, l in LESSONS:
    no = l['no']; t, gram, want = PLAN[no]
    if l['id'] != f'3-{no}' or l['lv'] != 3: err(f, 'id/lv sai')
    for k in ('title', 'zh', 'goal', 'words', 'grammar', 'dialogs', 'lecture'):
        if k not in l: err(f, 'thiếu ' + k)
    have = [w[0] for w in l['words']]
    miss = [norm(x) for x in want if norm(x) not in have]
    extra = [x for x in have if x not in [norm(y) for y in want]]
    if miss: err(f, f'thiếu từ {miss}')
    if extra: err(f, f'thừa từ {extra}')
    if len(set(have)) != len(have): err(f, 'trùng từ')
    for w in l['words']:
        if len(w) != 7 or not all(isinstance(x, str) and x.strip() for x in w): err(f, f'từ sai dạng {w[:2]}'); continue
        hz, py, hv, vi, ex, exPy, exVi = w
        n = len(CJK.findall(hz))
        # 儿 hóa viết gộp như Cấp 1–2: 面条儿 miàn tiáor
        rhot = hz.endswith('儿') and n > 1 and py.split(' ')[-1][-1] == 'r' and py.split(' ')[-1] not in ('ér', 'er')
        if len(py.split(' ')) != n - rhot: err(f, f'{hz}: pinyin "{py}" không khớp số chữ')
        if len(hv.split(' ')) != n: err(f, f'{hz}: Hán Việt "{hv}" không khớp số chữ')
        if hz not in ex.replace('|', ''): err(f, f'{hz}: ví dụ không chứa từ')
        if len(ex.split('|')) < 3: err(f, f'{hz}: ví dụ cần ≥3 đoạn |')
        if CJK.search(exPy) or CJK.search(exVi) or CJK.search(vi): err(f, f'{hz}: có chữ Hán trong pinyin/nghĩa')
        if not re.search(r'[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]', exPy): err(f, f'{hz}: pinyin ví dụ thiếu dấu')
    for g in l['grammar']:
        if not (isinstance(g['formula'], list) and 0 <= g['key'] < len(g['formula'])): err(f, f'formula/key sai: {g["title"]}')
        if len(g['ex']) < 2 or any(len(e) != 3 for e in g['ex']): err(f, f'ví dụ ngữ pháp sai: {g["title"]}')
        if not g.get('note'): err(f, 'thiếu note')
    if len(l['dialogs']) != 2: err(f, 'cần 2 hội thoại')
    for d in l['dialogs']:
        if CJK.search(d['title']): err(f, 'tên hội thoại có chữ Hán')
        if not 5 <= len(d['lines']) <= 10: err(f, f'hội thoại {d["title"]}: {len(d["lines"])} câu')
        for x in d['lines']:
            if len(x) != 4 or CJK.search(x[2]) or CJK.search(x[3]) or not CJK.search(x[1]): err(f, f'câu thoại sai: {x}')
    lec = l['lecture']
    for k in ('intro', 'outro'):
        if CJK.search(lec[k]): err(f, f'lecture.{k} có chữ Hán (giọng Việt sẽ đọc sai)')
    if any(CJK.search(x) for x in l['goal']): err(f, 'goal có chữ Hán')
    if len(lec['tips']) < 2: err(f, 'cần ≥2 tips')
    for x in [lec['intro'], lec['outro'], *lec['tips'], *l['goal'], *(g['note'] for g in l['grammar'])]:
        if re.search(r'[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]\w*[a-z]', x) and re.search(r'\b\w*[ǎǐǒǔǚěā]\w*\b', x): err(f, f'có pinyin trong lời giảng (bị lược khi đọc): {x[:60]}')
    print(f'{f}: {len(have)} từ, {len(l["grammar"])} ngữ pháp, {sum(len(d["lines"]) for d in l["dialogs"])} câu thoại')
done = [n for _, l in LESSONS for n in [l['no']]]
print(f'Đã soạn {len(done)}/{len(PLAN)} bài · {sum(len(PLAN[n][2]) for n in done)}/{sum(len(p[2]) for p in PLAN.values())} từ · '
      f'{sum(len(PLAN[n][1]) for n in done)}/{sum(len(p[1]) for p in PLAN.values())} điểm ngữ pháp')
print('LỖI' if bad else 'OK', bad)
