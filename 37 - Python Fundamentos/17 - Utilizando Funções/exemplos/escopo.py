taxa = 0.1           # variável global

def com_desconto(preco):
    desconto = preco * taxa   # local: só existe aqui dentro
    return preco - desconto

print(com_desconto(200))
print(taxa)
print(desconto)
