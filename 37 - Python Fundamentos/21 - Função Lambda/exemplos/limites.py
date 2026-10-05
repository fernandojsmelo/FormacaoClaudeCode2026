# lambda é uma única EXPRESSÃO: nada de blocos ou várias linhas
faixa = lambda n: "alto" if n > 10 else "baixo"  # ternário pode
print(faixa(15), faixa(3))

# PEP 8: não dê nome a uma lambda; para isso existe def
def faixa_def(n):
    return "alto" if n > 10 else "baixo"
print(faixa_def(15))
