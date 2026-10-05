def classificar(nota):
    if nota >= 7:
        return "aprovado"     # return encerra a função aqui
    return "reprovado"

for nota in [8.0, 5.5]:
    print(nota, classificar(nota))
