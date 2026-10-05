import zipfile
from pathlib import Path

Path("leia_me.txt").write_text("Estoque\n" * 100, "utf-8")
Path("dados.csv").write_text("item,qtd\ncaneta,10\n", "utf-8")

with zipfile.ZipFile("pacote.zip", "w",
                     compression=zipfile.ZIP_DEFLATED) as z:
    z.write("leia_me.txt")
    z.write("dados.csv")

with zipfile.ZipFile("pacote.zip") as z:
    for info in z.infolist():
        print(info.filename, info.file_size, "->",
              info.compress_size)
    print(z.read("dados.csv").decode("utf-8"), end="")
