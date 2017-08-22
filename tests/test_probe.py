import pytest
import asyncio
import time
import sys
import os
from probe.domain.probe import Probe
from probe.technology.config import Config
from probe.technology.loader import actions


@pytest.fixture
def conf():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'files', 'config_2.yml')
    cfg.from_yaml(fn)
    return cfg


@pytest.fixture
def act():
    path = sys.path
    sys.path.append(os.path.join(os.path.dirname(__file__), 'files'))
    import tactions_2
    sys.path = path
    return actions

"""
def test_create_a_task_from_async_action(conf, act):
    async def aaction():
        asyncio.sleep(3)

    action = aaction

    p = Probe(conf, act)
    p._taskerize(1, 'action one', action)

    assert len(p.tasks) == 1
    assert isinstance(p.tasks[0], asyncio.Task)


def test_create_a_task_from_non_async_action(conf, act):
    async def no_aaction():
        time.sleep(3)

    action = no_aaction

    p = Probe(conf, act)
    p._taskerize(1, 'action one', action)

    assert len(p.tasks) == 1
    assert isinstance(p.tasks[0], asyncio.Task)


def test_create_a_probe(conf, act):
    p = Probe(conf, act)
    p.create_tasks()
    print(p.tasks)
    assert p.tasks

"""
def test_execute_tasks(conf, act):
    p = Probe(conf, act)
    p.create_tasks()
    p.execute_tasks()
