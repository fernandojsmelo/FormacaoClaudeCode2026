# Exercício: ordenar produtos de várias formas
produtos = [{"nome": "Café", "preco": 18.9, "estoque": 4},
            {"nome": "Arroz", "preco": 6.5, "estoque": 20},
            {"nome": "Azeite", "preco": 32.0, "estoque": 0}]
baratos = sorted(produtos, key=lambda p: p["preco"])
print([p["nome"] for p in baratos])
disponiveis = list(filter(lambda p: p["estoque"] > 0, produtos))
print([p["nome"] for p in disponiveis])
print(max(produtos, key=lambda p: p["estoque"])["nome"])
