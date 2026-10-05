from operator import mul

bases = [2, 3, 4]
expoentes = [3, 2, 1]

print(list(map(pow, bases, expoentes)))   # pow(2, 3), ...
# para no menor iterável:
print(list(map(mul, [1, 2, 3], [10, 20, 30, 40])))
