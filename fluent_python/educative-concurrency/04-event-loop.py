import asyncio


async def do_something_important():
    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(do_something_important())
