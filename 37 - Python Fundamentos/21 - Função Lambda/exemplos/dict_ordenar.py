estoque = {"maçã": 12, "banana": 30, "uva": 5}
mais = sorted(estoque.items(), key=lambda p: p[1], reverse=True)
print(mais)
print(sorted(estoque, key=lambda f: estoque[f]))   # só os nomes
