import asyncio
from asyncio import Future


# @asyncio.coroutine
# def coro3(k):
#     # yield k + 3
#     return k + 3
#
#

# async def coro3(k):
#     return k + 3


# def coro3(k):
#     f = Future()
#     f.set_result(k + 3)
#     f.done()
#     return f


@asyncio.coroutine
def coro3(k):
    return k + 3


def coro2(j):
    j = j * j
    yield from coro3(j)


# async def coro2(j):
#     j = j * j
#     return await coro3(j)


def coro1():
    i = 0
    while True:
        yield from coro2(i)
        i += 1


async def execute_coro():
    # cr = coro1()

    # ts = asyncio.gather(*[coro2(v) for v in range(100)])

    ts = [asyncio.create_task(coro2(v)) for v in range(100)]
    x = await asyncio.gather(*ts)
    # x = await ts

    print(x)


if __name__ == "__main__":
    # The first 100 natural numbers evaluated for the following expression
    # x^2 + 3

    asyncio.run(execute_coro())
    # cr = coro1()
    # for v in range(100):
    #     print("f({0}) = {1}".format(v, next(cr)))
