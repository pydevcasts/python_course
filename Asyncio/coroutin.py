import time 
import asyncio

start = time.perf_counter()
async def one(name):
    # print(f"hello {name}")
    await asyncio.sleep(2)
    print(f"bye {name}")

async def main():
    await one("siyamak")
    await one("diyana")

asyncio.run(main())
end = time.perf_counter()
print(end -start)
# async does happen for this code 
# =====================================
# another way
import time 
import asyncio

start = time.perf_counter()
async def one(name):
    await asyncio.sleep(2)
    print(f"bye {name}")

async def main():
    await asyncio.create_task(one("siyamak"))
    await asyncio.create_task(one("diyana"))

asyncio.run(main())
end = time.perf_counter()
print(end -start)

