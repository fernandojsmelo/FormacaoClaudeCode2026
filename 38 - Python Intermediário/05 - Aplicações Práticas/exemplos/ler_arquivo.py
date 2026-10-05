def linhas(caminho):
    with open(caminho, encoding="utf-8") as arq:
        for linha in arq:        # o arquivo já é um iterador
            yield linha.rstrip("\n")


if __name__ == "__main__":
    for n, linha in enumerate(linhas("servidor.log"), 1):
        if n > 3:
            break
        print(n, linha)
