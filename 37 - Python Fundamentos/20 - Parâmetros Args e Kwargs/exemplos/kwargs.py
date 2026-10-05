def perfil(**dados):          # junta os nomeados num dict
    print(type(dados))
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

perfil(nome="Ana", cidade="Recife", linguagem="Python")
