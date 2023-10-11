import asyncio

async def main():
    process = await asyncio.create_subprocess_exec("sleep", "5")
    print(f"Process id is {process.pid}")
    try:
        status_code = await asyncio.wait_for(process.wait(), timeout=2)
        print(status_code)
    except asyncio.TimeoutError:
        print("Time out ...")
        process.terminate()
        status_code = await process.wait()
        print(status_code)

asyncio.run(main())