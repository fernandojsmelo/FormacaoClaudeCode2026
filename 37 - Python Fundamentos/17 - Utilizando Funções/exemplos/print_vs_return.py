def soma_print(a, b):
    print(a + b)

def soma_return(a, b):
    return a + b

x = soma_print(2, 3)     # mostra 5, mas devolve None
y = soma_return(2, 3)    # não mostra nada, devolve 5
print("x =", x, "| y =", y)
