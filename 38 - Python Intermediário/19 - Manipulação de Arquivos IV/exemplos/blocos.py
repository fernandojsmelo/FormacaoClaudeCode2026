from functools import partial
from pathlib import Path

Path("grande.bin").write_bytes(bytes(range(256)) * 400)

blocos = 0
with open("grande.bin", "rb") as origem, \
        open("copia.bin", "wb") as destino:
    for bloco in iter(partial(origem.read, 4096), b""):
        destino.write(bloco)
        blocos += 1

print(blocos, "blocos de até 4096 bytes")
iguais = Path("grande.bin").read_bytes() == \
    Path("copia.bin").read_bytes()
print("cópia idêntica:", iguais)
