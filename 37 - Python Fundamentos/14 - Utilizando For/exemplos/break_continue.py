numeros = [4, 7, -1, 12, 0, 9]
for n in numeros:
    if n < 0:
        continue          # pula este e segue
    if n == 0:
        print("achou zero, parando")
        break             # sai do for
    print(n)
