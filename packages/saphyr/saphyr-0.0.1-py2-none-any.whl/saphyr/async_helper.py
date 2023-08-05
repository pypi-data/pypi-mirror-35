import asyncio


def as_sync(f):
    asyncio.get_event_loop().run_until_complete(f())
