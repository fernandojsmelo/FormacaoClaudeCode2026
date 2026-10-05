from functools import reduce
precos = [10, 20, 30]
print(reduce(lambda total, p: total + p, precos))   # 60
print(sum(precos))     # mais simples
