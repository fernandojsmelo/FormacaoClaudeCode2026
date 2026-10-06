# pip install tiktoken
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

frases = [
    "The cat sat on the mat.",
    "O gato sentou no tapete.",
    "Inteligência artificial generativa",
    "anticonstitucionalissimamente",
]
for f in frases:
    ids = enc.encode(f)
    pedacos = [enc.decode([i]) for i in ids]
    print(f"{len(f):>3} caracteres -> {len(ids):>2} tokens")
    print("   ", pedacos)
