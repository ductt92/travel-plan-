"""Kiểm tra kế hoạch và bài của Cấp 4, 5, 6, 7–9 so với chuẩn HSK 3.0 bản 2021 (src/data/hsk30/capN-*).
Chạy (từ thư mục app):
  python3 tools/check_level.py 4                 kiểm tra kế hoạch cap4-ke-hoach.txt và các bài trong src/data/lessons-4.json
  python3 tools/check_level.py 4 nhap/4-1.json   kiểm tra bài nháp (mỗi file một bài hoặc một mảng bài)
  python3 tools/check_level.py 4 --show 3        in từ (pinyin, từ loại theo chuẩn) và điểm ngữ pháp của bài 3 trong kế hoạch
Cấp 7–9 dùng số 7 (id bài 7-1, 7-2...); bài của cấp này chia phần lessons-7-p1.json (bài 1–25), lessons-7-p2.json (26–50)…"""
import csv, json, re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.join(ROOT, 'src', 'data', 'hsk30')
args = sys.argv[1:]
if not args or args[0] not in ('4', '5', '6', '7'): sys.exit(__doc__)
LV = int(args[0]); NAME = 'cap7-9' if LV == 7 else f'cap{LV}'
# Mục từ có ngoặc, dấu … hay số đánh dấu trong chuẩn -> chữ Hán dùng làm mục từ trong bài
NORM = {'…分之…': '百分之', '差（一）点儿': '差点儿', '称2': '称', '品（工艺品）': '工艺品', '好（不）容易': '好不容易',
        '界（文艺界）': '文艺界', '力（影响力）': '影响力', '长（秘书长）': '秘书长', '族（上班族）': '上班族',
        '度（知名度）': '知名度', '非（非金属）': '非金属', '感（责任感）': '责任感', '率（成功率）': '成功率',
        '茅台（酒）': '茅台酒', '业（服务业）': '服务业'}
# Đã dạy ở Cấp 1–3 với cùng âm và nghĩa nên không lặp lại (các chữ khác trùng mặt chữ nhưng là âm/nghĩa mới thì vẫn học)
SKIP = {'女士', '妻子', '售货员', '丈夫', '蛋糕', '没意思'}
norm = lambda hz: NORM.get(hz, hz)
VOC = {}  # chữ Hán trong bài -> [(pinyin chuẩn, từ loại)]
for x in csv.DictReader(open(os.path.join(H, f'{NAME}-tu-vung.csv'))):
    hz = norm(x['Simplified'])
    if hz not in SKIP: VOC.setdefault(hz, []).append((x['Pinyin'], x['POS']))
GRAM = {int(x['No']): x for x in csv.DictReader(open(os.path.join(H, f'{NAME}-ngu-phap.csv')))}
PLAN = {}
bad = 0
def err(f, m):
    global bad; bad += 1; print(f'{f}: {m}')
pf = os.path.join(H, f'{NAME}-ke-hoach.txt')
if os.path.exists(pf):
    for line in open(pf):
        if line.startswith('#') or not line.strip(): continue
        no, t, g, w = line.rstrip('\n').split('|'); PLAN[int(no)] = (t, [int(x) for x in g.split(',') if x], w.split())
    seen = {}
    for no, (t, g, ws) in PLAN.items():
        for w in ws:
            if w not in VOC: err(f'kế hoạch bài {no}', f'{w} không có trong chuẩn {NAME} (hoặc thuộc danh sách bỏ qua)')
            if w in seen: err(f'kế hoạch bài {no}', f'{w} đã có ở bài {seen[w]}')
            seen[w] = no
        for x in g:
            if x not in GRAM: err(f'kế hoạch bài {no}', f'ngữ pháp {x} không thuộc {NAME}')
    miss = [w for w in VOC if w not in seen]
    if miss: err('kế hoạch', f'còn {len(miss)} từ chưa xếp bài: {" ".join(miss[:80])}')
    gm = sorted(set(GRAM) - {x for p in PLAN.values() for x in p[1]})
    if gm: err('kế hoạch', f'còn ngữ pháp chưa xếp bài: {gm}')
    if sorted(PLAN) != list(range(1, len(PLAN) + 1)): err('kế hoạch', 'số bài không liên tục')
else:
    print(f'chưa có {pf} ({NAME}: {len(VOC)} từ, {len(GRAM)} điểm ngữ pháp)')

if args[1:2] == ['--show']:
    t, g, ws = PLAN[int(args[2])]
    print(f'Bài {args[2]}: {t}')
    for w in ws: print(' ', w, ' / '.join(f'{p} ({pos})' for p, pos in VOC[w]))
    for x in g:
        d = GRAM[x]; print(f'  [{x}] {d["Group"]} · {d["Category"]} · {d["Details"]} · {d["Content"]}'.replace('\n', ' '))
    sys.exit()

CJK = re.compile(r'[㐀-鿿]')
TONE = 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ'
flat = lambda s: re.sub(r"[\s'’·-]", '', s).lower()
# 一, 不 ghi biến điệu (yí, bú) như Cấp 1–3 hay theo chuẩn (yī, bù) đều được
sandhi = lambda s: re.sub(r'y[íì]', 'yī', re.sub(r'bú', 'bù', s))
if args[1:]:
    LESSONS = []
    for f in args[1:]:
        d = json.load(open(f)); LESSONS += [(f'{f}#{x["id"]}', x) for x in (d if isinstance(d, list) else [d])]
