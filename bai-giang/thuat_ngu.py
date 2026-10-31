#!/usr/bin/env python3
"""Chép file Excel thuật ngữ thành web/terms.json để build_site.py nhúng vào trang (mục "Thuật ngữ").

Cách dùng:  python3 thuat_ngu.py Thuat_ngu_du_lich.xlsx
Giữ nguyên các sheet dạng hàng[][] (đúng dạng trang gửi lên khi bấm "Nhập file Excel");
việc chuẩn hóa, so chéo Tổng hợp với sheet chuyên ngành làm ở trang (hàm TERM_BE trong template).
Chỉ dùng thư viện chuẩn, không cần openpyxl.
"""
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def col_index(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def text_of(el):
    return "".join(t.text or "" for t in el.iter("{%s}t" % NS["m"]))


def read_xlsx(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        shared = [text_of(si) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS)]
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    sheets = {}
    for sh in ET.fromstring(z.read("xl/workbook.xml")).find("m:sheets", NS):
        target = rels[sh.get(REL)].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        rows = []
        for row in ET.fromstring(z.read(target)).iter("{%s}row" % NS["m"]):
            r = int(row.get("r")) - 1
            while len(rows) < r:
                rows.append([])
            cells = []
            for c in row.findall("m:c", NS):
                j, t, v = col_index(c.get("r")), c.get("t"), c.find("m:v", NS)
                if t == "inlineStr":
                    val = text_of(c.find("m:is", NS))
                elif t == "s":
                    val = shared[int(v.text)]
                elif v is not None:
                    val = v.text[:-2] if v.text.endswith(".0") else v.text
                else:
                    val = None
                while len(cells) < j:
                    cells.append(None)
                cells.append(val)
            while cells and cells[-1] in (None, ""):
                cells.pop()
            rows.append(cells)
        sheets[sh.get("name")] = rows
    return sheets


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    data = {"fileName": os.path.basename(src), "sheets": read_xlsx(src)}
    out = os.path.join(HERE, "web", "terms.json")
    json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(f"Xong: {out}  ({', '.join(f'{k}: {len(v)} dòng' for k, v in data['sheets'].items())})")


if __name__ == "__main__":
    main()
