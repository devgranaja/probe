from probe.technology.loader import action


@action
async def async_sleep():
    print('asyncio.sleep')


@action
def sync_sleep():
    print('asyncio.sleep')
