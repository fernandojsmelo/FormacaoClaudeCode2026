import asyncio


async def contar(nome, n):
    for i in range(1, n + 1):
        await asyncio.sleep(0.1)
        print(f"{nome} {i}")
    return f"{nome} terminou"


async def main():
    async with asyncio.TaskGroup() as grupo:      # Python 3.11+
        t1 = grupo.create_task(contar("A", 2))
        t2 = grupo.create_task(contar("B", 3))
    print(t1.result(), "|", t2.result())


asyncio.run(main())
