compras = []
item = input("Item (ENTER para terminar): ").strip()
while item:                       # texto vazio é False
    compras.append(item)
    item = input("Item (ENTER para terminar): ").strip()
print(f"{len(compras)} itens:", ", ".join(compras))
