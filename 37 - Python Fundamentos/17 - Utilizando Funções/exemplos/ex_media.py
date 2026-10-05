# Exercício: funções pequenas que se combinam
def media(notas):
    return sum(notas) / len(notas)

def situacao(valor):
    return "aprovado" if valor >= 7 else "recuperação"

notas = [7.5, 8.0, 6.5]
m = media(notas)
print(f"Média {m:.2f}: {situacao(m)}")
