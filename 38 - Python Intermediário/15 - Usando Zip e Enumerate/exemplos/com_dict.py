campos = ["nome", "idade", "cidade"]
valores = ["Ana", 30, "Recife"]

pessoa = dict(zip(campos, valores))
print(pessoa)

precos = {"café": 4.5, "pão": 0.8}
invertido = dict(zip(precos.values(), precos.keys()))
print(invertido)
