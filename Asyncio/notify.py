import asyncio

async def do_work(condition):
    async with condition:
        print("Locked ...")
        await condition.wait()
        print("Event happend..")
        await asyncio.sleep(2)
        print("work finished..")

async def fire_event(condition):
    await asyncio.sleep(2)
    async with condition:
        print("notification all task ...")
        condition.notify_all()
    print("Notification Finished ..")

async def main():
    condition = asyncio.Condition()
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))
asyncio.run(main())