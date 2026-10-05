import re

contatos = """Ana: 11 98765-4321
Bia (21)3456-7890 | Caio: (31) 99999-0000
Dani: 1234"""

padrao = r"\(?(\d{2})\)?\s*(\d{4,5})-(\d{4})"
for ddd, parte1, parte2 in re.findall(padrao, contatos):
    print(f"({ddd}) {parte1}-{parte2}")
