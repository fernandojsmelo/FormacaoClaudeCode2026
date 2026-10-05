from functools import reduce
import re


def compor(*funcoes):
    """Aplica as funções da esquerda para a direita."""
    return lambda x: reduce(lambda acc, f: f(acc), funcoes, x)


def juntar_espacos(texto):
    return re.sub(r"\s+", " ", texto)


normalizar = compor(str.strip, juntar_espacos, str.lower)

print(repr(normalizar("  Olá    MUNDO   Python  ")))
