#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
of the specified class

Args:
    obj: object
    a_class: parameter of the class

"""
def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance
of the specified class"""
    return type(obj) is a_class
