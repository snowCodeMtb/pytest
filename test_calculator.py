import pytest
from calculator import square

def test_positive_num():
    assert square(2) == 4
    assert square(4) == 16

def test_negative_num():
    assert square(-2) == 4
    assert square(-4) ==16
# test2
def test_zero():
    assert square(0) == 0
#test
def test_str():
    with pytest.raises(ValueError):
        square("cat")
