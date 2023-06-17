#!/usr/bin/python3
"""
Defines a function read_file
"""


def read_file(filename=""):
    """
    Reads filename

    Args:
        filename: Name of the file to be read

    """
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
