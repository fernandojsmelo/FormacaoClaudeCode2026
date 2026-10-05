from functools import cache

chamadas = 0


@cache                         # guarda o resultado de cada n
def fib(n):
    global chamadas
    chamadas += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(40), "em", chamadas, "chamadas")
print(fib(40), "de novo: ainda", chamadas)
