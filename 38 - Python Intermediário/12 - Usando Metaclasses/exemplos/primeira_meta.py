class Rastreada(type):
    def __new__(mcs, nome, bases, atributos):
        print(f"criando a classe {nome}...")
        atributos["origem"] = "Rastreada"     # injeta atributo
        return super().__new__(mcs, nome, bases, atributos)


class Pedido(metaclass=Rastreada):            # roda aqui!
    pass


print("depois do class")
print(Pedido.origem)
print(type(Pedido).__name__)
