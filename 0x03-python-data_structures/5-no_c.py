#!/usr/bin/python3
def no_c(my_string):
    b = my_string.translate({ord(r): None for r in 'cC'})
    return b
