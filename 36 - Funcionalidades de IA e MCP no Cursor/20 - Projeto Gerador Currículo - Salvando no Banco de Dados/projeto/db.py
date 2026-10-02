"""Banco SQLite dos currículos: cada currículo é guardado como JSON."""
import json
import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path(__file__).with_name("curriculos.db")


def conectar(caminho=CAMINHO_BANCO):
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    conexao.execute(
        """
        CREATE TABLE IF NOT EXISTS curriculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dados TEXT NOT NULL,
            atualizado_em TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
        )
        """
    )
    conexao.commit()
    return conexao


def listar(conexao):
    return conexao.execute(
        "SELECT id, nome, atualizado_em FROM curriculos ORDER BY atualizado_em DESC, id DESC"
    ).fetchall()


def carregar(conexao, id_curriculo):
    linha = conexao.execute("SELECT dados FROM curriculos WHERE id = ?", (id_curriculo,)).fetchone()
    return json.loads(linha["dados"]) if linha else None


def salvar(conexao, dados, id_curriculo=None):
    """Cria um currículo novo ou atualiza o existente. Devolve o id."""
    texto = json.dumps(dados, ensure_ascii=False)
    if id_curriculo is None:
        cursor = conexao.execute("INSERT INTO curriculos (nome, dados) VALUES (?, ?)", (dados["nome"], texto))
        id_curriculo = cursor.lastrowid
    else:
        conexao.execute(
            "UPDATE curriculos SET nome = ?, dados = ?, atualizado_em = datetime('now', 'localtime') WHERE id = ?",
            (dados["nome"], texto, id_curriculo),
        )
    conexao.commit()
    return id_curriculo


def excluir(conexao, id_curriculo):
    conexao.execute("DELETE FROM curriculos WHERE id = ?", (id_curriculo,))
    conexao.commit()
