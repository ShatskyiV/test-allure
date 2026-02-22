import allure
import pytest

pytestmark = [
    allure.epic("Suite One"),
    allure.feature("One One"),
]


def test_one_one_ok():
    assert True


def test_one_one_fail():
    assert False
