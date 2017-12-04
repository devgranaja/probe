import asyncio
import aiohttp
import async_timeout
import time


from probe.domain.taskerize import action


@action
async def async_sleep(p, loop):
    await asyncio.sleep(1)
    return ('OK')