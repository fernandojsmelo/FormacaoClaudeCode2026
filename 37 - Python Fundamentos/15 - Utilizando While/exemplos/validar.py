idade = input("Idade: ")
while not idade.isdigit():
    print("Digite só números.")
    idade = input("Idade: ")
print("Idade válida:", int(idade))
