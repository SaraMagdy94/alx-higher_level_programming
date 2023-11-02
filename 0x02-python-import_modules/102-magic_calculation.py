#!/usr/bin/python3
def magic_calculation(a, b):
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        r = add(a, b)
        for i in range(4, 6):
            r = add(r, i)
        return r
    else:
        return sub(a, b)
