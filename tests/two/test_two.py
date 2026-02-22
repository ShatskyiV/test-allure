import allure
import pytest

pytestmark = [
    allure.epic("Suite Two"),
    allure.feature("Two"),
]


def test_two():
    assert True
