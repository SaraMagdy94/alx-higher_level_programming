#!/usr/bin/python3
def print_last_digit(number):
    r = int(str(number)[-1])
    print("{:d}".format(r), end="")
    return (r)
