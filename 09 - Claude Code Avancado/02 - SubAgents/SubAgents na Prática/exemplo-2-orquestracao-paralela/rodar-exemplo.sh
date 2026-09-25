#!/usr/bin/env bash
# Reproduz o exemplo de orquestração paralela de subagentes: dispara duas
# pesquisas independentes (Explore) na mesma resposta e depois consolida.
#
# Uso: ./rodar-exemplo.sh   (execute a partir desta pasta)
set -euo pipefail

cd "$(dirname "$0")/../../.."  # raiz de "Claude Code Avancado"

PROMPT='Dispare dois subagentes Explore em paralelo, na mesma resposta (mesmo
bloco de tool calls, sem depender um do outro):

Agente A: resuma cada exemplo prático de Hooks em "Hooks/Hooks na Pratica/*"
— qual evento de hook usa, o que o script faz, como está registrado em
settings.json. Máximo 150 palavras, em português.

Agente B: liste tudo configurado dentro de ".claude/" (subagentes em
.claude/agents/, hooks em .claude/hooks/, settings.json) e resuma o
propósito de cada item. Máximo 150 palavras, em português.

Depois que os dois voltarem, junte os dois resumos em uma resposta única.'

claude -p "$PROMPT" \
  --allowedTools "Task,Read,Grep,Glob,Bash(ls*),Bash(cat*),Bash(find*)"
