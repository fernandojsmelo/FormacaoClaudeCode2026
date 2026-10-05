from datetime import datetime


def data_valida(texto):
    try:
        return datetime.strptime(texto, "%d/%m/%Y").date()
    except ValueError:
        return None


for d in ["05/10/2026", "31/02/2026",
          "29/02/2024", "2026-10-05"]:
    print(d, "->", data_valida(d))
