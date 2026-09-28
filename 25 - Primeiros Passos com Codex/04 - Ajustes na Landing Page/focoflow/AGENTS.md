# AGENTS.md — FocoFlow (landing page)

## Projeto
Landing page estática do FocoFlow, um app fictício de foco e produtividade.
Público: estudantes e profissionais que trabalham em blocos de foco (Pomodoro).

## Stack
- HTML5 + CSS3 puros, sem frameworks e sem etapa de build.
- Arquivos: `index.html` (estrutura), `styles.css` (estilo) e `script.js` (interações).
- Fontes via Google Fonts; nenhuma outra dependência externa.

## Convenções
- Todo o texto da página em português do Brasil.
- Cores e espaçamentos como variáveis CSS em `:root`.
- Classes em kebab-case (`.hero-title`, `.feature-card`).
- HTML semântico: `header`, `main`, `section`, `footer`.

- Mobile first: todo layout novo precisa funcionar de 360px a 1280px.
- Cores só via variáveis: o modo escuro redefine as mesmas variáveis.
- Acessibilidade: contraste AA, `aria-hidden` em ícones decorativos,
  foco visível e rótulo em todo campo de formulário.

## Como validar
- Pré-visualizar: `python3 -m http.server 8000` e abrir http://localhost:8000
- Conferir em 390px (celular), 768px (tablet) e 1280px (desktop).
- Conferir nos modos claro e escuro.
- Nenhuma rolagem horizontal em nenhuma largura.
