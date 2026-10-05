from itertools import zip_longest

nomes = ["Ana", "Bia", "Caio"]
notas = [9.5, 7.0]                       # faltou uma nota

print(list(zip(nomes, notas)))           # para no menor
print(list(zip_longest(nomes, notas, fillvalue="-")))
try:
    list(zip(nomes, notas, strict=True))  # exige mesmo tamanho
except ValueError as erro:
    print("Erro:", erro)
