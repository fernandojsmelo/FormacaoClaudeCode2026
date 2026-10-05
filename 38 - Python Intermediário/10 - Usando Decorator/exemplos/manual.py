def com_moldura(funcao):
    def embrulho():
        print("=" * 12)
        funcao()               # chama a função original
        print("=" * 12)
    return embrulho


def boas_vindas():
    print(" Bem-vindo!")


boas_vindas = com_moldura(boas_vindas)   # decorando à mão
boas_vindas()
