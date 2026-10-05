def somar(*numeros):          # junta os posicionais numa tupla
    print(type(numeros), numeros)
    return sum(numeros)

print(somar(1, 2))
print(somar(1, 2, 3, 4, 5))
print(somar())
