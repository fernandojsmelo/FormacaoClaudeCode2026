# Exercício: preço final com argumentos padrão
def preco_final(preco, desconto=0.0, frete=15.0):
    return preco * (1 - desconto) + frete

print(f"{preco_final(100):.2f}")
print(f"{preco_final(100, desconto=0.1):.2f}")
print(f"{preco_final(100, frete=0):.2f}")
print(f"{preco_final(frete=0, preco=250, desconto=0.2):.2f}")
