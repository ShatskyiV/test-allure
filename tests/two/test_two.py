import pytest

pytestmark = [
    pytest.mark.allure_label("Suite Two", label_type="epic"),
    pytest.mark.allure_label("Two", label_type="feature"),
]


def test_two():
    assert True
