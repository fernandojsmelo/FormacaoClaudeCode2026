def min_max(numeros):
    return min(numeros), max(numeros)   # devolve uma tupla

menor, maior = min_max([7, 2, 9, 4])
print(menor, maior)
resultado = min_max([7, 2, 9, 4])
print(resultado, type(resultado))
