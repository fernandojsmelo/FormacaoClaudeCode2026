# Formação Claude Code 2026 — CLAUDE.md

Curso em PDF organizado em módulos numerados (`NN - Nome do Módulo`), cada um com subpastas de aula também numeradas (`NN - Nome da Aula`). Todo PDF do curso segue o **tema escuro** definido abaixo — é o padrão obrigatório para qualquer PDF novo ou editado neste repositório.

## Antes de qualquer `git push` neste repositório

Sempre, antes de subir para o Git, verificar se algum PDF está fora do padrão de tema escuro. Não confiar apenas na inspeção visual de amostras — rodar a varredura em todos os PDFs do repositório:

```bash
.venv/bin/python scripts/check_pdfs.py --all
```

O script renderiza a primeira página de cada PDF a 20 DPI e aponta dois problemas:

- **PDF claro** — brilho médio acima de ~150. O normal do tema escuro fica entre ~20 e ~55 nessa métrica (a média sobe com o texto claro e o anti-aliasing em baixa resolução); não confundir isso com um PDF fora do padrão. Precisa ser reconstruído (passos abaixo).
- **Margens brancas** — conteúdo escuro, mas bordas da página claras. Corrigir com `.venv/bin/python scripts/fill_pdf_margins.py <arquivo.pdf>`, que pinta as margens com `--bg` por baixo do conteúdo, sem alterar texto, páginas ou links.

O hook versionado `.githooks/pre-push` roda a mesma checagem automaticamente, só nos PDFs adicionados, alterados ou renomeados nos commits do push, e bloqueia o envio se encontrar problema (ignorar só em caso excepcional com `git push --no-verify`). Ele usa o `.venv` do projeto: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`. A ativação é a mesma do pre-commit: `git config core.hooksPath .githooks`. O hook não dispensa a varredura completa acima, que pega também PDFs antigos.

Ao encontrar um PDF fora do padrão:
1. Extrair o texto completo com `pdftotext -layout` e ler por inteiro antes de reescrever — nunca inventar ou resumir conteúdo.
2. Reconstruir em HTML usando o design system abaixo, mantendo a contagem de páginas do original (ou o mais próximo possível).
3. Renderizar com o pipeline abaixo, validar contagem de páginas com `pdfinfo`, e conferir visualmente pelo menos a capa, uma página de conteúdo intermediária e a página final.
4. Salvar sobrescrevendo o arquivo original no mesmo caminho.

## Design system dos PDFs (tema escuro)

### Tokens de cor (CSS custom properties)

```css
:root{
  --bg:#171310; --surface:#1F1A15; --surface-2:#271F18;
  --border:#3A2F24; --border-2:#4A3C2D;
  --ink:#F3ECE2; --muted:#AE9F8C;
  --accent:#DE8B62; --accent-ink:#F0AB86; --accent-soft:#3A281F;
  --good:#8FC0A8; --good-soft:#243128;
  --warn:#DDB662; --warn-soft:#362A16;
  --danger:#DE8A80; --danger-soft:#3A2321;
  --mono:'IBM Plex Mono', ui-monospace, monospace;
  --display:'Fraunces', Georgia, serif;
  --body-f:'Inter', system-ui, sans-serif;
}
```

Fontes via Google Fonts:
`https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap`

### Duas famílias de formato de página

- **Obrigatório nas duas famílias:** incluir `background:#171310` dentro do `@page` (ex.: `@page{ size:A4; margin:15mm; background:#171310 }`). Sem isso o Chrome imprime as margens em branco, mesmo com o `body` escuro.
- **Lesson** (aulas com quiz, landscape): `@page{ size:960pt 540pt; margin:.5in .55in }`, `.wrap{max-width:920px}`, `section.block{page-break-before:always}`. Usado para decks de aula com capa, seções numeradas (01, 02...), quiz de fixação e encerramento com "Próxima aula →".
- **Resumo/Relatório** (A4 portrait): `@page{ size:A4; margin:14mm–16mm }`, `.wrap{max-width:720–740px}`. Usado para resumos de módulo, relatórios de sessão/projeto e documentação técnica.

