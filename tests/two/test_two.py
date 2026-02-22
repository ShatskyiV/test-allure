import pytest

pytestmark = [
    pytest.mark.mark_epic("Suite Two"),
    pytest.mark.mark_feature("Two"),
]


def test_two():
    assert True

