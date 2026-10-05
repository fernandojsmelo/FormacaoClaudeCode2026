class Unica(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):     # roda em Config()
        if cls not in cls._instancias:
            nova = super().__call__(*args, **kwargs)
            cls._instancias[cls] = nova
        return cls._instancias[cls]


class Config(metaclass=Unica):
    def __init__(self):
        print("carregando configurações...")


a = Config()
b = Config()
print(a is b)
