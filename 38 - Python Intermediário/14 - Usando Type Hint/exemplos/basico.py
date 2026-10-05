def preco_final(valor: float, desconto: float = 0.0) -> float:
    return round(valor * (1 - desconto), 2)


cliente: str = "Ana"
itens: int = 3

print(preco_final(200, 0.15))
print(preco_final.__annotations__)
