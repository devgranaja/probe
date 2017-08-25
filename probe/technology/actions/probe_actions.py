import asyncio
import aiohttp
import async_timeout
import time
from probe.technology.loader import action

@action
async def async_sleep():
    await asyncio.sleep(3)
    return('A_OK')

@action
async def get_url():
    async with aiohttp.ClientSession() as session:
        await fetch(session, 'http://www.python.org')
        await fetch(session, 'http://www.google.es')
        await fetch(session, 'http://www.juntadeandalucia.es')
        await fetch(session, 'http://www.saludjaen.es')
        await fetch(session, 'http://www.elpais.es')
        return ('web_OK')

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            await response.text()