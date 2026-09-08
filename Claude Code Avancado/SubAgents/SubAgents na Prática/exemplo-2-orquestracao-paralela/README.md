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

## O teste que fizemos

Disparamos duas tarefas de pesquisa sobre este mesmo repositório, ao mesmo
tempo, cada uma em um subagente `Explore` isolado:

- **Agente A**: resumir todos os exemplos práticos de Hooks em
  `Hooks/Hooks na Pratica/*`.
- **Agente B**: listar tudo configurado dentro de `.claude/` (subagentes,
  hooks, settings.json).

### Resultado do Agente A (sucesso)

> Existem dois exemplos práticos de Hooks:
>
> **1. exemplo-1-som-ao-finalizar** — evento `Stop`. Toca um som
> (`canberra-gtk-play -i complete`) sempre que o Claude termina de responder.
>
> **2. exemplo-2-bloquear-comandos-perigosos** — evento `PreToolUse` com
> matcher `Bash`. Detecta padrões destrutivos (`rm -rf /`, `git push --force`
> para main/master, `git reset --hard`) e retorna `exit 2` para bloquear a
> tool antes de rodar.

### Resultado do Agente B (bloqueado — e isso também é o exemplo)

```
Permission for this action was denied by the Claude Code auto mode
classifier. Reason: Blocked by classifier.
```

O subagente tentou ler arquivos dentro de `.claude/` via Bash e o
**classificador de auto mode** vetou a ação — o mesmo mecanismo de segurança
que se aplicaria se fosse o agente principal chamando a tool diretamente.
Subagentes **não pulam** as camadas de permissão do Claude Code; eles herdam
as mesmas regras. Tivemos que completar aquela pesquisa manualmente
(`ls .claude/agents .claude/hooks` + `cat .claude/settings.json`).

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
