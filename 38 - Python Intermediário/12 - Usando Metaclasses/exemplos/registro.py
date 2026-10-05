class RegistraPlugins(type):
    plugins = {}

    def __new__(mcs, nome, bases, atributos):
        classe = super().__new__(mcs, nome, bases, atributos)
        if bases:                      # não registra a base
            mcs.plugins[nome.lower()] = classe
        return classe


class Plugin(metaclass=RegistraPlugins):
    pass


class Pdf(Plugin):
    pass


class Csv(Plugin):
    pass


print(list(RegistraPlugins.plugins))
leitor = RegistraPlugins.plugins["csv"]()     # cria pelo nome
print(type(leitor).__name__)
