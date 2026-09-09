# Exemplo 2 — Atualização automática do índice no README

Um slash command que escaneia as pastas de nível superior do projeto e
mantém uma lista de conteúdo sempre em dia dentro do `README.md`, entre dois
marcadores fixos.

## O comando

[`atualizar-indice-readme.md`](atualizar-indice-readme.md), que viveria em
`.claude/commands/atualizar-indice-readme.md`:

```markdown
---
description: Escaneia as pastas de nível superior do projeto e atualiza a lista de conteúdo entre os marcadores INICIO-INDICE/FIM-INDICE do README.md.
allowed-tools: Bash(ls:*), Read, Edit
---

(instruções: listar pastas de topo, ler o README, substituir só o trecho
entre <!-- INICIO-INDICE --> e <!-- FIM-INDICE -->, e não editar nada se a
lista já estiver igual)
```

O README precisa ter os marcadores já presentes:

```markdown
<!-- INICIO-INDICE -->
<!-- FIM-INDICE -->
```

## Como isso se encaixa no `/loop`

```
/loop 1h /atualizar-indice-readme
```

Toda vez que uma pasta de tema nova é criada (como aconteceu com `Loop/`
nesta sessão), o índice do README se atualiza sozinho na próxima rodada.

## Teste end-to-end (sandbox isolado, headless)

Repositório temporário com 3 pastas (`Hooks`, `SubAgents`, `Loop`) e um
README com os marcadores vazios:

```bash
claude -p "/atualizar-indice-readme" --allowedTools "Bash(ls:*),Read,Edit"
```

**Resultado real obtido (1ª execução, índice vazio → preenchido):**

> README.md atualizado. O índice estava vazio e agora lista as 3 pastas de
> nível superior em ordem alfabética: **Hooks**, **Loop** e **SubAgents**
> (todas novas entradas, nenhuma removida).

README resultante, conferido em disco:

```markdown
<!-- INICIO-INDICE -->
- Hooks
- Loop
- SubAgents
<!-- FIM-INDICE -->
```

**Resultado real obtido (2ª execução, nada mudou — testa idempotência):**

Na primeira tentativa a resposta veio parcialmente em inglês
("The three top-level folders are Hooks, Loop, SubAgents — exactly matching
the current index." seguido de "**Índice já está atualizado.**"). Ajustei o
comando para exigir explicitamente resposta em português e resposta curta,
e testei de novo depois de criar uma 4ª pasta (`Agendamento com Loop`):

> Índice atualizado: a pasta "Agendamento com Loop" entrou na lista (as
> demais — Hooks, Loop, SubAgents — permaneceram).

README final no sandbox, confirmando que só o item novo foi acrescentado e
o resto do arquivo ficou intacto:

```markdown
<!-- INICIO-INDICE -->
- Agendamento com Loop
- Hooks
- Loop
- SubAgents
<!-- FIM-INDICE -->
```

## Por que isso importa

- **Edição cirúrgica**: os marcadores `INICIO-INDICE`/`FIM-INDICE` limitam
  onde o comando pode editar — ele não tem liberdade para mexer no resto do
  README.
- **Idempotência**: sem novidade, não edita o arquivo (evita diffs vazios
  e ruído em cada rodada do loop).
- **Pegadinha real encontrada no teste**: a instrução original não fixava o
  idioma da resposta, e numa das rodadas o resumo saiu em inglês. Fica como
  lição — para um comando que roda em `/loop` sem supervisão, vale ser
  explícito até sobre o idioma da saída, não só sobre a tarefa em si.

## Status

Testado apenas em repositório sandbox isolado. **Não foi instalado em
`.claude/commands/` deste projeto real, e nenhum `/loop` foi deixado
rodando** — é só material de referência/exemplo.
