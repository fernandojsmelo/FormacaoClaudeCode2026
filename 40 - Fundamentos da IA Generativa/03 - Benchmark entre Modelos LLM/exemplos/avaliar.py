import math
import random


def wilson(acertos, n, z=1.96):
    """Intervalo de confiança de 95% para uma proporção."""
    p = acertos / n
    d = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / d
    folga = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return centro - folga, centro + folga


def simular(taxa_real, n, semente):
    rnd = random.Random(semente)
    return sum(rnd.random() < taxa_real for _ in range(n))


# Dois modelos fictícios: A acerta 70% e B acerta 75% de verdade
for n in (40, 1000):
    a = simular(0.70, n, 1)
    b = simular(0.75, n, 2)
    print(f"--- benchmark com {n} perguntas ---")
    for nome, ac in (("A", a), ("B", b)):
        lo, hi = wilson(ac, n)
        print(f"modelo {nome}: {ac / n:.1%}  (IC 95%: {lo:.1%} a {hi:.1%})")
