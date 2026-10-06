```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Sumarização Básica
-  Tendências e desafios no desenvolvimento de jogos indie


```python
system_prompt = """
Você é um editor técnico especializado em jogos independentes.
Crie um resumo objetivo com aproximadamente 1/3 do tamanho do texto original,
preservando os pontos centrais e o tom informativo.
"""

user_prompt = """
A cena de jogos independentes segue em crescimento, com ferramentas como engines gratuitas,
marketplaces digitais e financiamento coletivo tornando possível a criação por equipes pequenas.
Desafios frequentes incluem descoberta (getting discovered) em lojas saturadas, financiamento
sustentável após o lançamento e equilíbrio entre inovação e usabilidade. Muitos estúdios optam
por construir comunidades durante o desenvolvimento (early access, betas) para reduzir riscos.
Tendências recentes mostram ênfase em experiências narrativas curtas, jogos como serviço
em modelo leve, e experimentos com integração de áudio procedural. O mercado também aponta
maior valorização por jogos com estética única e mecânicas originais, embora isso nem sempre
se traduza em vendas imediatas. Estratégias de monetização variam: premium, pay-what-you-want,
DLCs pequenas, e microtransações bem posicionadas em jogos multiplayer. Em suma, o sucesso
indie depende de produto de qualidade, comunidade engajada e escolhas estratégicas de lançamento.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.2
)

print("=== Sumarização Básica ===")
print(response.choices[0].message.content)
```

### Sumarização em Bullets
- Relatório piloto de mobilidade urbana (dados e ações)


```python
system_prompt = """
Você é um analista de políticas públicas. Gerei um resumo em bullet points claros e hierárquicos:
- Destaque resultados (métricas)
- Liste problemas prioritários
- Sugira 3 ações imediatas e 2 ações estruturais
Mantenha frases curtas.
"""

user_prompt = """
Relatório Piloto: Nova rota de ciclovia e corredores de ônibus rápidos implementada por 12 semanas.
Resultados preliminares: aumento no uso de bicicleta em 22% nas rotas testadas; redução de tempo médio de deslocamento em ônibus local em 8%; aumento de reclamações de comerciantes sobre estacionamento; registro de 3 incidentes leves envolvendo ciclistas.
Observações: infraestrutura temporária com sinalização provisória; campanhas educativas em 4 bairros; orçamento limitado para fiscalização.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.25
)

print("\n=== Bullet Points (Mobilidade Urbana) ===")
print(response.choices[0].message.content)
```

### Resumo Executivo


```python
system_prompt = """
Você é um consultor executivo. Construa um resumo executivo com:
1) Síntese em 2-3 frases
2) Principais métricas (visitantes, receita direta, parcerias)
3) 3 recomendações acionáveis para o próximo ano (priorizadas)
Seja conciso e orientado para decisão.
"""

user_prompt = """
Relatório: Festival "Olhar Curto" (3 dias).
Métricas: 4.200 visitantes (inclui sessões pagas e gratuitas), receita direta: R$ 180.000 (ingressos + barra),
patrocínios: R$ 70.000, custos operacionais: R$ 150.000.
Impacto local: aumento de 18% no movimento de bares e cafés próximos durante o evento;
envolvimento de 6 escolas técnicas; 25 curtas exibidos, 8 produções locais.
Desafios: logística de exibição ao ar livre (chuva reprogramou 2 sessões), bilheteria online com alta taxa de desistência.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.15
)

print("\n=== Resumo Executivo (Festival de Curtas) ===")
print(response.choices[0].message.content)

```

### Comparação de Estilos de Sumarização
- Resumo técnico (formal) e um resumo curto para redes sociais (casual)


```python
base_text = """
Projeto de conservação marinha no litoral: monitoramento de recifes por sensores acústicos e foto-identificação de tartarugas;
dados coletados trimestralmente mostram recuperação gradual de populações locais (+12% em 2 anos),
mas aumento de resíduos plásticos nas áreas de alimentação; parcerias com pescadores locais reduziram
incidentes de emalhe em 35%. Necessidade de financiamento para ampliar estações de monitoramento
e campanhas comunitárias de educação ambiental. Risco climático: eventos de branqueamento relacionados à elevação de temperatura da água.
"""

# Resumo técnico
system_prompt_tech = """
Você é um redator técnico-científico. Produza um resumo formal técnico (3-4 frases),
destacando metodologia, resultados quantitativos e limitações.
"""

response_tech = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_tech},
        {"role": "user", "content": base_text}
    ],
    temperature=0.2
)

# Resumo para redes sociais
system_prompt_social = """
Você é um comunicador digital. Faça uma versão curta e chamativa (1-2 frases) adequada para Instagram,
mantendo precisão mas com tom acessível e motivador.
"""

response_social = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_social},
        {"role": "user", "content": base_text}
    ],
    temperature=0.45
)
```


```python
print("\n=== Resumo Técnico ===")
print(response_tech.choices[0].message.content)
```


```python
print("\n=== Resumo para Redes Sociais ===")
print(response_social.choices[0].message.content)
```

### Sumarização em formato JSON


```python
texto = """
A inteligência artificial está transformando setores como saúde, finanças e educação.
Na medicina, auxilia no diagnóstico precoce de doenças. No setor financeiro, detecta fraudes
e otimiza investimentos. Na educação, personaliza o aprendizado para cada estudante.
Apesar dos avanços, existem preocupações éticas sobre privacidade, viés algorítmico
e substituição de empregos.
"""

# Prompt pedindo JSON estruturado
json_prompt = f"""
Resuma o seguinte texto em JSON.
O JSON deve conter as chaves:
- "setores" (lista com os setores impactados)
- "beneficios" (lista com os principais benefícios citados)
- "desafios" (lista com os riscos ou preocupações levantadas)

Texto:
{texto}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": json_prompt}],
    temperature=0.2
)

# Captura o conteúdo da resposta
resposta_json = response.choices[0].message.content

print("=== RESUMO EM JSON ===")
print(resposta_json)
```
