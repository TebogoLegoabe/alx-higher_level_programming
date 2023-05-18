#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    num = a_dictionary.copy()
    for i in num.key():
        num[i] *= 2
    return (num)
