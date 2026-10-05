with open("lista.txt", encoding="utf-8") as arq:  # "r": padrão
    tudo = arq.read()
print(repr(tudo))

with open("lista.txt", encoding="utf-8") as arq:
    print(arq.readline().strip())    # uma linha
    print(arq.readlines())           # o resto, numa lista
