from pathlib import Path

nota = Path("lembrete.txt")
nota.write_text("comprar café\n", encoding="utf-8")
print(nota.read_text(encoding="utf-8"), end="")
print(nota.exists(), nota.is_file(), nota.is_dir())
print(nota.stat().st_size, "bytes")
print(Path("sumiu.txt").exists())
