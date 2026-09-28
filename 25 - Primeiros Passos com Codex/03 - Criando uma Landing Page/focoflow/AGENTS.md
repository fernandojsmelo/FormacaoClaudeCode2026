# AGENTS.md — FocoFlow (landing page)

## Projeto
Landing page estática do FocoFlow, um app fictício de foco e produtividade.
Público: estudantes e profissionais que trabalham em blocos de foco (Pomodoro).

## Stack
- HTML5 + CSS3 puros, sem frameworks e sem etapa de build.
- Arquivos: `index.html` (estrutura) e `styles.css` (estilo).
- Fontes via Google Fonts; nenhuma outra dependência externa.

## Convenções
- Todo o texto da página em português do Brasil.
- Cores e espaçamentos como variáveis CSS em `:root`.
- Classes em kebab-case (`.hero-title`, `.feature-card`).
- HTML semântico: `header`, `main`, `section`, `footer`.

## Como validar
- Pré-visualizar: `python3 -m http.server 8000` e abrir http://localhost:8000
- Conferir a página em largura de desktop (1280px) antes de concluir.
