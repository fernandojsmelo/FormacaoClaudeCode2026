nomes = ["Ana", "Bia", "Caio"]
notas = [9.0, 7.5, 8.0]
for i, nome in enumerate(nomes, start=1):
    print(f"{i}º {nome}")
for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")
