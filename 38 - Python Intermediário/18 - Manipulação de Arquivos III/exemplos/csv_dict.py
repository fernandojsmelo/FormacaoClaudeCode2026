import csv

with open("produtos.csv", encoding="utf-8", newline="") as f:
    for item in csv.DictReader(f):
        valor = float(item["preco"]) * int(item["estoque"])
        print(f'{item["produto"]:<16} R$ {valor:>8.2f}')

clientes = [{"nome": "Ana", "cidade": "Recife"},
            {"nome": "Bia", "cidade": "Natal"}]
with open("clientes.csv", "w", encoding="utf-8",
          newline="") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "cidade"])
    escritor.writeheader()
    escritor.writerows(clientes)
print(open("clientes.csv", encoding="utf-8").read(), end="")
