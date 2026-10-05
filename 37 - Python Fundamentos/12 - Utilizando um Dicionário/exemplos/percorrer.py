estoque = {"maçã": 12, "banana": 30, "uva": 0}
print(list(estoque.keys()))
print(list(estoque.values()))
for fruta, qtd in estoque.items():
    print(f"{fruta:<8}{qtd:>4}")
print("Total:", sum(estoque.values()))
