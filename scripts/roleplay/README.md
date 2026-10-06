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

## Ferramentas auxiliares (Role plays 44 a 47)

Rode na pasta de trabalho com `PYTHONPATH=scripts/roleplay` (os módulos se importam entre si). Em `exemplos/` ficam os scripts de correção e os `metaNN.json` usados nos Role plays 41 a 47, como referência de uso.

| Script | Para quê |
|---|---|
| `xmlq.py` | `load(x.xml)` devolve `(página, top, left, fonte, texto)` de cada pedaço do XML do `pdftohtml -xml -i`; `python3 xmlq.py x.xml "trecho"` mostra o contexto. |
| `emoji_rp.py` | Acha os emojis quebrados nos títulos da transcrição (react-pdf), escolhe o emoji pelo resumo e aplica em `h|`/`p|`/`li|`. Os que aparecem como "padrão" ou "??" precisam de decisão manual. |
| `emo_res.py` | Lista os emojis do XML do resumo (fonte NotoColorEmoji) com o contexto. É a fonte de verdade para os emojis que o parser perde dentro do código. |
| `fences.py` | `fences()` transforma trechos ```` ``` ```` digitados na conversa em blocos de código com o recuo do XML; `recuo()` devolve o recuo do XML às linhas `c|`; `nulos()` conserta turnos partidos por `\x00`. |
| `rpfix.py` | Classe `Fix` para o markup do resumo: `rep`, `block`, `pct` ("100 %"), `headings` (títulos que perderam palavras em fonte de código), `code_xml` (código não presente na transcrição: recuo e emojis pelo XML), `code_from` (código completo pela transcrição), `numbered`, `t_to_h`, `save`. |
| `links_google.py` | Remonta as listas "Confira os principais resultados da Web" como `li| Título · <em>Fonte</em>`. |
| `cmp_xml.py` | Diff de palavras entre o original e o novo, pelo XML. |
| `sheet.py` | Folha de contato do PDF para a checagem visual. |
| `build_pdf.sh` / `render_resumo_pdf.sh` | Gera o PDF pelo Chrome e mostra o número de páginas; o segundo também renderiza o resumo com o CSS dado. |

Lições destes role plays:

- O `codigo_xml.py` agora casa os blocos **pelo conteúdo** (casar por ordem deslocava os blocos quando o markup não reconhecia algum, por exemplo com o rótulo "python" grudado no fim da frase).
- Emojis do plano básico (BMP) perdem o byte alto: `¡` = ⚡ ou ➡, `”` = ⚔, `(` = ✨, `L` = ❌; os de byte baixo invisível somem ou viram espaço (⚠, ✅, ⬅). Decodifique pelo contexto do resumo e nunca invente: se não houver fonte, remova o glifo e registre.
- Troque 📈 por 🚀 (renderiza quebrado neste ambiente).
- Linhas de rodapé/cabeçalho de página podem vazar para dentro de um bloco de código da transcrição; remova-as.
- No resumo, o código que não está na transcrição fica cortado à direita (como no original), mas com o recuo e os emojis do XML; registre isso no `foot`.
- Gráficos do original podem ser redesenhados em SVG com os mesmos eixos e legendas (ver `exemplos/fix_res44.py`).
- O `render_resumo.py` mantém a numeração de listas interrompidas por código (`<ol start>`), e o `render_rp.py` aceita `**negrito**` e `⏎` (quebra de linha) nas células de tabela.

## Role plays 48 a 51

- **`faltando.py rpNN.c.txt rpNN.fixed.txt`** lista as linhas do markup bruto que não aparecem no markup final. Linhas muito recuadas podem sumir do XML (texto fora da margem); confira cada ausência com o `pdftotext -layout` e recoloque à mão quando for conteúdo real (ver `exemplos/fix48.py`).
- **`fences.recuo(xml, s)`** devolve o recuo dos blocos de código pelo XML; `para_code()` (em `exemplos/fix49.py`) transforma blocos "csv"/"python" que o parser leu como parágrafos (os que terminam em "Use o código com cuidado.") em blocos `code:`.
- `Fix.headings(pdf)` já reconstrói títulos com palavras em fonte mono (ex.: "O que é esse <code>index=False</code>?"); confira antes de corrigi-los à mão.
- `Fix.code_from(..., langs=(..., 'csv'))` aceita blocos com rótulo `csv`/`text` quando eles também existirem na transcrição.
- Resumos que começam no meio de uma lista de links: abra a seção com a pergunta do cabeçalho da página 1, liste só os links visíveis e registre isso no `foot` (ver `exemplos/meta50.json`).
- Os exemplos `fix48`–`fix54`, `fix_res48`–`fix_res54` e `meta48`–`meta54` estão em `exemplos/`.
- Prompts colados na conversa saem quebrados pela largura da página: no XML, a linha quebrada chega à margem (largura ≥ 740). `exemplos/fix53.py` junta só essas, sem grudar itens numerados ou com marcador; confira com o resumo, que mostra cada linha original numa linha só.

## Role plays 55 a 59

- **`codigo_xml.py`** refaz sozinho os blocos de código da transcrição (recuo e comentários `#`/`//` que viravam título). Quando o rótulo da linguagem (`python`) não aparece no markup, insira uma linha `p| python` antes do bloco e rode de novo (ver o Role play 55).
- **`falta_linhas.py original.pdf markup.txt`** compara o `pdftotext` do PDF original com o markup e lista linhas perdidas pelo parser, como a primeira linha de uma página (no Role play 56 sumiu um item de lista inteiro). Ignore cards de links e rodapés.
- Tabelas do resumo e da transcrição saem coladas ("MecanismoO que faz..."): reescreva com `th|`/`tr|`, usando `⏎` para quebras dentro da célula (ver `exemplos/fix57.py`). Ao trocar um trecho do markup entre dois marcadores, confira se não há conteúdo entre eles (o Role play 57 perdeu um parágrafo assim).
- Diagramas em texto (`┌─┐`) cortados à direita no resumo: refaça a caixa à mão e complete com o texto da transcrição (ver `exemplos/fix_res55.py`); registre isso no `foot`.
- Emojis de texto sem seletor de variação (🗄 🛠 🗺 🛡 ⚖ ✈ ⚙ ⚠ ✉ 🕵) aparecem como quadrado no Chrome deste ambiente: acrescente `U+FE0F` depois deles no HTML antes de gerar o PDF.
- O `%` e o `+` de uma linha (`t| %`, `t| +`) voltam ao lugar com `Fix.pct()` ou à mão (`Python + PostgreSQL`).
- Os exemplos `fix55`–`fix59`, `fix_res55`–`fix_res59` e `meta55`–`meta59` estão em `exemplos/`.
