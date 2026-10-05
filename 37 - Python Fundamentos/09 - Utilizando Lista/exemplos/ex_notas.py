# Exercício: estatísticas de uma turma
notas = [8.5, 6.0, 9.5, 7.0, 5.5, 10.0]
media = sum(notas) / len(notas)
print("Notas ordenadas:", sorted(notas))
print(f"Média: {media:.2f}")
print("Maior e menor:", max(notas), min(notas))
print("Amplitude:", max(notas) - min(notas))
notas.append(8.0)
print("Com a nota do aluno novo:", len(notas), "notas")
