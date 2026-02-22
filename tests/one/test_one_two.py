import pytest

pytestmark = [
    pytest.mark.allure_label("Suite One", label_type="epic"),
    pytest.mark.allure_label("One Two", label_type="feature"),
]


def test_one_two_ok():
    assert True


def test_one_two_fail():
    assert False
