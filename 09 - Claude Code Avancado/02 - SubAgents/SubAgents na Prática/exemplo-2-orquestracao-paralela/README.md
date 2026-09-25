# Exemplo 2 — Orquestração paralela de subagentes

Diferente do Exemplo 1 (subagente custom definido em arquivo), este exemplo
usa os agentes **já embutidos** no Claude Code (`Explore`, `general-purpose`,
`Plan`, ...) e mostra a técnica de disparar vários de uma vez, em paralelo,
para tarefas de pesquisa independentes — protegendo o contexto da conversa
principal, que recebe só o resumo final de cada um.

## A regra

> Se as tarefas não dependem uma da outra, dispare todas as chamadas da tool
> `Agent` **na mesma mensagem** (mesmo bloco de tool calls). Se uma depende
> do resultado da outra, chame em sequência.

## Como reproduzir

O script [`rodar-exemplo.sh`](rodar-exemplo.sh) dispara uma sessão nova e
isolada (`claude -p`) com um único prompt pedindo duas pesquisas
independentes sobre este mesmo repositório, cada uma em um subagente
`Explore`:

- **Agente A**: resumir todos os exemplos práticos de Hooks em
  `Hooks/Hooks na Pratica/*`.
- **Agente B**: listar tudo configurado dentro de `.claude/` (subagentes,
  hooks, settings.json).

```bash
./rodar-exemplo.sh
```

### Primeira tentativa (dentro da conversa principal): Agente B bloqueado

Na primeira vez que rodamos esse teste — chamando a tool `Agent` direto na
conversa principal, sem passar `--allowedTools` explícito — o Agente B
voltou com este erro em vez de um resumo:

```
Permission for this action was denied by the Claude Code auto mode
classifier. Reason: Blocked by classifier.
```

O subagente tentou ler arquivos dentro de `.claude/` via Bash e o
**classificador de auto mode** vetou a ação — o mesmo mecanismo de segurança
que se aplicaria se fosse o agente principal chamando a tool diretamente.
Subagentes **não pulam** as camadas de permissão do Claude Code; eles herdam
as mesmas regras. Foi por isso que o script acima passa
`--allowedTools "Task,Read,Grep,Glob,Bash(ls*),Bash(cat*),Bash(find*)"`
explicitamente: sem liberar os comandos de leitura, o classificador barra o
subagente na segunda tentativa também.

### Rodando `rodar-exemplo.sh` (resultado real, com as permissões corretas)

> **Agente A — Exemplos práticos de Hooks**
>
> **Exemplo 1 — Som ao finalizar** — evento `Stop`. Toca um som
> (`canberra-gtk-play -i complete`) sempre que o Claude termina de responder.
> Registro: matcher vazio `""`.
>
> **Exemplo 2 — Bloquear comandos perigosos** — evento `PreToolUse`, matcher
> `Bash`. O script `block-dangerous.sh` detecta padrões destrutivos
> (`rm -rf /`, `git push --force` em main/master, `git reset --hard`) e
> retorna `exit 2` para bloquear a tool antes de rodar.
>
> **Agente B — Inventário de `.claude/`**
>
> - `agents/code-reviewer.md`: revisor de código sênior (Read, Grep, Glob,
>   Bash), uso proativo após implementações.
> - `hooks/block-dangerous.sh`: mesmo script do Exemplo 2 dos Hooks.
> - `settings.json`: registra o `PreToolUse`(Bash) → `block-dangerous.sh` e
>   o `Stop` → som de finalização. Sem bloco `permissions`.
>
> Observação do próprio agente: os hooks do `.claude/` real do projeto são
> exatamente os mesmos dos Exemplos 1 e 2 da pasta de prática de Hooks — os
> exemplos didáticos foram promovidos para a configuração ativa do projeto.

Dessa vez os dois agentes rodaram em paralelo e voltaram com sucesso — a
diferença entre essa tentativa e a anterior foi só a lista de tools
liberadas explicitamente para a sessão headless.

### Detalhe extra observado: neutralização de conteúdo com formato de instrução

O resultado do Agente A veio com um aviso do harness:

```
[harness: subagent output matched instruction-shaped pattern(s):
settings-json. Control tags below are neutralized...]
```

O texto que o subagente devolveu mencionava `settings.json` de um jeito que
bateu com um padrão "parece instrução embutida", então o sistema neutralizou
tags de controle antes de me entregar o resultado — uma proteção contra
prompt injection vinda de saída de tool/subagente. Nesse caso era falso
positivo (o conteúdo era só a explicação do hook), mas mostra que a saída de
um subagente é tratada como **dado**, não como comando, mesmo dentro do
próprio Claude Code.

## Por que isso importa

- **Paralelismo real**: as duas pesquisas rodaram ao mesmo tempo, não uma
  depois da outra — mais rápido quando as tarefas são independentes.
- **Contexto principal protegido**: eu não vi os passos intermediários de
  cada agente (comandos rodados, arquivos lidos) — só o resumo final de cada
  um chegou aqui.
- **Sem escalada de privilégio**: um subagente não ganha mais acesso do que
  o agente principal teria; as mesmas regras de permissão valem para ele.

## Quando usar (e quando não)

Use paralelismo de subagentes para pesquisa/exploração de partes
**independentes** de um problema (ex: "resuma o módulo A" + "resuma o módulo
B" ao mesmo tempo). Não use para tarefas sequenciais ou quando o passo 2
precisa do resultado do passo 1 — nesse caso, chame um agente, espere o
resultado, e só então decida a próxima chamada.
