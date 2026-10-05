from pathlib import Path

ASSINATURAS = {
    b"\x89PNG\r\n\x1a\n": "imagem PNG",
    b"%PDF": "documento PDF",
    b"PK\x03\x04": "arquivo ZIP (ou .docx, .xlsx)",
}

Path("foto.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\0" * 20)
Path("contrato.pdf").write_bytes(b"%PDF-1.7\n...")
Path("falso.pdf").write_bytes(b"MZ\x90\x00")    # extensão mente


def tipo_real(caminho):
    inicio = Path(caminho).read_bytes()[:8]
    for magica, nome in ASSINATURAS.items():
        if inicio.startswith(magica):
            return nome
    return "desconhecido"


for nome in ["foto.png", "contrato.pdf", "falso.pdf"]:
    print(f"{nome:13} -> {tipo_real(nome)}")
