ponto = (3, 4)
x, y = ponto                  # desempacotamento
print(x, y)
nome, idade, cidade = ("Ana", 29, "Recife")
print(f"{nome} ({idade}) mora em {cidade}")
primeiro, *resto = (1, 2, 3, 4)
print(primeiro, resto)        # resto vira lista
a, b = 1, 2
a, b = b, a                   # troca usando tupla
print(a, b)
