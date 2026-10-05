pares = [("Ana", 9.5), ("Bia", 7.0), ("Caio", 8.2)]

nomes, notas = zip(*pares)        # o * espalha os pares
print(nomes)
print(notas)

tabela = [[1, 2, 3],
          [4, 5, 6]]
print(list(zip(*tabela)))         # linhas viram colunas
