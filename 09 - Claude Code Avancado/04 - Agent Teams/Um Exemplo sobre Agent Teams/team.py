"""
Agent Teams com o Claude Agent SDK (Python) — Fan-Out / Fan-In

Versao em codigo do time definido em .claude/agents/review-team/*.md:
os mesmos 3 sub-agents (security, quality, tests), mas definidos
programaticamente via AgentDefinition e orquestrados pelo proprio
Claude atraves da tool "Agent" (equivalente a Task tool do Claude Code).

Requisitos:
    pip install claude-agent-sdk
    Node.js 18+ instalado (o SDK usa o binario do Claude Code por baixo)
    export ANTHROPIC_API_KEY=...

Uso:
    python team.py

Documentacao oficial:
    https://code.claude.com/docs/en/agent-sdk/python.md
    https://code.claude.com/docs/en/agent-sdk/subagents.md
"""

import asyncio
from pathlib import Path

from claude_agent_sdk import (
    AgentDefinition,
    ClaudeAgentOptions,
    ResultMessage,
    ToolUseBlock,
    query,
)

AGENTS = {
    "security-agent": AgentDefinition(
        description=(
            "Revisa codigo em busca de vulnerabilidades de seguranca "
            "(OWASP Top 10, segredos hardcoded, injecao, etc)."
        ),
        prompt=(
            "Voce e um revisor de seguranca. Revise APENAS os arquivos indicados quanto a:\n"
            "- Segredos, senhas ou tokens hardcoded no codigo\n"
            "- Injecao (SQL, comando, template) por concatenacao de strings nao sanitizadas\n"
            "- Validacao de entrada ausente em pontos que recebem dados externos\n\n"
            "Nao opine sobre nomenclatura, estilo ou testes — isso e responsabilidade de outros agents.\n"
            "Liste cada achado como: [severidade: critico|aviso] arquivo:linha — descricao do risco."
        ),
        tools=["Read", "Grep"],
    ),
    "quality-agent": AgentDefinition(
        description=(
            "Revisa codigo quanto a legibilidade, nomenclatura e complexidade desnecessaria."
        ),
        prompt=(
            "Voce e um revisor de qualidade. Revise APENAS os arquivos indicados quanto a:\n"
            "- Nomes de variaveis e funcoes pouco claros\n"
            "- Funcoes fazendo mais de uma coisa\n"
            "- Duplicacao de logica e complexidade desnecessaria\n\n"
            "Nao opine sobre seguranca ou testes — isso e responsabilidade de outros agents.\n"
            "Liste cada achado como: [severidade: critico|aviso] arquivo:linha — sugestao objetiva."
        ),
        tools=["Read"],
    ),
    "test-agent": AgentDefinition(
        description="Revisa codigo quanto a cobertura e qualidade de testes.",
        prompt=(
            "Voce e um revisor de testes. Revise APENAS os arquivos indicados quanto a:\n"
            "- Funcoes ou caminhos criticos sem nenhum teste associado\n"
            "- Casos de borda obvios nao cobertos (entradas vazias, erros, valores limite)\n\n"
            "Nao opine sobre seguranca ou estilo de codigo — isso e responsabilidade de outros agents.\n"
            "Liste cada achado como: [severidade: critico|aviso] arquivo:linha — o que falta testar."
        ),
        tools=["Read", "Grep"],
    ),
}

ORCHESTRATOR_PROMPT = """\
Revise o arquivo exemplo/auth.js usando os agents security-agent, quality-agent \
e test-agent, disparando os tres EM PARALELO (nao um de cada vez).

Aguarde os tres concluirem antes de responder. Consolide tudo em um unico \
relatorio, removendo duplicatas e priorizando por severidade, no formato:

### Critico (bloqueia merge)
### Avisos
### Pontos positivos
"""


async def main() -> None:
    exemplo_dir = Path(__file__).parent

    async for message in query(
        prompt=ORCHESTRATOR_PROMPT,
        options=ClaudeAgentOptions(
            cwd=str(exemplo_dir),
            allowed_tools=["Read", "Grep", "Agent"],
            agents=AGENTS,
        ),
    ):
        # Evidencia de que o fan-out aconteceu: cada Task(...)/Agent(...)
        # disparado pelo orquestrador aparece aqui como um ToolUseBlock.
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if isinstance(block, ToolUseBlock) and block.name in ("Task", "Agent"):
                    print(f"-> sub-agent disparado: {block.input.get('subagent_type')}")

        is_subagent = hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id
        if is_subagent:
            print("   (executando dentro de um sub-agent)")

        # Sub-agents tambem emitem ResultMessage ao concluir; so a do
        # orquestrador (sem parent_tool_use_id) e o relatorio final consolidado.
        if isinstance(message, ResultMessage) and not is_subagent:
            print("\n=== Relatorio consolidado ===\n")
            print(message.result)
            print(f"\nCusto total: ${message.total_cost_usd:.4f} · {message.num_turns} turno(s)")


if __name__ == "__main__":
    asyncio.run(main())
