import pytest

pytestmark = [
    pytest.mark.mark_epic("Suite Three"),
    pytest.mark.mark_feature("Three Two"),
]


def test_three():
    assert True
