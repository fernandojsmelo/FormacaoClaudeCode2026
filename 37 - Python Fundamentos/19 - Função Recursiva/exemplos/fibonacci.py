from functools import lru_cache

chamadas = 0

def fib(n):
    global chamadas
    chamadas += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(25), "com", chamadas, "chamadas")

@lru_cache(maxsize=None)   # guarda o que já calculou
def fib_rapido(n):
    return n if n < 2 else fib_rapido(n - 1) + fib_rapido(n - 2)

resultado = fib_rapido(25)
calculos = fib_rapido.cache_info().misses
print(resultado, "com", calculos, "cálculos")
