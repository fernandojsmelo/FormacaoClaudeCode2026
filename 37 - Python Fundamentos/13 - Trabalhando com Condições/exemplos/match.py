comando = input("Comando: ").strip().lower()
match comando:
    case "iniciar":
        print("Iniciando...")
    case "pausar" | "parar":
        print("Pausando...")
    case _:
        print("Comando desconhecido")
