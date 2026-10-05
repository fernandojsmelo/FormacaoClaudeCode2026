nomes = ["Ana", "Bia", "Caio"]
notas = [9.5, 7.0, 8.2]
turmas = ["A", "B", "A"]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")

print(list(zip(nomes, notas, turmas)))   # três de uma vez
