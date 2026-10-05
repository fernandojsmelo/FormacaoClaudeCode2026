import re

agenda = "Prova 12/11/2026, entrega 03/12/2026"
padrao = r"(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})"

for m in re.finditer(padrao, agenda):
    print(m.group(), "->", m["dia"], m["mes"], m["ano"])

primeira = re.search(padrao, agenda)
print(primeira.groupdict())
print(re.findall(padrao, agenda))   # com grupos: tuplas
