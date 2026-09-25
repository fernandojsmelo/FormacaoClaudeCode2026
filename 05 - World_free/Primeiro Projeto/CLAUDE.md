# Word Frequency

## Descrição

Aplicação Tier 1 (Iniciante) que conta a frequência de palavras em um bloco de
texto. O usuário cola um texto (até 2048 caracteres) em uma caixa de input,
clica em "Translate" e vê uma tabela com cada palavra única e sua contagem de
ocorrências, ordenada de forma decrescente por frequência.

Especificação completa das user stories em [App.md](App.md).

## Stack

- **Front-end:** HTML + CSS + JavaScript vanilla (sem framework na Fase 1-4).
- **Gráfico (Fase 5, bônus):** Chart.js.
- **Backend (Fase 6, bônus):** Node.js + Express, apenas para buscar conteúdo
  de URLs externas (evita CORS) usando `cheerio` para extrair texto do HTML.
- Sem banco de dados — toda a lógica de contagem roda no cliente, em memória.

## Fases de desenvolvimento

1. **Estrutura estática** — layout com input de texto, botão "Translate" e
   tabela vazia. Validação de limite de 2048 caracteres.
2. **Lógica de contagem (core)** — tokenização de palavras (normalização de
   case, remoção de pontuação), contagem de ocorrências, renderização da
   tabela sem ordenação.
3. **Ordenação e validações** — ordenar tabela por frequência decrescente,
   mensagem de erro para input vazio, tratamento de edge cases (múltiplos
   espaços, quebras de linha, acentuação).
4. **Polimento de UX** — estilização, responsividade, feedback visual ao
   clicar em "Translate".
5. **Bônus: gráfico** — bubble/column chart com Chart.js a partir dos dados já
   calculados.
6. **Bônus: análise via URL** — endpoint backend para buscar e extrair texto
   de uma URL, campo alternativo de input (texto vs. URL), tratamento de erros
   de rede/URL inválida.

## Estrutura de pastas

```
World_free/
├── App.md              # Especificação original (user stories)
├── CLAUDE.md            # Este arquivo
├── index.html            # Entry point (Fases 1-5)
├── css/
│   └── style.css
├── js/
│   ├── main.js           # Bootstrap e event listeners
│   ├── wordFrequency.js   # Lógica pura de tokenização e contagem
│   └── chart.js           # Renderização do gráfico (Fase 5)
├── tests/
│   └── wordFrequency.test.js
└── server/                # Somente Fase 6 (bônus URL)
    ├── index.js
    └── package.json
```

## Comandos para rodar e testar

**Rodar (Fases 1-5, front-end estático):**
```bash
npx serve .
# ou
python3 -m http.server 8000
```

**Testar (lógica de contagem):**
```bash
npm test
```

**Rodar o backend (Fase 6, bônus):**
```bash
cd server
npm install
npm start
```

## Convenções de código

- **JavaScript vanilla, ES modules** (`import`/`export`), sem transpiladores
  nas Fases 1-5.
- **Nomenclatura:** `camelCase` para variáveis e funções, `PascalCase`
  reservado para classes (se houver).
- **Separação de responsabilidades:** lógica pura de contagem
  (`wordFrequency.js`) não deve manipular o DOM — recebe uma string e retorna
  dados. `main.js` cuida de eventos e renderização.
- **Sem comentários óbvios** — só comentar o que não é evidente pelo nome das
  funções/variáveis (ex.: por que uma regex específica foi escolhida).
- **Indentação:** 2 espaços.
- **Strings:** aspas simples, exceto em template literals.
- **Testes:** um teste por comportamento (tokenização, contagem, ordenação,
  edge cases de pontuação/espaços), sem mocks — testar a função pura
  diretamente com inputs/outputs esperados.
