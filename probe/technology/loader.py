import logging
import asyncio
import time

log = logging.getLogger(__name__)

actions = {}


def action(coro):

    async def coro_helper():
        start = time.time()
        result = await coro()
        total = time.time() - start
        print('{} {} {:06.2f}'.format(coro.__name__, result, total))
        return result, total

    async def loop_helper(period):
        if period == 0:
            (result, timing) = await coro_helper()
        else:
            while True:
                (result, timing) = await coro_helper()
                await asyncio.sleep(period)

    if asyncio.iscoroutinefunction(coro):
        actions[coro.__name__] = loop_helper
        log.debug('Action {} registered.'.format(coro.__name__))
    else:
        log.warning('Action {} is not registered. It is not a coroutine function'.format(coro.__name__))
    return loop_helper


