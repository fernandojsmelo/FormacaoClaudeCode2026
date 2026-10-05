# Modelos das aulas (tema escuro)

Kit para criar decks de aula e manuais no padrão do curso (design system do `CLAUDE.md`), sem recriar o CSS a cada aula. Foi tirado das aulas dos módulos 34 e 35.

| Arquivo | Para quê |
|---|---|
| `head_lesson.html` | Cabeçalho do **deck de aula** (paisagem 960×540pt): tokens, componentes e extras (`.promptbox`, `.code`, `.shot`, `.flow`, `.kbd`, `.sim`) |
| `head_manual.html` | Cabeçalho do **manual A4** (retrato): `.header`, `.toc`, `.sec`/`.brk`, `.osbar` por sistema |
| `body_exemplo.html` | Corpo de deck com capa, seções, tela ilustrativa, passos, prompt, tabela, fluxo, quiz e encerramento |
| `body_manual_exemplo.html` | Corpo de manual com sumário, visão geral, seção por sistema e checklist |
| `mock_exemplo.html` | Tela ilustrativa simples (mockup autocontido de 1200×560) |
| `mock_base.css` | Peças das telas do Cursor (janela, explorer, editor com diff, painel do agente, campo do chat, menus, configurações, ícone de microfone). O mockup inclui com o marcador `<!--MOCK_BASE-->` |
| `telas/` | Fontes das telas usadas nas aulas (`mNN_aXX_nome.html`), para renderizar de novo. As prévias `.png` ficam fora do Git |
| `preview_mock.py` | Gera a prévia `.png` de um mockup e avisa se ele transbordou de uma página |
| `incluir_codigo.py` | Troca `{{CODE:arquivo:ini-fim}}` no corpo pelas linhas reais do arquivo (escapadas, sem o recuo comum, comentários em destaque), para o código do deck ser o mesmo que foi testado |
| `build_aula.py` | Junta cabeçalho + corpo, embute as telas, gera `.html` autocontido e `.pdf`, confere páginas e monta a folha de contato |

## Fluxo de uma aula

```bash
A="36 - Funcionalidades de IA e MCP no Cursor/01 - Agentes no Cursor"
W=~/.cache/formacao-aulas/aula && mkdir -p $W   # fora do /tmp: o scratchpad é apagado
cp scripts/aulas/body_exemplo.html $W/body.html     # escreva o conteúdo aqui
cp scripts/aulas/mock_exemplo.html $W/tela.html     # se a aula tiver tela ilustrativa

python3 scripts/aulas/build_aula.py $W/body.html "$A/Agentes_no_Cursor.html" \
  --title "Agentes no Cursor" --img TELA=$W/tela.html --sheet $W
.venv/bin/python scripts/check_pdfs.py "$A"/*.pdf
```

- `--img NOME=arquivo` troca `{{IMG_NOME}}` no corpo; aceita `.html` (mockup, renderizado a 144 DPI) ou `.jpg`. Pode repetir.
- `--manual` usa o cabeçalho A4.
- O script avisa se o número de páginas do deck for diferente do número de `<section class="block">`: alguma seção transbordou e precisa ser enxugada.
- `--sheet DIR` salva `DIR/<nome>_sheet.png`. Olhe a folha **sempre** (capa, meio e fim), como pede o `CLAUDE.md`.

## Código de projetos nos slides

```bash
python3 scripts/aulas/incluir_codigo.py corpo.html corpo.final.html pasta_dos_projetos
python3 scripts/aulas/build_aula.py corpo.final.html "<aula>/Nome.html" --title "…" --img APP=print.jpg
```

Nas aulas de projeto, o código de referência fica testado na pasta `projeto/` da aula, e os slides citam trechos dele com `{{CODE:…}}`. Rode os testes antes de renderizar.

`{{OUT:arquivo.py}}` roda o script e coloca no slide a **saída real**, inclusive mensagens de erro (com caminho curto, como no terminal). Se existir `arquivo.in` ao lado, ele vira a entrada do `input()`, e cada resposta aparece logo depois da pergunta, como alguém digitando. Foi assim que as aulas do módulo 37 (exemplos em `exemplos/`) foram feitas. Mantenha as linhas dos exemplos com até 64 caracteres para caberem na coluna de código.

## Telas ilustrativas

```bash
cp scripts/aulas/telas/m36_a01_agent.html scripts/aulas/telas/mNN_aXX_nova.html   # partir de uma tela parecida
python3 scripts/aulas/preview_mock.py scripts/aulas/telas/mNN_aXX_nova.html        # conferir a prévia .png
python3 scripts/aulas/build_aula.py corpo.html "<aula>/Nome.html" --title "…" --img TELA=scripts/aulas/telas/mNN_aXX_nova.html
```

Prints **reais** (de um app rodando) também entram por `--img NOME=print.jpg`; na legenda, diga "print real" em vez de "reprodução ilustrativa".

Para trocar só a imagem de uma aula já pronta, sem refazer o corpo: substitua o `data:image/jpeg;base64,…` no `.html` pelo resultado de `build_aula.image_uri()` e renderize o PDF de novo.

## Onde guardar o trabalho

O scratchpad da sessão (`/tmp/claude-…`) **é apagado sem aviso**. Guarde os corpos e rascunhos numa pasta persistente fora do repositório, por exemplo `~/.cache/formacao-aulas/mNN/`. O `.html` final, salvo ao lado do `.pdf`, é a fonte da verdade da aula.

## Convenções das aulas

- Capa com `eyebrow` "Módulo · Aula N", `h1` com `<em>`, `lead`, `chips` e `byline` com as fontes e o mês da consulta.
- Seções numeradas (`.pagehead` com rótulo e `01`, `02`...), uma por página; 10 a 17 seções.
- Telas são **reprodução ilustrativa** (dizer isso na legenda); números de exemplo marcados como tal.
- Penúltima seção: quiz de 4 perguntas (`.qcard`). Última: encerramento com "Próxima aula → NN · Nome" (ou "Fim do módulo").
- Aulas "Instalando", "Configurando" ou "Instalando e Configurando" ganham também um **manual A4** separado com Windows, Linux e macOS.
- Fatos (atalhos, menus, preços, versões) vêm da documentação oficial consultada na hora; a do Cursor está em `https://cursor.com/llms.txt` (páginas em `.md`).
- Emojis 🎚️ e 📈 renderizam quebrados: use 🔧 e 🚀.
- Versionar o `.html` gerado ao lado do `.pdf`; para editar, mude o `.html` e renderize de novo.
