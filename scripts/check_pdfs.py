"""Verifica se PDFs seguem o tema escuro do curso.

Duas checagens por PDF (primeira página, renderizada a 20 DPI):
  * claro:   brilho médio acima de 150 (o normal do tema escuro fica em ~20-55);
  * margens: algum canto da página quase branco (conteúdo escuro, bordas claras).

Uso (a partir da raiz do repositório):
    .venv/bin/python scripts/check_pdfs.py --all              # todos os PDFs do repositório
    .venv/bin/python scripts/check_pdfs.py arquivo.pdf [...]  # arquivos específicos
    .venv/bin/python scripts/check_pdfs.py --pre-push         # modo hook: lê as refs do stdin

Sai com código 1 se algum PDF estiver fora do padrão.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageStat

LIMITE_BRILHO = 150
LIMITE_CANTO = 200
IGNORAR = ("/.git", "/.venv", "/.idea", "/.claude", "/.agents")
ZERO = "0" * 40


def analisar(pdf_path):
    """Devolve (brilho médio, maior valor entre os cantos) da primeira página."""
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "p"
        subprocess.run(["pdftoppm", "-png", "-f", "1", "-l", "1", "-r", "20", str(pdf_path), str(base)],
                       check=True, capture_output=True, timeout=60)
        img = Image.open(next(Path(tmp).glob("p*.png"))).convert("L")
        w, h = img.size
        brilho = ImageStat.Stat(img).mean[0]
        cantos = [img.getpixel(p) for p in ((1, 1), (w - 2, 1), (1, h - 2), (w - 2, h - 2))]
        return brilho, max(cantos)


def problemas(pdf_path):
    try:
        brilho, canto = analisar(pdf_path)
    except Exception as erro:  # PDF ilegível também é problema
        return [f"não foi possível renderizar ({erro.__class__.__name__})"]
    achados = []
    if brilho > LIMITE_BRILHO:
        achados.append(f"claro (brilho {brilho:.0f}): reconstruir no tema escuro")
    elif canto > LIMITE_CANTO:
        achados.append("margens brancas: corrigir com scripts/fill_pdf_margins.py")
    return achados


def todos_os_pdfs():
    for dirpath, _, arquivos in os.walk("."):
        if any(seg in dirpath for seg in IGNORAR):
            continue
        for nome in arquivos:
            if nome.lower().endswith(".pdf"):
                yield Path(dirpath, nome)


def pdfs_do_push():
    """Para cada ref enviada, lista (sha, caminho) dos PDFs adicionados, alterados, renomeados ou copiados.

    Renomeados (R) e copiados (C) entram para que mover uma pasta não deixe os PDFs sem conferência;
    com --name-only, o git devolve o caminho novo.
    """
    vistos = {}
    for linha in sys.stdin:
        partes = linha.split()
        if len(partes) != 4:
            continue
        _, local_sha, _, remote_sha = partes
        if local_sha == ZERO:  # branch sendo apagado
            continue
        if remote_sha != ZERO:
            cmd = ["git", "diff", "--name-only", "-z", "--diff-filter=AMRC", remote_sha, local_sha]
        else:  # branch novo: só o que ainda não existe em nenhum remoto
            cmd = ["git", "log", "--name-only", "-z", "--diff-filter=AMRC", "--pretty=format:",
                   local_sha, "--not", "--remotes"]
        saida = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
        for caminho in saida.split("\0"):
            caminho = caminho.strip("\n")
            if caminho.lower().endswith(".pdf"):
                vistos[caminho] = local_sha
    return vistos


def main(args):
    ruins = []
    if args == ["--pre-push"]:
        alvos = pdfs_do_push()
        with tempfile.TemporaryDirectory() as tmp:
            for caminho, sha in sorted(alvos.items()):
                destino = Path(tmp, str(len(os.listdir(tmp))) + ".pdf")
                conteudo = subprocess.run(["git", "show", f"{sha}:{caminho}"], capture_output=True, check=True).stdout
                destino.write_bytes(conteudo)
                for achado in problemas(destino):
                    ruins.append((caminho, achado))
        total = len(alvos)
    else:
        caminhos = list(todos_os_pdfs()) if args == ["--all"] else [Path(a) for a in args]
        if not caminhos and args != ["--all"]:
            sys.exit(__doc__)
        for caminho in sorted(caminhos):
            for achado in problemas(caminho):
                ruins.append((str(caminho), achado))
        total = len(caminhos)

    for caminho, achado in ruins:
        print(f"  ✗ {caminho}: {achado}", file=sys.stderr)
    print(f"check_pdfs: {total} PDF(s) verificado(s), {len(ruins)} fora do padrão.", file=sys.stderr)
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
