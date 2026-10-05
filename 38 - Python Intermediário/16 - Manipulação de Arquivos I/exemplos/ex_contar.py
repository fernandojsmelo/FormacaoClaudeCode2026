from collections import Counter
import re

with open("texto.txt", "w", encoding="utf-8") as arq:
    arq.write("O sol nasce. O sol se põe.\n")
    arq.write("A lua nasce depois do sol.\n")

palavras = Counter()
with open("texto.txt", encoding="utf-8") as arq:
    for linha in arq:
        palavras.update(re.findall(r"\w+", linha.lower()))

print(palavras.most_common(3))
print(sum(palavras.values()), "palavras no total")
