import asyncio


async def mensagens():               # gerador assíncrono
    for texto in ["oi", "tudo bem?", "tchau"]:
        await asyncio.sleep(0.1)     # chegam aos poucos
        yield texto


async def main():
    async for msg in mensagens():
        print("recebido:", msg)


asyncio.run(main())
