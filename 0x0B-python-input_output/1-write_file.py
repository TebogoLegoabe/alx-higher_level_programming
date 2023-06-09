#!/usr/bin/python3
"""
Defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    Args:
        filename: Name of the file to write to
        text: the txt to write to file name
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
