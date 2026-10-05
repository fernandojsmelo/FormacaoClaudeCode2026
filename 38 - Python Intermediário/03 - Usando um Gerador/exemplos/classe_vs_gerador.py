# Aula 01: uma classe com __iter__ e __next__
# Com gerador, o Python cria esses métodos para você:
def contagem(n):
    while n >= 1:
        yield n
        n -= 1


g = contagem(3)
print(iter(g) is g)        # é seu próprio iterador
print(hasattr(g, "__next__"))
print(list(g), list(g))        # e também se esgota
