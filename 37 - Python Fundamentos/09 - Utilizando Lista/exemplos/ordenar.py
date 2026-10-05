notas = [7.5, 9.0, 6.0, 8.5]
print(sorted(notas))              # lista nova, ordenada
print(notas)                      # a original não mudou
notas.sort(reverse=True)          # ordena a própria lista
print(notas)
print(max(notas), min(notas), sum(notas) / len(notas))
nomes = ["bia", "Ana", "carlos", "Bruno"]
print(sorted(nomes))                   # maiúsculas vêm antes
print(sorted(nomes, key=str.lower))    # alfabética de verdade
