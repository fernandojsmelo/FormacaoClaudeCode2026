import csv

with open("produtos.csv", encoding="utf-8", newline="") as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)              # primeira linha
    for linha in leitor:
        print(linha)

print(cabecalho)
print(type(linha[1]))                # tudo chega como texto
