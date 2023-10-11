# import asyncio
# import aiohttp

# async def show(session, url):
#     async with session.get(url) as result:
#         return result.status

# async def main():
#     async with aiohttp.ClientSession() as session:
#         requests = [asyncio.create_task(show(session, 'https://python.org')),
#                     asyncio.create_task(show(session, 'https://querycosdde.ir'))
#         ]
#         done, pending = await asyncio.wait(requests, return_when=asyncio.FIRST_EXCEPTION)
#         print(f"Done is ====>{done}")
#         print(f"Pending ===>{pending}")
#         for d in done:
#             x = await d
#             print(x)
#         for p in pending:
#             p.cancel()
            
#         print(f"after cancelled {pending}")
# asyncio.run(main())

# ======================================================
import asyncio
import aiohttp

async def show(session, url, delay):
    await asyncio.sleep(delay)
    async with session.get(url) as response:
        return response.status

async def main():
    async with aiohttp.ClientSession() as session:
        requests = [asyncio.create_task(show(session, 'https://querycode.ir', 1)),
                    asyncio.create_task(show(session, 'https://python.org', 4))
        ]
        done, pending = await asyncio.wait(requests, timeout=2)
        print(f"Done is ====>{done}")
        print(f"Pending ===>{pending}")
        for d in done:
            x = await d
            print(x)
        for p in pending:
            p.cancel()
        print(f"{pending}...")
asyncio.run(main())