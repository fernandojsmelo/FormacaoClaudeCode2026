from functools import wraps


def repetir(vezes):            # recebe o argumento...
    def decorador(funcao):     # ...e devolve o decorador
        @wraps(funcao)
        def embrulho(*args, **kwargs):
            for _ in range(vezes):
                resultado = funcao(*args, **kwargs)
            return resultado
        return embrulho
    return decorador


@repetir(3)
def avisar(msg):
    print("aviso:", msg)


avisar("backup concluído")