### Vocabulário de componentes reutilizáveis

- `.header`/`.cover` + `.eyebrow` (mono, uppercase, cor accent-ink) + `.lead` + `.byline` + `.chips` (pills com `--accent-soft`)
- `.grid.g2/g3/g4/g5` + `.card`/`.stat` (`.k`/`.v` para indicador/valor)
- `.table-wrap table` com `th` em `--surface-2`/mono/uppercase e `td` com borda superior `--border`
- `.term`/`.promptbox` — blocos de código/prompt em mono sobre `#100D0A`, com `.c` para comentários
- `.callout` (variantes default/`good-soft`/`warn-soft`/`danger-soft`)
- `.bullets` (marcador `●` customizado) e `.checklist` (marcador `✓` em `--good`)
- `.qcard` — quiz: `.qtext`, `.opts` (grid 2 colunas), `.answer` (fundo `good-soft`)
- `.expand` — princípios/técnicas expansíveis (título + `+`)
- `.steps`/`.step` — passos numerados com badge circular em `--accent`
- `.filelist`/`.source`/`.foot` — rodapés e índices de arquivo

### Pipeline de renderização

```bash
google-chrome --headless --disable-gpu --no-sandbox \
  --run-all-compositor-stages-before-draw --virtual-time-budget=4000 \
  --no-pdf-header-footer --print-to-pdf="<DESTINO.pdf>" "file://<ORIGEM.html>"
```

Validar com `pdfinfo` (contagem de páginas/tamanho) e `pdftoppm -png -f N -l N -r 80-90 <pdf> <prefixo>` + inspeção visual antes de considerar o arquivo pronto. Nunca pular a checagem visual.

Ao criar um PDF novo a partir de HTML, versionar o `.html` fonte ao lado do `.pdf`, com o mesmo nome base (ex.: `A_Interface_Codex_Cloud.html` + `.pdf`). Para editar uma aula, altere o HTML e renderize de novo — nunca reconstrua do zero a partir do PDF. O HTML precisa ser autocontido (CSS inline; só as fontes vêm do Google Fonts).

### Armadilha conhecida

Os emojis 🎚️ e 📈 renderizam quebrados neste ambiente Chrome/fontes — substituir por 🔧 e 🚀 respectivamente sempre que aparecerem no conteúdo original.

### Material de apoio gerado a partir de notebooks

Aulas com notebook `.ipynb` têm ao lado um `.md` (células sem saídas) e um `.pdf` (A4, tema escuro) gerados dele. Sempre que um notebook mudar, regenerar os dois com:

```bash
.venv/bin/python scripts/notebook_to_pdf.py "<módulo>/<aula>/notebook.ipynb" [...]
```

O notebook é a fonte da verdade — nunca editar o `.md`/`.pdf` à mão. Dependências: `.venv/bin/pip install -r requirements.txt`. Depois, fazer a mesma checagem visual do pipeline acima.

O hook versionado `.githooks/pre-commit` bloqueia commits que alteram um `.ipynb` sem incluir o `.md` correspondente. Ativar uma vez por clone com `git config core.hooksPath .githooks`. Usar `git commit --no-verify` só quando a mudança no notebook não afeta o material.

## Estrutura e numeração

Módulos de nível raiz numerados `NN - Nome` (01 a 22+) por ordem cronológica real do curso (evidência de data de criação de arquivos nunca editados — não confiar em mtime de PDFs já convertidos, pois é sobrescrito a cada conversão). Subpastas de aula dentro de cada módulo seguem o mesmo padrão de numeração, refletindo a ordem pedagógica. Ao adicionar um novo módulo, numerar sequencialmente a partir do maior número existente.
