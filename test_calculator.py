import pytest
from calculator import square

# test positive number input 
def test_positive_num():
    assert square(2) == 4
    assert square(4) == 16
# test negative number input
def test_negative_num():
    assert square(-2) == 4
    assert square(-4) ==16
# test zero input
def test_zero():
    assert square(0) == 0

#test invalid input type
def test_str():
    with pytest.raises(ValueError):
        square("cat")
