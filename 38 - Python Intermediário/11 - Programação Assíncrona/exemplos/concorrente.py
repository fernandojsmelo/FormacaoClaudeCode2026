import asyncio
import time
from sequencial import baixar


async def main():
    inicio = time.perf_counter()
    resultados = await asyncio.gather(   # ao mesmo tempo
        baixar("a.pdf", 1),
        baixar("b.pdf", 1),
        baixar("c.pdf", 1),
    )
    print(resultados)
    print(f"total: {time.perf_counter() - inicio:.1f} s")


asyncio.run(main())
