"""
Basic arithmetic operations module.

This module provides simple arithmetic functions for calculations.
"""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of two numbers as float.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Result of division as float
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    return a / b

