#!/usr/bin/python3
"""
Defines a text file insertion function
"""


def append_after(filename="", search_string="", new_string=""):
  """
  Appends a line of text to a file, after each line containing a specific string

  Args:

  """
  with open(filename, "r+") as f:
    for line in f:
      if search_string in line:
        f.write(new_string + "\n")
      f.write(line)
