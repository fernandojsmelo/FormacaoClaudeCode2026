with open("diario.txt", "w", encoding="utf-8") as arq:
    arq.write("segunda: estudei iteradores\n")

with open("diario.txt", "a", encoding="utf-8") as arq:  # "a"
    arq.write("terça: estudei geradores\n")
    print("quarta: estudei regex", file=arq)   # print grava

with open("diario.txt", encoding="utf-8") as arq:
    print(arq.read(), end="")
