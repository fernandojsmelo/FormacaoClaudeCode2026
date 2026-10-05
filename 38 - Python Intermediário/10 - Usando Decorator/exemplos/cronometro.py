import time
from functools import wraps


def cronometrar(funcao):
    @wraps(funcao)
    def embrulho(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcao(*args, **kwargs)
        gasto = time.perf_counter() - inicio
        print(f"{funcao.__name__} levou {gasto:.1f} s")
        return resultado
    return embrulho


@cronometrar
def relatorio():
    time.sleep(0.3)            # simula um trabalho demorado
    return "pronto"


print(relatorio())
