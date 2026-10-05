aluno = {"nome": "Ana", "idade": 29}
print(aluno.get("email"))             # None: não existe
print(aluno.get("email", "sem email"))  # valor padrão
print(aluno.get("nome", "?"))
