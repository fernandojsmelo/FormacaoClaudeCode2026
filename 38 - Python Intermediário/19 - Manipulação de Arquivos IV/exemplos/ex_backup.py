import zipfile
from pathlib import Path

pasta = Path("notas")
pasta.mkdir(exist_ok=True)
for n in range(1, 4):
    arquivo = pasta / f"aula{n}.txt"
    arquivo.write_text(f"resumo {n}\n" * 30, "utf-8")

with zipfile.ZipFile("backup_notas.zip", "w",
                     compression=zipfile.ZIP_DEFLATED) as z:
    for arquivo in sorted(pasta.glob("*.txt")):
        z.write(arquivo)

original = sum(a.stat().st_size for a in pasta.glob("*.txt"))
compactado = Path("backup_notas.zip").stat().st_size
print(f"{original} bytes -> {compactado} bytes")
print(zipfile.ZipFile("backup_notas.zip").namelist())
