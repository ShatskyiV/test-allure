import pytest

pytestmark = [
    pytest.mark.mark_epic("Suite One"),
    pytest.mark.mark_feature("One Two"),
]


def test_one_two_ok():
    assert True


def test_one_two_fail():
    assert False
