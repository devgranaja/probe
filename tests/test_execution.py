import asyncio
import os
import pytest
from probe.application.execution import create_probe, cancel_probe
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
    from .files import tactions_2
    return actions


def test_run_probe(conf, act):
    loop = asyncio.get_event_loop()
    tasks = create_probe(conf, act, loop)

    try:
        print("\n[ ---------- Running probe ---------- ]\n"
              "(Press CTRL-C to quit)\n")
        loop.run_until_complete(*tasks)
    except KeyboardInterrupt:
        pass
    finally:
        cancel_probe()
        loop.close()
