quadrados = (n * n for n in range(1, 6))   # parênteses
print(quadrados)
print(list(quadrados))

# Dentro de uma função, nem precisa dos parênteses extras
print(sum(n * n for n in range(1, 6)))
print(max(len(p) for p in ["sol", "lua", "estrela"]))
