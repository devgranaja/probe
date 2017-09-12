import asyncio
import os
import pytest
from probe.application.interactor import create_probe, start_probe, cancel_probe
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
async def test_create_probe(event_loop, conf, act):
    p = await create_probe(conf, act)
    assert p


@pytest.mark.asyncio
async def test_execute_tasks(conf, act, event_loop):
    p = await create_probe(conf, act)
    await start_probe()
    assert result[0] == 'OK'





