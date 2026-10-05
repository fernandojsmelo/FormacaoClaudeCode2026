alunos = ["Ana", "Bia", "Caio", "Davi"]
p1 = [8.0, 6.5, 9.0, 7.0]
p2 = [9.0, 7.5, 8.5, 5.0]

medias = [(a + b) / 2 for a, b in zip(p1, p2, strict=True)]
ranking = sorted(zip(alunos, medias), key=lambda t: t[1],
                 reverse=True)

for posicao, (nome, media) in enumerate(ranking, start=1):
    print(f"{posicao}º {nome:<5} {media:.2f}")
