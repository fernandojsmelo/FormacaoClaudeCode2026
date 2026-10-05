SEGREDO = 7
tentativas = 0
while tentativas < 3:
    palpite = int(input("Palpite (1 a 10): "))
    tentativas += 1
    if palpite == SEGREDO:
        print(f"Acertou em {tentativas} tentativa(s)!")
        break
    print("Maior" if palpite < SEGREDO else "Menor")
else:
    print("Acabaram as tentativas. Era", SEGREDO)
