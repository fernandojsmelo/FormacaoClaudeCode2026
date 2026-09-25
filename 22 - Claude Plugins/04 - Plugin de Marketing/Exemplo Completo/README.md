# Exemplo Completo — Plugin de Marketing

Este é um exemplo aplicável, do zero ao fim, usando o **Plugin de Marketing** do Claude. O caso usado é o mesmo já iniciado na pasta deste módulo (`Campanha_Metodo_Foco_Digital.pptx`, criado com o Plugin de Design): o lançamento do curso online **Método Foco Digital**.

Aqui estão os **documentos de trabalho reais** por trás daquela apresentação — o que cada skill do plugin efetivamente produz quando você a aciona, na ordem em que um lançamento de verdade seria conduzido.

## Ordem de execução e skills usadas

| # | Arquivo | Skill | O que faz |
|---|---|---|---|
| 1 | `01-campaign-plan.md` | `marketing:campaign-plan` | Plano estratégico completo: objetivo, público, mensagens, canais, calendário, orçamento, métricas, riscos |
| 2 | `02-conteudo-draft-content.md` | `marketing:draft-content` | Conteúdo real a partir do plano: post de blog (SEO), 3 posts de Instagram, landing page do lead magnet |
| 3 | `03-email-sequence.md` | `marketing:email-sequence` | Sequência completa de 7 e-mails de lançamento, com lógica de branching, condição de saída e métricas |
| 4 | `04-brand-review.md` | `marketing:brand-review` | Revisão de uma peça de conteúdo contra um guia de voz de marca, com achados por severidade e sinalizações de compliance |
| 5 | `05-performance-report.md` | `marketing:performance-report` | Relatório pós-campanha (dados simulados): o que funcionou, o que não funcionou, recomendações priorizadas |

## Como reproduzir

Cada arquivo foi gerado invocando a skill correspondente do plugin (`/campaign-plan`, `/draft-content`, `/email-sequence`, `/brand-review`, `/performance-report`) e passando o contexto do passo anterior como entrada do seguinte — exatamente como uma campanha real evolui: **plano → conteúdo → revisão → execução → resultado analisado**.

## Por que esta ordem importa

- O **campaign-plan** vem primeiro porque define objetivo, público e mensagens-chave — tudo que as outras skills herdam.
- O **draft-content** e o **email-sequence** só fazem sentido depois do plano, porque usam as mensagens-chave e o calendário definidos nele.
- O **brand-review** entra antes da veiculação, revisando o conteúdo já produzido — é o "controle de qualidade" antes de gastar orçamento de mídia.
- O **performance-report** fecha o ciclo, e suas recomendações (seção 8) alimentariam um novo `campaign-plan` para a próxima campanha — o loop se repete.

---
*Entregável do módulo "04 - Plugin de Marketing" — Formação Claude Code 2026.*
