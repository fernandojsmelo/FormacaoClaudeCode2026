try:
    with open("nao_existe.txt", encoding="utf-8") as arq:
        print(arq.read())
except FileNotFoundError:
    print("Arquivo não encontrado: confira o nome e a pasta")

with open("lista.txt", "rb") as arq:       # os bytes de verdade
    print(arq.read(8))
