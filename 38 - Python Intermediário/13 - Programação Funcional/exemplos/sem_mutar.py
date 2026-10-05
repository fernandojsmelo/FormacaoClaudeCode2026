notas = [7, 10, 5]

ordenadas = sorted(notas)        # cria uma lista nova
print(notas, ordenadas)          # a original não mudou

aluno = {"nome": "Ana", "nota": 7}
atualizado = {**aluno, "nota": 9}    # novo dicionário
print(aluno)
print(atualizado)

ponto = (2, 3)                   # tupla: não dá para alterar
print(ponto + (4,))              # cria outra tupla
