nums = [1, 2, 3, 4]

print(list(map(str, nums)))         # função pronta: curto
print([str(n) for n in nums])

print(list(map(lambda n: n * n, nums)))      # lambda...
print([n * n for n in nums])        # ...lê melhor assim
