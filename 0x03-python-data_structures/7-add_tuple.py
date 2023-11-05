#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    r = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (r[0] + b[0], r[1] + b[1])
