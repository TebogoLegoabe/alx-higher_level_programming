#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        col = 0
        for i in row:
            col += 1
            print("{:d}".format(i), end=(" " if col < len(row) else ""))
        print("")
