# 🎨 Teste de Plugin de Design – Elementos Visuais e Estrutura

Este arquivo Markdown foi estruturado especificamente para testar a capacidade de renderização, estilização e interpretação de layouts por um **Plugin de Design** no Claude. Ele contém uma variedade de blocos de componentes comuns em interfaces (UI/UX).

---

## 1. Tipografia e Hierarquia de Texto

# Título Principal (H1)
## Subtítulo de Seção (H2)
### Tópico de Conteúdo (H3)
#### Subtópico Detalhado (H4)

Este é um parágrafo padrão contendo texto corrido. Aqui testamos o espaçamento de linha (*line-height*), a legibilidade da fonte e a transição entre blocos de texto. Podemos ter textos em **negrito**, textos em *itálico* e também termos combinados como ***negrito e itálico*** ou até mesmo texto ~~taxado~~.

---

## 2. Componentes de UI e Blocos de Destaque

> 💡 **Nota Importante de Destaque (Callout)**
> Este bloco serve para verificar se o plugin consegue renderizar cartões de alerta, notas com bordas laterais coloridas, fundos diferenciados ou cantos arredondados.

```json
{
  "componente": "Card",
  "estilo": "dark-mode",
  "propriedades": {
    "padding": "24px",
    "borderRadius": "8px",
    "shadow": "0 4px 12px rgba(0,0,0,0.1)"
  }
}
```

---

## 3. Elementos de Navegação e Seleção

### Links e Interações
* Acesse a documentação oficial no [MDN Web Docs](https://developer.mozilla.org).
* Acesse uma referência visual na comunidade [Figma](https://www.figma.com/community).

### Listas de Tarefas (Checklists / Tasklists)
- [x] **Fase 1:** Configuração do Design System global (Cores e Fontes)
- [x] **Fase 2:** Renderização de cards responsivos
- [/] **Fase 3:** Animações e micro-interações de botões
- [ ] **Fase 4:** Teste de acessibilidade (Contraste WCAG)

---

## 4. Estruturas de Dados (Tabelas)

Esta tabela avalia o alinhamento de colunas, formatação de cabeçalhos e preenchimento de células (*padding*).

| Componente | Tipo de Token | Cor Padrão (Hex) | Status de Validação |
| :--- | :---: | :---: | :--- |
| **Primary Button** | Background | `#0070F3` | 🟢 Validado |
| **Secondary Button** | Border | `#E2E8F0` | 🟢 Validado |
| **Alert Banner** | Surface | `#FFF5F5` | 🟡 Em Revisão |
| **Text Main** | Typography | `#1A202C` | 🔴 Erro de Contraste |

---

## 5. Fluxo de Processo e Listas

1. **Definição de Escopo:** Coleta de requisitos de UI com stakeholders.
2. **Wireframing:** Esboços de baixa fidelidade para validar a arquitetura de informação.
3. **Prototipagem:** Desenvolvimento do fluxo de alta fidelidade e interações.
   * *Métricas:* Coletar cliques errados por tela.
   * *Feedback:* Ajustar transições lentas.
4. **Handoff:** Exportação de tokens de design diretamente para os desenvolvedores.

---

## 6. Recursos Visuais (Mídia)

Abaixo estão testes de carregamento e posicionamento de elementos gráficos externos:

![Logotipo Placeholder](https://via.placeholder.com/150 "Exemplo de Logo para Teste de Imagem")

---

*Fim do arquivo de teste. Atualize os parâmetros conforme a necessidade do seu sistema de design.*
