"""Simulacao: o 'modelo' abaixo e um stub com regras, sem API.
O objetivo e mostrar QUEM decide o proximo passo, nao a qualidade da IA."""

PEDIDOS = {"123": "enviado em 02/10, entrega prevista 08/10"}
POLITICA = "Devolucao em ate 7 dias apos o recebimento."
chamadas = 0


def modelo(tarefa, contexto=""):
    """Faz de conta de uma chamada a um LLM."""
    global chamadas
    chamadas += 1
    return f"<resposta do modelo para: {tarefa}>"


# ---------- WORKFLOW: o codigo decide a ordem ----------
def workflow(pergunta):
    passos = ["classificar", "consultar pedido", "consultar politica", "responder"]
    modelo("classificar a pergunta")
    status = PEDIDOS.get("123", "nao encontrado")
    politica = POLITICA
    modelo("responder", f"{status} | {politica}")
    return passos


# ---------- AGENTE: o modelo decide a ordem, em laco ----------
def decidir(pergunta, historico):
    """Stub da decisao do modelo: qual ferramenta usar agora?"""
    global chamadas
    chamadas += 1
    if "pedido" in pergunta and "consultar_pedido" not in historico:
        return "consultar_pedido"
    if "devol" in pergunta and "consultar_politica" not in historico:
        return "consultar_politica"
    return "responder"


def agente(pergunta, max_passos=5):
    historico = []
    for _ in range(max_passos):
        acao = decidir(pergunta, historico)
        historico.append(acao)
        if acao == "responder":
            break
    return historico


perguntas = [
    "meu pedido 123 chegou? posso devolver?",
    "qual o horario de atendimento?",
]
for p in perguntas:
    print("PERGUNTA:", p)
    chamadas = 0
    print("  workflow:", workflow(p), "| chamadas ao modelo:", chamadas)
    chamadas = 0
    print("  agente:  ", agente(p), "| chamadas ao modelo:", chamadas)
