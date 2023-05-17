#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
     num = []
    for i in matrix:
        num.append(list(map(lambda i: i**2, i)))
    return (num)
