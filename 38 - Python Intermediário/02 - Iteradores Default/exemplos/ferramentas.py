from itertools import count, cycle, islice, chain

print(list(islice(count(10, 5), 4)))     # 10, 15, 20, 25
print(list(islice(cycle("AB"), 5)))      # A B A B A
print(list(chain([1, 2], (3,), "45")))   # junta iteráveis
