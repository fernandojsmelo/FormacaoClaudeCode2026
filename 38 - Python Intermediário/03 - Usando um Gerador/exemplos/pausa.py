def passos():
    print("  começou")
    yield 1
    print("  voltou depois do 1")
    yield 2
    print("  terminou")


g = passos()             # nada roda ainda
print("criado")
print(next(g))
print(next(g))
try:
    next(g)
except StopIteration:
    print("StopIteration")
