def ler_notas(notas):
    validas = 0
    for nota in notas:
        if 0 <= nota <= 10:
            validas += 1
            yield nota
    return validas           # vira o resultado do yield from


def relatorio(notas):
    qtd = yield from ler_notas(notas)
    print("notas válidas:", qtd)


print(list(relatorio([8, 11, 6, -1, 9])))
