def multiplos(numero, limite):
    """Gera os múltiplos de numero até limite."""
    atual = numero
    while atual <= limite:
        yield atual
        atual += numero


print(list(multiplos(7, 50)))
print(sum(multiplos(3, 30)))
print(next(multiplos(9, 100)))
