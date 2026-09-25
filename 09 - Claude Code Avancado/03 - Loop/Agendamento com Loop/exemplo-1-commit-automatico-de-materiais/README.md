# Exemplo 1 — Commit automático de materiais novos

Um slash command que verifica se há arquivos não versionados no repositório
e, se houver, cria um commit descritivo — pensado para rodar em intervalos
via `/loop` enquanto novos PDFs/exemplos vão sendo adicionados às pastas do
curso.

## O comando

[`verificar-novos-materiais.md`](verificar-novos-materiais.md), que viveria
em `.claude/commands/verificar-novos-materiais.md` para ficar disponível
como `/verificar-novos-materiais`:

```markdown
---
description: Verifica se há arquivos novos não versionados no repositório e cria um commit descritivo para eles (sem dar push).
allowed-tools: Bash(git status:*), Bash(git add:*), Bash(git commit:*), Bash(git log:*)
---

(instruções: rodar git status, se não houver nada responder "Nada para
commitar." e parar; se houver, dar add só nos arquivos relevantes, commitar
com mensagem no padrão do repo, e nunca dar git push)
```

Pontos importantes:

- `allowed-tools` restringe às operações de `git status/add/commit/log` —
  o comando fisicamente não consegue rodar `git push` ou qualquer outro
  comando do shell.
- A instrução reforça duas vezes para **nunca** dar push: automação de
  commit é razoável, automação de push para um repositório remoto sem
  supervisão não é.

## Como isso se encaixa no `/loop`

```
/loop 20m /verificar-novos-materiais
```

A cada 20 minutos, se novos arquivos tiverem sido adicionados às pastas do
curso, o comando cria um commit local sozinho. Push continua manual.

## Teste end-to-end (sandbox isolado, headless)

Para não mexer no repositório real do curso, o teste rodou num repositório
git **temporário** (fora deste projeto), com o comando instalado em
`.claude/commands/` só ali dentro:

```bash
git init
echo "conteudo pdf fake" > Modulo-Teste/aula-nova.pdf   # arquivo novo, não versionado

claude -p "/verificar-novos-materiais" \
  --allowedTools "Bash(git status:*),Bash(git add:*),Bash(git commit:*),Bash(git log:*)"
```

**Resultado real obtido (1ª execução, com arquivo novo):**

> Commit criado localmente (`eaea704`): adicionou `Modulo-Teste/aula-nova.pdf`
> (novo material de aula) e `.claude/commands/verificar-novos-materiais.md`
> (comando de automação). Nenhum push foi feito.

Conferido com `git log --oneline` e `git status` no sandbox: commit criado,
working tree limpa, nenhum push executado (o repositório sandbox nem tinha
remoto configurado).

**Resultado real obtido (2ª execução, sem nada novo — testa a idempotência
que o `/loop` exige, já que ele roda o comando repetidamente):**

> Nada para commitar.

Nenhum commit vazio foi criado, como esperado.

## Por que isso importa

- **Idempotência**: rodar o comando várias vezes seguidas sem novidade não
  gera commits vazios nem barulho no histórico — essencial para algo
  reagendado em loop.
- **Tools restritas**: o `allowed-tools` do próprio comando é a rede de
  segurança contra um push acidental, além da instrução em texto.
- **Push continua manual**: decisão deliberada. Automatizar commit local é
  seguro e reversível (`git reset`); automatizar push para o remoto não é o
  tipo de coisa que deve rodar sem supervisão.

## Status

Testado apenas em repositório sandbox isolado. **Não foi instalado em
`.claude/commands/` deste projeto real, e nenhum `/loop` foi deixado
rodando** — é só material de referência/exemplo.
