import aiohttp
import asyncio

async def show(session, url):
    async with session.get(url) as response:
        return response.status

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://querycode.ir', 'https://realpython.com', 'https://python.org']
        coros = [show(session, url) for url in urls]

        tasks = [asyncio.create_task(coroutine) for coroutine in coros]
        for future in asyncio.as_completed(tasks):
            result = await future
            print(result)

asyncio.run(main())
