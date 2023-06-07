#!/usr/python3

def text_indentation(text):
  """
  Prints a text with 2 new lines after each of these characters: ., ? and :.

  Args:
    text: The text to indent.

  Raises:
    TypeError: If text is not a string.
  """

  if not isinstance(text, str):
    raise TypeError("text must be a string")

  for i in range(len(text)):
    if text[i] in ".?!":
      print()
      print()
    else:
      print(text[i], end="")
