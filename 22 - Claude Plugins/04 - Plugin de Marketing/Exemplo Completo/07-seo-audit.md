# Auditoria de SEO — Método Foco Digital
**Skill utilizada:** `marketing:seo-audit`
**Escopo:** landing page do checklist + post de blog (arquivo `02-conteudo-draft-content.md`)
**Domínio (fictício):** methodofocodigital.com.br
**Nota metodológica:** site fictício sem rastreamento real nesta sessão — achados simulados de forma plausível, no lugar de dados reais de ferramenta de SEO/analytics (que a skill usaria automaticamente se estivessem conectadas).

---

## Resumo Executivo

O conteúdo já produzido tem boa base de intenção de busca (fala diretamente a dor "sobrecarga digital"), mas o site fictício, como a maioria dos sites recém-lançados de infoproduto, provavelmente teria **fundação técnica fraca** (sem sitemap, sem dados estruturados) e **cobertura de conteúdo rasa** (1 post vs. um cluster de tópicos). Prioridade máxima: transformar o post único em um cluster (pilar + 3-4 posts de apoio) e resolver o básico técnico antes de investir em link building.

---

## Tabela de Oportunidades de Palavras-Chave

| Palavra-chave | Dificuldade est. | Oportunidade | Ranking atual | Intenção | Formato recomendado |
|---|---|---|---|---|---|
| sobrecarga digital | Média | Alta | Não indexado (site novo) | Informacional | Post pilar (já existe — expandir) |
| como ser mais produtivo no trabalho | Alta | Média | Não indexado | Informacional | Post pilar |
| gestão do tempo para profissionais | Média | Alta | Não indexado | Informacional | Post de apoio |
| como parar de procrastinar reuniões | Baixa | Alta | Não indexado | Informacional | Post de apoio (long-tail) |
| teste de produtividade gratuito | Baixa | Alta | Não indexado | Comercial | Landing page (já existe) |
| notificações em excesso trabalho | Baixa | Média | Não indexado | Informacional | Post de apoio (long-tail) |
| método de produtividade que funciona | Média | Alta | Não indexado | Comercial | Landing page de vendas |
| como priorizar tarefas no trabalho | Média | Alta | Não indexado | Informacional | Post de apoio |
| apps de produtividade não funcionam | Baixa | Alta | Não indexado | Informacional | Post de apoio (ataca gap do Concorrente B — ver `06-competitive-brief.md`) |
| rotina matinal produtiva profissional | Média | Baixa | Não indexado | Informacional | Post de apoio |
| trabalho remoto e sobrecarga | Baixa | Média | Não indexado | Informacional | Post de apoio |
| burnout digital sintomas | Média | Média | Não indexado | Informacional | Post de apoio (atenção: não fazer claim de saúde/diagnóstico) |
| como recuperar tempo produtivo | Baixa | Alta | Não indexado | Informacional/Comercial | Post de apoio → CTA para o teste |
| checklist de produtividade grátis | Baixa | Alta | Não indexado | Comercial | Landing page (já existe) |
| curso de produtividade online | Alta | Média | Não indexado | Transacional | Página de vendas |
| como organizar a rotina de trabalho | Média | Média | Não indexado | Informacional | Post de apoio |
| gestão de notificações celular trabalho | Baixa | Média | Não indexado | Informacional | Post de apoio (long-tail) |
| reuniões improdutivas como evitar | Baixa | Alta | Não indexado | Informacional | Post de apoio |
| sistema de produtividade sem app | Baixa | Alta | Não indexado | Informacional/Comercial | Post de apoio (diferenciador direto) |
| quanto tempo perdemos com distrações | Baixa | Baixa | Não indexado | Informacional | Estatística/infográfico |
| foco no trabalho técnicas | Média | Média | Não indexado | Informacional | Post de apoio |

---

## Tabela de Problemas On-Page

| Página | Problema | Severidade | Correção recomendada |
|---|---|---|---|
| Post de blog | Meta descrição já definida, mas falta verificar contagem de caracteres em produção (alvo: até 160) | Baixa | Validar no CMS antes de publicar |
| Post de blog | Apenas 1 link interno sugerido (para a landing page do checklist) | Média | Adicionar 2-3 links internos para posts de apoio futuros do cluster |
| Post de blog | Sem menção a dados estruturados (Article schema) | Média | Implementar schema.org/Article com autor, data de publicação |
| Landing page (checklist) | Título e meta descrição definidos corretamente na copy | — | Pass |
| Landing page (checklist) | FAQ já sugerido no conteúdo, mas sem marcação de FAQ schema | Média | Implementar FAQPage schema — habilita rich snippet no Google |
| Landing page (checklist) | CTA principal não tem texto de âncora descritivo definido (ex.: "clique aqui" genérico deve ser evitado) | Baixa | Garantir que o botão real use texto como "Fazer o teste gratuito" |
| Ambas | Nenhuma imagem com alt text definido no conteúdo (copy não especifica) | Média | Definir alt text descritivo ao produzir as peças visuais (ex.: "diagrama das 3 armadilhas de produtividade") |
| Site (geral) | Sitemap XML e robots.txt não mencionados no plano de lançamento | Alta | Adicionar ao checklist técnico da semana 1 (arquivo `01-campaign-plan.md`, calendário) |

