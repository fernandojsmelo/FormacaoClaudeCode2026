# FormacaoClaudeCode2026

Material da Formação Claude Code 2026: módulos numerados (`NN - Nome do Módulo`), cada um com aulas em PDF no tema escuro, com o HTML fonte e os projetos de apoio ao lado. As regras de conteúdo e de design estão no [CLAUDE.md](CLAUDE.md).

## Configuração do repositório

Faça isto uma vez em cada clone para que as proteções automáticas funcionem.

**Pré-requisitos:** Python 3, Google Chrome (para gerar PDFs) e o `poppler-utils` (`pdftoppm`, `pdfinfo`, `pdftotext`). No Ubuntu, instale o último com `sudo apt install poppler-utils`.

```bash
# 1. Ambiente Python com as dependências dos scripts
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# 2. Ativar os hooks versionados em .githooks/
git config core.hooksPath .githooks

# 3. Conferir: deve terminar com "0 fora do padrão"
.venv/bin/python scripts/check_pdfs.py --all
```

## O que os hooks garantem

| Hook | Quando roda | O que bloqueia |
| --- | --- | --- |
| `pre-commit` | a cada `git commit` | notebook `.ipynb` alterado sem o `.md` de apoio regenerado |
| `pre-push` | a cada `git push` | PDF enviado claro ou com margens brancas (fora do tema escuro) |

Em um caso excepcional, dá para pular com `--no-verify`, mas corrigir é sempre o caminho certo.

## Scripts

| Script | Para que serve |
| --- | --- |
| `scripts/check_pdfs.py` | Verifica se os PDFs seguem o tema escuro (`--all` para o repositório inteiro) |
| `scripts/fill_pdf_margins.py` | Pinta margens brancas de PDFs com a cor de fundo do tema, sem alterar o conteúdo |
| `scripts/notebook_to_pdf.py` | Gera o `.md` e o `.pdf` de apoio a partir de um notebook `.ipynb` |
