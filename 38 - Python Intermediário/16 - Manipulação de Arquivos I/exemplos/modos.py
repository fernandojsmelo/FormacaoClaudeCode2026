import os

if os.path.exists("unico.txt"):
    os.remove("unico.txt")        # para o exemplo recomeçar

with open("unico.txt", "x", encoding="utf-8") as arq:  # cria
    arq.write("primeira vez\n")
print("criado")

try:
    open("unico.txt", "x", encoding="utf-8")   # já existe
except FileExistsError as erro:
    print("Erro:", erro)
