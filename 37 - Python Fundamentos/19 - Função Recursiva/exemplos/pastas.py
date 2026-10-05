# Recursão brilha em estruturas que se repetem por dentro
projeto = {"src": {"app.py": None, "util": {"texto.py": None}},
           "README.md": None}

def listar(pasta, recuo=0):
    for nome, conteudo in pasta.items():
        print("  " * recuo + nome)
        if conteudo is not None:       # é uma subpasta
            listar(conteudo, recuo + 1)

listar(projeto)
