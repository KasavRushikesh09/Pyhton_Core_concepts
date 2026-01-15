import pytest
from Test_Coverage.app.calculator import add, sub, div
def test_add():
    assert add(1,2) == 3
def test_sub():
    assert sub(5,3) == 2
def test_div():
    assert div(10,2) == 5
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):div(10,0)
