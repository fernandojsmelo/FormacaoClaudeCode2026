numeros = [7, 12, 5, 30, 18, 3]

pares = filter(lambda n: n % 2 == 0, numeros)
print(pares)
print(list(pares))                       # só os True passam
print(list(filter(lambda n: n > 15, numeros)))
