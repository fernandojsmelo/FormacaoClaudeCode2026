# Com for + append
quadrados = []
for n in range(1, 6):
    quadrados.append(n ** 2)
print(quadrados)

# Com list comprehension: a mesma coisa em uma linha
quadrados = [n ** 2 for n in range(1, 6)]
print(quadrados)
