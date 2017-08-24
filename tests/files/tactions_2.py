
import asyncio
import time

from probe.technology.loader import action


@action
async def async_sleep():

    print('asyncio.sleep step1')
    await asyncio.sleep(1)
    print('asyncio.sleep step2')
    await asyncio.sleep(1)
    print('asyncio.sleep step3')
    await asyncio.sleep(1)
    return('A_OK')


@action
def sync_sleep():
    print('time.sleep 5s')
    time.sleep(10)
    return('S_OK')


@action
def sync_sleep2():
    print('time.sleep 10s')
    time.sleep(10)
    return('S2_OK')
