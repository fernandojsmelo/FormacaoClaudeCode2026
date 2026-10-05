from pathlib import Path
from preparar import preparar

raiz = preparar()
destino = raiz / "backup" / "outubro"
destino.mkdir(parents=True, exist_ok=True)  # cria tudo
destino.mkdir(parents=True, exist_ok=True)  # não reclama
print(destino.is_dir())

antigo = raiz / "docs" / "notas.txt"
novo = antigo.rename(raiz / "docs" / "notas_2026.txt")
print(novo.name, antigo.exists())

(raiz / "fotos" / "logo.png").unlink()          # apaga
print(sorted(p.name for p in (raiz / "fotos").iterdir()))
