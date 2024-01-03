import asyncio

async def main():
    process = await asyncio.create_subprocess_exec("python", "two.py", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
    std_out, std_err = await process.communicate(b'siyamak')
    print(std_err)
    print(std_out)

asyncio.run(main())