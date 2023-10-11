import asyncio
from asyncio import TimeoutError



# async def show():
#     await asyncio.sleep(3)
#     print("hello")

# async def main():
#     a = asyncio.create_task(show())
#     try:
#         await asyncio.wait_for(a, timeout=2)
#     except TimeoutError:
#         print("Deadline reached ...")

#     print(f"was task cancelled? {a.cancelled()}")
    
# asyncio.run(main())
# ==================================================


async def show():
    await asyncio.sleep(6)
    print("hello")

async def main():
    a = asyncio.create_task(show())
    try:
        await asyncio.wait_for(asyncio.shield(a), timeout=5)#for doesnot stop my task
    except TimeoutError:
        print("Taking longer than usual we are working ...")
        await a #sure to add a in here to continue our task
    print(f"was task cancelled? {a.cancelled()}")
    
asyncio.run(main())

