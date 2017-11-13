import asyncio
import time
import datetime
import logging
from enum import Enum
from collections import namedtuple

# TODO Support not coroutines https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
# TODO coroutines without parameters

actions = {}

log = logging.getLogger()
log.setLevel(logging.INFO)


_loop = asyncio.get_event_loop()


class TypeResult(Enum):
    DONE = 0
    ERROR = 1

TaskResult = namedtuple('TaskResult', 'timestamp, action, item, type, value, time')


def action(coro):
    async def loop_helper(items, iterations, period, repository, loop):
        # TODO infinite number of iterations
        iteration = 0
        while True:
            try:
                results = await launcher_helper(coro, items, loop)
                iteration += 1
                for r in results:
                    repository.add(r)
                    log.debug('Result stored: '.format(r))
                    print(r)
                if iteration == iterations:
                    return
            except Exception as e:
                log.exception('Unexpected error: '.format(e))
                return
            await asyncio.sleep(period)

    if asyncio.iscoroutinefunction(coro):
        actions[coro.__name__] = loop_helper
        log.debug('Action {} registered.'.format(coro.__name__))
    else:
        log.warning('Action {} is not registered. It is not a coroutine function'.format(coro.__name__))

    return loop_helper


async def launcher_helper(coro, items, loop):
    tasks = [coro_helper(coro, item, loop) for item in items]
    tasks_results = await asyncio.gather(*tasks, return_exceptions=True)

    final_results = []
    for i, r in zip(items, tasks_results):
        if isinstance(r, Exception):
            final_results.append(TaskResult(datetime.datetime.now(), coro.__name__, i, TypeResult.ERROR, None, None))
            log.error('Error executing {}({}): {}'.format(coro.__name__, i, r))
        else:
            final_results.append(r)
            log.info('{}({}) executed. Time {:.2f} s'.format(coro.__name__, i, r.time))

    return final_results

async def coro_helper(coro, item, loop):
    start = time.time()
    value = await coro(item, loop)
    end = time.time()

    return TaskResult(datetime.datetime.now(), coro.__name__, item, TypeResult.DONE, value, end - start)
