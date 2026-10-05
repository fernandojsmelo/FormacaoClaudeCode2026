import asyncio
import time

LOJAS = {"Loja A": (0.6, 199.9), "Loja B": (0.3, 189.0),
         "Loja C": (0.9, 205.5)}


async def consultar(loja):
    demora, preco = LOJAS[loja]
    await asyncio.sleep(demora)          # simula a API da loja
    return loja, preco


async def main():
    inicio = time.perf_counter()
    respostas = await asyncio.gather(*map(consultar, LOJAS))
    loja, preco = min(respostas, key=lambda r: r[1])
    print(f"menor preço: {loja} (R$ {preco:.2f})")
    print(f"tempo: {time.perf_counter() - inicio:.1f} s")


asyncio.run(main())
