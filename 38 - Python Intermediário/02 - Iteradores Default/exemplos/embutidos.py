for valor in ["ab", (1, 2), {"x": 1}, {7}]:
    it = iter(valor)
    print(type(it).__name__, "->", next(it))
