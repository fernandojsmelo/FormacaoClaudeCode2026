import asyncio


async def consulta_lenta():
    await asyncio.sleep(2)
    return "dados"


async def main():
    try:
        async with asyncio.timeout(0.5):    # desiste em 0,5 s
            print(await consulta_lenta())
    except TimeoutError:
        print("A consulta demorou demais: cancelada")


asyncio.run(main())
