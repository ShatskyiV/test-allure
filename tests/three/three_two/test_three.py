import pytest

pytestmark = [
    pytest.mark.allure_label("Suite Three", label_type="epic"),
    pytest.mark.allure_label("Three Two", label_type="feature"),
]


def test_three():
    assert True
