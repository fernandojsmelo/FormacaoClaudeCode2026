def saudacao(nome, cumprimento="Olá", pontuacao="!"):
    return f"{cumprimento}, {nome}{pontuacao}"

print(saudacao("Ana"))
print(saudacao("Bia", "Bom dia"))
print(saudacao("Caio", pontuacao="..."))
