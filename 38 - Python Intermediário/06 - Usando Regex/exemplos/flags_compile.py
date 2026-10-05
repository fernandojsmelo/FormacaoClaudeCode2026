import re

nomes = ["Ana", "ana", "ANA", "Mariana"]
ana = re.compile(r"^ana$", re.IGNORECASE)   # compila uma vez
print([n for n in nomes if ana.search(n)])

print(re.split(r"\s*[;,]\s*", "maçã; uva,kiwi ,  pera"))
