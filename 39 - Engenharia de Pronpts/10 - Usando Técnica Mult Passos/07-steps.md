### Quebrar Tarefas em Múltiplos Passos


```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

#### Multi Step Básico


```python
system_prompt = """
Você é um guia de trekking ultraleve. Siga a metodologia multi-step:
1) Liste e some os pesos por categoria
2) Calcule o peso-base (sem comida/água/combustível)
3) Defina a meta de redução (15% do peso-base)
4) Proponha trocas/reduções para alcançar a meta
5) Verifique consistência e riscos (clima/segurança)
Formate cada passo com títulos claros.
"""

user_prompt = """
PLANEJAMENTO (2 dias, clima ameno, sem chuva prevista)
ITENS E PESOS (g):
• Abrigo (barraca): 1450
• Saco de dormir: 900
• Isolante: 420
• Mochila: 1100
• Fogareiro: 85
• Panela titânio: 120
• Garrafa 1L (vazia): 110
• Kit primeiros socorros: 160
• Capa de chuva: 180
• Fleece: 320
• Camiseta extra: 110
• Meias extra: 60
• Lanterna: 90
• Power bank: 210
• Kit higiene: 140

META: reduzir o peso-base em 15% mantendo segurança e conforto térmico.
PASSOS: execute 1→5 conforme metodologia.
"""
```


```python
resp = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "system", "content": system_prompt},
              {"role": "user", "content": user_prompt}],
    temperature=0.25
)
print("=== Multi Step Básico ===")
print(resp.choices[0].message.content)
```

### Multi Passo Avançado
- Qualidade do ar em 4 bairros e recomendações operacionais


```python
system_prompt = """
Você é um analista ambiental. Metodologia:
1) Estruture os dados em tabela mental e calcule médias/medianas por bairro
2) Detecte tendências (alta/baixa) e outliers
3) Calcule correlações qualitativas (tráfego x PM2.5; área verde x PM2.5)
4) Classifique risco por bairro (baixo/médio/alto) com justificativa
5) Recomende 3 ações operacionais e 2 ações estruturais
6) Valide limitações dos dados
Responda com seções numeradas.
"""

user_prompt = """
DADOS (4 semanas, valores médios semanais):
Bairro A: PM2.5[23, 26, 29, 31] μg/m³; Tráfego[alto]; Área verde[baixa]
Bairro B: PM2.5[14, 13, 16, 15]; Tráfego[médio]; Área verde[média]
Bairro C: PM2.5[11, 12, 10, 12]; Tráfego[baixo]; Área verde[alta]
Bairro D: PM2.5[28, 35, 33, 37]; Tráfego[muito alto]; Área verde[baixa]
Limite guia OMS (anual): 5 μg/m³ (referência).
Aplique a metodologia.
"""
```


```python
resp2 = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "system", "content": system_prompt},
              {"role": "user", "content": user_prompt}],
    temperature=0.3
)
print("\n=== Análise Complexa (Qualidade do Ar) ===")
print(resp2.choices[0].message.content)
```

### Multi Passo Criativo


```python
system_prompt = """
Você é um diretor de criação. Processo:
1) Defina público-alvo e objetivo mensurável
2) Faça brainstorming (5 ideias, variadas)
3) Escolha 2 ideias e crie um conceito central para cada
4) Esboce roteiro de peça principal (30s vídeo) com gancho, meio e CTA
5) Ajuste tom/linguagem para canais (outdoor, social, escola)
6) Checklist de validação (mensagem, viabilidade, medição)
Responda com tópicos claros e curtos.
"""

user_prompt = """
BRIEF: Reduzir descarte de lixo nas praças de uma cidade média em 20% em 3 meses.
Recursos: verba limitada, apoio de escolas e associações de bairro.
Restrições: não usar linguagem punitiva; incentivar orgulho local.
"""
```


```python
resp3 = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "system", "content": system_prompt},
              {"role": "user", "content": user_prompt}],
    temperature=0.6
)
print("\n=== Multi Step Criativo (Campanha Ambiental) ===")
print(resp3.choices[0].message.content)
```

### Comparação Passo Único x Multi Passo
- Planejamento de implantação de microgeração solar residencial.


```python
# Single Step
single_prompt = """
Crie um plano para instalar painéis solares residenciais para uma casa de 3 quartos.
Considere orçamento moderado e retorno em 6-8 anos.
"""

single = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": single_prompt}],
    temperature=0.5
)
print("\n=== Single Step ===")
print(single.choices[0].message.content)
```


```python
# Multi Step
multi_prompt = """
Elabore o plano em múltiplos passos:
PASSO 1: Levantamento (perfil de consumo mensal, telhado, sombreamento)
PASSO 2: Dimensionamento preliminar (kWp, inversor, string)
PASSO 3: Custos (equipamentos, instalação, manutenção) e incentivos
PASSO 4: Projeção financeira (payback, TIR, sensibilidade)
PASSO 5: Riscos operacionais e mitigação
PASSO 6: Checklist de execução e cronograma em 30/60/90 dias
Formate cada passo com bullets + mini-tabela quando pertinente.
"""

multi = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": multi_prompt}],
    temperature=0.45
)
print("\n=== Multi Step ===")
print(multi.choices[0].message.content)
```
