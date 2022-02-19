import asyncio
from asyncio import Future


async def bar(future):
    print("bar will sleep for 3 seconds")
    await asyncio.sleep(3)
    print("bar resolving the future")
    future.done()
    future.set_result("future is resolved")


async def foo(future):
    print("foo will await the future")
    result = await future
    print("foo finds the future resolved. the result is \"{0}\"".format(result))


async def main():
    future = Future()
    results = await asyncio.gather(foo(future), bar(future))
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
    print("main exiting")
