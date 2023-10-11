import asyncio


# async def show(smp):
#     await smp.acquire()
#     print("hello ...")
#     await asyncio.sleep(3)
#     smp.release()
#     smp.release()

# async def main():
#     smp = asyncio.Semaphore(2)
#     await asyncio.gather(*[show(smp) for _ in range(10)])

# asyncio.run(main())
# ===========================================


async def show(smp):
    await smp.acquire()
    print("hello ...")
    await asyncio.sleep(3)
    smp.release()
    smp.release()

async def main():
    smp = asyncio.BoundedSemaphore(2)
    await asyncio.gather(*[show(smp) for _ in range(10)])

asyncio.run(main())