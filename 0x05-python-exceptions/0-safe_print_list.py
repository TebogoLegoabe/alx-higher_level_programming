#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                print(my_list[i], end='')
                count += 1
            except Error:
                break
        print()
        return (count)
    except Err:
        return (0)
