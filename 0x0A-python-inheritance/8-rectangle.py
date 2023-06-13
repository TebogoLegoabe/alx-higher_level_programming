#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry

Args:
    width: width of rectangle
    height: height of rectangle

"""
class BaseGeometry:
    """Base class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """inherited class"""
    def __int__(self, width, height):
        self.__width = width
        self.__height = height
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)

