# Análise de Logs de API — Erros e Latência

Sep 25, 2026 · @Fernando Melo

## Resumo Executivo

- **Taxa de erro geral: 28,6%** (286 de 1.000 requests), muito acima do saudável para uma API em produção.
- **`/api/v1/payments` é o principal ponto crítico**: taxa de erro de **73,81%**, quase 3x o segundo colocado, além de latência consistentemente mais alta em qualquer status code.
- **Erros 5xx (500/502) são o gargalo de latência real**: requests que falham com 500 ou 502 demoram em média \~2.000-2.200 ms, 15-17x mais que uma request bem-sucedida — padrão típico de timeout em dependência downstream.
- Não há um pico horário dominante e consistente para erros 500; a distribuição ao longo do dia é relativamente uniforme, com leve concentração de madrugada (0h-6h) puxada majoritariamente por `/api/v1/products/{id}`.

## Metodologia

- **Fonte:** planilha `api_logs.xlsx`, aba "API Logs", com 1.000 registros de requisições de API (timestamp, endpoint, método, status code, latência, tamanho de payload, serviço, região, usuário).
- **Período:** requests distribuídas ao longo de múltiplas datas a partir de 01/03/2024 (amostra, não contínua ao longo de várias semanas).
- **Definição de erro:** status code ≥ 400 (inclui 4xx de cliente e 5xx de servidor). Onde relevante, os erros 5xx são analisados separadamente por representarem falhas de infraestrutura/dependência.
- **Ressalva:** o volume de erros 500 específicos (34 ocorrências) é baixo para análises horárias granulares — diferenças de 1-2 ocorrências entre horas não devem ser tratadas como padrão operacional forte sem mais dados.

## Ranking de Endpoints por Taxa de Erro

| # | Endpoint | Requests | Erros | Taxa de Erro |
| --- | --- | --: | --: | --: |
| 1 | `/api/v1/payments` | 84 | 62 | **73,81%** |
| 2 | `/api/v1/products/{id}` | 104 | 30 | 28,85% |
| 3 | `/api/v1/products` | 100 | 28 | 28,00% |
| 4 | `/api/v1/users/{id}` | 96 | 25 | 26,04% |
| 5 | `/api/v1/orders/{id}` | 98 | 25 | 25,51% |
| 6 | `/api/v1/webhooks` | 101 | 25 | 24,75% |
| 7 | `/api/v1/users` | 111 | 27 | 24,32% |
| 8 | `/api/v1/auth/refresh` | 92 | 22 | 23,91% |
| 9 | `/api/v1/orders` | 113 | 25 | 22,12% |
| 10 | `/api/v1/auth/login` | 101 | 17 | 16,83% |

`/api/v1/payments` é um outlier claro: quase 3x a taxa de erro do segundo colocado, com quase 3 em cada 4 requests falhando. Os principais status nesse endpoint são 400 (14), 404 (8), 500 (7), 502 (7), 503 (6) e 429 (5) — uma mistura de erros de cliente, servidor e indisponibilidade, sugerindo instabilidade generalizada no serviço, não só validação de entrada.

## Padrão Horário dos Erros 500

Dos 1.000 requests, 34 retornaram status 500. Agrupando por hora do dia:

| Hora | Erros 500 | Requests no período | Taxa de erro 500 |
| --- | --: | --: | --: |
| **08h** | **4** | 50 | 8,00% |
| 00h | 3 | 39 | 7,69% |
| 05h | 3 | 53 | 5,66% |
| 06h | 3 | 44 | 6,82% |
| 18h | 3 | 41 | 7,32% |
| 23h | 3 | 42 | 7,14% |
| 04h | 3 | 32 | 9,38% |
| 03h | 2 | 25 | 8,00% |
| 14h | 2 | 30 | 6,67% |
| 12h | 2 | 46 | 4,35% |
| demais horas | 0-1 | — | ≤ 2,9% |

O pico isolado é 8h (4 ocorrências), mas com diferença mínima para vários outros horários — dado o baixo volume total, isso não é um padrão forte.

**Cruzamento com endpoint** (os 4 endpoints com mais erros 500):

| Hora | payments | products | webhooks | products/{id} |
| --- | --: | --: | --: | --: |
| 0h | – | – | 1 | 1 |
| 3h | 1 | – | – | – |
| 4h | – | 1 | – | 1 |
| 5h | – | 1 | – | **2** |
| 6h | 1 | – | – | – |
| **8h** | – | **2** | – | – |
| 12h | 1 | – | – | – |
| 18h | 1 | – | – | – |
| 20h | 1 | – | – | – |
| 23h | **2** | – | – | – |

O pico de 8h é explicado inteiramente por `/api/v1/products`. A leve concentração de madrugada (0h-6h) é puxada majoritariamente por `/api/v1/products/{id}` (3 dos seus 4 erros 500 entre 4h-5h) — não por `/api/v1/payments`, que está disperso ao longo do dia (3h, 6h, 12h, 18h, 20h, 23h). Nenhum endpoint domina um horário específico de forma consistente; com células de 1-2 ocorrências, isso ainda é mais ruído estatístico do que um padrão operacional confiável.

## Latência Média por Endpoint e por Status Code

**Por endpoint** (ordenado do mais lento pro mais rápido):

