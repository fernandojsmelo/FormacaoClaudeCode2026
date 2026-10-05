nome = input("Nome (pode deixar vazio): ").strip()
if nome:                      # texto vazio é False
    print(f"Olá, {nome}!")
else:
    print("Olá, visitante!")
