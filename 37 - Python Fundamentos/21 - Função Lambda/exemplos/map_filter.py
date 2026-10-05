numeros = [1, 2, 3, 4, 5, 6]
print(list(map(lambda n: n * 10, numeros)))
print(list(filter(lambda n: n % 2 == 0, numeros)))
# Com list comprehension (aula 16): costuma ser mais claro
print([n * 10 for n in numeros])
print([n for n in numeros if n % 2 == 0])
