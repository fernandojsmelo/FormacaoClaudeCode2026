from pathlib import Path
from preparar import preparar

raiz = preparar()
baguncada = raiz / "downloads"
baguncada.mkdir()
for nome in ["foto.jpg", "nota.pdf", "selfie.JPG", "doc.txt"]:
    (baguncada / nome).write_text("", encoding="utf-8")

for arquivo in list(baguncada.iterdir()):   # lista antes
    tipo = arquivo.suffix.lower().lstrip(".") or "sem_tipo"
    pasta = baguncada / tipo
    pasta.mkdir(exist_ok=True)
    arquivo.rename(pasta / arquivo.name)

for pasta in sorted(baguncada.iterdir()):
    print(pasta.name, sorted(p.name for p in pasta.iterdir()))
