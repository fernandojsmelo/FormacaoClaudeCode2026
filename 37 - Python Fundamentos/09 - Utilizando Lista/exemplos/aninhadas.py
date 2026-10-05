alunos = [["Ana", 9.0], ["Bruno", 7.5], ["Carla", 8.0]]
print(alunos[1])        # ['Bruno', 7.5]
print(alunos[1][0])     # Bruno
for nome, nota in alunos:
    print(f"{nome}: {nota}")
