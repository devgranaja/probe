import pytest
import os


def pytest_namespace():
    return {'filename': './test_config.yml',
            'chromedriver': '../probe/technology/automaton/driver/chromedriver/mac/chromedriver'}


# https://stackoverflow.com/questions/42652228/removing-cached-files-after-a-py-test-run
@pytest.yield_fixture(autouse=True, scope='session')
def test_suite_cleanup_thing():
    # setup
    yield
    # teardown - put your command here
    os.remove(pytest.filename)
