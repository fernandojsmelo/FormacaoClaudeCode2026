# Exemplo 2 — Bloquear comandos perigosos antes de executar

Hook `PreToolUse` que intercepta chamadas da tool `Bash` **antes** de rodarem.
O script recebe o JSON da chamada via stdin, checa o comando com uma regex e,
se achar um padrão destrutivo, retorna exit code `2` — isso faz o Claude Code
cancelar a execução e mostrar a mensagem de erro para o modelo/usuário.

## Como já está ativo neste projeto

O `.claude/settings.json` na raiz já registra este hook para o matcher `Bash`,
apontando para `.claude/hooks/block-dangerous.sh` (mesmo script deste exemplo).

## Padrões bloqueados

- `rm -rf /` (e variações com espaço/barra no final)
- `git push --force` (ou `--force` com `origin/main`/`origin/master`) para `main`/`master`
- `git reset --hard`

## Testado

```bash
# Bloqueado (exit 2):
echo '{"tool_input":{"command":"rm -rf /"}}' | bash block-dangerous.sh
echo '{"tool_input":{"command":"git push --force origin main"}}' | bash block-dangerous.sh

# Permitido (exit 0):
echo '{"tool_input":{"command":"ls -la"}}' | bash block-dangerous.sh
echo '{"tool_input":{"command":"rm -rf node_modules"}}' | bash block-dangerous.sh
```

Também testado end-to-end: pedir ao Claude Code para rodar `rm -rf /` real
resultou no bloqueio pelo hook, sem o comando chegar a executar:

```
PreToolUse:Bash hook error: [bash .claude/hooks/block-dangerous.sh]:
Bloqueado pelo hook PreToolUse: comando potencialmente destrutivo detectado (rm -rf /)
```

## Por que isso importa

Diferente de pedir "seja cuidadoso" no prompt, esse bloqueio é **determinístico**:
não depende do modelo decidir evitar o comando — o script veta antes de a tool
rodar, então funciona mesmo se o modelo "errar".

## Limitações (vale citar)

- É um filtro por regex sobre a string do comando — pode ser contornado por
  ofuscação (ex: variáveis, `$(...)`, comandos equivalentes não previstos).
  Serve como rede de segurança adicional, não como sandboxing completo.
- Ajuste os padrões da regex para o seu contexto (branches protegidas, paths
  sensíveis do seu projeto, etc.).
