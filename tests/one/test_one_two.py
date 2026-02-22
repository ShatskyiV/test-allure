import allure
import pytest

pytestmark = [
    allure.epic("Suite One"),
    allure.feature("One Two"),
]


def test_one_two_ok():
    assert True


def test_one_two_fail():
    assert False
