nums = [3, 1, 2]
pares = enumerate(nums)
print(pares)              # um objeto, não uma lista
print(list(pares))        # materializa os itens
print(list(pares))        # e ele já se esgotou
print(list(reversed(nums)))
print(list(zip("abc", nums)))
