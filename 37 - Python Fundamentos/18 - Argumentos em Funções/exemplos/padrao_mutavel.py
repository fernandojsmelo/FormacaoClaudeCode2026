def adicionar(item, lista=[]):        # armadilha!
    lista.append(item)
    return lista

print(adicionar("a"))
print(adicionar("b"))     # a lista "lembra" da chamada anterior

def adicionar_ok(item, lista=None):
    if lista is None:
        lista = []        # lista nova a cada chamada
    lista.append(item)
    return lista

print(adicionar_ok("a"), adicionar_ok("b"))
