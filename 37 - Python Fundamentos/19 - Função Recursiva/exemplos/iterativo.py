def fatorial_loop(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(fatorial_loop(5), fatorial_loop(20))
import sys
print("Limite de recursão:", sys.getrecursionlimit())
