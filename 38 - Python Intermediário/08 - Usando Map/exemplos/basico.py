nomes = ["ana", "bia", "caio"]

maiusculos = map(str.upper, nomes)   # aplica em cada item
print(maiusculos)
print(list(maiusculos))
print(list(map(len, nomes)))
