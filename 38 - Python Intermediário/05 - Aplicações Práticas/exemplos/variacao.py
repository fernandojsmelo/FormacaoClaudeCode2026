from itertools import pairwise

cotacoes = [5.10, 5.18, 5.05, 5.05, 5.22]

for antes, depois in pairwise(cotacoes):
    dif = depois - antes
    seta = "↑" if dif > 0 else "↓" if dif < 0 else "="
    print(f"{antes:.2f} -> {depois:.2f} {seta}")
