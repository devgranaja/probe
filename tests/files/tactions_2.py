
import asyncio
import time

from probe.technology.loader import action


@action
async def async_sleep():
    print('asyncio.sleep 5s')
    await asyncio.sleep(5)
    return('A_OK')


@action
def sync_sleep():
    print('time.sleep 10s')
    time.sleep(10)
    return('S_OK')
