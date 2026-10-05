frase = "o rato roeu a roupa do rei de roma"
contagem = {}
for palavra in frase.split():
    letra = palavra[0]
    contagem[letra] = contagem.get(letra, 0) + 1
print(contagem)
