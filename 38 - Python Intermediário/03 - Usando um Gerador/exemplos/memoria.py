import sys

lista = [n * 2 for n in range(1_000_000)]
gerador = (n * 2 for n in range(1_000_000))

print("lista:  ", sys.getsizeof(lista), "bytes")
print("gerador:", sys.getsizeof(gerador), "bytes")
print(sum(gerador) == sum(lista))
