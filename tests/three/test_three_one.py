import allure
import pytest

pytestmark = [
    allure.epic("Suite Three"),
    allure.feature("Three One"),
]


def test_solution():
    assert False
