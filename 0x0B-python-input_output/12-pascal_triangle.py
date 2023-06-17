#!/usr/bin/python3
"""Defines a function pascal triangle."""


def pascal_triangle(n):
  """Returns a list of lists of integers representing the Pascal's triangle of n.

  Args:
    n: The number of rows in the triangle.

  Returns:
    A list of lists of integers, where each inner list represents a row in the triangle.

  """
  if n <= 0:
    return []

  triangle = [[1]]
  for i in range(1, n):
    new_row = []
    for j in range(i + 1):
      if j == 0 or j == i:
        new_row.append(1)
      else:
        new_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(new_row)

  return triangle
