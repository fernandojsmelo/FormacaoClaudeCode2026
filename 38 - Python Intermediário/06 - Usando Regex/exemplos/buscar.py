import re

texto = "Pedido 4821 enviado em 05/10/2026"

print(re.search(r"\d+", texto))         # primeira ocorrência
print(re.search(r"\d+", texto).group())
print(re.match(r"\d+", texto))          # só no começo: None
print(re.fullmatch(r"\d{4}", "4821"))   # a string inteira
print(bool(re.fullmatch(r"\d{4}", "48210")))
