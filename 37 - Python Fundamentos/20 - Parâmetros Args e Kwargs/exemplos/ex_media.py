# Exercício: média de quantas notas vierem
def media(*notas, casas=1):
    if not notas:
        return None
    return round(sum(notas) / len(notas), casas)

print(media(7, 8, 9))
print(media(6.5, 7.25, casas=2))
print(media())
