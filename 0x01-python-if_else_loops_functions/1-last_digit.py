#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
R = abs(number) % 10

print(f"Last digit of {number:d} is {R:d}", end=" ")

if R > 5:
    print(f"and is greater than 5")
elif R == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
