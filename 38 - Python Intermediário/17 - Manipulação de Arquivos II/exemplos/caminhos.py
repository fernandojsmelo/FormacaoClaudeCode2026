from pathlib import Path

arquivo = Path("relatorios") / "2026" / "vendas_outubro.csv"
print(arquivo)                 # o / junta partes do caminho
print(arquivo.name)
print(arquivo.stem, "|", arquivo.suffix)
print(arquivo.parent)
print(arquivo.with_suffix(".xlsx"))
print(arquivo.parts)
