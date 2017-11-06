import asyncio
import io
import pytest
from probe.technology.text_file_repository import TextFileRepository
from probe.domain.taskerize import TaskResult
from probe.domain.taskerize import TypeResult


@pytest.fixture
def result():
    return TaskResult('mycoroutine', 'param', TypeResult.DONE, 'OK', 0.34)


@pytest.fixture
def result_error():
    return TaskResult('mycoroutine', 'paramError', TypeResult.ERROR, None, None)


@pytest.fixture
def result2():
    return TaskResult('mycoroutine', 'param2', TypeResult.DONE, 'OK', 0.66)


def test_add_one_item(result, tmpdir):
    file = tmpdir.join('testrepo.txt')
    repo = TextFileRepository(file)
    repo.add(result)
    with open(file) as f:
        content = f.read()

    assert 'mycoroutine,param,DONE,OK,0.34' == content


def test_add_error_item(result_error, tmpdir):
    file = tmpdir.join('testrepo.txt')
    repo = TextFileRepository(file)
    repo.add(result_error)
    with open(file) as f:
        content = f.read()

    assert 'mycoroutine,paramError,ERROR,None,None' == content

def test_get_first_item(result, tmpdir):
    file = tmpdir.join('testrepo.txt')
    repo = TextFileRepository(file)
    repo.add(result)

    retrieved = repo.get_first()
    assert result == retrieved


def test_get_first_error_item(result_error, tmpdir):
    file = tmpdir.join('testrepo.txt')
    repo = TextFileRepository(file)
    repo.add(result_error)

    retrieved = repo.get_first()
    assert result_error == retrieved


def test_get_last_item(result, result2, result_error, tmpdir):
    file = tmpdir.join('testrepo.txt')
    repo = TextFileRepository(file)
    repo.add(result)
    repo.add(result_error)
    repo.add(result2)

    retrieved = repo.get_last()
    assert retrieved == result2

def get_all(result, result2, tmpdir):
    file = tmpdir.join('testrepo.txt')
    repo = TextFileRepository(file)
    repo.add(result)
    repo.add(result2)

    retrieved = repo.get_all()

    assert [result, result2] == retrieved
