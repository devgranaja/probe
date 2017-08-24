import asyncio
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
