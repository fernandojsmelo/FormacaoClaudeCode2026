# Exemplo 1 — Subagente custom "code-reviewer"

Um subagente é definido como um arquivo Markdown com frontmatter YAML dentro
de `.claude/agents/`. Ele roda em uma **janela de contexto isolada**, com seu
próprio system prompt e (opcionalmente) um conjunto restrito de tools —
diferente de pedir "revise como um code reviewer" no meio da conversa
principal, que usa o mesmo contexto e as mesmas tools de sempre.

## O arquivo do subagente

Já está ativo neste projeto em [`.claude/agents/code-reviewer.md`](../../../.claude/agents/code-reviewer.md):

```markdown
---
name: code-reviewer
description: Revisa as alterações de código pendentes (git diff) em busca de
  bugs, problemas de segurança e más práticas. Use proativamente depois de
  terminar uma implementação, ou quando o usuário pedir uma revisão de código.
tools: Read, Grep, Glob, Bash
model: sonnet
---

(system prompt completo com instruções de como revisar, o que procurar,
o que não fazer e o formato de resposta esperado)
```

Pontos importantes do frontmatter:

- `name` — o identificador usado para chamar o subagente explicitamente.
- `description` — é o que o Claude Code principal lê para decidir, sozinho,
  se deve delegar uma tarefa a este subagente (invocação automática/proativa).
- `tools` — lista restrita de tools. Aqui ficou só `Read, Grep, Glob, Bash`:
  o revisor não precisa (e não deve) editar arquivos.
- `model` — opcional; fixa qual modelo esse subagente usa, independente do
  modelo da conversa principal.

## Como invocar

**Explicitamente**, pedindo por nome:

> "Use o subagente code-reviewer para revisar minhas mudanças"

**Automaticamente**, pela tool `Agent` — o Claude principal decide sozinho
com base na `description`, por exemplo depois de terminar uma implementação
maior sem que você peça a revisão de propósito.

## Detalhe que testamos na prática (pegadinha real)

Subagentes definidos em `.claude/agents/*.md` são carregados **no início da
sessão**. Criar o arquivo e tentar chamar o subagente na mesma sessão em que
ele foi criado falha:

```
Agent type 'code-reviewer' not found. Available agents: claude,
claude-code-guide, Explore, general-purpose, Plan, statusline-setup
```

Ou seja: depois de criar/editar um subagente, é preciso **abrir uma sessão
nova** (`claude` de novo, ou reiniciar a atual) para ele aparecer na lista.

## Teste end-to-end (sessão nova, headless)

Para confirmar que funciona de verdade, rodamos uma sessão nova e isolada
(`claude -p`, modo não-interativo) pedindo pra usar o subagente contra o
arquivo [`exemplo-com-bug.py`](exemplo-com-bug.py) deste diretório — um
arquivo escrito de propósito com 4 problemas:

```bash
claude -p "Use o subagente code-reviewer para revisar o arquivo \
SubAgents/SubAgents na Prática/exemplo-1-agente-revisor-de-codigo/exemplo-com-bug.py" \
  --allowedTools "Task,Read,Grep,Glob,Bash(git status)"
```

Resultado real obtido:

> **Bloqueador**
> - Linhas 9-10 — SQL Injection: query montada por concatenação de string
>   com `nome` do usuário, sem parametrização. Corrigir com
>   `cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))`.
>
> **Importantes**
> - Linhas 7-11 — a conexão SQLite nunca é fechada (sem `try/finally` ou
>   `with`), vaza recursos.
> - Linhas 14-18 — `calcular_media` não trata lista vazia → `ZeroDivisionError`.
> - Linhas 21-24 — `carregar_config` abre o arquivo sem `with` e não trata
>   `FileNotFoundError`/`PermissionError`.

Os 4 bugs propositais do arquivo foram encontrados, com a severidade correta
e sem nenhum falso positivo.

## Por que isso importa

- **Contexto isolado**: o subagente não "suja" a conversa principal com todo
  o processo de leitura de arquivo/diff — só o veredito final volta.
- **Tools restritas**: como o `code-reviewer` só tem `Read, Grep, Glob, Bash`,
  ele fisicamente não consegue editar código por engano durante uma revisão.
- **Reuso**: o mesmo subagente serve em qualquer conversa deste projeto, sem
  reescrever o prompt de revisão toda vez.

## Limitações (vale citar)

- Mudou o arquivo do subagente? Precisa de sessão nova pra valer.
- `description` mal escrita = invocação automática ruim (o Claude principal
  decide só com base nesse texto, então ele precisa deixar claro *quando*
  usar o subagente).
