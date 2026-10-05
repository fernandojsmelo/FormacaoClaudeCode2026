from functools import reduce

pedidos = [120.0, 35.5, 980.0, 15.0, 410.0]

total_grandes = reduce(
    lambda acc, v: acc + v,
    map(lambda v: v * 0.9,              # 10% de desconto
        filter(lambda v: v >= 100, pedidos)),
    0,
)
print(round(total_grandes, 2))

# o mesmo, mais legível:
print(round(sum(v * 0.9 for v in pedidos if v >= 100), 2))
