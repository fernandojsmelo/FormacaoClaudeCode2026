"""cmp_xml.py original.pdf novo.pdf: diff de palavras usando o XML do pdftohtml (não sofre com texto sobreposto)."""
import difflib, html, os, re, subprocess, sys, tempfile
def palavras(pdf):
    t = tempfile.mkdtemp(); subprocess.run(["pdftohtml", "-xml", "-i", "-q", pdf, t + "/x"], check=True)
    x = open(t + "/x.xml", encoding="utf-8").read()
    txt = " ".join(html.unescape(re.sub(r"<[^>]+>", "", m)) for m in re.findall(r"<text [^>]*>(.*?)</text>", x))
    return re.findall(r"\w+", txt.lower())
a, b = palavras(sys.argv[1]), palavras(sys.argv[2])
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        print(op, "ORIG:", " ".join(a[i1:i2])[:110], "| NOVO:", " ".join(b[j1:j2])[:110])
print(f"{len(a)} palavras no original, {len(b)} no novo, semelhança {sm.ratio():.4f}")
