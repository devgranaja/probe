import asyncio
import aiohttp
import async_timeout
import re
import time

from probe.domain.taskerize import action

@action
async def asleep(item, loop):
    await asyncio.sleep(3)
    return('sleep_OK')


@action
async def afetch(url, loop):

    async def get_url(session, url, loop):
        with async_timeout.timeout(10, loop=loop):
            async with session.get(url) as response:
                await response.text()

    async with aiohttp.ClientSession() as session:
        start = time.time()
        await get_url(session, url, loop)
        end = time.time()
        return end - start


@action
async def aping(host, loop):
    p = await asyncio.create_subprocess_exec(
        'ping', host, '-c', '10',
        stdout=asyncio.subprocess.PIPE, loop=loop)
    total_time = 0
    count = 0
    while True:
        with async_timeout.timeout(10, loop=loop):
            line = await p.stdout.readline()
            if line:
                search = re.search('time=([0-9]*.[0-9]*)', str(line))
                if search:
                    count += 1
                    ping_time = float(search.group(1))
                    total_time += ping_time
            else:
                break
    if total_time:
        return total_time / count
    else:
        return None
