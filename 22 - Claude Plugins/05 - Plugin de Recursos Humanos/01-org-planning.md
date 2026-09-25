# Planejamento de Headcount e Estrutura — Time de Dados & Analytics
**Empresa:** TechNova Soluções (SaaS B2B, ~180 colaboradores)
**Horizonte:** 12 meses | **Data:** 25/09/2026

## 1. Contexto

Hoje não existe um time de Dados & Analytics formal. As demandas de dados (dashboards, análises pontuais, extrações) são atendidas de forma ad-hoc por engenheiros de Produto, o que gera:
- Fila de espera e baixa priorização de pedidos de dados frente a features;
- Falta de padronização de métricas entre times (cada um calcula "ativação" ou "churn" de um jeito);
- Nenhuma governança sobre qualidade e confiabilidade dos dados usados em decisões.

## 2. Estrutura recomendada ao final dos 12 meses

```
VP de Produto
   └── Coordenador(a) de Dados & Analytics  (contratação M7)
          ├── Analista de Dados Pleno        (contratação M1 — já em andamento)
          ├── Analista de Dados Júnior       (contratação M9)
          └── Analytics/Data Engineer Pleno  (contratação M4)
```

- **Reporte:** o time nasce dentro de Produto (não em Engenharia nem Financeiro), porque a dor inicial é de priorização e padronização de métricas de produto/negócio. Reavaliar em 12–18 meses se deve virar área independente reportando à liderança executiva.
- **Span of control:** o Coordenador termina o ano com 3 reports diretos — abaixo da faixa saudável (5–8), mas correto para um time nascente; a expectativa é chegar a 5–6 reports no ano 2 antes de abrir uma segunda liderança.
- **Sem camada de gestão intermediária** por enquanto: time pequeno demais para justificar um segundo nível de management (evita over-hiring de gestão, ver "sinais de alerta" do benchmark).

## 3. Sequenciamento das contratações (ordem e racional)

| Ordem | Posição | Mês alvo | Por quê nessa ordem |
|---|---|---|---|
| 1 | Analista de Dados Pleno | M1 (agora) | Maior alívio imediato de dor: alguém que já sai produzindo dashboards e análises sem precisar de estrutura de dados madura. Não depende de nenhuma outra contratação. |
| 2 | Analytics/Data Engineer Pleno | M4 | Depois que o Analista de Dados mapear as fontes e dores de dados mais urgentes, o Data Engineer entra para industrializar pipelines (parar de depender de extrações manuais). |
| 3 | Coordenador(a) de Dados & Analytics | M7 | Só faz sentido contratar liderança quando já há 2 ICs entregando e escopo suficiente para coordenar; contratar liderança antes disso é comum erro (gestor sem o que gerir). |
| 4 | Analista de Dados Júnior | M9 | Uma vez que o Coordenador está no papel e há processos/documentação mínima (criada pelo Pleno e pelo Data Engineer), um júnior consegue ser produtivo com onboarding estruturado. |

**Ponto de atenção (single point of failure):** entre M1 e M4, toda a operação de dados do time depende de uma única pessoa (o Analista Pleno). Recomenda-se:
- Documentar desde o dia 1 (ver plano de onboarding em anexo);
- Ter um "buddy" técnico em Engenharia de Produto como backup informal até a chegada do Data Engineer.

## 4. Modelagem de custo (estimativa, CLT + encargos ~80% sobre salário-base, Brasil)

| Posição | Salário-base/mês (R$) | Custo total/mês c/ encargos (R$) | Custo anualizado (R$) |
|---|---:|---:|---:|
| Analista de Dados Pleno | 9.000 | 16.200 | 194.400 |
| Analytics/Data Engineer Pleno | 11.500 | 20.700 | 248.400 |
| Coordenador(a) de Dados & Analytics | 15.000 | 27.000 | 324.000 |
| Analista de Dados Júnior | 5.500 | 9.900 | 118.800 |
| **Total ao final dos 12 meses (run-rate anualizado)** | | **73.800/mês** | **885.600/ano** |

Custo real do ano 1 é menor que o run-rate acima, pois as contratações são escalonadas (M1, M4, M7, M9) — o gasto efetivo nos primeiros 12 meses fica em torno de **R$ 460–500 mil**, crescendo para o run-rate completo apenas no ano 2.

## 5. Riscos e recomendações
- **Não pular a etapa do Data Engineer**: contratar um segundo Analista antes do Data Engineer perpetua o trabalho manual e não escala.
- **Não contratar o Coordenador cedo demais**: aguardar ter 2 ICs entregando evita "gestor sem time para gerir".
- **Revisar span of control em 12 meses**: se a demanda por dados crescer mais rápido que o previsto (ex: expansão para novos mercados), considerar antecipar a 2ª contratação de Analytics Engineer.
