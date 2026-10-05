type Ponto = tuple[float, float]     # apelido (Python 3.12+)


def distancia(a: Ponto, b: Ponto) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def primeiro[T](itens: list[T]) -> T:    # T: tipo genérico
    return itens[0]


print(distancia((0, 0), (3, 4)))
print(primeiro(["x", "y"]), primeiro([10, 20]))
