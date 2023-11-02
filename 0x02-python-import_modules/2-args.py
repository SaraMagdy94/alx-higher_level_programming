#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    r = len(argv) - 1

    if r == 0:
        print("0 arguments.")
    elif r == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(r))

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
