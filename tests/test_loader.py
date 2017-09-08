import pytest
from probe.domain.taskerize import actions


def test_no_actions():
    assert len(actions) == 0


def test_load_actions():
    from .files.tactions_1 import simple_action
    assert len(actions) > 0


def test_is_not_a_action():
    previous = len(actions)
    from .files.tactions_1 import no_decorated_function
    assert len(actions) == previous
