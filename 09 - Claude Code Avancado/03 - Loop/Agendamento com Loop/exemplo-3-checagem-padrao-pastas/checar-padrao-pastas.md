---
description: Confere se as pastas de exemplo dentro de cada tema seguem o padrão "exemplo-N-descricao" com um README.md dentro, e relata divergências (não corrige nada automaticamente).
allowed-tools: Bash(find:*), Read
---

Este projeto segue a convenção: dentro de cada subpasta "<Tema> na Prática",
cada exemplo fica em uma pasta chamada `exemplo-<N>-<descricao-curta>`
(minúsculo, com hífens) e contém um `README.md`.

1. Use `find` para localizar todas as subpastas imediatas de pastas cujo
   nome contenha "na Pratica" ou "na Prática".
2. Para cada uma, verifique:
   - o nome bate com o padrão `exemplo-N-descricao` (N = número)?
   - existe um `README.md` dentro dela?
3. Gere um relatório em português, só com as pastas que **não** seguem o
   padrão (nome ou README ausente), explicando o motivo de cada uma.
   Se estiver tudo certo, responda "Nenhuma divergência encontrada.".
4. **Não edite nem renomeie nada** — este comando é só de relatório/leitura.
