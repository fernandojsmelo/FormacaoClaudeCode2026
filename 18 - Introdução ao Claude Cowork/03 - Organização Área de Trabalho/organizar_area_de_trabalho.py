"""
Organiza uma pasta (ex.: Área de Trabalho) separando os arquivos em subpastas por tipo.

Uso:
    python organizar_area_de_trabalho.py CAMINHO_DA_PASTA            # simulação (não move nada)
    python organizar_area_de_trabalho.py CAMINHO_DA_PASTA --executar # move de verdade
"""
import sys
import shutil
from pathlib import Path
from collections import defaultdict

CATEGORIAS = {
    "Imagens":      {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".heic", ".ico"},
    "Documentos":   {".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf", ".md"},
    "Planilhas":    {".xls", ".xlsx", ".ods", ".csv"},
    "Apresentacoes": {".ppt", ".pptx", ".odp", ".key"},
    "Videos":       {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"},
    "Musicas":      {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
    "Compactados":  {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Instaladores": {".exe", ".msi", ".dmg", ".pkg", ".deb", ".apk"},
    "Codigo":       {".py", ".js", ".html", ".css", ".json", ".java", ".c", ".cpp", ".sql"},
}
IGNORAR = {".lnk", ".url", ".ini", ".desktop"}  # atalhos e arquivos de sistema ficam onde estão


def categoria_de(arquivo: Path) -> str | None:
    ext = arquivo.suffix.lower()
    if ext in IGNORAR:
        return None
    for nome, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return nome
    return "Outros"


def destino_livre(destino: Path) -> Path:
    """Evita sobrescrever: arquivo.pdf -> arquivo (1).pdf"""
    if not destino.exists():
        return destino
    n = 1
    while True:
        candidato = destino.with_name(f"{destino.stem} ({n}){destino.suffix}")
        if not candidato.exists():
            return candidato
        n += 1


def organizar(pasta: Path, executar: bool) -> None:
    plano = defaultdict(list)
    ignorados = []
    for item in sorted(pasta.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue
        cat = categoria_de(item)
        if cat is None:
            ignorados.append(item.name)
        else:
            plano[cat].append(item)

    modo = "EXECUTANDO" if executar else "SIMULAÇÃO (nada será movido)"
    print(f"== {modo} em: {pasta} ==\n")
    total = 0
    for cat in sorted(plano):
        print(f"📁 {cat}/  ({len(plano[cat])})")
        for arq in plano[cat]:
            print(f"    ← {arq.name}")
            if executar:
                (pasta / cat).mkdir(exist_ok=True)
                shutil.move(str(arq), destino_livre(pasta / cat / arq.name))
            total += 1
    if ignorados:
        print(f"\nMantidos no lugar (atalhos/sistema): {', '.join(ignorados)}")
    print(f"\nTotal: {total} arquivos {'movidos' if executar else 'seriam movidos'} "
          f"para {len(plano)} pastas.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    organizar(Path(sys.argv[1]).expanduser(), executar="--executar" in sys.argv)
