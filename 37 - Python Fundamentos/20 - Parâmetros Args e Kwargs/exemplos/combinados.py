def registrar(evento, *detalhes, nivel="INFO", **extras):
    print(f"[{nivel}] {evento}", detalhes, extras)

registrar("login")
registrar("erro", "timeout", 30, nivel="ERRO", usuario="ana")
