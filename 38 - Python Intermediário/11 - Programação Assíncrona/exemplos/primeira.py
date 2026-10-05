import asyncio


async def saudar(nome):          # função assíncrona (corrotina)
    await asyncio.sleep(0.1)     # espera sem travar o programa
    return f"Olá, {nome}!"


c = saudar("Ana")
print(type(c).__name__)          # chamar só cria a corrotina
print(asyncio.run(c))            # o asyncio.run executa
