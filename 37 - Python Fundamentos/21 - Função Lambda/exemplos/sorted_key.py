alunos = [("Ana", 9.5), ("Bruno", 7.0), ("Carla", 8.5)]
por_nota = sorted(alunos, key=lambda a: a[1], reverse=True)
print(por_nota)
palavras = ["Python", "é", "muito", "legal"]
print(sorted(palavras, key=lambda p: len(p)))
print(max(alunos, key=lambda a: a[1]))
