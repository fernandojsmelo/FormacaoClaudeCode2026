from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()  # lê o arquivo .env da pasta atual
chave = os.environ.get("GROQ_API")
print("Chave carregada?", "sim" if chave else "não")

client = Groq(api_key=chave)
resposta = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "Diga olá em uma frase."}],
)
print(resposta.choices[0].message.content)
