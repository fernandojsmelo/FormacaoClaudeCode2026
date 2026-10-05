import csv
import json
from collections import defaultdict

with open("vendas.csv", "w", encoding="utf-8", newline="") as f:
    f.write("vendedor,valor\nAna,300\nBia,120\n")
    f.write("Ana,80\nCaio,50\n")

totais = defaultdict(float)
with open("vendas.csv", encoding="utf-8", newline="") as f:
    for venda in csv.DictReader(f):
        totais[venda["vendedor"]] += float(venda["valor"])

with open("totais.json", "w", encoding="utf-8") as f:
    json.dump(totais, f, indent=2, ensure_ascii=False)

print(open("totais.json", encoding="utf-8").read())
