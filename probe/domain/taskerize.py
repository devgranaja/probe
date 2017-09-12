import asyncio
import time
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

TaskResult = namedtuple('TaskResult', 'action, item, type, result, time')


def action(coro):
    async def loop_helper(items, iterations, period):
        # TODO infinite number of iterations
        iteration = 0
        while True:
            try:
                results = await launcher_helper(coro, items)
                iteration += 1
                for r in results:
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


async def launcher_helper(coro, items):
    tasks = [coro_helper(coro, item) for item in items]
    tasks_results = await asyncio.gather(*tasks, return_exceptions=True)

    final_results = []
    for i, r in zip(items, tasks_results):
        if isinstance(r, Exception):
            final_results.append(TaskResult(coro.__name__, None, TypeResult.ERROR, None, None))
            log.error('Error executing {}({}): {}'.format(coro.__name__, i, r))
        else:
            final_results.append(r)
            log.info('{}({}) executed. Time {:.2f} s'.format(coro.__name__, i, r.time))

    return final_results

async def coro_helper(coro, item):
    start = time.time()
    result = await coro(item)
    total = time.time() - start

    return TaskResult(coro.__name__, item, TypeResult.DONE, result, total)