else:
    # một cấp là lessons-N.json hoặc chia phần lessons-N-p1.json, lessons-N-p2.json… (Cấp 7–9)
    D = os.path.join(ROOT, 'src', 'data')
    files = sorted(f for f in os.listdir(D) if re.fullmatch(f'lessons-{LV}(-p\\d+)?\\.json', f))
    LESSONS = [(l['id'], l) for f in files for l in json.load(open(os.path.join(D, f)))]
for f, l in LESSONS:
    no = l.get('no')
    if no not in PLAN: err(f, f'bài {no} không có trong kế hoạch'); continue
    t, gram, want = PLAN[no]
    if l['id'] != f'{LV}-{no}' or l['lv'] != LV: err(f, 'id/lv sai')
    for k in ('title', 'zh', 'goal', 'words', 'grammar', 'dialogs', 'lecture'):
        if k not in l: err(f, 'thiếu ' + k)
    have = [w[0] for w in l['words']]
    miss = [x for x in want if x not in have]
    extra = [x for x in have if x not in want]
    if miss: err(f, f'thiếu từ {miss}')
    if extra: err(f, f'thừa từ {extra}')
    if len(set(have)) != len(have): err(f, 'trùng từ')
    for w in l['words']:
        if len(w) != 7 or not all(isinstance(x, str) and x.strip() for x in w): err(f, f'từ sai dạng {w[:2]}'); continue
        hz, py, hv, vi, ex, exPy, exVi = w
        n = len(CJK.findall(hz))
        rhot = hz.endswith('儿') and n > 1 and py.split(' ')[-1][-1] == 'r' and py.split(' ')[-1] not in ('ér', 'er')
        if len(py.split(' ')) != n - rhot: err(f, f'{hz}: pinyin "{py}" không khớp số chữ')
        if len(hv.split(' ')) != n: err(f, f'{hz}: Hán Việt "{hv}" không khớp số chữ')
        if hz in VOC and hz not in NORM.values() and not any(sandhi(flat(py)) == sandhi(flat(p)) for p, _ in VOC[hz]):
            err(f, f'{hz}: pinyin "{py}" khác chuẩn {[p for p, _ in VOC[hz]]}')
        if hz not in ex.replace('|', ''): err(f, f'{hz}: ví dụ không chứa từ')
        if len(ex.split('|')) < 3: err(f, f'{hz}: ví dụ cần ≥3 đoạn |')
        if CJK.search(exPy) or CJK.search(exVi) or CJK.search(vi) or CJK.search(hv): err(f, f'{hz}: có chữ Hán trong pinyin/nghĩa')
        if not re.search(f'[{TONE}]', exPy): err(f, f'{hz}: pinyin ví dụ thiếu dấu')
    for g in l['grammar']:
        if not (isinstance(g.get('formula'), list) and 0 <= g.get('key', -1) < len(g['formula'])): err(f, f'formula/key sai: {g.get("title")}')
        if len(g.get('ex', [])) < 2 or any(len(e) != 3 for e in g['ex']): err(f, f'ví dụ ngữ pháp sai: {g.get("title")}')
        if not g.get('note'): err(f, 'thiếu note')
    if len(l['grammar']) < max(1, len(gram)): err(f, f'cần ít nhất {max(1, len(gram))} mục ngữ pháp')
    if len(l['dialogs']) != 2: err(f, 'cần 2 hội thoại')
    for d in l['dialogs']:
        if CJK.search(d['title']): err(f, 'tên hội thoại có chữ Hán')
        if not 5 <= len(d['lines']) <= 12: err(f, f'hội thoại {d["title"]}: {len(d["lines"])} câu')
        for x in d['lines']:
            if len(x) != 4 or CJK.search(x[2]) or CJK.search(x[3]) or not CJK.search(x[1]): err(f, f'câu thoại sai: {x}')
    lec = l['lecture']
    for k in ('intro', 'outro'):
        if CJK.search(lec[k]): err(f, f'lecture.{k} có chữ Hán (giọng Việt sẽ đọc sai)')
    if any(CJK.search(x) for x in l['goal']): err(f, 'goal có chữ Hán')
    if len(lec['tips']) < 2: err(f, 'cần ≥2 tips')
    for x in [lec['intro'], lec['outro'], *lec['tips'], *l['goal'], *(g['note'] for g in l['grammar'])]:
        if re.search(f'[{TONE}]\\w*[a-z]', x) and re.search(r'\b\w*[ǎǐǒǔǚěā]\w*\b', x): err(f, f'có pinyin trong lời giảng (bị lược khi đọc): {x[:60]}')
    print(f'{f}: {len(have)} từ, {len(l["grammar"])} ngữ pháp, {sum(len(d["lines"]) for d in l["dialogs"])} câu thoại')
if PLAN:
    done = sorted({l['no'] for _, l in LESSONS if l.get('no') in PLAN})
    print(f'{NAME}: {len(VOC)} từ, {len(GRAM)} điểm ngữ pháp, kế hoạch {len(PLAN)} bài · đã soạn {len(done)}/{len(PLAN)} bài · '
          f'{sum(len(PLAN[n][2]) for n in done)}/{sum(len(p[2]) for p in PLAN.values())} từ')
print('LỖI' if bad else 'OK', bad)
