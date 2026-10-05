import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as pasta:
    rascunho = Path(pasta) / "rascunho.txt"
    rascunho.write_text("rascunho", encoding="utf-8")
    print("existe durante o bloco:", rascunho.exists())

print("existe depois do bloco:", rascunho.exists())
