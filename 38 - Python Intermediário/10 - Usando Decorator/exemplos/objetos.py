def saudar(nome):
    return f"Olá, {nome}!"


falar = saudar                 # a função é um objeto
print(falar("Ana"))


def aplicar(funcao, valor):    # recebida como argumento
    return funcao(valor)


print(aplicar(len, "decorador"))


def criar_multiplicador(fator):
    def multiplicar(n):        # função criada dentro de outra
        return n * fator       # e lembra de 'fator' (closure)
    return multiplicar


triplo = criar_multiplicador(3)
print(triplo(7))
