total = 0


def somar_impura(valor):        # depende e altera algo de fora
    global total
    total += valor
    return total


def somar_pura(acumulado, valor):   # só usa o que recebe
    return acumulado + valor


print(somar_impura(5), somar_impura(5))   # mesma entrada...
print(somar_pura(0, 5), somar_pura(0, 5))  # ...mesma saída
