# Exemplo 3 — Checagem periódica de padrão de pastas

Um slash command **somente leitura** que confere se as pastas de exemplo de
cada tema seguem a convenção `exemplo-N-descricao` com um `README.md`
dentro, e relata divergências — sem corrigir nada sozinho.

## O comando

[`checar-padrao-pastas.md`](checar-padrao-pastas.md), que viveria em
`.claude/commands/checar-padrao-pastas.md`:

```markdown
---
description: Confere se as pastas de exemplo dentro de cada tema seguem o padrão "exemplo-N-descricao" com um README.md dentro, e relata divergências (não corrige nada automaticamente).
allowed-tools: Bash(find:*), Read
---

(instruções: localizar subpastas de "<Tema> na Prática", checar nome e
README.md de cada uma, gerar relatório em português só com as que
divergem, e nunca editar/renomear nada)
```

Ponto importante: `allowed-tools` só libera `find` e `Read` — nem `Edit`
nem `Bash(mv:*)` estão disponíveis, então o comando **não tem como**
corrigir nada mesmo que "decidisse" fazer isso.

## Como isso se encaixa no `/loop`

```
/loop 1h /checar-padrao-pastas
```

Diferente dos exemplos 1 e 2 (que agem), este é pensado para só **avisar**
— o valor de rodar em loop é ter uma checagem de qualidade recorrente sem
precisar lembrar de rodar manualmente, mantendo a decisão de corrigir com
a pessoa.

## Teste end-to-end (sandbox isolado, headless)

Repositório temporário com duas pastas de tema (`Hooks na Pratica`,
`SubAgents na Prática`), cada uma com um exemplo correto
(`exemplo-1-...`, `exemplo-2-...` com README) e **uma pasta fora do
padrão** de propósito (`teste-rapido/`, sem número no nome e sem README):

```bash
claude -p "/checar-padrao-pastas" --allowedTools "Bash(find:*),Read"
```

**Resultado real obtido:**

> ## Relatório de conformidade
>
> Verifiquei as subpastas de **"SubAgents na Prática"** e **"Hooks na
> Pratica"**. Encontrei 1 divergência:
>
> ### ❌ `SubAgents/SubAgents na Prática/teste-rapido`
> - **Nome fora do padrão**: `teste-rapido` não segue o formato
>   `exemplo-N-descricao` (falta o prefixo `exemplo-` e o número).
> - **README.md ausente**: a pasta não contém nenhum arquivo `README.md`.
>
> ### ✅ Demais pastas — conformes
> - `SubAgents/SubAgents na Prática/exemplo-2-orquestracao-paralela` —
>   nome correto, tem README.md.
> - `Hooks/Hooks na Pratica/exemplo-1-som-ao-finalizar` — nome correto,
>   tem README.md.
>
> Nenhuma alteração foi feita (comando apenas de leitura/relatório).

A pasta fora do padrão foi encontrada corretamente, com os dois motivos
certos (nome e README ausente), sem falso positivo nas pastas conformes.
Conferido com `git status`/`ls` no sandbox depois da execução: nada foi
renomeado, movido ou criado.

## Por que isso importa

- **Comando de relatório ≠ comando de ação**: para checagens onde você quer
  manter controle manual da correção, restringir `allowed-tools` a
  ferramentas só de leitura (`find`, `Read`) é a garantia de que o `/loop`
  nunca vai "decidir" corrigir sozinho.
- **Complementa os exemplos 1 e 2**: nem tudo que roda em loop precisa
  agir — às vezes o valor é só a visibilidade recorrente.

## Status

Testado apenas em repositório sandbox isolado. **Não foi instalado em
`.claude/commands/` deste projeto real, e nenhum `/loop` foi deixado
rodando** — é só material de referência/exemplo.
