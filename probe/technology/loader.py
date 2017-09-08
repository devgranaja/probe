import logging
import asyncio
import time

log = logging.getLogger(__name__)



"""
def action(coro):

    async def coro_helper():
        result = None
        total = None
        start = time.time()
        try:
            result = await coro()
            total = time.time() - start
            init_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
            print('[{}] {} {} {:06.2f}'.format(init_date, coro.__name__, result, total))
        except Exception as e:
            log.error('Unable to execute {}: {}'.format(coro.__name__, e.strerror))
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


"""