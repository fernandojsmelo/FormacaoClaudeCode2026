def aplicar_duas_vezes(funcao, valor):
    return funcao(funcao(valor))


def compor(f, g):
    return lambda x: f(g(x))     # devolve uma função nova


print(aplicar_duas_vezes(lambda n: n * 3, 2))

limpar = compor(str.title, str.strip)
print(repr(limpar("   maria da silva  ")))
