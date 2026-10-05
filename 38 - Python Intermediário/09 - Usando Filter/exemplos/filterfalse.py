from itertools import filterfalse

notas = [8.5, 4.0, 7.0, 5.5, 9.0]


def aprovado(nota):
    return nota >= 6


print("aprovados: ", list(filter(aprovado, notas)))
print("reprovados:", list(filterfalse(aprovado, notas)))
