class Modulo:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        versao = str(getattr(cls, "versao", ""))
        if versao.count(".") != 2:
            raise TypeError(f"{cls.__name__}: versao 'X.Y.Z'")


class Pagamentos(Modulo):
    versao = "2.1.0"


print("Pagamentos ok:", Pagamentos.versao)
try:
    class Estoque(Modulo):
        versao = "2"
except TypeError as erro:
    print("Erro:", erro)
