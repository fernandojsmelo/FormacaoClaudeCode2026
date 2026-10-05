def apresentar(nome, idade, cidade):
    print(f"{nome}, {idade}, {cidade}")

dados = ["Ana", 29, "Recife"]
apresentar(*dados)                   # * espalha a lista
info = {"cidade": "Natal", "nome": "Bia", "idade": 31}
apresentar(**info)                   # ** espalha o dict
print(*["a", "b", "c"], sep="-")     # funciona no print também
