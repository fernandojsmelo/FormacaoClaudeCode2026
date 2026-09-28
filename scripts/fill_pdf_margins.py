"""Pinta as margens brancas de PDFs do curso com a cor de fundo do tema escuro.

PDFs gerados pelo Chrome com `@page{ margin:… }` sem `background` saem com a área
de conteúdo escura e as margens brancas. Este script insere, por baixo do conteúdo
de cada página, um retângulo do tamanho da página na cor --bg (#171310). Nada do
conteúdo original é alterado: texto, vetores, imagens e links continuam iguais.

Uso (a partir da raiz do repositório):
    .venv/bin/python scripts/fill_pdf_margins.py arquivo.pdf [...]            # corrige no lugar
    .venv/bin/python scripts/fill_pdf_margins.py --check arquivo.pdf [...]    # só lista os que precisam

Dependências: pypdf (no .venv) e pdftoppm (poppler-utils) para a checagem.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DecodedStreamObject, NameObject

BG_RGB = (0x17 / 255, 0x13 / 255, 0x10 / 255)  # --bg: #171310
MARKER = b"%fill-margins-bg"


def has_white_corners(pdf_path):
    """True se algum canto da primeira página renderizada for quase branco."""
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "p"
        subprocess.run(["pdftoppm", "-png", "-f", "1", "-l", "1", "-r", "20", str(pdf_path), str(base)],
                       check=True, capture_output=True)
        img = Image.open(next(Path(tmp).glob("p*.png"))).convert("L")
        w, h = img.size
        corners = [img.getpixel(p) for p in ((1, 1), (w - 2, 1), (1, h - 2), (w - 2, h - 2))]
        return max(corners) > 200


def fill_margins(pdf_path):
    writer = PdfWriter(clone_from=PdfReader(str(pdf_path)))
    for page in writer.pages:
        box = page.mediabox
        x0, y0 = float(box.left), float(box.bottom)
        w, h = float(box.width), float(box.height)
        existing = page.get(NameObject("/Contents"))
        if existing is not None and MARKER in page.get_contents().get_data()[:64]:
            continue  # já corrigida
        r, g, b = BG_RGB
        bg = DecodedStreamObject()
        bg.set_data(MARKER + f"\nq {r:.4f} {g:.4f} {b:.4f} rg {x0} {y0} {w} {h} re f Q\n".encode())
        bg_ref = writer._add_object(bg)
        if existing is None:
            page[NameObject("/Contents")] = bg_ref
        else:
            existing = existing.get_object()
            items = list(existing) if isinstance(existing, ArrayObject) else [page[NameObject("/Contents")]]
            page[NameObject("/Contents")] = ArrayObject([bg_ref] + items)
    tmp_out = Path(pdf_path).with_suffix(".tmp.pdf")
    with open(tmp_out, "wb") as f:
        writer.write(f)
    tmp_out.replace(pdf_path)


def main(args):
    check_only = "--check" in args
    paths = [Path(a) for a in args if a != "--check"]
    if not paths:
        sys.exit(__doc__)
    for p in paths:
        if not has_white_corners(p):
            continue
        if check_only:
            print(p)
        else:
            fill_margins(p)
            print(("ok     " if not has_white_corners(p) else "FALHOU ") + str(p))


if __name__ == "__main__":
    main(sys.argv[1:])
