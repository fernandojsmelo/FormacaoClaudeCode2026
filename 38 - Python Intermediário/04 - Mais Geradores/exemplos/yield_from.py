def letras():
    yield from "ab"          # delega para outro iterável
    yield from ["c", "d"]


def tudo():
    yield 1
    yield from letras()      # delega para outro gerador
    yield 2


print(list(tudo()))
