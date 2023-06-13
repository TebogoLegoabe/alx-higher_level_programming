#!/usr/bin/python3
"""
MyList class that inherits from list

Args:
    list: list of parameters

"""
class MyList(list):
    """MyList class that inherits from list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
