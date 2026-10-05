class Plugin:
    plugins = {}

    def __init_subclass__(cls, **kwargs):   # sem metaclasse
        super().__init_subclass__(**kwargs)
        Plugin.plugins[cls.__name__.lower()] = cls


class Pdf(Plugin):
    pass


class Csv(Plugin):
    pass


print(list(Plugin.plugins))
