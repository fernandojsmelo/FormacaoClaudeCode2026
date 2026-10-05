from functools import partial
import io

texto = io.StringIO("abcdefgh")
ler4 = partial(texto.read, 4)

# iter(função, sentinela): chama até receber ""
for bloco in iter(ler4, ""):
    print(bloco)
