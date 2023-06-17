#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
  """Defines a student."""

  def __init__(self, first_name, last_name, age):
    """Initializes a student with the given first name, last name, and age."""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def to_json(self, attrs=None):
    """Retrieves a dictionary representation of a Student instance."""
    if attrs is None:
      attrs = []

    json_dict = {}
    for attr in attrs:
      json_dict[attr] = getattr(self, attr)

    return json_dict

