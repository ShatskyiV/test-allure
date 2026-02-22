import pytest

pytestmark = [
    pytest.mark.allure_label("Suite One", label_type="epic"),
    pytest.mark.allure_label("One One", label_type="feature"),
]


def test_one_one_ok():
    assert True


def test_one_one_fail():
    assert False
