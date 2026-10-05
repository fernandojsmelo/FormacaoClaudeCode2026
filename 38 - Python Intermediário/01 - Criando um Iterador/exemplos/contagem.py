class Contagem:
    """Iterador: conta de n até 1."""

    def __init__(self, n):
        self.atual = n

    def __iter__(self):
        return self          # o iterador devolve a si mesmo

    def __next__(self):
        if self.atual < 1:
            raise StopIteration
        valor = self.atual
        self.atual -= 1
        return valor


if __name__ == "__main__":
    for x in Contagem(3):
        print(x)
    print(list(Contagem(5)))
