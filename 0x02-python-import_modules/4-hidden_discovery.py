#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for r in sorted(names):
        if not r.startswith("__"):
            print(r)
