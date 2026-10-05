def cumprimentar(nome, cumprimento="Olá"):
    return f"{cumprimento}, {nome}!"

def gritar(*args, **kwargs):     # repassa tudo, sem conhecer
    return cumprimentar(*args, **kwargs).upper()

print(gritar("Ana"))
print(gritar("Bia", cumprimento="Bom dia"))
