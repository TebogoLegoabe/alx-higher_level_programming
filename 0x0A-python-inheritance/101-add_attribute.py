#!/usr/bin/python
"""
function that adds a new attributes
"""
class MyClass:
    pass

obj = MyClass()
add_attribute(obj, "name", "John")
print(obj.name)

add_attribute(obj, "age", 25)
print(obj.age)

add_attribute(obj, "name", "Jane")
