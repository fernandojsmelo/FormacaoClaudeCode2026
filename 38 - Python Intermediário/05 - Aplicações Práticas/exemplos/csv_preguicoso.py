import csv
from collections import defaultdict


def vendas(caminho):
    with open(caminho, encoding="utf-8", newline="") as arq:
        for registro in csv.DictReader(arq):
            registro["valor"] = float(registro["valor"])
            yield registro


total = defaultdict(float)
for v in vendas("vendas.csv"):
    total[v["categoria"]] += v["valor"]
print(dict(total))
