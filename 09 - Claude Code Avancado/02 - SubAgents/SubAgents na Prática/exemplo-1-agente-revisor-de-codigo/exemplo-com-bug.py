"""Arquivo de demonstração com bugs propositais, só para testar o subagente code-reviewer."""

import sqlite3


def buscar_usuario(nome):
    conexao = sqlite3.connect("app.db")
    cursor = conexao.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"
    cursor.execute(query)
    return cursor.fetchone()


def calcular_media(valores):
    total = 0
    for v in valores:
        total += v
    return total / len(valores)


def carregar_config(caminho):
    arquivo = open(caminho)
    conteudo = arquivo.read()
    return conteudo
