def conexao():
    print("abriu")
    try:
        while True:
            yield "dado"
    finally:
        print("fechou")      # roda quando o gerador é fechado


g = conexao()
print(next(g))
print(next(g))
g.close()
