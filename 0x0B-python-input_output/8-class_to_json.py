#!/usr/bin/python3
"""
Defines a function class_to_json
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data str
    Args:

        obj: object
    """
    return obj.__dict__
