"""Acesso ao banco SQLite das tarefas."""
import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path(__file__).with_name("tarefas.db")


def conectar(caminho=CAMINHO_BANCO):
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela(conexao):
    conexao.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            concluida INTEGER NOT NULL DEFAULT 0,
            criada_em TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
        )
        """
    )
    conexao.commit()


def listar(conexao):
    linhas = conexao.execute("SELECT id, texto, concluida FROM tarefas ORDER BY id").fetchall()
    return [{"id": l["id"], "texto": l["texto"], "concluida": bool(l["concluida"])} for l in linhas]


def adicionar(conexao, texto):
    conexao.execute("INSERT INTO tarefas (texto) VALUES (?)", (texto,))
    conexao.commit()


def marcar(conexao, id_tarefa, concluida):
    conexao.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (int(concluida), id_tarefa))
    conexao.commit()


def remover(conexao, id_tarefa):
    conexao.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()


def remover_concluidas(conexao):
    conexao.execute("DELETE FROM tarefas WHERE concluida = 1")
    conexao.commit()
