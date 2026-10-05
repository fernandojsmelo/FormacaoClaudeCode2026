email = "   Ana.Souza@Exemplo.com  \n"
print(repr(email.strip()))           # tira espaços das pontas
print(repr(email.lstrip()))          # só da esquerda
print(email.strip().lower())         # encadeando métodos
print("---olá---".strip("-"))        # tira outros caracteres
