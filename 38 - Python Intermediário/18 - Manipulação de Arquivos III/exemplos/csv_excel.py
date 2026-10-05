import csv

dados = [["mês", "receita"], ["outubro", "1.250,90"]]

# O Excel em português costuma usar ; como separador
with open("excel_br.csv", "w", encoding="utf-8-sig",
          newline="") as f:
    csv.writer(f, delimiter=";").writerows(dados)

with open("excel_br.csv", encoding="utf-8-sig",
          newline="") as f:
    for linha in csv.reader(f, delimiter=";"):
        print(linha)
