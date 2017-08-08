import pytest
from probe.technology.loader import actions
import os
import sys

path = sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'files'))


def test_no_actions():
    assert len(actions) == 0


def test_load_actions():
    from tactions import simple_action
    assert len(actions) > 0


def test_is_not_a_action():
    previous = len(actions)
    from tactions import no_decorated_function
    assert len(actions) == previous


sys.path = path
