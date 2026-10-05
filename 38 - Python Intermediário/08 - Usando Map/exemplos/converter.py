entrada = "10 25 7 40"           # como viria de um input()

numeros = list(map(int, entrada.split()))
print(numeros, sum(numeros))

precos = map(float, ["9.90", "15", "0.5"])
print(sum(precos))
