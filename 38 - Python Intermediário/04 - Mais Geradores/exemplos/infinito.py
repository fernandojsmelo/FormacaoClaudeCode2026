from itertools import islice


def ids(prefixo):
    n = 1
    while True:              # nunca termina sozinho
        yield f"{prefixo}-{n:03d}"
        n += 1


gerar = ids("PED")
print(next(gerar), next(gerar))
print(list(islice(gerar, 3)))   # pega só os próximos 3
