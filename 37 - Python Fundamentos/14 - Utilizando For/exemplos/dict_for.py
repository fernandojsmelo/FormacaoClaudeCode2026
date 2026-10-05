estoque = {"maçã": 12, "banana": 0, "uva": 5}
for fruta, qtd in estoque.items():
    if qtd == 0:
        print(f"{fruta}: ESGOTADO")
    else:
        print(f"{fruta}: {qtd}")
