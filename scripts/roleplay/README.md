# Conversão de Role plays para o tema escuro

Scripts para reconstruir os PDFs claros de `19 - Roles Plays/NN - Role play NN/` no padrão escuro do curso (o mesmo do Role play 35 em diante).

Cada role play tem dois PDFs de origem:

| Arquivo | Origem | Parser | Renderizador |
|---|---|---|---|
| `RolePlayNN.pdf` | Transcrição da Udemy (react-pdf) | `parse_rp.py` | `render_rp.py` |
| `ResumoRolePlayNN.pdf` | Impressão do Modo IA do Google (Chrome) | `parse_google.py` | `render_resumo.py` |

Os estilos ficam em `rp_style.css` (transcrição) e `res_style.css` (resumo). Os renderizadores leem esses arquivos da mesma pasta.

## Fluxo

```bash
D="19 - Roles Plays/NN - Role play NN"
W=/tmp/rpNN && mkdir -p $W            # pasta de trabalho fora do repositório
cp "$D"/*.pdf $W/                     # guarde os originais antes de sobrescrever

# 1. Extrair para markup editável (uma linha por bloco)
python3 scripts/roleplay/parse_rp.py     $W/RolePlayNN.pdf       $W/rpNN.txt
python3 scripts/roleplay/parse_google.py $W/ResumoRolePlayNN.pdf $W/resNN.txt

# 2. Ler o markup INTEIRO e corrigir à mão (ver "Correções típicas")

# 3. Renderizar
python3 scripts/roleplay/render_rp.py $W/rpNN.fixed.txt "$D/RolePlayNN.html" "Role Play NN" "body{font-size:9.8pt;line-height:1.47}"
python3 scripts/roleplay/render_resumo.py $W/resNN.fixed.txt $W/metaNN.json "$D/ResumoRolePlayNN.html"

# 4. Gerar o PDF (pipeline do CLAUDE.md) e conferir páginas e tema
google-chrome --headless --disable-gpu --no-sandbox --run-all-compositor-stages-before-draw \
  --virtual-time-budget=4000 --no-pdf-header-footer \
  --print-to-pdf="$PWD/$D/RolePlayNN.pdf" "file://$PWD/$D/RolePlayNN.html"
.venv/bin/python scripts/check_pdfs.py "$D"/*.pdf
```

O 4º argumento de `render_rp.py` (opcional) acrescenta CSS. Use para ajustar a fonte até o número de páginas ficar igual (ou próximo) ao original.

## Markup

Transcrição (`parse_rp.py`): `@title`, `@meta`, `@turn Nome|00:00` e, em cada turno, `p|`, `li|`, `h|`, além de blocos `code:` / `c| linha` / `endcode:` (mostra "Use o código com cuidado.") ou `endnote:` (sem a nota), `flow|` para fluxos com setas, `th|`/`tr|` para tabelas (células separadas por ` | `) e `end:` para "Fim da sessão".

Resumo (`parse_google.py`): `q|` (pergunta), `h|`/`h4|`, `p|`, `li|`, `n|` (item numerado) com `sub|`/`subli|` (subitens), `th|`/`tr|`, blocos `code:`, `diag|` e `t|` (linha crua que **precisa** ser resolvida à mão). Linhas `#cards` no fim listam textos de cards omitidos.

`metaNN.json` do resumo:

```json
{"rp": "NN", "h1": "Título", "lead": "Resumo de uma frase...",
 "byline": "Fernando Melo · data · Pesquisa no Modo IA do Google, hora",
 "secs": ["Título curto de cada pergunta, na ordem"],
 "foot": "Nota de rodapé sobre o que foi omitido",
 "body_css": "body{font-size:10.6pt;line-height:1.62}\ntable{break-inside:avoid}"}
```

`secs` precisa ter um item por pergunta (`q|`); o renderizador confere.

## Correções típicas (sempre lendo o texto inteiro antes)

- **Tabelas** saem com as células grudadas ("MecanismoO que faz..."): reescreva como `th|`/`tr|`.
- **Emojis** viram glifos quebrados na transcrição (`=d`, `<÷`, `¡`): recupere pelo resumo, que costuma ter os emojis certos. Troque 🎚️ por 🔧 e 📈 por 🚀 (renderizam quebrados).
- **"%", "+", "G" soltos** em linhas `t|` no resumo: devolva ao lugar ("100%", "Gatilho").
- **Itens que grudaram** ("...simultaneamente. 2. Fim da Caixa..."): separe em linhas.
- **Código**: o resumo corta as linhas à direita e a transcrição perde a indentação; use o texto completo da transcrição com indentação de 4 espaços, sem inventar linhas.
- **Negrito como código**: em algumas impressões o parser marca negrito como `<code>`; confira com uma imagem da página e troque por `<strong>`.
- Nunca resumir nem inventar conteúdo. Compare palavra por palavra com o original no fim.

## Recursos extras (Role plays 41 a 43)

- **`codigo_xml.py`** refaz os blocos de código da transcrição com o texto e o recuo exatos do PDF (o XML do `pdftohtml -xml -i` guarda o recuo que o `parse_rp.py` perde): `python3 scripts/roleplay/codigo_xml.py RolePlayNN.pdf rpNN.txt rpNN.codigo.txt`. Os blocos completos da transcrição servem depois para completar o código cortado à direita no resumo (mesma ordem; mantenha as linhas em branco do resumo).
- **Emojis do react-pdf** viram o caractere alto do surrogate (`=` para D83D, `<` para D83C, `>` para D83E) seguido do byte baixo em cp1252; emojis do plano básico viram só o byte baixo. Já vistos: `=€` 🚀, `<‰` 🎉, `=%` 🔥, `=Á` 📁, `>„` 🪄, `>Ÿ` 🪟, `<O` 🍏, `='` 🐧, `L` ❌, `³` ↳, `ñ` ⏱.
- **Byte nulo**: o `parse_rp.py` pode deixar um `\x00` num cabeçalho de turno partido; o `grep` passa a tratar o arquivo como binário. Corrija com Python, incluindo o `\x00` no padrão.
- **Diagramas em texto do resumo** perdem o recuo no `parse_google.py`. No XML, as linhas em `left=156` começam na margem do bloco e as em `left=166` têm um espaço a mais; case as linhas em sequência (não por dicionário, porque `│` e `▼` se repetem).
- **Seções só com links** ("Confira os principais resultados da Web..."): reproduza como `li| Título · <em>Fonte</em>`, montando o título pelos trechos da linha 33 px abaixo do nome da fonte no XML (ou no topo da página seguinte) e descartando as abas (Tudo, Imagens, Vídeos...) que caem na mesma altura.
- **Texto sobreposto** no original atrapalha o `seqdiff.py`; para a comparação final, extraia as palavras pelo XML de cada PDF.
