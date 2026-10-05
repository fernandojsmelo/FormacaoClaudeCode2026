with open("lista.txt", "w", encoding="utf-8") as arq:
    arq.write("café\n")          # write não põe o \n sozinho
    arq.write("pão\n")
    arq.writelines(["leite\n", "maçã\n"])

print("arquivo gravado")
print(arq.closed)                    # o with já fechou
