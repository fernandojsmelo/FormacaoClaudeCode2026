# Exercício: distância entre dois pontos (tuplas)
a = (1, 2)
b = (4, 6)
x1, y1 = a
x2, y2 = b
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Distância entre {a} e {b}: {distancia}")
