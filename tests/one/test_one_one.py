import pytest

pytestmark = [
    pytest.mark.mark_epic("Suite One"),
    pytest.mark.mark_feature("One One"),
]


def test_one_one_ok():
    assert True


def test_one_one_fail():
    assert False
