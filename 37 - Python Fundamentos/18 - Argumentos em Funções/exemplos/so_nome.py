def transferir(valor, *, de, para):   # depois do * só por nome
    print(f"R$ {valor:.2f}: {de} -> {para}")

transferir(100, de="Ana", para="Bia")
transferir(100, "Ana", "Bia")
