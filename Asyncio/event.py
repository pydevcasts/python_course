import asyncio
import functools

# async def show(name):
#     await asyncio.sleep(3)
#     print(f"hello {name}")

# async def main():
#     a =  asyncio.create_task(show("siyamak"))
#     b = asyncio.create_task(show("diyana"))
#     await a
#     await b

# loop = asyncio.new_event_loop()
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()
# ============================================
def  trigger_event(event):
    event.set()

async def do_work_en_event(event):
    print("Waiting for Event...")
    await event.wait()
    print("Peforming work!")
    await asyncio.sleep(2)
    print("Finished work")
    event.clear()

async def main():
    event = asyncio.Event()
    asyncio.get_running_loop().call_later(5, functools.partial(trigger_event, event))
    await asyncio.gather(do_work_en_event(event), do_work_en_event(event))

asyncio.run(main())