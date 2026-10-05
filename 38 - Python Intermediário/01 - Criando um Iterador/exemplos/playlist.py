class Playlist:
    """Iterável: cada for ganha um iterador novo."""

    def __init__(self, *musicas):
        self.musicas = list(musicas)

    def __iter__(self):
        return iter(self.musicas)


p = Playlist("Intro", "Refrão", "Final")
print(list(p))
print(list(p))   # funciona de novo
print("Refrão" in p)
