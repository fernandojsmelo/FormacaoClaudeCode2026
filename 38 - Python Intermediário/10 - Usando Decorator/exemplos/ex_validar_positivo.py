from functools import wraps


def exige_positivos(funcao):
    @wraps(funcao)
    def embrulho(*numeros):
        if any(n <= 0 for n in numeros):
            raise ValueError(f"{funcao.__name__}: só positivos")
        return funcao(*numeros)
    return embrulho


@exige_positivos
def area_retangulo(base, altura):
    return base * altura


print(area_retangulo(3, 4))
try:
    area_retangulo(3, -4)
except ValueError as erro:
    print("Erro:", erro)
