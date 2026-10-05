dados = [3, -1, 8, 0, -5, 12]
# Difícil de ler: duas condições e uma conta numa linha só
r = [x * 2 if x > 0 else 0 for x in dados if x != 0 and x > -3]
print(r)
# Mais claro com for comum
resultado = []
for x in dados:
    if x != 0 and x > -3:
        resultado.append(x * 2 if x > 0 else 0)
print(resultado)
