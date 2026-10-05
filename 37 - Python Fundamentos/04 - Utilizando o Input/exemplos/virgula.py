preco = input("Preço (use vírgula se quiser): ")
preco = float(preco.replace(",", "."))  # aceita 12,50 e 12.50
print("Com 10% de desconto:", round(preco * 0.9, 2))
