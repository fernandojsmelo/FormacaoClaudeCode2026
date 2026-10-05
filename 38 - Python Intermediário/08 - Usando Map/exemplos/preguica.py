def dobrar(n):
    print(f"  dobrando {n}")
    return n * 2


m = map(dobrar, [1, 2, 3])
print("map criado")        # nada foi calculado ainda
print(next(m))
print(list(m))             # calcula o resto
print(list(m))             # e se esgota
