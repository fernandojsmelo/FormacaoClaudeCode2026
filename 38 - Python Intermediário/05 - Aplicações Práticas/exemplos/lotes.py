from itertools import batched

pedidos = [f"P{n}" for n in range(1, 8)]

for lote in batched(pedidos, 3):      # Python 3.12+
    print("enviando", lote)
