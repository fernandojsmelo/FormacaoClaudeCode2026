def descrever(self):
    return f"Ponto({self.x}, {self.y})"


# type(nome, bases, atributos) cria uma classe na hora
Ponto = type("Ponto", (), {"x": 0, "y": 0,
                           "descrever": descrever})

p = Ponto()
p.x = 3
print(p.descrever())
print(Ponto.__name__, type(Ponto))
