def registrar(funcao):
    def embrulho(*args, **kwargs):
        print(f"-> {funcao.__name__}{args}")
        resultado = funcao(*args, **kwargs)
        print(f"<- {resultado}")
        return resultado
    return embrulho


@registrar          # o mesmo que somar = registrar(somar)
def somar(a, b):
    return a + b


total = somar(2, 3)
print("total:", total)
