precos = ["10,50", "3,99", "120,00"]
numeros = [float(p.replace(",", ".")) for p in precos]
print(numeros, sum(numeros))
palavras = "o rato roeu a roupa".split()
print([len(p) for p in palavras])
