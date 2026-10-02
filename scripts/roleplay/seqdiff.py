"""Diff de sequência de palavras, ignorando cabeçalho/rodapé repetidos. Uso: seqdiff.py orig.pdf novo.pdf"""
import sys, subprocess, re, difflib
SKIP = re.compile(r"^(Formação Claude Code 2026: IA com Claude e Cowork|Esta transcrição inclui conteúdo gerado por IA.*|\d+/\d+|\d\d/\d\d/\d{4}, \d\d:\d\d.*|https://www\.google\.com/.*|Modo IA|Tudo|Imagens|Shopping|Vídeos|Mais|Pergunte o que quiser)$")
def words(p):
    t = subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True).stdout.splitlines()
    t = [l for l in t if not SKIP.match(l.strip())]
    t = re.sub(r"(\w)-\n(\w)", r"\1\2", "\n".join(t))
    return re.findall(r"\w+", t.lower())
a, b = words(sys.argv[1]), words(sys.argv[2])
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op in ("delete", "replace") and (i2 - i1) > 0:
        print(op, "ORIG:", " ".join(a[i1:i2])[:110], "| NOVO:", " ".join(b[j1:j2])[:60])
