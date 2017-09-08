import pytest
import asyncio
import time
import sys
import os
from probe.domain.probe import Probe
from probe.technology.config import Config
from probe.domain.taskerize import actions


@pytest.fixture
def conf():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'files', 'config_2.yml')
    cfg.from_yaml(fn)
    return cfg


@pytest.fixture
def act():
    from .files import tactions_2
    return actions


@pytest.mark.asyncio
async def test_execute_tasks(conf, act, event_loop):
    p = Probe(conf, act)
    await p.execute_tasks()
    assert p._all_tasks

@pytest.mark.asyncio
async def test_cancel_tasks(conf, act, event_loop):
    p = Probe(conf, act)
    await p.execute_tasks()
    await p.cancel_tasks()
