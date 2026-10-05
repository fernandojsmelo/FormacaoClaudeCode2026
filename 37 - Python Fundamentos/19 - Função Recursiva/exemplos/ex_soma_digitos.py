# Exercício: soma dos dígitos com recursão
def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)

print(soma_digitos(2026))   # 2 + 0 + 2 + 6
print(soma_digitos(7))
