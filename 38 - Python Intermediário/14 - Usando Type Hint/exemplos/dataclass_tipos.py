from dataclasses import dataclass, field


@dataclass
class Pedido:
    cliente: str
    itens: list[str] = field(default_factory=list)
    pago: bool = False


p = Pedido("Ana", ["livro"])
print(p)
print(Pedido("Bia"))
