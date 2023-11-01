#!/usr/bin/python3

for r in range(10):
    for b in range(r+1, 10):
        if r < 8:
            print('{:d}{:d}, '.format(r, b), end='')
        else:
            print('{:d}{:d}'.format(r, b))
