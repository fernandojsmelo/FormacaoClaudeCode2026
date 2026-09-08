# Exemplo 1 — Som ao finalizar a resposta

Hook simples: toca um som sempre que o Claude termina de responder (evento `Stop`).

## Como já está ativo neste projeto

O arquivo `.claude/settings.json` na raiz do projeto já tem essa configuração — é só
usar o Claude Code normalmente que o som toca ao fim de cada resposta.

## Config usada (Linux)

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "canberra-gtk-play -i complete 2>/dev/null"
          }
        ]
      }
    ]
  }
}
```

`canberra-gtk-play -i complete` toca o som "complete" do tema de sons do freedesktop
(pacote `libcanberra-gtk-module` / `libcanberra-gtk3-module`, já presente neste sistema).

## Alternativas por sistema operacional

- **macOS**: `afplay /System/Library/Sounds/Glass.aiff`
- **Linux com PulseAudio**: `paplay /usr/share/sounds/freedesktop/stereo/complete.oga`
- **Linux genérico (sem canberra)**: `ffplay -nodisp -autoexit -loglevel quiet /usr/share/sounds/freedesktop/stereo/complete.oga`

## Testar isoladamente

```bash
canberra-gtk-play -i complete
```
