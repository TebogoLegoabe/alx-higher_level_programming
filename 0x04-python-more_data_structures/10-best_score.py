#!/usr/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)
    biggest_int = max(a_dictionary.value())
    for i, value in a_dictionary.item():
        if value is bigger_int:
            return (i)
