"""Cria a pasta area_teste/ usada nos exemplos desta aula."""
import shutil
from pathlib import Path


def preparar():
    raiz = Path("area_teste")
    if raiz.exists():
        shutil.rmtree(raiz)              # recomeça do zero
    (raiz / "fotos").mkdir(parents=True)
    (raiz / "docs" / "2026").mkdir(parents=True)
    for nome in ["praia.jpg", "festa.jpg", "logo.png"]:
        (raiz / "fotos" / nome).write_bytes(b"\x00" * 10)
    (raiz / "docs" / "notas.txt").write_text("8\n9\n", "utf-8")
    plano = raiz / "docs" / "2026" / "plano.md"
    plano.write_text("# Plano", "utf-8")
    return raiz
