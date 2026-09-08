#!/bin/bash
input=$(cat)
command=$(echo "$input" | jq -r '.tool_input.command // ""')

if echo "$command" | grep -qE 'rm[[:space:]]+-rf[[:space:]]+/([[:space:]]|$)|push[[:space:]]+--force.*\b(main|master)\b|--force.*origin/(main|master)|git[[:space:]]+reset[[:space:]]+--hard'; then
  echo "Bloqueado pelo hook PreToolUse: comando potencialmente destrutivo detectado ($command)" >&2
  exit 2
fi

exit 0
