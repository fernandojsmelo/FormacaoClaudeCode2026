```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Compreendendo os Roles

- User: Mensagem do usuário
- Assistant: Resposta do modelo
- System: Instruções de comportamento para o modelo



```python
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Me explique de forma reduzida o que são as LLMs",
        }
    ],
    model="openai/gpt-oss-120b",
)
print(chat_completion.choices[0].message.content)
```

### Definindo um comportamento para modelo


```python
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em IA que responde de forma clara e objetiva."
        },
        {
            "role": "user",
            "content": "Me explique de forma reduzida o que são as LLMs",
        }
    ],
    model="openai/gpt-oss-120b",
)
print(chat_completion.choices[0].message.content)
```

### Controlando Resposta do Modelo 


```python
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em IA que responde de forma clara e objetiva."
        },
        {
            "role": "user",
            "content": "Explique a importância de LLMs com baixa latência."
        },
        {
            "role": "assistant",
            "content": "LLMs com baixa latência permitem respostas mais rápidas, o que melhora a experiência do usuário."
        },
        {
            "role": "user",
            "content": "Pode dar exemplos de aplicações práticas?"
        }
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)
```

### Usando System Prompt Refinados


```python
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": (
                "Você é um especialista em Inteligência Artificial focado em explicar conceitos "
                "de forma clara, estruturada e prática. Sempre inicie suas respostas com um "
                "resumo em até 3 linhas, depois detalhe com exemplos reais e aplicações no mundo "
                "dos negócios e tecnologia. Evite termos excessivamente técnicos sem explicação "
                "e, quando necessário, use analogias simples. "
                "Se o usuário pedir código, forneça exemplos em Python bem comentados."
            ),
        },
        {
            "role": "user",
            "content": "Explique a importância de LLMs com baixa latência."
        }
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)
```
