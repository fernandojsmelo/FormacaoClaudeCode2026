class Passos:
    """Como range(inicio, fim, passo), só com inteiros."""

    def __init__(self, inicio, fim, passo=1):
        self.atual = inicio
        self.fim = fim
        self.passo = passo

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual >= self.fim:
            raise StopIteration
        valor = self.atual
        self.atual += self.passo
        return valor


print(list(Passos(0, 10, 3)))
print(list(Passos(5, 8)))
print(list(Passos(4, 2)))
