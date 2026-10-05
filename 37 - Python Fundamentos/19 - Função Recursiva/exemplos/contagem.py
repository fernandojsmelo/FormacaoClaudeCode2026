def contagem_regressiva(n):
    if n == 0:                 # caso base: para aqui
        print("Fogo!")
        return
    print(n)
    contagem_regressiva(n - 1) # chama a si mesma, menor

contagem_regressiva(3)
