produtos = [
    {"nome": "Teclado", "preco": 250, "estoque": 4},
    {"nome": "Mouse", "preco": 90, "estoque": 0},
    {"nome": "Monitor", "preco": 899, "estoque": 2},
    {"nome": "Cabo", "preco": 25, "estoque": 30},
]

disponiveis = filter(lambda p: p["estoque"] > 0, produtos)
baratos = filter(lambda p: p["preco"] < 300, disponiveis)
print([p["nome"] for p in baratos])
