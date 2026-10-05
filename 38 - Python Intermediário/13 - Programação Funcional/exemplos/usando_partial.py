from functools import partial

binario = partial(int, base=2)         # fixa o argumento base
print(binario("1011"), binario("11111111"))


def preco_final(valor, imposto):
    return round(valor * (1 + imposto), 2)


com_icms = partial(preco_final, imposto=0.18)
print(com_icms(100), com_icms(59.9))
