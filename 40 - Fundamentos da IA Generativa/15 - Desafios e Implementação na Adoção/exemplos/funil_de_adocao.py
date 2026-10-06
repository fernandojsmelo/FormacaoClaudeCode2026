# Numeros ficticios de uma empresa com 200 licencas compradas
etapas = [
    ("licencas atribuidas",             200),
    ("usaram ao menos 1 vez",           150),
    ("usam toda semana",                 90),
    ("usam em tarefas do processo",      45),
    ("tarefas com resultado medido",     20),
]
print(f"{'etapa':<32}{'pessoas':>8}{'do total':>10}{'da anterior':>13}")
anterior = etapas[0][1]
for nome, n in etapas:
    print(f"{nome:<32}{n:>8}{n / etapas[0][1]:>10.0%}{n / anterior:>13.0%}")
    anterior = n
maior = max(range(1, len(etapas)), key=lambda i: etapas[i - 1][1] - etapas[i][1])
print("maior perda de pessoas entre:", etapas[maior - 1][0], "->", etapas[maior][0])
