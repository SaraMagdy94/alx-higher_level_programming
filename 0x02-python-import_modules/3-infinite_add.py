#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]

    if len(args) == 0:
        print("0")
    else:
        r = sum(map(int, args))
        print(r)
