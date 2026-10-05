with open("lista.txt", encoding="utf-8") as arq:
    for numero, linha in enumerate(arq, start=1):
        print(numero, linha.rstrip("\n"))
