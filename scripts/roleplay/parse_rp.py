"""Transcrição de role play (PDF react-pdf da Udemy) -> markup editável.
Uso: python3 parse_rp.py arquivo.pdf saida.txt"""
import re, subprocess, sys, tempfile, os
import xml.etree.ElementTree as ET

pdf, out = sys.argv[1], sys.argv[2]
tmp = tempfile.mkdtemp()
subprocess.run(["pdftohtml", "-xml", "-i", "-q", pdf, os.path.join(tmp, "x")], check=True)
root = ET.parse(os.path.join(tmp, "x.xml")).getroot()

lines, fonts = [], {}
for page in root.iter("page"):
    pno = int(page.get("number"))
    for fs in page.iter("fontspec"):
        fonts[fs.get("id")] = int(fs.get("size"))
    for t in page.iter("text"):
        lines.append((pno, int(t.get("top")), int(t.get("left")), int(t.get("width")),
                      fonts.get(t.get("font"), 0), t.find("b") is not None, "".join(t.itertext())))

SKIP = re.compile(r"^(Formação Claude Code 2026: IA com Claude e Cowork|Esta transcrição inclui conteúdo gerado por IA.*|\d+/\d+)$")
title_lines, meta, clean = [], "", []
for l in lines:
    txt = l[6].strip()
    if SKIP.match(txt):
        continue
    if l[4] >= 24:
        if l[0] == 1:
            title_lines.append(txt)
        continue
    if l[0] == 1 and l[1] < 220 and (txt.startswith("Transcrição da prática") or txt.startswith("| ")):
        meta += txt + " "
        continue
    clean.append(l)

merged = []
for l in clean:
    if merged and merged[-1][0] == l[0] and abs(merged[-1][1] - l[1]) <= 2:
        p = merged[-1]
        merged[-1] = (p[0], p[1], p[2], max(p[3], l[2] + l[3] - p[2]), p[4], p[5] or l[5], p[6] + "\u0000" + l[6])
    else:
        merged.append(l)

turns, cur, prev = [], None, None
for l in merged:
    txt = l[6]
    m = re.match(r"^(.*?)\u0000\s*(\d\d:\d\d)\s*$", txt)
    if l[5] and m:
        cur = {"who": m.group(1).strip(), "time": m.group(2), "blocks": []}
        turns.append(cur); prev = None
        continue
    if cur is None:
        continue
    parts = txt.split("\u0000")
    heading = False
    if len(parts) == 2 and len(parts[0].strip()) <= 3 and not parts[0].strip().isalnum():
        heading, txt = True, parts[1].strip()
    else:
        txt = txt.replace("\u0000", "")
    raw = txt.strip()
    m2 = re.match(r"^([^\w\s(\"'“‘•\-–—*#]{1,3})\s+(\S.*)$", raw)
    if not heading and m2:
        heading, raw = True, m2.group(2)
    new_block = (prev is None or heading or raw.startswith("•") or prev["end_short"]
                 or l[1] - prev["top"] > 22 or l[0] != prev["page"])
    if heading:
        cur["blocks"].append({"t": "h", "text": raw})
        prev = {"top": l[1], "page": l[0], "end_short": True}
        continue
    if raw.startswith("•"):
        cur["blocks"].append({"t": "li", "text": raw.lstrip("• ").strip()})
    elif new_block:
        cur["blocks"].append({"t": "p", "text": raw})
    else:
        b = cur["blocks"][-1]
        b["text"] = (b["text"].rstrip() + " " + raw).strip()
    prev = {"top": l[1], "page": l[0], "end_short": l[3] < 700 or (l[3] < 770 and raw.rstrip().endswith((".", ":", "!", "?")))}

res = [f"@title {' '.join(title_lines).strip()}", f"@meta {meta.strip()}"]
for t in turns:
    res.append(f"@turn {t['who']}|{t['time']}")
    incode = False
    for b in t["blocks"]:
        x = re.sub(r"([a-zà-ú])- ([a-zà-ú])", r"\1\2", b["text"]).replace(" ” ", " → ").replace(" ’ ", " → ")
        if x.strip() == "“": res.append("arrowdown:"); continue
        if x.strip() == "text" and b["t"] == "p": res.append("code:"); incode = True; continue
        if x.strip() == "Fim da sessão": res.append("end:"); continue
        if incode:
            if x.endswith("Use o código com cuidado."):
                rest = x[: -len("Use o código com cuidado.")].strip()
                if rest: res.append("c| " + rest)
                res.append("endcode:"); incode = False; continue
            res.append("c| " + x); continue
        res.append({"p": "p| ", "li": "li| ", "h": "h| "}[b["t"]] + x)
open(out, "w").write("\n".join(res) + "\n")
print("turnos:", len(turns))
