# Exercício: menu que repete até sair
saldo = 0
while True:
    opcao = input("[1] Depositar [2] Ver saldo [0] Sair: ")
    if opcao == "1":
        saldo += float(input("Valor: "))
    elif opcao == "2":
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida")
