# content of test_assert1.py
'''
def f():
    return 3

def test_function():
    assert f() == 4
'''
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0