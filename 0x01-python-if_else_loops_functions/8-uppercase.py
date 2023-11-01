#!/usr/bin/python3
def uppercase(str):
    case = 0
    for r in str:
        if ord(r) >= ord('a') and ord(r) <= ord('z'):
            case = 32
        else:
            case = 0
        print('{:c}'.format(ord(r) - case), end='')
    print()
