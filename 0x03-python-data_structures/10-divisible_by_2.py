#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    even = []

    for i in my_list:
        even.append(i % 2 == 0)

    return (even)
