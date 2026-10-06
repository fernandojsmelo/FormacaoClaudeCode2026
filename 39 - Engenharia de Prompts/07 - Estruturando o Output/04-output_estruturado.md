```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Saída em Formato de Tabela


```python
system_prompt = """
Você é um historiador especializado em civilizações antigas.
Sempre responda no formato de tabela:

| Civilização | Período | Contribuição Marcante | Região |
|-------------|---------|-----------------------|--------|
"""

user_prompt = "Crie uma tabela comparando 4 civilizações antigas (Egito, Mesopotâmia, Grécia, Roma)."

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    
    temperature=0.5
)

print(response.choices[0].message.content)
```

### Saída em uma Lista Simples


```python
system_prompt_simples = "Você é um crítico de cinema que apresenta informações em listas claras."
user_prompt_simples = "Liste 5 filmes premiados no Oscar que marcaram a história do cinema."

response_simples = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_simples},
        {"role": "user", "content": user_prompt_simples}
    ],
    temperature=0.6
)
print(response_simples.choices[0].message.content)
print()

```

### Lista Numerada


```python
system_prompt_numerada = """
Você cria listas numeradas no formato:
1. [Título]: [Descrição curta]
"""
user_prompt_numerada = "Liste 4 estratégias de treinamento usadas por atletas olímpicos."

response_numerada = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_numerada},
        {"role": "user", "content": user_prompt_numerada}
    ],
    max_completion_tokens=200,
    temperature=0.6
)
print(response_numerada.choices[0].message.content)
print()
```

### Lista Hierárquica


```python
system_prompt_hierarquica = """
Você organiza informações em listas hierárquicas no formato:
• Categoria Principal
  - Subcategoria 1
  - Subcategoria 2
"""
user_prompt_hierarquica = "Organize áreas da ciência em categorias: Física, Biologia, Química."

response_hierarquica = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_hierarquica},
        {"role": "user", "content": user_prompt_hierarquica}
    ],
    temperature=0.6
)
print(response_hierarquica.choices[0].message.content)
```

### Parágrafos Estruturados


```python
system_prompt = """
Você escreve textos estruturados no formato:

INTRODUÇÃO: [1-2 frases de contexto]
DESENVOLVIMENTO: [Explicação detalhada]
CONCLUSÃO: [Síntese final]
"""

user_prompt = "Explique a importância da moda como expressão cultural."

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)

```

### Formato Customizado


```python
system_prompt_card = """
Você cria cards informativos sobre missões espaciais no formato:

🚀 MISSÃO: [Nome]
📅 ANO: [Ano]
🌌 OBJETIVO: [Resumo em 1 frase]
🔭 RESULTADO: [Principais descobertas]
"""
user_prompt_card = "Crie um card sobre a missão Voyager 1."

response_card = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_card},
        {"role": "user", "content": user_prompt_card}
    ],
    temperature=0.6
)
print(response_card.choices[0].message.content)
print()
```

### Formato Checklist


```python
system_prompt_checklist = """
Você cria checklists no formato:

✅ [Tarefa 1]
✅ [Tarefa 2]
✅ [Tarefa 3]
"""
user_prompt_checklist = "Monte um checklist para organizar um festival de música ao ar livre."

response_checklist = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt_checklist},
        {"role": "user", "content": user_prompt_checklist}
    ],
    max_completion_tokens=400,
    temperature=0.6
)
print(response_checklist.choices[0].message.content)

```

### Unindo tudo


```python
system_prompt = """
Você cria relatórios executivos no formato:

📊 RESUMO
[Resumo em 2-3 frases]

📈 DESTAQUES
1. [Ponto-chave 1]
2. [Ponto-chave 2]
3. [Ponto-chave 3]

💡 RECOMENDAÇÕES
• Curto prazo: [Ação imediata]
• Médio prazo: [Ação estratégica]
• Longo prazo: [Visão futura]
"""

user_prompt = """
Crie um relatório executivo sobre os impactos da exploração de Marte para a economia global.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    max_completion_tokens=700,
    temperature=0.6
)

print(response.choices[0].message.content)
```
