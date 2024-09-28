''' My Calculator Test with Calculator object'''
import pytest
from calculator import Calculator

def test_add():
    '''Tests the addition function'''
    result = Calculator.add(2,2)
    assert  result == 4

def test_subtract():
    '''Tests the subtraction function'''
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Tests the multiplication function'''
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Tests the division function'''
    assert Calculator.divide(2,2) == 1

def test_dividebyzero():
    '''Testing if the divide by zero condition is working properly'''
    with pytest.raises(ValueError):
        Calculator.divide(2,0)
