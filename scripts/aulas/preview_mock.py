"""Pré-visualiza mockups de tela: gera <nome>.png (72 DPI) ao lado de cada .html.

Uso: python3 scripts/aulas/preview_mock.py tela1.html [tela2.html ...]
O marcador <!--MOCK_BASE--> é trocado pelo mock_base.css, como no build_aula.py.
"""
import os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
from build_aula import CHROME  # noqa: E402  (reaproveita as flags do Chrome)

css = open(os.path.join(HERE, "mock_base.css")).read()
for path in sys.argv[1:]:
    path = os.path.abspath(path)
    src = open(path).read().replace("<!--MOCK_BASE-->", "<style>\n" + css + "</style>")
    page = os.path.join(os.path.dirname(path), ".render_" + os.path.basename(path))
    open(page, "w").write(src)
    with tempfile.TemporaryDirectory() as tmp:
        pdf = os.path.join(tmp, "m.pdf")
        try:
            subprocess.run(CHROME + [f"--print-to-pdf={pdf}", "file://" + page], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        finally:
            os.remove(page)
        out = os.path.splitext(path)[0]
        subprocess.run(["pdftoppm", "-png", "-r", "72", "-singlefile", "-f", "1", "-l", "1", pdf, out], check=True)
        pages = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
        n = [l.split()[-1] for l in pages.splitlines() if l.startswith("Pages")][0]
        print(out + ".png", "" if n == "1" else f"(ATENÇÃO: {n} páginas; a tela transbordou)")
