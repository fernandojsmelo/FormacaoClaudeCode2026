cores = ["azul", "verde", "roxo"]

# Jeito antigo: índice para pegar o item
for i in range(len(cores)):
    if cores[i] == "verde":
        print("verde na posição", i)

# Jeito pythônico: índice e item juntos
for i, cor in enumerate(cores):
    if cor == "verde":
        print("verde na posição", i)
