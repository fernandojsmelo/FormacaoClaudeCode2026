precos = [100.0, 59.9, 12.5]

com_reajuste = map(lambda p: round(p * 1.10, 2), precos)
print(list(com_reajuste))


def formatar(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


print(list(map(formatar, precos)))
