aluno = {"nome": "Ana", "idade": 29}
aluno["idade"] = 30            # chave existe: atualiza
aluno["email"] = "ana@ex.com"  # chave nova: adiciona
print(aluno)
removido = aluno.pop("email")  # remove e devolve o valor
del aluno["idade"]             # remove sem devolver
print(removido, aluno)
