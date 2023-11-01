#!/usr/bin/python3
def uppercase(str):
    for r in str:
        if ord(r) >= 97 and ord(r) <= 122:
            print(chr(ord(r) - 32), end="")
        else:
            print(r, end="")
    print("")
