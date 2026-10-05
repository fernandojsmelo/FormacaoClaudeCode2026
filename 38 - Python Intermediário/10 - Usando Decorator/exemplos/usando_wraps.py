from functools import wraps

def sem_wraps(funcao):
    def embrulho(*args, **kwargs):
        return funcao(*args, **kwargs)
    return embrulho

def com_wraps(funcao):
    @wraps(funcao)             # copia nome, docstring...
    def embrulho(*args, **kwargs):
        return funcao(*args, **kwargs)
    return embrulho

@sem_wraps
def area(l):
    """Área de um quadrado."""
    return l * l

@com_wraps
def perimetro(l):
    """Perímetro de um quadrado."""
    return 4 * l

print(area.__name__, "|", area.__doc__)
print(perimetro.__name__, "|", perimetro.__doc__)
