#!/usr/bin/python3
"""
    prints My name is <first name> <last name>

    Args:
        first_name: first name as parameter
        last_name: last name as parameter

    Raises:
        TypeError: when either/both parameters are not strings

"""

def say_my_name(first_name, last_name=""):
    """function that print first and last name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
