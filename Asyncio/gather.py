import aiohttp
import asyncio

# async def show_status(session, url):
#     async with session.get(url) as result:
#         return result.status

# async def main():
#     async with aiohttp.ClientSession() as session:
#         urls='https://querycode.ir'
#         response = await show_status(session, urls)
#         print(response)

# asyncio.run(main())
# ================================================

async def show_status(session, url):
    async with session.get(url) as result:
        return result.status

async def main():
    async with aiohttp.ClientSession() as session:
        urls=['https://querycode.ir', 'https://realpython.com', 'https://python.org']
        response = [show_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*response, return_exceptions=True)
        print(status_codes)
asyncio.run(main())
