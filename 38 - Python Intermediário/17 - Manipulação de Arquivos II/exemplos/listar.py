from preparar import preparar

raiz = preparar()

print(sorted(p.name for p in raiz.iterdir()))       # 1 nível
print(sorted(p.name for p in raiz.glob("fotos/*.jpg")))
for p in sorted(raiz.rglob("*.*")):        # todos os níveis
    print(p.relative_to(raiz))
