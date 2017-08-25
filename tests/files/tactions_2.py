import asyncio
import aiohttp
import async_timeout
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
async def get_url():
    async with aiohttp.ClientSession() as session:
        await fetch(session, 'http://www.python.org')
        await fetch(session, 'http://www.google.es')
        await fetch(session, 'http://www.juntadeandalucia.es')
        await fetch(session, 'http://www.saludjaen.es')
        return('web_OK')

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            start = time.time()
            await response.text()
            total = time.time() - start
            print('{}: {:.3f}'.format(url, total))