| Endpoint | Requests | Média (ms) | Mediana (ms) | Máx (ms) | p95 (ms) |
| --- | --: | --: | --: | --: | --: |
| `/api/v1/payments` | 84 | 360,9 | 354,8 | 541,8 | 491,6 |
| `/api/v1/products` | 100 | 293,7 | 117,3 | 3116,7 | **2480,4** |
| `/api/v1/products/{id}` | 104 | 285,8 | 119,0 | 3691,1 | **2094,8** |
| `/api/v1/webhooks` | 101 | 245,8 | 117,3 | 3003,3 | 208,4 |
| `/api/v1/users/{id}` | 96 | 242,9 | 105,9 | 3857,8 | 619,6 |
| `/api/v1/orders/{id}` | 98 | 238,9 | 115,1 | 3874,2 | 186,1 |
| `/api/v1/orders` | 113 | 236,5 | 117,3 | 3915,2 | 219,8 |
| `/api/v1/auth/refresh` | 92 | 208,0 | 110,8 | 3911,6 | 213,9 |
| `/api/v1/users` | 111 | 189,9 | 112,1 | 3182,0 | 209,7 |
| `/api/v1/auth/login` | 101 | 132,8 | 114,2 | 1665,8 | 204,3 |

**Por status code:**

| Status | Requests | Média (ms) | Mediana (ms) |
| --- | --: | --: | --: |
| **500** | 34 | **2231,2** | 2579,4 |
| **502** | 18 | **1961,8** | 2417,2 |
| 503 | 8 | 874,9 | 377,7 |
| 422 | 26 | 167,9 | 96,2 |
| 404 | 36 | 152,6 | 98,8 |
| 204 / 400 / 200 / 201 / 401 | — | 112-141 | \~95-125 |
| 429 / 403 | — | \~113 | \~52-92 |

Requests com status 500 ou 502 demoram, em média, 15-17x mais que uma request bem-sucedida (\~130 ms).

## Gargalos Críticos

1. **Erros 5xx são o gargalo de latência mais grave.** Requests com 500/502 levam \~2.000-2.200 ms em média — padrão típico de **timeout em dependência downstream** (espera, tenta, falha, só então retorna o erro).
2. **`/api/v1/products` e `/api/v1/products/{id}` têm o pior p95** (2.480 ms e 2.095 ms) apesar de mediana baixa — distribuição bimodal: a maioria das requests é rápida, mas uma cauda (as que resultam em 500) trava por segundos. Indício de timeout/retry mal configurado na dependência downstream do catálogo de produtos.
3. **`/api/v1/payments` tem latência estruturalmente alta e estável** (330-400 ms independente do status), diferente do padrão de falha dos outros endpoints — sugere processamento síncrono mais pesado (ex.: chamada a gateway de pagamento externo), não picos de timeout.
4. **Piores casos pontuais de latência-em-erro:** `orders/{id}` com 500 (3.358 ms), `users/{id}` com 502 (2.897 ms) e `webhooks` com 500 (2.829 ms) — cada erro 5xx nesses endpoints trava a request por quase 3 a 3,4 segundos.

## Recomendações Priorizadas

1. **Investigar `/api/v1/payments` com urgência** — taxa de erro de 73,81% é incompatível com um serviço em produção estável. A mistura de 400/404/500/502/503/429 sugere instabilidade generalizada, não um bug pontual.
2. **Aplicar timeout agressivo (500ms-1s) nas chamadas downstream** de `/api/v1/products` e `/api/v1/products/{id}` — o ganho mais rápido para reduzir o p95 sem mexer na lógica de negócio: falhar rápido em vez de segurar a conexão por segundos.
3. **Configurar alertas de monitoramento em tempo real** por serviço e endpoint usando a query SQL abaixo, com threshold de taxa de erro (ex.: >5%) e volume mínimo (ex.: ≥10 requests) para evitar falsos positivos.
4. **Coletar mais dados antes de investir em análise horária** — com apenas 34 erros 500 na amostra atual, qualquer padrão por hora do dia tem ruído estatístico relevante; recomenda-se acumular várias semanas de logs antes de tomar decisões operacionais baseadas em horário.

## Query SQL para Monitoramento em Tempo Real (PostgreSQL)

Taxa de erro por serviço nas últimas 24h:

```sql
SELECT
    service,
    COUNT(*) AS total_requests,
    COUNT(*) FILTER (WHERE status_code >= 400) AS total_errors,
    COUNT(*) FILTER (WHERE status_code >= 500) AS server_errors_5xx,
    COUNT(*) FILTER (WHERE status_code BETWEEN 400 AND 499) AS client_errors_4xx,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE status_code >= 400) / NULLIF(COUNT(*), 0),
        2
    ) AS error_rate_pct,
    ROUND(AVG(latency_ms) FILTER (WHERE status_code >= 400), 2) AS avg_latency_erros_ms,
    MAX(timestamp) AS last_seen
FROM api_logs
WHERE timestamp >= NOW() - INTERVAL '24 hours'
GROUP BY service
ORDER BY error_rate_pct DESC;
```

Variante com quebra por endpoint (filtra endpoints com pouco tráfego):

```sql
SELECT
    service,
    endpoint,
    COUNT(*) AS total_requests,
    COUNT(*) FILTER (WHERE status_code >= 400) AS total_errors,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE status_code >= 400) / NULLIF(COUNT(*), 0),
        2
    ) AS error_rate_pct
FROM api_logs
WHERE timestamp >= NOW() - INTERVAL '24 hours'
GROUP BY service, endpoint
HAVING COUNT(*) >= 10
ORDER BY error_rate_pct DESC
LIMIT 20;
```

**Recomendações de performance:** criar índice composto `(timestamp, service)`; considerar particionamento diário da tabela para volumes altos; usar o filtro `HAVING COUNT(*) >= 10` em monitoramento contínuo para evitar alertas de falso-positivo.
