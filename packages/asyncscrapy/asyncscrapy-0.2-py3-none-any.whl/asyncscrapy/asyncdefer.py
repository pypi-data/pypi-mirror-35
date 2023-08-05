def asyncfut_iterback(iterable, errback, *a, **kw):
    async def consumegen(asyncgen):
        val = list()
        async for i in asyncgen:
            val.append(i)
        return val
    future = asyncio.ensure_future(consumegen(iterable))
    return future