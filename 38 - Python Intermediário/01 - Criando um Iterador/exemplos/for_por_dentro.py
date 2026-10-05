frutas = ["maçã", "uva", "kiwi"]

# O que o for faz por baixo dos panos:
it = iter(frutas)
while True:
    try:
        fruta = next(it)
    except StopIteration:
        break
    print(fruta)
