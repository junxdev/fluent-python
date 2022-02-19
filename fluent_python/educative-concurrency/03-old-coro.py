import asyncio
import datetime


@asyncio.coroutine
def go_to_sleep(sleep):
    print("sleeping for " + str(sleep) + " seconds")
    yield from asyncio.sleep(sleep)
    print("woke up after " + str(sleep) + " seconds")


@asyncio.coroutine
def do_something_important(sleep):
    # what is more important than getting
    # enough sleep!
    yield from go_to_sleep(sleep)


@asyncio.coroutine
def supervisor(sleeps):
    for sleep in sleeps:
        yield from do_something_important(sleep)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print(datetime.datetime.now())
    futures = asyncio.gather(do_something_important(1), do_something_important(2), do_something_important(3))
    loop.run_until_complete(futures)
    print(datetime.datetime.now())
    loop.close()
