notas = [8.5, 4.0, 9.5, 6.0, 7.0, 3.5]
aprovadas = [n for n in notas if n >= 7]
print(aprovadas)
nomes = ["ana", "", "bia", "  ", "caio"]
validos = [n.title() for n in nomes if n.strip()]
print(validos)
