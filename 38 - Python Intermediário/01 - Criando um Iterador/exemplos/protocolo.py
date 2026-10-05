notas = [7, 9, 10]
it = iter(notas)          # pede um iterador à lista
print(type(it).__name__)
print(next(it))           # entrega um item por vez
print(next(it))
print(next(it))
try:
    next(it)              # acabou: não há próximo
except StopIteration:
    print("StopIteration: fim dos itens")
