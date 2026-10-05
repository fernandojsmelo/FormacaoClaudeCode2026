import shutil
from preparar import preparar

raiz = preparar()
copia = shutil.copy(raiz / "docs" / "notas.txt", raiz / "fotos")
print(copia)


shutil.copytree(raiz / "fotos", raiz / "fotos_bkp")  # pasta
shutil.move(raiz / "docs" / "2026", raiz / "morto")   # move
shutil.rmtree(raiz / "fotos_bkp")              # apaga tudo
print(sorted(p.name for p in raiz.iterdir()))
