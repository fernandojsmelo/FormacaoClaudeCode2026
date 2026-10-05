import re

cadastros = ["ana@site.com", "bia@", "caio@x.com.br",
             "", "dani site.com", "edu@empresa.org"]

PADRAO = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")

validos = list(filter(PADRAO.fullmatch, cadastros))
print(validos)
print(f"{len(validos)} de {len(cadastros)} são válidos")
