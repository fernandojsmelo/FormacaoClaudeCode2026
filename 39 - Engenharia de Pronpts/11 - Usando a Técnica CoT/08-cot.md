## Cadeia de Pensamento

Útil em situações:
- Raciocínio estruturado e explícito
- Explicação transparente do raciocínio
- Clareza na tomada de decisão


```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### CoT para Estratégia de Marketing


```python
system_prompt = """
Você é um estrategista de marketing que sempre usa Chain of Thoughts (CoT).
Mostre o raciocínio dentro de <cot> e depois dê uma conclusão objetiva.
"""

user_prompt = """
Uma empresa de moda quer lançar uma campanha para atrair a Geração Z.
Dados:
- Orçamento: R$ 500 mil
- Principais canais: Instagram, TikTok, YouTube
- Objetivo: aumentar vendas online em 30% em 6 meses
- Concorrência: 3 marcas fortes no mesmo segmento

Crie um plano de campanha explicando o raciocínio passo a passo.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "developer", "content": system_prompt},
           {"role": "user", "content": user_prompt}],
    temperature=0.4
)

print("Plano de Marketing:", response.choices[0].message.content)
```

### Cot em Saúde
- Apoio em raciocínio clínico


```python
system_prompt = """
Você é um médico que usa Chain of Thoughts (CoT) para raciocínio clínico.
Sempre apresente hipóteses dentro de <cot> e finalize com recomendação objetiva.
"""

user_prompt = """
Paciente: 45 anos, sedentário, fumante, apresenta dores no peito durante esforço físico.
Exames iniciais: colesterol alto, pressão arterial elevada.

Qual deve ser a recomendação inicial para o paciente?
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "developer", "content": system_prompt},
           {"role": "user", "content": user_prompt}],
    temperature=0.3
)

print("Análise clínica:", response.choices[0].message.content)
```

### Cot em Análise de Investimentos
- Avaliação de riscos e oportunidades


```python
system_prompt = """
Você é um consultor financeiro que usa Chain of Thoughts (CoT).
Mostre seu raciocínio dentro de <cot> e termine com uma recomendação objetiva.
"""

user_prompt = """
Uma startup de tecnologia está levantando R$ 5 milhões.
Dados:
- Receita atual: R$ 300 mil/mês
- Crescimento: 12% ao mês
- Equipe: 20 pessoas
- Concorrência: forte no mercado nacional
- Risco: dependência de um único grande cliente

Devo recomendar o investimento?
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "developer", "content": system_prompt},
           {"role": "user", "content": user_prompt}],
    temperature=0.4
)

print("Recomendação de investimento:", response.choices[0].message.content)
```

### Cot em Design de Produto
- Raciocínio para priorização de funcionalidades


```python
system_prompt = """
Você é um Product Manager que usa Chain of Thoughts (CoT).
Mostre o raciocínio dentro de <cot> e finalize com a priorização.
"""

user_prompt = """
Estamos desenvolvendo um aplicativo de bem-estar.
Funcionalidades propostas:
1. Meditação guiada
2. Monitoramento de sono
3. Gamificação de hábitos
4. Relatórios personalizados

Orçamento permite lançar apenas duas no MVP.
Qual priorizar?
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "developer", "content": system_prompt},
           {"role": "user", "content": user_prompt}],
    temperature=0.3
)

print("Funcionalidades prioritárias:", response.choices[0].message.content)
```


```python
# Chain of Thoughts
cot_prompt = """
Quais as vantagens de trabalhar remoto? 
Use Chain of Thoughts para pensar passo a passo antes de responder.
"""

response_cot = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": cot_prompt}],
    temperature=0.5
)

print("=== CHAIN OF THOUGHTS ===")
print(response_cot.choices[0].message.content)
```
