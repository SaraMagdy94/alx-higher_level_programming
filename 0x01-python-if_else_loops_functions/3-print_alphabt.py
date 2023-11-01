#!/usr/bin/python3
for r in range(ord('a'), ord('z') + 1):
    if r != ord('q') and r != ord('e'):
        print('{:c}'.format(r), end='')
