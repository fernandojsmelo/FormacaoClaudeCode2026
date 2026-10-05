"""Regras do Pedra, Papel e Tesoura."""
import random

OPCOES = ["Pedra", "Papel", "Tesoura"]
# Quem cada opção vence.
VENCE = {"Pedra": "Tesoura", "Papel": "Pedra", "Tesoura": "Papel"}


def jogada_do_computador():
    return random.choice(OPCOES)


def resultado(jogador, computador):
    """Devolve 'vitoria', 'derrota' ou 'empate' do ponto de vista do jogador."""
    if jogador == computador:
        return "empate"
    return "vitoria" if VENCE[jogador] == computador else "derrota"