---

## Recomendações de Gap de Conteúdo

| Tópico/palavra-chave | Por que importa | Formato | Prioridade | Esforço estimado |
|---|---|---|---|---|
| "Apps de produtividade não funcionam — por quê" | Ataca diretamente o gap do Concorrente B (app de assinatura); alta intenção de busca de quem já tentou e desistiu | Post de blog | Alta | Moderado (meio dia) |
| "Como priorizar tarefas sem depender de mais um app" | Complementa o post pilar; alimenta o topo do funil de quem busca solução prática | Post de blog | Alta | Moderado |
| "Reuniões improdutivas: como reduzir sem virar o chato da equipe" | Long-tail de baixa dificuldade, alta relevância para a dor nº2 do público (mensagens-chave do plano) | Post de blog | Média | Rápido (1-2h) |
| Página de comparação honesta "Método vs. App vs. Curso longo" | Conecta diretamente com o battlecard do `06-competitive-brief.md`; ajuda decisão sem citar concorrentes por nome | Página de comparação | Média | Substancial (multi-dia) |
| Glossário/infográfico "As 3 Armadilhas de Produtividade" | Formato visual e compartilhável, reforça a marca do diagnóstico do teste | Infográfico/página | Baixa | Moderado |

---

## Checklist Técnico de SEO

| Verificação | Status | Detalhes |
|---|---|---|
| HTTPS ativo | Warning | Confirmar certificado antes do lançamento (padrão em qualquer host atual, mas checar) |
| Sitemap XML enviado ao Search Console | Fail | Não mencionado no plano — adicionar ao checklist da semana 1 |
| Robots.txt configurado corretamente | Fail | Mesmo ponto acima — garantir que não bloqueia páginas que devem ser indexadas |
| Mobile-friendly (responsivo) | Warning | Página com formulário de quiz precisa de teste específico em mobile (maior parte do tráfego de Instagram Ads é mobile) |
| Velocidade de carregamento | Warning | Página com quiz interativo (Typeform embutido, conforme e-mail 1) pode pesar — testar Core Web Vitals antes do lançamento |
| Dados estruturados (schema) | Fail | Nenhum schema definido ainda (Article no blog, FAQPage na landing page) |
| Canonical tags | Warning | Verificar se a landing page do checklist não conflita com a página de vendas em conteúdo duplicado |
| Links internos | Warning | Cluster de conteúdo ainda não existe — apenas 1 post publicado no plano atual |

---

## Plano de Ação Priorizado

### Vitórias Rápidas (esta semana)
- Adicionar sitemap.xml e configurar robots.txt corretamente — **alto impacto, baixo esforço**
- Definir alt text descritivo para todas as imagens do post e da landing page — **médio impacto, baixo esforço**
- Implementar FAQPage schema na landing page do checklist — **médio impacto, baixo esforço**
- Escrever o post "Reuniões improdutivas: como reduzir sem virar o chato da equipe" (long-tail fácil) — **médio impacto, baixo esforço**

### Investimentos Estratégicos (planejar para o trimestre)
- Construir o cluster de conteúdo em torno de "sobrecarga digital" (pilar + 4 posts de apoio) — **alto impacto, esforço substancial**; depende do post pilar já existente
- Criar a página de comparação "Método vs. App vs. Curso longo" — **alto impacto, esforço substancial**; depende do battlecard (`06-competitive-brief.md`)
- Implementar Article schema em todos os posts do blog — **médio impacto, esforço moderado**
- Testar e otimizar Core Web Vitals da landing page do quiz antes de escalar mídia paga — **alto impacto, esforço moderado**; pré-requisito para o canal orgânico/pago do `01-campaign-plan.md`

---

## Observação de fechamento do loop

O `05-performance-report.md` já havia identificado captação de leads no aquecimento **14% abaixo da meta**. Esta auditoria aponta uma causa técnica plausível (falta de schema, sitemap, e possível peso da página com o quiz embutido) que complementa a hipótese de fricção no quiz levantada naquele relatório — as duas juntas apontam para o mesmo pré-requisito: **QA técnico da landing page antes de escalar tráfego pago**, item já refletido no `08-campaign-plan-v2.md`.
