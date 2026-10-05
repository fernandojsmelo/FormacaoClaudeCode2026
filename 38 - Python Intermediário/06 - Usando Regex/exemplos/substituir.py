import re

ficha = "CPF 123.456.789-09   tel  (11) 98765-4321"

print(re.sub(r"\s+", " ", ficha))          # espaços extras
print(re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "***", ficha))
print(re.sub(r"\d", "#", "senha 2026"))

# Grupo na troca: inverte data de AAAA-MM-DD para DD/MM/AAAA
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1",
             "2026-10-05"))
