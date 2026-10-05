def fatorial(n, nivel=0):
    recuo = "  " * nivel
    print(f"{recuo}fatorial({n})")
    if n <= 1:
        resultado = 1
    else:
        resultado = n * fatorial(n - 1, nivel + 1)
    print(f"{recuo}-> {resultado}")
    return resultado

fatorial(4)
