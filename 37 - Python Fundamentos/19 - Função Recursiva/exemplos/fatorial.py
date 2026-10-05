def fatorial(n):
    if n <= 1:                     # caso base
        return 1
    return n * fatorial(n - 1)     # caso recursivo

print(fatorial(5))    # 5 * 4 * 3 * 2 * 1
print(fatorial(20))
