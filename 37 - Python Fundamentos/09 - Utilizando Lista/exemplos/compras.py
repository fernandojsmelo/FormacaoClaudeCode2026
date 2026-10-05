compras = []
compras.append(input("1º item: ").strip())
compras.append(input("2º item: ").strip())
compras.append(input("3º item: ").strip())
compras.sort()
print(f"{len(compras)} itens:", ", ".join(compras))
