class ExigeExecutar(type):
    def __new__(mcs, nome, bases, atributos):
        if bases and "executar" not in atributos:
            raise TypeError(f"{nome} precisa de executar()")
        return super().__new__(mcs, nome, bases, atributos)


class Tarefa(metaclass=ExigeExecutar):
    pass


class Backup(Tarefa):
    def executar(self):
        return "backup feito"


print(Backup().executar())


class Relatorio(Tarefa):       # esqueceu o executar()
    pass
