import pytest
from src.math import add_two_numbers, diff_two_numbers, mult_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(a=5, b=2) == 7

def test_diff_two_numbers():
    assert diff_two_numbers(a=6, b=3) == 3

@pytest.mark.skip(reason="Buggy function to be fixed in ticket A-123")
def test_mult_two_numbers():
    assert mult_two_numbers(a=3, b=4) == 12

# def test_failure():
#     assert [1, 2, 3] == [1, 3, 2]

class TestSomething:
    def test_one(self):
        assert True