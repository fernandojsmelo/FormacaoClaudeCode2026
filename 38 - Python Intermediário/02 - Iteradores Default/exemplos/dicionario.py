estoque = {"maçã": 4, "uva": 0, "kiwi": 7}
print(list(estoque))            # chaves
print(list(estoque.values()))
for fruta, qtd in estoque.items():
    if qtd == 0:
        print(fruta, "esgotou")
