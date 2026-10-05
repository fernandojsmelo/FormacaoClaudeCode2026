def contagem(n):
    while n > 0:
        yield n          # entrega um valor e pausa aqui
        n -= 1


g = contagem(3)
print(type(g).__name__)
print(list(g))
for x in contagem(2):
    print("for:", x)
