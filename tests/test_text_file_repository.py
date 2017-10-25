import io
import pytest
from probe.technology.text_file_repository import TextFileRepository
from probe.domain.taskerize import TaskResult
from probe.domain.taskerize import TypeResult


@pytest.fixture
def file():
    return io.StringIO()

@pytest.fixture
def result():
    return TaskResult('mycoroutine', 'param', TypeResult.DONE, 'OK', 0.34)


def test_add_one_item(file, result):

    repo = TextFileRepository(file)
    repo.add_item(result)

    assert 'mycoroutine,param,0,OK,0.34' == file.getvalue()


def test_get_all_items(file, result):

    repo = TextFileRepository(file)
    repo.add_item(result)
    repo.add_item(result)

    from_file = repo.get_all()

    assert [result, result] == from_file
