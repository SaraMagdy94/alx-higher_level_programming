#!/usr/bin/python3

for r in range(100):
    if r < 99:
        print('{:02d}, '.format(r), end='')
    else:
        print('{:02d}'.format(r))
