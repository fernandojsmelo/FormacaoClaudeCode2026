import csv

linhas = [
    ["produto", "preco", "estoque"],
    ["Caneta", 2.5, 120],
    ["Caderno, 96 fls", 18.9, 40],    # vírgula no texto
]

with open("produtos.csv", "w", encoding="utf-8",
          newline="") as f:
    csv.writer(f).writerows(linhas)

with open("produtos.csv", encoding="utf-8") as f:
    print(f.read(), end="")
