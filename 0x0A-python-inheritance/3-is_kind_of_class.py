#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
of if the object is an instance of a class that inherited from,
the specified class;otherwise False

Args:
    obj: object
    a_class: parameter of the class

"""
def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
of if the object is an instance of a class that inherited from,
the specified class;otherwise False"""
    return isinstance(obj, a_class)
