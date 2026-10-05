from collections.abc import Callable, Iterable


def aplicar(
    funcao: Callable[[int], int],
    valores: Iterable[int],
) -> list[int]:
    return [funcao(v) for v in valores]


print(aplicar(lambda n: n * n, range(4)))
