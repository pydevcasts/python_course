import asyncio
import aiohttp


async def show(session, url):
    async with session.get(session, url) as response:
        return response.status
    
async def main():
    async with aiohttp.ClientSession() as session:
        urls = []
        coros = [show(session, url)for url in urls]
        tasks = [asyncio.create_task(corotin) for corotin in coros]
        for i in asyncio.as_completed(tasks):
            return await i

