import asyncio
import time
from probe.domain.probe import Probe


def test_create_a_task_from_async_action():
    async def aaction():
        print('async function started')
        asyncio.sleep(3)
        print('async function finished')

    action = aaction

    p = Probe()
    p.taskerize(1, 'action one', action)

    assert len(p.tasks) == 1
    assert isinstance(p.tasks[0], asyncio.Task)


def test_create_a_task_from_non_async_action():
    async def no_aaction():
        print('non async function started')
        time.sleep(3)
        print('non async function finished')

    action = no_aaction

    p = Probe()
    p.taskerize(1, 'action one', action)

    assert len(p.tasks) == 1
    assert isinstance(p.tasks[0], asyncio.Task)
