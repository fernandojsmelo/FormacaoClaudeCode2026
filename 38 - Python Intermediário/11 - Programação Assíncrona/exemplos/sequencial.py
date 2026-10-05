import asyncio
import time


async def baixar(arquivo, segundos):
    print(f"  início {arquivo}")
    await asyncio.sleep(segundos)        # simula a rede
    print(f"  fim {arquivo}")
    return arquivo


async def main():
    inicio = time.perf_counter()
    await baixar("a.pdf", 1)             # um depois do outro
    await baixar("b.pdf", 1)
    print(f"total: {time.perf_counter() - inicio:.1f} s")


if __name__ == "__main__":
    asyncio.run(main())
