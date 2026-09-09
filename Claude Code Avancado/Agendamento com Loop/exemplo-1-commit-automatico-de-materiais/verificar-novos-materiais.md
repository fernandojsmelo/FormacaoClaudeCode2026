---
description: Verifica se há arquivos novos não versionados no repositório e cria um commit descritivo para eles (sem dar push).
allowed-tools: Bash(git status:*), Bash(git add:*), Bash(git commit:*), Bash(git log:*)
---

Você é responsável por manter o histórico do repositório organizado enquanto
novos materiais de curso (PDFs, exemplos, READMEs) são adicionados às pastas.

1. Rode `git status` para ver o que está não versionado ou modificado.
2. Se não houver nada novo, apenas responda "Nada para commitar." e pare.
3. Se houver arquivo(s) novo(s):
   - Adicione com `git add` apenas os arquivos relevantes (nunca use `-A`
     ou `.` cegamente; revise o que está sendo incluído).
   - Crie um commit com mensagem curta e descritiva em português,
     no padrão dos commits já existentes no repositório (`git log` para
     conferir o estilo), explicando o que foi adicionado.
   - **Não faça `git push`** — este comando só commita localmente.
4. Ao final, resuma em 1-2 linhas o que foi commitado (ou que não havia
   nada a fazer).
