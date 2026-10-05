from functools import reduce
from operator import add, mul

nums = [3, 4, 5]

print(reduce(add, nums))               # ((3 + 4) + 5)
print(reduce(mul, nums))               # ((3 * 4) * 5)
print(reduce(lambda a, b: a if a > b else b, nums))
print(reduce(add, [], 0))         # valor inicial evita erro
