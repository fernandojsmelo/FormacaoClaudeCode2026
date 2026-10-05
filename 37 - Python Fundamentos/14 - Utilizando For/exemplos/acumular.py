notas = [8.5, 6.0, 9.5, 7.0]
soma = 0
for nota in notas:
    soma += nota
print("Soma:", soma, "| Média:", soma / len(notas))

maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota
print("Maior:", maior)
