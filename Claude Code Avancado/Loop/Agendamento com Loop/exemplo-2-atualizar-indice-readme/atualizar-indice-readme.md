---
description: Escaneia as pastas de nível superior do projeto e atualiza a lista de conteúdo entre os marcadores INICIO-INDICE/FIM-INDICE do README.md.
allowed-tools: Bash(ls:*), Read, Edit
---

O README.md deste projeto tem uma seção delimitada por:

```
<!-- INICIO-INDICE -->
<!-- FIM-INDICE -->
```

1. Liste as pastas de nível superior do projeto (ignore `.claude`, `.git` e
   arquivos soltos).
2. Leia o README.md atual.
3. Gere uma lista em markdown (um item por pasta, em ordem alfabética) e
   substitua **apenas o conteúdo entre os dois marcadores**, preservando o
   restante do arquivo intacto.
4. Se a lista gerada já for idêntica à existente, não edite o arquivo e
   responda "Índice já está atualizado."
5. Ao final, resuma em português o que mudou (quais pastas entraram/saíram
   do índice), em 1-2 linhas, sem raciocínio intermediário na resposta.
