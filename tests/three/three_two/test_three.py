import allure
import pytest

pytestmark = [
    allure.epic("Suite Three"),
    allure.feature("Three Two"),
]


def test_three():
    assert True
