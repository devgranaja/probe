import asyncio
import aiohttp
import async_timeout
import aioping


from probe.domain.taskerize import action

@action
async def asleep(item):
    await asyncio.sleep(3)
    return('A_OK')

@action
async def get_url(url):
    async with aiohttp.ClientSession() as session:
        await fetch(session, url)
        return ('web_OK')

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            await response.text()


@action
async def aping(host):
    return await aioping.ping(host) * 1000

