import io

arquivo = io.StringIO("8.5\n\n7\nausente\n10\n6.5\n")


def notas_validas(linhas):
    for linha in linhas:
        try:
            yield float(linha)
        except ValueError:
            continue                 # ignora vazias e texto


notas = list(notas_validas(arquivo))
print(notas)
print(f"média: {sum(notas) / len(notas):.2f}")
