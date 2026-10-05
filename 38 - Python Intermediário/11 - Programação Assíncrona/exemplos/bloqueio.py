import asyncio
import time


async def errado():
    time.sleep(0.5)              # trava o loop inteiro


async def certo():
    await asyncio.sleep(0.5)     # libera o loop enquanto espera


async def medir(funcao):
    inicio = time.perf_counter()
    await asyncio.gather(funcao(), funcao(), funcao())
    gasto = time.perf_counter() - inicio
    print(f"{funcao.__name__}: {gasto:.1f} s")


asyncio.run(medir(errado))
asyncio.run(medir(certo))
