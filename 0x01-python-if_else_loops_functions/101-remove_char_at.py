#!/usr/bin/python3
def remove_char_at(str, r):
    if r < 0 or r >= len(str):
        return str
    else:
        return str[:r] + str[r+1:]
