import pytest
import asyncio
import time
import sys
import os
from probe.domain.probe import Probe
from probe.technology.config import Config
from probe.domain.taskerize import actions
from probe.technology.text_file_repository import TextFileRepository


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

@pytest.fixture
def repo(tmpdir):
    file = tmpdir.join('testrepo.txt')
    return TextFileRepository(file)


@pytest.mark.asyncio
async def test_execute_tasks(conf, act, repo, event_loop):
    p = Probe(conf, act, repo, event_loop)
    await p.execute_tasks()
    assert p._all_tasks

@pytest.mark.asyncio
async def test_cancel_tasks(conf, act, repo, event_loop):
    p = Probe(conf, act, repo, event_loop)
    await p.execute_tasks()
    await p.cancel_tasks()


def test_get_configuration(conf, act, repo, event_loop):
    p = Probe(conf, act, repo, event_loop)
    c = p.configuration()
    assert conf == c
