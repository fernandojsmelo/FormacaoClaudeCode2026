# Exemplo: Agent Teams (Fan-Out / Fan-In)

Exemplo mínimo de um "time" de sub-agents rodando em paralelo no Claude Code,
seguindo o padrão ensinado na Aula 4 (ver PDF na pasta ao lado).

## Estrutura

```
.claude/agents/review-team/
  orchestrator.md   ← coordena o time, dispara os 3 agents em paralelo e consolida
  security-agent.md ← só olha vulnerabilidades
  quality-agent.md  ← só olha legibilidade/nomenclatura
  test-agent.md     ← só olha cobertura de testes
exemplo/
  auth.js           ← código de propósito didático, com problemas plantados
team.py             ← o mesmo time, via Claude Agent SDK (Python)
```

`auth.js` tem, de propósito, um segredo hardcoded, uma injeção de SQL por
concatenação de string, nomes de função ruins (`f`, `chk`, `u`, `p`, `q`, `r`, `t`)
e nenhum teste — o suficiente para os 3 agents terem o que reportar.

## Como testar

1. Abra o Claude Code **dentro desta pasta** (`Um Exemplo sobre Agent Teams/`),
   para que ele enxergue `.claude/agents/review-team/`.
2. Peça, por exemplo:

   ```
   Use o review-orchestrator para revisar exemplo/auth.js
   ```

3. Observe: o orquestrador deve disparar os 3 sub-agents juntos (em paralelo,
   não um de cada vez) e no final devolver um único relatório consolidado com
   as seções 🔴 Crítico / ⚠️ Avisos / ✅ Pontos positivos.

## Como testar (via Claude Agent SDK / Python)

`team.py` é o mesmo time, mas definido em código com `AgentDefinition`
em vez de arquivos `.md`, e disparado via `query()` do SDK.

1. `pip install claude-agent-sdk` (requer Node.js 18+ instalado e a
   variável `ANTHROPIC_API_KEY` configurada no ambiente).
2. Rode `python team.py` dentro desta pasta.
3. O script imprime cada sub-agent conforme é disparado (prova do
   paralelismo) e, ao final, o relatório único consolidado pelo Claude.

## O que observar

- Cada sub-agent só comenta sobre seu domínio (isolamento de escopo).
- O tempo total deve ser próximo ao do agent mais lento, não a soma dos três
  (é isso que caracteriza paralelismo, e não execução sequencial).
- A síntese final é responsabilidade exclusiva do orquestrador — os sub-agents
  não se comunicam entre si.

## Para adaptar a um projeto real

Copie a pasta `.claude/agents/review-team/` para a raiz do seu projeto e troque
`exemplo/auth.js` pelo diff/PR real que você quer revisar.
