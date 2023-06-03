#!/usr/bin/python3
"""Defines a dunctions that add two integers"""

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
