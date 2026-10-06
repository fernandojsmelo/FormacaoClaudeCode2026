"""Simulacao: quantos casos a IA decide sozinha e quantos vao para
uma pessoa, conforme o limiar de confianca. Dados ficticios."""
import random

rnd = random.Random(7)
casos = []
for _ in range(1000):
    confianca = rnd.choice([0.55, 0.65, 0.75, 0.85, 0.95, 0.98])
    acertou = rnd.random() < confianca   # suposicao: confianca calibrada
    casos.append((confianca, acertou))

print("limiar | decide sozinha | erros nesses | vai para pessoa")
for limiar in (0.5, 0.8, 0.9, 0.97):
    auto = [c for c in casos if c[0] >= limiar]
    erros = sum(1 for _, ok in auto if not ok)
    print(f"{limiar:>6.2f} | {len(auto) / len(casos):>13.0%} | "
          f"{erros / len(auto):>11.1%} | {1 - len(auto) / len(casos):>14.0%}")
