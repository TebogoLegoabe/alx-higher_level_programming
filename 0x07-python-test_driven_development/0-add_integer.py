#!/usr/bin/python3
"""
    adds 2 integers.

    Args:
        a: integer parameter
        b: integer parameter

    Raises:
        TypeError: a must be an integer or b must be an integer
"""

def add_integer(a, b=98):
    """function that adds two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
       b = int(b)

    return int(a + b)
