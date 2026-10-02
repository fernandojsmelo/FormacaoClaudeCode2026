"""Impressão do Modo IA do Google (Chrome) -> markup editável.
Uso: python3 parse_google.py arquivo.pdf saida.txt
  q| pergunta  h| título  p| parágrafo  li| item  t| linha crua  c| linha de código (fonte mono)"""
import re, sys, subprocess, tempfile, os, html, collections
import xml.etree.ElementTree as ET

pdf, out = sys.argv[1], sys.argv[2]
tmp = tempfile.mkdtemp()
subprocess.run(["pdftohtml", "-xml", "-i", "-q", pdf, os.path.join(tmp, "x")], check=True)
root = ET.parse(os.path.join(tmp, "x.xml")).getroot()
fonts = {}
E = lambda s: html.escape(s, quote=False)
items = []
for page in root.iter("page"):
    pno = int(page.get("number"))
    for f in page.iter("fontspec"):
        fonts[f.get("id")] = (int(f.get("size")), f.get("color"), f.get("family"))
    for t in page.iter("text"):
        sz, col, fam = fonts[t.get("font")]
        items.append((pno, int(t.get("top")), int(t.get("left")), int(t.get("width")), sz, col,
                      t.find("b") is not None, "".join(t.itertext()), "Mono" in fam))
BODY = ("#94979c", "#6682ab")
BS = collections.Counter(i[4] for i in items if i[5] == "#94979c" and not i[8]).most_common(1)[0][0]
keep, cards = [], []
for it in items:
    pno, top, left, w, sz, col, b, txt, mono = it
    if col not in BODY and not mono:
        continue
    if top < 100 and txt.strip() == "Modo IA":
        continue
    if sz == 14 and txt.strip() == "YouTube ·":
        continue
    if sz == 16 and left in range(150, 160) and not b and not mono and BS == 22:
        cards.append((pno, txt.strip())); continue
    if txt.strip() == "Mostrar tudo":
        continue
    keep.append(it)
keep.sort(key=lambda x: (x[0], x[1], x[2]))
lines = []
for it in keep:
    if lines and lines[-1]["page"] == it[0] and abs(lines[-1]["top"] - it[1]) <= 7:
        lines[-1]["parts"].append(it)
    else:
        lines.append({"page": it[0], "top": it[1], "parts": [it]})

def render_parts(parts):
    parts = sorted(parts, key=lambda x: x[2]); s = ""
    for p in parts:
        txt = E(p[7])
        if p[8] and any(not q[8] for q in parts):  # trecho em fonte mono dentro de texto = código inline
            txt = f"<code>{txt.strip()}</code>"
            if s and not s.endswith((" ", "(")): s += " "
        elif p[6]:
            lead = len(txt) - len(txt.lstrip()); trail = len(txt) - len(txt.rstrip())
            txt = txt[:lead] + f"<strong>{txt.strip()}</strong>" + (txt[len(txt) - trail:] if trail else "")
        s += txt
    return s

blocks, prev = [], None
for ln in lines:
    parts = ln["parts"]
    left = min(p[2] for p in parts); sizes = {p[4] for p in parts}
    raw = "".join(p[7] for p in sorted(parts, key=lambda x: x[2])).strip()
    if all(p[8] for p in parts): kind = "c"
    elif left >= 255 and all(p[4] == BS for p in parts): kind = "q"
    elif max(sizes) > BS + 1: kind = "h"
    elif BS not in sizes: kind = "t"
    elif left >= 155: kind = "li"
    else: kind = "p"
    gap = None if prev is None or prev["page"] != ln["page"] else ln["top"] - prev["top"]
    cont = (prev is not None and blocks and blocks[-1][0] == kind and kind in ("p", "li", "q", "h")
            and (gap is None and kind != "h" or gap is not None and gap <= (37 if kind == "h" else 34)))
    if kind == "li" and cont and gap is not None and gap > 30: cont = False
    if kind == "c":
        p0 = min(parts, key=lambda x: x[2])
        cw = max(p0[3] / max(len(p0[7]), 1), 1)
        txt = "".join(p[7] for p in sorted(parts, key=lambda x: x[2])).rstrip()
        blocks.append(["c", txt.strip(), left, cw]); prev = ln; continue
    text = raw if kind == "t" else render_parts(parts)
    if cont: blocks[-1][1] = (blocks[-1][1].rstrip() + " " + text.strip()).strip()
    else: blocks.append([kind, text.strip()])
    prev = ln
# indentação do código: posição horizontal relativa à menor margem do bloco contíguo
i = 0
while i < len(blocks):
    if blocks[i][0] == "c":
        j = i
        while j < len(blocks) and blocks[j][0] == "c": j += 1
        base = min(b[2] for b in blocks[i:j]); cw = sorted(b[3] for b in blocks[i:j])[(j - i) // 2]
        for b in blocks[i:j]:
            b[1] = " " * round((b[2] - base) / cw) + b[1]; del b[2:]
        i = j
    else: i += 1
res = []
for k, t in blocks:
    if k == "c": res.append("c| " + t.rstrip()); continue
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"</strong>(\s*)<strong>", r"\1", t)
    t = t.replace(" ➔ ", " → ").replace("➔", "→")
    res.append(f"{k}| {t}")
res.append("")
pg = {}
for p, c in cards: pg.setdefault(p, []).append(c)
for p, cs in pg.items(): res.append(f"#cards pág {p}: " + " || ".join(cs))
open(out, "w").write("\n".join(res) + "\n")
print(len(blocks), "blocos;", sum(1 for b in blocks if b[0] == "q"), "perguntas;", len(cards), "linhas de cards; corpo", BS)
