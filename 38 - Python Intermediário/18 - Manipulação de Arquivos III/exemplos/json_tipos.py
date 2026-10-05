import json
from datetime import date

evento = {"nome": "Workshop", "data": date(2026, 11, 20),
          "tags": {"python", "dados"}}

try:
    json.dumps(evento)
except TypeError as erro:
    print("Erro:", erro)

def converter(valor):
    if isinstance(valor, date):
        return valor.isoformat()
    if isinstance(valor, set):
        return sorted(valor)
    raise TypeError(type(valor))

print(json.dumps(evento, default=converter, ensure_ascii=False))
