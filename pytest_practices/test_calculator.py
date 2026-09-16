# writing pytest for calculator file test
'''
from calculator import add
def test_add():
    assert add(2, 3) == 5
    

import pytest
from calculator import calculate_subtotal, apply_discount

def test_calculate_subtotal_success():
    """Verify that multiplying prices by quantities returns the correct total."""
    result = calculate_subtotal(4.50, 3)
    assert result == 13.50

def test_calculate_subtotal_negative_raises_error():
    """Verify that negative inputs trigger a ValueError."""
    with pytest.raises(ValueError):
        calculate_subtotal(-4.50, 3)

def test_apply_discount():
    """Verify that discounts are deducted correctly."""
    result = apply_discount(10.00, 0.10)
    assert result == 9.00
    '''

from calculator import greet
def test_greet():
    assert greet("Alex") == "Hello, Alex"