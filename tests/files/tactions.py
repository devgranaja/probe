from probe.technology.loader import aaction


@aaction
async def simple_aaction():
    print('my first action')


@aaction
def no_async_action():
    print('I am not async')
