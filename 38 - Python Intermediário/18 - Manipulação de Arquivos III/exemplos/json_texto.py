import json

pedido = {"cliente": "João", "itens": [{"sku": "A1", "qtd": 2}]}

texto = json.dumps(pedido, ensure_ascii=False)   # vira string
print(texto)
print(json.dumps(pedido))                   # sem ensure_ascii

volta = json.loads(texto)                   # string -> dict
print(volta["itens"][0]["qtd"])
